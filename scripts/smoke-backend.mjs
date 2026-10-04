import assert from 'node:assert/strict';
import { spawn, spawnSync } from 'node:child_process';
import { randomBytes } from 'node:crypto';
import { closeSync, openSync } from 'node:fs';
import { access, mkdir, mkdtemp, writeFile } from 'node:fs/promises';
import net from 'node:net';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { setTimeout as delay } from 'node:timers/promises';

// Exercise the original sidecar with a fresh database and its normal license checks.
// No providers, generation jobs, toolkit installation, or existing user data are used.
const workspace = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const runtime = path.join(workspace, '.runtime');
const executable = path.join(runtime, 'desktop', 'resources', 'backend', 'backend.exe');
const reportPath = path.join(runtime, 'smoke-result.json');
const report = { ok: false, startedAt: new Date().toISOString(), executable };
let child;
let childExited = false;
let childError;
let requestedSignal;
let logDescriptor;

for (const signal of ['SIGINT', 'SIGTERM']) {
  process.once(signal, () => { requestedSignal = signal; });
}

async function freeLoopbackPort() {
  const server = net.createServer();
  await new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(0, '127.0.0.1', resolve);
  });
  const { port } = server.address();
  await new Promise((resolve, reject) => server.close(error => error ? reject(error) : resolve()));
  return port;
}

function ensureRunning() {
  if (requestedSignal) throw new Error(`Smoke test interrupted by ${requestedSignal}.`);
  if (childError) throw new Error(`Cannot start backend: ${childError.message}`);
  if (childExited) throw new Error(`Backend exited before verification (code ${child.exitCode}, signal ${child.signalCode}).`);
}

async function request(url, headers = {}) {
  return fetch(url, { headers, signal: AbortSignal.timeout(1500), redirect: 'error' });
}

function stopOwnedProcessTree() {
  if (!child?.pid || childExited) return;
  const taskkill = path.join(process.env.SystemRoot || 'C:\\Windows', 'System32', 'taskkill.exe');
  const stopped = spawnSync(taskkill, ['/PID', String(child.pid), '/T', '/F'], {
    windowsHide: true,
    stdio: 'pipe',
    timeout: 15000,
  });
  if (stopped.error || stopped.status !== 0) {
    report.cleanupError = stopped.error?.message || `taskkill returned ${stopped.status}`;
    report.ok = false;
  }
}

try {
  if (process.platform !== 'win32') throw new Error('The recovered backend requires Windows x64.');
  await access(executable).catch(() => {
    throw new Error('Backend runtime is missing. Run npm run setup first.');
  });
  const smokeRoot = path.join(runtime, 'smoke-data');
  await mkdir(smokeRoot, { recursive: true });
  const dataDirectory = await mkdtemp(path.join(smokeRoot, 'run-'));
  const logPath = path.join(dataDirectory, 'backend.log');
  const port = await freeLoopbackPort();
  const token = randomBytes(32).toString('hex');
  const baseUrl = `http://127.0.0.1:${port}/api/v1/system`;
  Object.assign(report, { dataDirectory, logPath, port, licenseEnforced: true });
  logDescriptor = openSync(logPath, 'w');
  child = spawn(executable, [
    '--host', '127.0.0.1', '--port', String(port), '--token', token,
    '--data-dir', dataDirectory, '--device-id', `smoke-${randomBytes(12).toString('hex')}`,
  ], {
    cwd: path.dirname(executable),
    windowsHide: true,
    stdio: ['ignore', logDescriptor, logDescriptor],
    env: {
      ...process.env,
      VS_DATA_DIR: dataDirectory,
      REVO_LICENSE_ENFORCE: '1',
      PYTHONUTF8: '1',
      PYTHONIOENCODING: 'utf-8',
    },
  });
  child.once('error', error => { childError = error; });
  child.once('exit', () => { childExited = true; });
  closeSync(logDescriptor);
  logDescriptor = undefined;

  const deadline = Date.now() + 45000;
  let health;
  while (Date.now() < deadline) {
    ensureRunning();
    try {
      const response = await request(`${baseUrl}/health`);
      if (response.status === 200) {
        health = await response.json();
        break;
      }
      await response.body?.cancel();
    } catch {
      // A refused connection is normal while imports and migrations complete.
    }
    await delay(250);
  }
  ensureRunning();
  assert.ok(health, 'Backend did not become healthy within 45 seconds. Inspect the backend log.');
  assert.equal(health.status, 'ok');
  assert.equal(health.db, 'ok');
  report.health = health;

  const unauthenticated = await request(`${baseUrl}/ffmpeg`);
  report.unauthenticatedStatus = unauthenticated.status;
  await unauthenticated.body?.cancel();
  assert.equal(unauthenticated.status, 401, 'The protected endpoint must reject a missing token.');

  const authenticated = await request(`${baseUrl}/ffmpeg`, { 'x-studio-token': token });
  report.authenticatedStatus = authenticated.status;
  assert.equal(authenticated.status, 200, 'The protected endpoint must accept the sidecar token.');
  const ffmpeg = await authenticated.json();
  assert.equal(typeof ffmpeg.ok, 'boolean', 'Unexpected FFmpeg check response.');
  report.ffmpeg = { available: ffmpeg.ok, ...(ffmpeg.error_code ? { errorCode: ffmpeg.error_code } : {}) };
  ensureRunning();
  report.ok = true;
} catch (error) {
  report.error = error.message;
} finally {
  stopOwnedProcessTree();
  if (logDescriptor !== undefined) closeSync(logDescriptor);
  report.finishedAt = new Date().toISOString();
  await mkdir(runtime, { recursive: true });
  await writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, 'utf8');
}

if (report.ok) {
  console.log(`Backend smoke passed: healthy database, token rejected/accepted correctly. FFmpeg available: ${report.ffmpeg.available}.`);
} else {
  console.error(`Backend smoke failed: ${report.error || report.cleanupError}`);
}
console.log(`Report: ${reportPath}`);
if (report.logPath) console.log(`Backend log: ${report.logPath}`);
process.exitCode = requestedSignal === 'SIGINT' ? 130 : report.ok ? 0 : 1;
