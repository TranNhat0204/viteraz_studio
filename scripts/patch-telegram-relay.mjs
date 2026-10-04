import fs from 'node:fs';
import path from 'node:path';

const files = [
  path.resolve('recovered/app/dist-electron/telegram/relay.js'),
  path.resolve('dist-release/Viteraz-Studio-v1.4.3/resources/app/dist-electron/telegram/relay.js')
];

for (const file of files) {
  if (!fs.existsSync(file)) {
    console.log(`Skipping missing file: ${file}`);
    continue;
  }
  let content = fs.readFileSync(file, 'utf8');

  // Replace cpJson function
  const cpJsonStart = content.indexOf('async function cpJson(');
  const cpJsonEnd = content.indexOf('async function postResult(', cpJsonStart);
  if (cpJsonStart >= 0 && cpJsonEnd >= 0) {
    const safeCpJson = `async function cpJson(_0x46ec84, _0x14e901 = {}) { return { 'status': 503, 'data': null }; }\n`;
    content = content.slice(0, cpJsonStart) + safeCpJson + content.slice(cpJsonEnd);
    console.log(`[OK] Replaced cpJson in ${path.basename(file)}`);
  }

  // Replace link, status, unlink
  const linkStart = content.indexOf('async function link(){');
  const relayStart = content.indexOf('function startTelegramRelay(){');
  if (linkStart >= 0 && relayStart >= 0) {
    const safeTelegramFunctions = `async function link() {
  return { 'ok': false, 'error': 'RELAY_OFFLINE' };
}
async function status() {
  return { 'loggedIn': false, 'linked': false, 'devices': 0 };
}
async function unlink() {
  return { 'ok': true };
}
`;
    content = content.slice(0, linkStart) + safeTelegramFunctions + content.slice(relayStart);
    console.log(`[OK] Replaced link/status/unlink in ${path.basename(file)}`);
  }

  fs.writeFileSync(file, content, 'utf8');
  console.log(`Successfully patched: ${file}`);
}
