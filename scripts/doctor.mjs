import { createHash } from 'node:crypto';
import { createReadStream } from 'node:fs';
import { lstat, readFile, realpath, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const workspaceRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const desktopRoot = path.join(workspaceRoot, '.runtime', 'desktop');
export const desktopExecutable = path.join(desktopRoot, 'Revo Studio.exe');
export const userDataDirectory = path.join(workspaceRoot, '.runtime', 'user-data');

// Decode only the known 1.4.3 string table. Never import or evaluate recovered code.
export function readExpectedBackendHash(source) {
  const direct = source.match(/EXPECTED_BACKEND_SHA256\s*=\s*['"]([a-f0-9]{64})['"]/i);
  if (direct) return direct[1].toLowerCase();

  const table = source.match(/\b_0x2c6fcb\s*=\s*\[([^\]]+)\]/);
  if (!table) throw new Error('Unsupported backendIntegrity.js format; cannot verify the backend.');
  const values = [...table[1].matchAll(/'([a-zA-Z0-9+/=]+)'/g)].map(([, encoded]) => {
    const standardBase64 = encoded.replace(/[a-zA-Z]/g, (char) => (
      char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase()
    ));
    return Buffer.from(standardBase64, 'base64').toString('utf8');
  });
  const anchor = values.indexOf('EXPECTED_B');
  if (anchor < 0 || values.length !== 22) throw new Error('Unexpected backend integrity string table.');
  const decode = (index) => values[((index - 0x13c + anchor) % values.length + values.length) % values.length];
  if (decode(0x13c) + decode(0x13a) + decode(0x13e) !== 'EXPECTED_BACKEND_SHA256') {
    throw new Error('Cannot locate the backend integrity constant.');
  }
  const assignment = source.slice(source.lastIndexOf('exports['));
  const expression = assignment.match(/^exports\[[^\]]+\]\s*=\s*([^;]+);/)?.[1];
  if (!expression) throw new Error('Cannot read the backend integrity assignment.');
  const hash = expression.split('+').map((term) => {
    const literal = term.trim().match(/^'([a-f0-9]+)'$/i);
    if (literal) return literal[1];
    const lookup = term.trim().match(/^_0x4d9b88\((0x[a-f0-9]+)\)$/i);
    if (lookup) return decode(Number(lookup[1]));
    throw new Error('Unsupported expression in the backend integrity assignment.');
  }).join('');
  if (!/^[a-f0-9]{64}$/i.test(hash)) throw new Error('Invalid backend SHA256 constant.');
  return hash.toLowerCase();
}

async function sha256(filename) {
  const hash = createHash('sha256');
  for await (const chunk of createReadStream(filename)) hash.update(chunk);
  return hash.digest('hex');
}

export async function inspectRuntime({ verifyBackendHash = true } = {}) {
  const checks = [];
  const check = (name, ok, detail) => checks.push({ name, ok, detail });
  const checkFile = async (relative, base = desktopRoot) => {
    const filename = path.join(base, relative);
    try {
      const info = await stat(filename);
      const ok = info.isFile() && info.size > 0;
      check(relative, ok, ok ? undefined : 'File is empty or is not a regular file.');
      return ok;
    } catch (error) {
      check(relative, false, error.code === 'ENOENT' ? 'Missing; run npm run setup.' : error.message);
      return false;
    }
  };

  check('Windows runtime', process.platform === 'win32', process.platform === 'win32' ? undefined : 'The recovered native runtime requires Windows.');
  await checkFile('Revo Studio.exe');
  for (const relative of ['icudtl.dat', 'resources.pak', 'v8_context_snapshot.bin', 'ffmpeg.dll']) {
    await checkFile(relative);
  }
  const backendPresent = await checkFile('resources/backend/backend.exe');
  await checkFile('resources/ima2/node.exe');
  await checkFile('resources/ima2/node_modules/ima2-gen/server.js');
  for (const relative of ['package.json', 'dist-electron/main.js', 'dist-electron/preload.js', 'dist/index.html']) {
    await checkFile(relative, path.join(workspaceRoot, 'recovered', 'app'));
  }

  const appLink = path.join(desktopRoot, 'resources', 'app');
  try {
    const info = await lstat(appLink);
    const actual = await realpath(appLink);
    const expected = await realpath(path.join(workspaceRoot, 'recovered', 'app'));
    const normalize = (value) => process.platform === 'win32' ? value.toLowerCase() : value;
    check('Runtime links to recovered/app', info.isSymbolicLink() && normalize(actual) === normalize(expected), actual);
  } catch (error) {
    check('Runtime links to recovered/app', false, error.code === 'ENOENT' ? 'Missing junction; run npm run setup.' : error.message);
  }
  try {
    await lstat(path.join(desktopRoot, 'resources', 'app.asar'));
    check('Recovered app takes precedence', false, 'resources/app.asar would override the recovered/app junction; rerun setup.');
  } catch (error) {
    check('Recovered app takes precedence', error.code === 'ENOENT', error.code === 'ENOENT' ? undefined : error.message);
  }

  try {
    const distRoot = path.join(workspaceRoot, 'recovered', 'app', 'dist');
    const html = await readFile(path.join(distRoot, 'index.html'), 'utf8');
    const assets = [...html.matchAll(/(?:src|href)=["'](\.\/assets\/[^"']+)["']/g)].map(([, asset]) => asset);
    check('Frontend asset references', assets.length > 0);
    for (const asset of assets) {
      const resolved = path.resolve(distRoot, asset);
      if (!resolved.startsWith(distRoot + path.sep)) {
        check(asset, false, 'Asset path is outside the frontend directory.');
      } else {
        await checkFile(asset, distRoot);
      }
    }
  } catch (error) {
    check('Frontend assets', false, error.message);
  }

  if (backendPresent && verifyBackendHash) {
    try {
      const integritySource = await readFile(path.join(workspaceRoot, 'recovered', 'app', 'dist-electron', 'backendIntegrity.js'), 'utf8');
      const expected = readExpectedBackendHash(integritySource);
      const actual = await sha256(path.join(desktopRoot, 'resources', 'backend', 'backend.exe'));
      check('Backend SHA256 matches the app', actual === expected, actual === expected ? actual : `Expected ${expected}; found ${actual}.`);
    } catch (error) {
      check('Backend SHA256 matches the app', false, error.message);
    }
  } else if (backendPresent) {
    check('Backend SHA256', true, 'Skipped for fast launch; run npm run doctor for full verification.');
  }

  return { ok: checks.every(({ ok }) => ok), workspaceRoot, desktopRoot, userDataDirectory, checks };
}

export function printRuntimeReport(report) {
  for (const { name, ok, detail } of report.checks) {
    console.log(`${ok ? 'OK' : 'FAIL'} ${name}${detail ? `: ${detail}` : ''}`);
  }
  console.log(report.ok ? 'Runtime is ready. Run npm start.' : 'Runtime is not ready. Resolve the failures above, then run npm run doctor.');
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const report = await inspectRuntime();
  if (process.argv.includes('--json')) console.log(JSON.stringify(report, null, 2));
  else printRuntimeReport(report);
  process.exitCode = report.ok ? 0 : 1;
}
