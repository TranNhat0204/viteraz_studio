import fs from 'node:fs';

console.log('--- Patching License Manager for MAX Tier ---');
const managerPath = 'recovered/app/dist-electron/license/manager.js';
let managerContent = fs.readFileSync(managerPath, 'utf8');

const oldEnterprise = "'tier':'enterprise'";
const newMax = "'tier':'max'";
const oldPlan = "'planName':'Personal Pro Lifetime'";
const newPlan = "'planName':'MAX'";

if (!managerContent.includes(oldEnterprise)) {
  console.log('Warning: old enterprise tier string not found in manager.js (already patched?)');
} else {
  managerContent = managerContent.replace(oldEnterprise, newMax);
}

if (!managerContent.includes(oldPlan)) {
  console.log('Warning: old planName string not found in manager.js (already patched?)');
} else {
  managerContent = managerContent.replace(oldPlan, newPlan);
}

fs.writeFileSync(managerPath, managerContent, 'utf8');
console.log('Patched manager.js successfully!');

console.log('--- Patching Frontend Bundle for MAX Tier Enforcement ---');
const bundlePath = 'recovered/app/dist/assets/index-BQXyDjPh.js';
let bundleContent = fs.readFileSync(bundlePath, 'utf8');

const targetH1 = 'function H1(_0x59b808,_0x41e47e){return(Qd[_0x59b808]??-0x13*-0x141+-0x10e4+-0x6ef)>=(Qd[_0x41e47e]??0x19a3*-0x1+-0x10d5*0x1+-0x714*-0x6);}';
const replaceH1 = 'function H1(_0x59b808,_0x41e47e){return true;}';

if (!bundleContent.includes(targetH1)) {
  console.error('ERROR: Target H1 function string not found in index-BQXyDjPh.js!');
} else {
  bundleContent = bundleContent.replace(targetH1, replaceH1);
  console.log('Replaced H1 check to return true unconditionally!');
}

fs.writeFileSync(bundlePath, bundleContent, 'utf8');
console.log('Patched index-BQXyDjPh.js successfully!');
