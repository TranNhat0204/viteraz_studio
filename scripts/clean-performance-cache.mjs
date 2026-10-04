import { execFileSync } from 'node:child_process';
import { lstat, readdir, realpath, rm, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const userData = path.join(root, '.runtime', 'user-data');
const apply = process.argv.includes('--apply');
const deep = process.argv.includes('--deep');
const unknown = process.argv.slice(2).filter(value => !['--apply', '--deep'].includes(value));
if (unknown.length) throw new Error(`Unknown option: ${unknown.join(', ')}`);

const safeNames = new Set(['Cache', 'Code Cache', 'GPUCache', 'DawnGraphiteCache', 'DawnWebGPUCache']);
const deepNames = new Set(['component_crx_cache', 'optimization_guide_model_store']);

async function measureTree(target) {
  let files = 0;
  let bytes = 0;
  const pending = [target];
  while (pending.length) {
    const current = pending.pop();
    let entries;
    try { entries = await readdir(current, { withFileTypes: true }); } catch { continue; }
    for (const entry of entries) {
      const filename = path.join(current, entry.name);
      if (entry.isDirectory()) pending.push(filename);
      else if (entry.isFile()) {
        try { bytes += (await stat(filename)).size; files++; } catch {}
      }
    }
  }
  return { files, bytes };
}

async function findTargets(target) {
  const matches = [];
  const pending = [target];
  while (pending.length) {
    const current = pending.pop();
    let entries;
    try { entries = await readdir(current, { withFileTypes: true }); } catch { continue; }
    for (const entry of entries) {
      if (!entry.isDirectory()) continue;
      const filename = path.join(current, entry.name);
      const selected = safeNames.has(entry.name) || (deep && deepNames.has(entry.name));
      if (selected) matches.push(filename);
      else pending.push(filename);
    }
  }
  return matches;
}

function studioIsRunning() {
  if (process.platform !== 'win32') return false;
  try {
    const output = execFileSync('tasklist.exe', ['/FI', 'IMAGENAME eq Revo Studio.exe', '/FO', 'CSV', '/NH'], {
      encoding: 'utf8', windowsHide: true,
    });
    return /Revo Studio\.exe/i.test(output);
  } catch (error) {
    throw new Error(`Cannot verify whether Viteraz Studio is running: ${error.message}`);
  }
}

const canonicalRoot = await realpath(userData);
const targets = await findTargets(canonicalRoot);
const rows = [];
for (const target of targets) {
  const info = await lstat(target);
  if (info.isSymbolicLink()) throw new Error(`Refusing to clean symlink: ${target}`);
  const canonicalTarget = await realpath(target);
  if (!canonicalTarget.startsWith(canonicalRoot + path.sep)) {
    throw new Error(`Cache path escaped user-data root: ${canonicalTarget}`);
  }
  rows.push({ target: canonicalTarget, ...(await measureTree(canonicalTarget)) });
}

const totalBytes = rows.reduce((sum, row) => sum + row.bytes, 0);
console.log(`${apply ? 'Cleaning' : 'Dry run:'} ${rows.length} cache directories, ${(totalBytes / 1024 / 1024).toFixed(1)} MB.`);
for (const row of rows.sort((a, b) => b.bytes - a.bytes).slice(0, 20)) {
  console.log(`  ${(row.bytes / 1024 / 1024).toFixed(1).padStart(8)} MB  ${path.relative(canonicalRoot, row.target)}`);
}

if (!apply) {
  console.log('\nNothing was deleted. Close Viteraz Studio, then add -- --apply to clean.');
  if (!deep) console.log('Add -- --deep to also include Chromium component/model caches.');
  process.exit(0);
}
if (studioIsRunning()) throw new Error('Viteraz Studio is running. Close it before cleaning caches.');
for (const row of rows) await rm(row.target, { recursive: true, force: true });
console.log(`Removed ${(totalBytes / 1024 / 1024).toFixed(1)} MB of regenerable cache data.`);
