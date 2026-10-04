import fs from 'node:fs';

const bundlePaths = [
  'recovered/app/dist/assets/index-BQXyDjPh.js',
  'dist-release/Viteraz-Studio-v1.4.3/resources/app/dist/assets/index-BQXyDjPh.js',
];

const oldPrefix = "'banner_title_prefix':_0x491a85(0x276c)+'o'";
const newPrefix = "'banner_title_prefix':'Viteraz\\x20Studio'";

for (const bundlePath of bundlePaths) {
  if (!fs.existsSync(bundlePath)) continue;

  const source = fs.readFileSync(bundlePath, 'utf8');
  const matches = source.split(oldPrefix).length - 1;

  if (matches === 0 && source.includes(newPrefix)) {
    console.log(`[SKIP] ${bundlePath} already uses Viteraz Studio`);
    continue;
  }
  if (matches !== 2) {
    throw new Error(`${bundlePath}: expected 2 Dashboard banner prefixes, found ${matches}`);
  }

  fs.writeFileSync(bundlePath, source.replaceAll(oldPrefix, newPrefix), 'utf8');
  console.log(`[OK] ${bundlePath}: updated Vietnamese and English Dashboard banners`);
}
