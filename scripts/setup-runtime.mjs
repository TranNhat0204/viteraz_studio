// Restore the exact shipped runtime without executing the NSIS installer.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const runtime = path.join(root, '.runtime');
const desktop = path.join(runtime, 'desktop');
const resources = path.join(desktop, 'resources');
const source = path.join(root, 'recovered', 'app');
const marker = path.join(runtime, 'setup.json');
const expectedInstaller = '46b7dcf70bcab02048fe8d99a7ef9df9e762ed46a4fae7c23789b3f4e46049da';
const expectedAsar = 'c27fef737e7128e9ba1038ad0f30ecf4feb9406c07087a8b89132fb8dba164f9';
const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');

function runTar(args, capture = false) {
  const result = spawnSync('tar.exe', args, {
    cwd: root, windowsHide: true, encoding: 'utf8',
    stdio: capture ? 'pipe' : 'inherit', maxBuffer: 32 * 1024 * 1024,
  });
  if (result.error) throw new Error(`Cannot run Windows tar.exe: ${result.error.message}`);
  if (result.status !== 0) throw new Error(`tar.exe failed (${result.status}): ${result.stderr ?? ''}`);
  return result.stdout;
}

function validatePaths(list) {
  const entries = list.split(/\r?\n/).filter(Boolean);
  for (const entry of entries) {
    const normalized = entry.replaceAll('\\', '/');
    if (normalized.startsWith('/') || normalized.includes(':') || normalized.split('/').includes('..')) {
      throw new Error(`Unsafe archive path: ${entry}`);
    }
  }
  if (!entries.includes('resources/app.asar') || !entries.includes('Revo Studio.exe')) {
    throw new Error('Archive does not contain the expected Revo Studio runtime.');
  }
  return entries.length;
}

function prepareApp() {
  const executable = fs.readFileSync(path.join(desktop, 'Revo Studio.exe'));
  const fuse = executable.indexOf(Buffer.from('dL7pKGdnNz796PbbjQWNKmHXBZaB9tsX'));
  // Electron fuse wire: sentinel, version, count, ASCII switch values.
  if (fuse < 0 || executable[fuse + 32] !== 1 || executable[fuse + 33] < 6) {
    throw new Error('Unknown Electron fuse layout; cannot verify support for resources/app.');
  }
  let modified = false;
  const exePath = path.join(desktop, 'Revo Studio.exe');
  // Fuse 4: enableEmbeddedAsarIntegrityValidation
  if (executable[fuse + 34 + 4] === 0x31) {
    executable[fuse + 34 + 4] = 0x30;
    modified = true;
  }
  // Fuse 5: onlyLoadAppFromAsar
  if (executable[fuse + 34 + 5] === 0x31) {
    executable[fuse + 34 + 5] = 0x30;
    modified = true;
  }
  if (modified) {
    fs.writeFileSync(exePath, executable);
    console.log('Flipped Electron fuses (onlyLoadAppFromAsar, enableEmbeddedAsarIntegrityValidation) to allow folder launch.');
  }
  const archive = path.join(resources, 'app.asar');
  const backup = path.join(runtime, 'original-app.asar');
  if (fs.existsSync(archive)) {
    if (sha256(fs.readFileSync(archive)) !== expectedAsar) throw new Error('Original app.asar checksum mismatch.');
    if (!fs.existsSync(backup)) fs.renameSync(archive, backup);
    else {
      if (sha256(fs.readFileSync(backup)) !== expectedAsar) throw new Error('Backup app.asar checksum mismatch.');
      fs.unlinkSync(archive); // Identical generated copy; original retained in backup.
    }
  }
  if (!fs.existsSync(backup)) throw new Error('Missing original-app.asar backup.');
  const app = path.join(resources, 'app');
  if (fs.existsSync(app)) {
    if (fs.realpathSync(app).toLowerCase() !== fs.realpathSync(source).toLowerCase()) {
      throw new Error(`Existing resources/app does not point to ${source}; leaving it untouched.`);
    }
  } else {
    fs.symlinkSync(source, app, 'junction');
  }
}

try {
  if (process.platform !== 'win32' || process.arch !== 'x64') throw new Error('This recovered runtime requires Windows x64.');
  const args = process.argv.slice(2);
  if (args.length > 1 || args[0]?.startsWith('--')) throw new Error('Usage: npm run setup -- [path/to/Revo.Studio.Setup.1.4.3.exe or .zip]');
  if (!fs.existsSync(path.join(source, 'dist-electron', 'main.js'))) throw new Error('Missing recovered/app/dist-electron/main.js.');
  fs.mkdirSync(runtime, { recursive: true });
  if (!fs.existsSync(marker)) {
    let installer = args[0] ? path.resolve(args[0]) : path.resolve(root, '..', 'Revo.Studio.Setup.1.4.3.exe');
    if (!args[0] && !fs.existsSync(installer)) installer = installer.replace(/\.exe$/, '.zip');
    if (!fs.existsSync(installer)) throw new Error('Installer not found. Run npm run setup -- "C:/path/Revo.Studio.Setup.1.4.3.exe"');
    if (path.extname(installer).toLowerCase() === '.zip') {
      const target = path.join(runtime, 'installer');
      fs.mkdirSync(target, { recursive: true });
      runTar(['-xf', installer, '-C', target, 'Revo.Studio.Setup.1.4.3.exe']);
      installer = path.join(target, 'Revo.Studio.Setup.1.4.3.exe');
    }
    console.log('Verifying the original 1.4.3 installer...');
    const bytes = fs.readFileSync(installer);
    if (sha256(bytes) !== expectedInstaller) throw new Error('Installer SHA256 does not match reports/inputs.sha256 (version 1.4.3).');
    const offset = bytes.indexOf(Buffer.from('377abcaf271c', 'hex'));
    if (offset < 0 || offset + 32 > bytes.length) throw new Error('Embedded 7z payload not found.');
    const length = 32n + bytes.readBigUInt64LE(offset + 12) + bytes.readBigUInt64LE(offset + 20);
    if (length > BigInt(bytes.length - offset)) throw new Error('Embedded 7z payload is truncated.');
    const payload = path.join(runtime, 'payload.7z');
    fs.writeFileSync(payload, bytes.subarray(offset, offset + Number(length)));
    const count = validatePaths(runTar(['-tf', payload], true));
    fs.mkdirSync(desktop, { recursive: true });
    if (!fs.existsSync(path.join(desktop, 'Revo Studio.exe'))) {
      console.log(`Extracting ${count} archive entries (first setup only)...`);
      runTar(['-xf', payload, '-C', desktop]);
    } else {
      console.log('Archive entries already extracted in .runtime/desktop.');
    }
    prepareApp();
    fs.writeFileSync(marker, JSON.stringify({ version: '1.4.3', installerSha256: expectedInstaller,
      appAsarSha256: expectedAsar, archiveEntries: count, preparedAt: new Date().toISOString() }, null, 2) + '\n');
    fs.unlinkSync(payload); // Only the temporary payload created above.
  } else {
    const state = JSON.parse(fs.readFileSync(marker, 'utf8'));
    if (state.installerSha256 !== expectedInstaller) throw new Error('Unexpected runtime marker version.');
    prepareApp();
  }
  console.log('Runtime ready. The desktop loads recovered/app through resources/app.');
  console.log('Next: npm run doctor && npm start');
} catch (error) {
  console.error(`Setup failed: ${error.message}`);
  process.exitCode = 1;
}
