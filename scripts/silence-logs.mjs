import fs from 'node:fs';

console.log('=== FIXING TELEGRAM RELAY AND POWERSHELL LOGS ===');

// 1. Patch telegram relay in recovered/app/dist-electron/telegram/relay.js
const relayPath = 'recovered/app/dist-electron/telegram/relay.js';
let relayCode = fs.readFileSync(relayPath, 'utf8');

// Target 1: Disable startTelegramRelay unless explicitly enabled via TELEGRAM_RELAY_ENABLED=1
const targetStart = 'function startTelegramRelay(){';
const newStart = "function startTelegramRelay(){if(process.env.TELEGRAM_RELAY_ENABLED!=='1'){return;}";

if (relayCode.includes(targetStart)) {
  if (relayCode.includes(newStart)) {
    console.log('[telegram/relay.js] startTelegramRelay already guarded!');
  } else {
    relayCode = relayCode.replace(targetStart, newStart);
    console.log('[telegram/relay.js] Patched startTelegramRelay to check TELEGRAM_RELAY_ENABLED!');
  }
} else {
  console.warn('[telegram/relay.js] targetStart not found!');
}

// Target 2: If pull encounters 401 error in pumpLoop, stop polling instead of spamming indefinitely
const targetPumpCatch = "console['warn'](_0x4f562d['ghYoj'],String(_0xcfc878)),await _0x4f562d['zRvFw'](sleep,BACKOFF_MS);";
const newPumpCatch = "if(String(_0xcfc878).includes('401')){running=false;return;}console['warn'](_0x4f562d['ghYoj'],String(_0xcfc878)),await _0x4f562d['zRvFw'](sleep,BACKOFF_MS);";

if (relayCode.includes(targetPumpCatch)) {
  relayCode = relayCode.replace(targetPumpCatch, newPumpCatch);
  console.log('[telegram/relay.js] Patched pumpLoop to stop on 401 error!');
}

fs.writeFileSync(relayPath, relayCode, 'utf8');
console.log('[telegram/relay.js] Saved successfully!');

// 2. Patch dpapiStore in recovered/app/dist-electron/security/dpapiStore.js
const dpapiPath = 'recovered/app/dist-electron/security/dpapiStore.js';
let dpapiCode = fs.readFileSync(dpapiPath, 'utf8');

const targetExec = "{'encoding':_0x502428(0x161)}";
const newExec = "{'encoding':_0x502428(0x161),'stdio':['ignore','pipe','ignore']}";

if (dpapiCode.includes(targetExec)) {
  if (dpapiCode.includes(newExec)) {
    console.log('[security/dpapiStore.js] stdio already guarded!');
  } else {
    dpapiCode = dpapiCode.replace(targetExec, newExec);
    console.log('[security/dpapiStore.js] Patched powershell execSync to ignore stderr!');
  }
  fs.writeFileSync(dpapiPath, dpapiCode, 'utf8');
  console.log('[security/dpapiStore.js] Saved successfully!');
} else {
  console.warn('[security/dpapiStore.js] targetExec not found!');
}

console.log('=== ALL LOG FIXES APPLIED SUCCESSFULLY ===');
