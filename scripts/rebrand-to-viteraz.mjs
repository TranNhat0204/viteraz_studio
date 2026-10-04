import fs from 'node:fs';
import path from 'node:path';

console.log('====================================================');
console.log('   VITERAZ STUDIO — REBRANDING & DE-LICENSING SCRIPT');
console.log('====================================================\n');

// 1. Patch cpUrl.js — Kill Control Plane phone-home
const cpUrlPath = 'recovered/app/dist-electron/cpUrl.js';
if (fs.existsSync(cpUrlPath)) {
  let content = fs.readFileSync(cpUrlPath, 'utf8');
  const target = "PROD_CP_URL='https://ap'+_0x5eb6ce(0x16a)+_0x5eb6ce(0x161);";
  const replacement = "PROD_CP_URL='http://127.0.0.1:9';";

  if (content.includes(target)) {
    content = content.replace(target, replacement);
    fs.writeFileSync(cpUrlPath, content, 'utf8');
    console.log('[1/9] [OK] cpUrl.js: Revo Control Plane URL redirected to 127.0.0.1:9');
  } else if (content.includes("PROD_CP_URL='http://127.0.0.1:9';")) {
    console.log('[1/9] [SKIP] cpUrl.js: Already redirected to 127.0.0.1:9');
  } else {
    content = content.replace(/PROD_CP_URL=[^;]+;/, "PROD_CP_URL='http://127.0.0.1:9';");
    fs.writeFileSync(cpUrlPath, content, 'utf8');
    console.log('[1/9] [OK] cpUrl.js: Revo Control Plane URL replaced via regex');
  }
} else {
  console.log('[1/9] [WARN] cpUrl.js not found');
}

// 2. Patch updater.js — Disable auto-update to prevent Revo updates
const updaterPath = 'recovered/app/dist-electron/updater.js';
if (fs.existsSync(updaterPath)) {
  let content = fs.readFileSync(updaterPath, 'utf8');
  const target = 'function initUpdater(){';
  const replacement = 'function initUpdater(){return;';

  if (content.includes(target) && !content.includes(replacement)) {
    content = content.replace(target, replacement);
    fs.writeFileSync(updaterPath, content, 'utf8');
    console.log('[2/9] [OK] updater.js: Auto-updater disabled completely');
  } else if (content.includes(replacement)) {
    console.log('[2/9] [SKIP] updater.js: Auto-updater already disabled');
  } else {
    console.log('[2/9] [WARN] updater.js: Target initUpdater() function signature not found');
  }
} else {
  console.log('[2/9] [WARN] updater.js not found');
}

// 3. Patch sidecar.js — Always enforce REVO_LICENSE_ENFORCE = '0'
const sidecarPath = 'recovered/app/dist-electron/sidecar.js';
if (fs.existsSync(sidecarPath)) {
  let content = fs.readFileSync(sidecarPath, 'utf8');
  const targetRegex = /const _0x480f3c\s*=\s*process\.env\.REVO_LICENSE_ENFORCE\s*\?\?\s*\(electron_1\[[^\]]+\]\['isPackaged'\]\s*\?\s*'1'\s*:\s*'0'\);/;
  const replacement = "const _0x480f3c = '0';";

  if (targetRegex.test(content)) {
    content = content.replace(targetRegex, replacement);
    fs.writeFileSync(sidecarPath, content, 'utf8');
    console.log('[3/9] [OK] sidecar.js: Backend license enforcement hardcoded to 0');
  } else if (content.includes("const _0x480f3c = '0';")) {
    console.log('[3/9] [SKIP] sidecar.js: Already hardcoded to 0');
  } else {
    console.log('[3/9] [WARN] sidecar.js: Target REVO_LICENSE_ENFORCE logic not matched');
  }
} else {
  console.log('[3/9] [WARN] sidecar.js not found');
}

// 4. Patch branding.js — Set Viteraz Studio name & App ID
const brandingPath = 'recovered/app/dist-electron/branding.js';
if (fs.existsSync(brandingPath)) {
  let content = fs.readFileSync(brandingPath, 'utf8');
  let updated = false;

  if (!content.includes("exports.APP_NAME = 'Viteraz Studio';")) {
    content += "\nexports.APP_NAME = 'Viteraz Studio';";
    updated = true;
  }
  if (!content.includes("exports.APP_USER_MODEL_ID = 'io.viterazstudio.app';")) {
    content += "\nexports.APP_USER_MODEL_ID = 'io.viterazstudio.app';";
    updated = true;
  }

  if (updated) {
    fs.writeFileSync(brandingPath, content, 'utf8');
    console.log('[4/9] [OK] branding.js: APP_NAME & APP_USER_MODEL_ID set to Viteraz Studio');
  } else {
    console.log('[4/9] [SKIP] branding.js: Already configured for Viteraz Studio');
  }
} else {
  console.log('[4/9] [WARN] branding.js not found');
}

// 5. Patch main.js — Set environment variables right at the start
const mainPath = 'recovered/app/dist-electron/main.js';
if (fs.existsSync(mainPath)) {
  let content = fs.readFileSync(mainPath, 'utf8');
  const envPrefix = "process.env.REVO_LICENSE_ENFORCE = '0'; process.env.REVO_HIDE_BROWSER = '1'; process.env.FLOW_SHOW = '0';\n";

  if (!content.includes("process.env.REVO_LICENSE_ENFORCE = '0';")) {
    content = envPrefix + content;
    fs.writeFileSync(mainPath, content, 'utf8');
    console.log('[5/9] [OK] main.js: Default environment flags injected at startup');
  } else {
    console.log('[5/9] [SKIP] main.js: Environment flags already present');
  }
} else {
  console.log('[5/9] [WARN] main.js not found');
}

// 6. Patch llm_presets.json — OpenRouter X-Title header
const presetsPath = 'recovered/backend/shipped/app/resources/llm_presets.json';
if (fs.existsSync(presetsPath)) {
  let content = fs.readFileSync(presetsPath, 'utf8');
  const target = '"X-Title": "Revo Studio"';
  const replacement = '"X-Title": "Viteraz Studio"';

  if (content.includes(target)) {
    content = content.replace(target, replacement);
    fs.writeFileSync(presetsPath, content, 'utf8');
    console.log('[6/9] [OK] llm_presets.json: OpenRouter X-Title rebranded to Viteraz Studio');
  } else if (content.includes(replacement)) {
    console.log('[6/9] [SKIP] llm_presets.json: Already rebranded');
  } else {
    console.log('[6/9] [WARN] llm_presets.json: X-Title string not found');
  }
} else {
  console.log('[6/9] [WARN] llm_presets.json not found');
}

// 7. Patch recovered/app/package.json — Desktop app metadata
const pkgPath = 'recovered/app/package.json';
if (fs.existsSync(pkgPath)) {
  let pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
  let updated = false;

  if (pkg.name !== 'viteraz-studio-desktop') {
    pkg.name = 'viteraz-studio-desktop';
    updated = true;
  }
  if (pkg.author !== 'Viteraz Studio') {
    pkg.author = 'Viteraz Studio';
    updated = true;
  }
  if (pkg.description !== 'Viteraz Studio — Xưởng sản xuất video AI tự động') {
    pkg.description = 'Viteraz Studio — Xưởng sản xuất video AI tự động';
    updated = true;
  }

  if (updated) {
    fs.writeFileSync(pkgPath, JSON.stringify(pkg, null, 2) + '\n', 'utf8');
    console.log('[7/9] [OK] recovered/app/package.json: Package metadata rebranded');
  } else {
    console.log('[7/9] [SKIP] recovered/app/package.json: Already rebranded');
  }
} else {
  console.log('[7/9] [WARN] recovered/app/package.json not found');
}

// 8. Patch license/manager.js — Silence syncEngines (no remote engine fetch needed)
const managerPath = 'recovered/app/dist-electron/license/manager.js';
if (fs.existsSync(managerPath)) {
  let content = fs.readFileSync(managerPath, 'utf8');
  const target = 'async function syncEngines(_0x28566a){';
  const replacement = 'async function syncEngines(_0x28566a){return true;';

  if (content.includes(target) && !content.includes(replacement)) {
    content = content.replace(target, replacement);
    fs.writeFileSync(managerPath, content, 'utf8');
    console.log('[8/9] [OK] manager.js: syncEngines silenced (using local channel engines)');
  } else if (content.includes(replacement)) {
    console.log('[8/9] [SKIP] manager.js: syncEngines already silenced');
  } else {
    console.log('[8/9] [WARN] manager.js: syncEngines signature not found');
  }
} else {
  console.log('[8/9] [WARN] manager.js not found');
}

// 9. Patch security/mtlsClient.js — Silence ensureClientCertificate (no remote cert needed)
const mtlsPath = 'recovered/app/dist-electron/security/mtlsClient.js';
if (fs.existsSync(mtlsPath)) {
  let content = fs.readFileSync(mtlsPath, 'utf8');
  const target = 'async function ensureClientCertificate(_0x2f4b98){';
  const replacement = "async function ensureClientCertificate(_0x2f4b98){return {certPem:'',privateKeyPem:''};";

  if (content.includes(target) && !content.includes(replacement)) {
    content = content.replace(target, replacement);
    fs.writeFileSync(mtlsPath, content, 'utf8');
    console.log('[9/9] [OK] mtlsClient.js: ensureClientCertificate silenced (no remote mTLS needed)');
  } else if (content.includes(replacement)) {
    console.log('[9/9] [SKIP] mtlsClient.js: ensureClientCertificate already silenced');
  } else {
    console.log('[9/9] [WARN] mtlsClient.js: ensureClientCertificate signature not found');
  }
} else {
  console.log('[9/9] [WARN] mtlsClient.js not found');
}

console.log('\n--- Rebranding and de-licensing completed successfully! ---');
