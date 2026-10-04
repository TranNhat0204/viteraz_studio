import { createHash } from 'node:crypto';
import { createReadStream } from 'node:fs';
import { lstat, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const userData = path.join(root, '.runtime', 'user-data');
const bundle = path.join(root, 'recovered', 'app', 'dist', 'assets', 'index-BQXyDjPh.js');
const backend = path.join(root, '.runtime', 'desktop', 'resources', 'backend', 'backend.exe');
const cacheNames = new Set([
  'Cache',
  'Code Cache',
  'GPUCache',
  'DawnGraphiteCache',
  'DawnWebGPUCache',
  'component_crx_cache',
  'optimization_guide_model_store',
]);

function mb(bytes) {
  return Math.round(bytes / 1024 / 1024 * 10) / 10;
}

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
        try {
          const info = await stat(filename);
          files++;
          bytes += info.size;
        } catch {}
      }
    }
  }
  return { files, bytes };
}

async function findCacheRoots(target) {
  const matches = [];
  const pending = [target];
  while (pending.length) {
    const current = pending.pop();
    let entries;
    try { entries = await readdir(current, { withFileTypes: true }); } catch { continue; }
    for (const entry of entries) {
      if (!entry.isDirectory()) continue;
      const filename = path.join(current, entry.name);
      if (cacheNames.has(entry.name)) matches.push(filename);
      else pending.push(filename);
    }
  }
  return matches;
}

async function hashTiming(filename) {
  const started = performance.now();
  const hash = createHash('sha256');
  for await (const chunk of createReadStream(filename)) hash.update(chunk);
  hash.digest('hex');
  return Math.round(performance.now() - started);
}

const [bundleInfo, backendInfo] = await Promise.all([lstat(bundle), lstat(backend)]);
const topLevel = [];
for (const entry of await readdir(userData, { withFileTypes: true })) {
  if (!entry.isDirectory()) continue;
  const measured = await measureTree(path.join(userData, entry.name));
  topLevel.push({ name: entry.name, ...measured });
}
topLevel.sort((a, b) => b.bytes - a.bytes);

const cacheRoots = await findCacheRoots(userData);
const cacheRows = [];
for (const cacheRoot of cacheRoots) {
  const measured = await measureTree(cacheRoot);
  cacheRows.push({ path: path.relative(userData, cacheRoot), ...measured });
}
cacheRows.sort((a, b) => b.bytes - a.bytes);

const report = {
  frontendBundleMb: mb(bundleInfo.size),
  backendExecutableMb: mb(backendInfo.size),
  backendHashMs: await hashTiming(backend),
  userDataMb: mb(topLevel.reduce((sum, row) => sum + row.bytes, 0)),
  disposableCacheMb: mb(cacheRows.reduce((sum, row) => sum + row.bytes, 0)),
  userDataLargest: topLevel.slice(0, 8).map(row => ({ ...row, mb: mb(row.bytes) })),
  cacheLargest: cacheRows.slice(0, 12).map(row => ({ ...row, mb: mb(row.bytes) })),
  notes: [
    'The 5.5 MB obfuscated frontend is a single eager bundle; safe code-splitting requires the original React source.',
    'Electron starts four local provider bridges before the Python backend.',
    'The runtime keeps renderers active in the background so automation can continue while windows are hidden.',
    'Cache cleanup excludes cookies, sessions, projects, AI models, voices, and ffmpeg resources.',
  ],
};

if (process.argv.includes('--json')) {
  console.log(JSON.stringify(report, null, 2));
} else {
  console.log('Viteraz Studio performance audit');
  console.log(`Frontend bundle: ${report.frontendBundleMb} MB`);
  console.log(`Backend executable: ${report.backendExecutableMb} MB; SHA-256 read: ${report.backendHashMs} ms`);
  console.log(`User data: ${report.userDataMb} MB; disposable cache candidates: ${report.disposableCacheMb} MB`);
  console.log('\nLargest user-data groups:');
  for (const row of report.userDataLargest) console.log(`  ${String(row.mb).padStart(8)} MB  ${row.name}`);
  console.log('\nLargest cache roots:');
  for (const row of report.cacheLargest) console.log(`  ${String(row.mb).padStart(8)} MB  ${row.path}`);
  console.log('\nFindings:');
  for (const note of report.notes) console.log(`  - ${note}`);
  console.log('\nRun "npm run perf:clean-cache" for a dry run of safe cache cleanup.');
}
