import fs from 'node:fs';

const managerPath = 'recovered/app/dist-electron/license/manager.js';
let content = fs.readFileSync(managerPath, 'utf8');

// 1. Locate start of createEngine and end of updateEngine
const cStart = content.indexOf('async function createEngine');
const uEnd = content.indexOf('function _0x29fa');
if (cStart === -1 || uEnd === -1) {
  throw new Error('createEngine / _0x29fa not found in manager.js');
}

// 2. Locate deleteEngine and end of cloneEngine
const dStart = content.indexOf('async function deleteEngine');
const clEnd = content.indexOf('async function forwardToSidecar');
if (dStart === -1 || clEnd === -1) {
  throw new Error('deleteEngine / forwardToSidecar not found in manager.js');
}

const helpersAndCreateAndUpdate = `
const node_fs_engine = require('node:fs');
const node_path_engine = require('node:path');

function getLocalEnginesDir() {
  const candidates = [
    node_path_engine.resolve(__dirname, '../../..', 'backend', '_internal', 'app', 'resources', 'channel_engines'),
    node_path_engine.resolve(__dirname, '../../../..', '.runtime', 'desktop', 'resources', 'backend', '_internal', 'app', 'resources', 'channel_engines'),
    node_path_engine.resolve(__dirname, '../../../..', 'recovered', 'backend', 'shipped', 'app', 'resources', 'channel_engines'),
  ];
  for (const c of candidates) {
    if (node_fs_engine.existsSync(c)) return c;
  }
  return null;
}

function getNextOrder(dir) {
  let maxOrder = 32;
  const files = node_fs_engine.readdirSync(dir);
  for (const f of files) {
    const m = f.match(/^(\\d{2})-.+\\.md$/);
    if (m) {
      const num = parseInt(m[1], 10);
      if (num > maxOrder && num < 99) maxOrder = num;
    }
  }
  return String(maxOrder + 1).padStart(2, '0');
}

function findEngineFile(dir, id) {
  const files = node_fs_engine.readdirSync(dir);
  for (const f of files) {
    if (!f.endsWith('.md')) continue;
    if (f.endsWith('-' + id + '.md') || f === (id + '.md')) {
      return node_path_engine.join(dir, f);
    }
    try {
      const c = node_fs_engine.readFileSync(node_path_engine.join(dir, f), 'utf8');
      if (c.includes('id: ' + id) || c.includes('id: "' + id + '"')) {
        return node_path_engine.join(dir, f);
      }
    } catch {}
  }
  return null;
}

async function reloadBackendEngines() {
  if (sidecar && sidecar.baseUrl && sidecar.token) {
    try {
      await fetch(sidecar.baseUrl + '/api/v1/ai-studio/engines/reload', {
        method: 'POST',
        headers: { 'X-Studio-Token': sidecar.token }
      });
    } catch {}
  }
}

function slugifyEngine(name) {
  if (!name) return 'niche';
  return name.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'niche';
}

function engineToMarkdown(data, id) {
  const meta = data.meta || {};
  const lines = [
    '---',
    'id: ' + id,
    'name: "' + (data.name || meta.name || id).replace(/"/g, '\\\\"') + '"',
    'niche: "' + (data.niche || meta.niche || '').replace(/"/g, '\\\\"') + '"',
    'language: ' + (data.language || meta.language || 'vi'),
    'aspect_ratio: "' + (data.aspect_ratio || data.aspectRatio || meta.aspect_ratio || '16:9') + '"',
    'visual_style: "' + (data.visual_style || data.visualStyle || meta.visual_style || '').replace(/"/g, '\\\\"') + '"',
    'style_anchor: "' + (data.style_anchor || data.styleAnchor || meta.style_anchor || '').replace(/"/g, '\\\\"') + '"',
    'style_lock: "' + (data.style_lock || data.styleLock || meta.style_lock || '').replace(/"/g, '\\\\"') + '"',
  ];
  if (data.tts_mood || meta.tts_mood) lines.push('tts_mood: "' + (data.tts_mood || meta.tts_mood).replace(/"/g, '\\\\"') + '"');
  if (data.music_mood || meta.music_mood) lines.push('music_mood: "' + (data.music_mood || meta.music_mood).replace(/"/g, '\\\\"') + '"');
  if (data.narration_tone || meta.narration_tone) lines.push('narration_tone: "' + (data.narration_tone || meta.narration_tone).replace(/"/g, '\\\\"') + '"');
  if (data.narration_pov || meta.narration_pov) lines.push('narration_pov: "' + (data.narration_pov || meta.narration_pov).replace(/"/g, '\\\\"') + '"');
  lines.push('tags: [custom, user]');
  lines.push('---');
  lines.push('');
  lines.push(data.body || meta.body || '<!-- Custom engine -->');
  return lines.join('\\n');
}

async function createEngine(data) {
  try {
    const dir = getLocalEnginesDir();
    const id = data.id || data.code || ('custom-' + slugifyEngine(data.name || 'style') + '-' + Date.now().toString(36));
    if (dir) {
      const order = getNextOrder(dir);
      const filename = order + '-' + id + '.md';
      const content = engineToMarkdown(data, id);
      node_fs_engine.writeFileSync(node_path_engine.join(dir, filename), content, 'utf8');
      await reloadBackendEngines();
    }
    return { ok: true, code: id };
  } catch (err) {
    return { ok: false, error: err.message || 'CREATE_ENGINE_FAILED' };
  }
}

async function updateEngine(id, data) {
  try {
    const dir = getLocalEnginesDir();
    if (dir) {
      let targetFile = findEngineFile(dir, id);
      if (!targetFile) {
        const order = getNextOrder(dir);
        targetFile = node_path_engine.join(dir, order + '-' + id + '.md');
      }
      const content = engineToMarkdown(data, id);
      node_fs_engine.writeFileSync(targetFile, content, 'utf8');
      await reloadBackendEngines();
    }
    return { ok: true, code: id };
  } catch (err) {
    return { ok: false, error: err.message || 'UPDATE_ENGINE_FAILED' };
  }
}
`;

const newDeleteAndClone = `
async function deleteEngine(id) {
  try {
    const dir = getLocalEnginesDir();
    if (dir) {
      const targetFile = findEngineFile(dir, id);
      if (targetFile && node_fs_engine.existsSync(targetFile)) {
        node_fs_engine.unlinkSync(targetFile);
        await reloadBackendEngines();
      }
    }
    return { ok: true };
  } catch (err) {
    return { ok: false, error: err.message || 'DELETE_ENGINE_FAILED' };
  }
}

async function cloneEngine(id) {
  try {
    const dir = getLocalEnginesDir();
    const newId = id + '-copy-' + Date.now().toString(36);
    if (dir) {
      const targetFile = findEngineFile(dir, id);
      if (targetFile && node_fs_engine.existsSync(targetFile)) {
        const order = getNextOrder(dir);
        const existingContent = node_fs_engine.readFileSync(targetFile, 'utf8');
        let cloned = existingContent.replace(new RegExp('id:\\\\s*' + id), 'id: ' + newId);
        cloned = cloned.replace(/name:\\s*"([^"]+)"/, 'name: "$1 (Bản sao)"');
        node_fs_engine.writeFileSync(node_path_engine.join(dir, order + '-' + newId + '.md'), cloned, 'utf8');
        await reloadBackendEngines();
      }
    }
    return { ok: true, code: newId };
  } catch (err) {
    return { ok: false, error: err.message || 'CLONE_ENGINE_FAILED' };
  }
}
`;

// Replace delete and clone first (so bottom indices don't shift top)
content = content.slice(0, dStart) + newDeleteAndClone + content.slice(clEnd);

// Recompute cStart and uEnd
const newCStart = content.indexOf('async function createEngine');
const newUEnd = content.indexOf('function _0x29fa');
content = content.slice(0, newCStart) + helpersAndCreateAndUpdate + content.slice(newUEnd);

fs.writeFileSync(managerPath, content, 'utf8');
console.log('Successfully updated manager.js with numbered custom engines logic!');

