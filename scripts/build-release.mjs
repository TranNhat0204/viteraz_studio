import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

console.log('====================================================');
console.log('   VITERAZ STUDIO — BUILD PORTABLE RELEASE PACKAGE  ');
console.log('====================================================\n');

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const desktopDir = path.join(root, '.runtime', 'desktop');
const recoveredAppDir = path.join(root, 'recovered', 'app');
const userDataDir = path.join(root, '.runtime', 'user-data');
const releaseDir = path.join(root, 'dist-release', 'Viteraz-Studio-v1.4.3');

console.log(`[Target Directory] ${releaseDir}\n`);

// 1. Clean and recreate release directory
if (fs.existsSync(releaseDir)) {
  console.log('[1/6] Cleaning existing release folder...');
  fs.rmSync(releaseDir, { recursive: true, force: true });
}
fs.mkdirSync(releaseDir, { recursive: true });
console.log('[1/6] [OK] Created clean target directory.');

// 2. Copy Electron runtime binaries
console.log('[2/6] Copying Electron core binaries...');
const electronFiles = [
  'chrome_100_percent.pak',
  'chrome_200_percent.pak',
  'd3dcompiler_47.dll',
  'ffmpeg.dll',
  'icudtl.dat',
  'libEGL.dll',
  'libGLESv2.dll',
  'LICENSE.electron.txt',
  'LICENSES.chromium.html',
  'resources.pak',
  'snapshot_blob.bin',
  'v8_context_snapshot.bin',
  'vk_swiftshader.dll',
  'vk_swiftshader_icd.json',
  'vulkan-1.dll',
];

for (const file of electronFiles) {
  const src = path.join(desktopDir, file);
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, path.join(releaseDir, file));
  }
}

// Copy locales directory
const localesSrc = path.join(desktopDir, 'locales');
if (fs.existsSync(localesSrc)) {
  fs.cpSync(localesSrc, path.join(releaseDir, 'locales'), { recursive: true });
}

// Copy and rename executable to Viteraz Studio.exe (and also keep Revo Studio.exe for safety)
const exeSrc = path.join(desktopDir, 'Revo Studio.exe');
if (fs.existsSync(exeSrc)) {
  fs.copyFileSync(exeSrc, path.join(releaseDir, 'Viteraz Studio.exe'));
  fs.copyFileSync(exeSrc, path.join(releaseDir, 'Revo Studio.exe'));
}
console.log('[2/6] [OK] Electron runtime and executables copied.');

// 3. Copy resources (backend, ffmpeg, ima2, elevate)
console.log('[3/6] Copying backend, ffmpeg, ima2...');
const resTargetDir = path.join(releaseDir, 'resources');
fs.mkdirSync(resTargetDir, { recursive: true });

for (const folder of ['backend', 'ffmpeg', 'ima2']) {
  const src = path.join(desktopDir, 'resources', folder);
  if (fs.existsSync(src)) {
    console.log(`      -> Copying resources/${folder}...`);
    fs.cpSync(src, path.join(resTargetDir, folder), { recursive: true });
  }
}

const elevateSrc = path.join(desktopDir, 'resources', 'elevate.exe');
if (fs.existsSync(elevateSrc)) {
  fs.copyFileSync(elevateSrc, path.join(resTargetDir, 'elevate.exe'));
}
console.log('[3/6] [OK] Resources copied.');

// 4. Copy fully patched recovered/app into resources/app (NOT as symlink)
console.log('[4/6] Copying patched Viteraz app files into resources/app...');
const appTargetDir = path.join(resTargetDir, 'app');
fs.cpSync(recoveredAppDir, appTargetDir, { recursive: true });
console.log('[4/6] [OK] Viteraz Studio app source copied.');

// 5. Setup portable clean data folder with pre-bundled offline voice models
console.log('[5/6] Pre-bundling offline Vietnamese voice models...');
const targetModelsDir = path.join(releaseDir, 'data', 'resources', 'revo_voice', 'models');
fs.mkdirSync(targetModelsDir, { recursive: true });

const srcModelsDir = path.join(userDataDir, 'resources', 'revo_voice', 'models');
if (fs.existsSync(srcModelsDir)) {
  const models = fs.readdirSync(srcModelsDir);
  for (const m of models) {
    fs.copyFileSync(path.join(srcModelsDir, m), path.join(targetModelsDir, m));
  }
  console.log(`      -> Bundled ${models.length} voice model files (Ban Mai, Mai, Minh Quang, Ngoc Huyen).`);
}
console.log('[5/6] [OK] Portable data directory prepared (100% clean, no personal data).');

// 6. Create Launchers & Documentation
console.log('[6/6] Generating 1-click launchers and user guide...');

// Launcher BAT (Portable mode)
const batContent = `@echo off
title Khởi động Viteraz Studio
cd /d "%~dp0"
start "" "Viteraz Studio.exe" --user-data-dir="%~dp0data"
`;
fs.writeFileSync(path.join(releaseDir, 'Khoi-Dong-Viteraz-Studio.bat'), batContent, 'utf8');

// Launcher VBS (Silent / No console window)
const vbsContent = `Set WshShell = CreateObject("WScript.Shell")
strPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
WshShell.CurrentDirectory = strPath
WshShell.Run """" & strPath & "\\Viteraz Studio.exe"" --user-data-dir=""" & strPath & "\\data""", 0, False
`;
fs.writeFileSync(path.join(releaseDir, 'Khoi-Dong-Viteraz-Studio.vbs'), vbsContent, 'utf8');

// User Guide TXT
const guideContent = `================================================================================
                    VITERAZ STUDIO v1.4.3 — HƯỚNG DẪN SỬ DỤNG
================================================================================

1. CÁCH KHỞI ĐỘNG PHẦN MỀM:
--------------------------------------------------------------------------------
- Cách 1 (Khuyên dùng): Click đúp vào file "Khoi-Dong-Viteraz-Studio.vbs"
  (Phần mềm sẽ mở lên mượt mà không hiện cửa sổ đen).
- Cách 2: Click đúp vào file "Khoi-Dong-Viteraz-Studio.bat"
- Cách 3: Click đúp trực tiếp vào file "Viteraz Studio.exe"

Toàn bộ dữ liệu của bạn (dự án, kịch bản, cài đặt) sẽ được lưu trữ cục bộ 
trong thư mục "data" ngay bên cạnh phần mềm (Chuẩn Portable, copy sang máy 
khác dùng tiếp bình thường).

2. CẤU HÌNH AI BAN ĐẦU:
--------------------------------------------------------------------------------
Để tạo kịch bản, phân cảnh và dịch tự động, bạn cần cấu hình nhà cung cấp AI:
1. Mở Viteraz Studio -> Vào mục "Cài đặt" (biểu tượng bánh răng).
2. Chọn "AI Dịch & Ảnh" hoặc "AI Nhà cung cấp".
3. Nhập API Key của một trong các nhà cung cấp:
   - Google Gemini (Khuyên dùng, miễn phí & tốc độ cao)
   - DeepSeek (Giá cực rẻ, văn phong kể chuyện rất hay)
   - OpenAI (ChatGPT)
4. Bấm "Lưu" để hoàn tất.

3. KHO GIỌNG ĐỌC TIẾNG VIỆT CÓ SẴN (OFFLINE):
--------------------------------------------------------------------------------
Phần mềm đã được tích hợp sẵn 4 giọng đọc nơ-ron tiếng Việt chất lượng cao 
chạy hoàn toàn Offline trên máy của bạn (không tốn phí API, không cần mạng):
- Ban Mai (Nữ miền Bắc)
- Mai (Nữ miền Nam)
- Minh Quang (Nam miền Bắc)
- Ngọc Huyền (Nữ miền Bắc)

Ngoài ra, bạn có thể sử dụng thêm:
- Edge-TTS (Hàng chục giọng đọc tự nhiên miễn phí của Microsoft)
- Vbee TTS, ElevenLabs (Nếu bạn có tài khoản/API Key riêng)

4. CẤU HÌNH PHẦN CỨNG ĐỀ XUẤT:
--------------------------------------------------------------------------------
- Hệ điều hành: Windows 10 / Windows 11 (64-bit)
- RAM: Tối thiểu 8 GB (Khuyên dùng 16 GB trở lên khi render video dài)
- Bộ nhớ trống: Tối thiểu 5 GB

================================================================================
Chúc bạn sản xuất được nhiều video triệu view với Viteraz Studio!
================================================================================
`;
fs.writeFileSync(path.join(releaseDir, 'HUONG_DAN_SU_DUNG.txt'), guideContent, 'utf8');
console.log('[6/6] [OK] Launchers and guide created.');

console.log('\n====================================================');
console.log('   BUILD HOÀN TẤT! THƯ MỤC RELEASE:');
console.log(`   ${releaseDir}`);
console.log('====================================================\n');

