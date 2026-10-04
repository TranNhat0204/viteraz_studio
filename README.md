# RevoStudio 1.4.3 — mã và tài nguyên khôi phục

Đây là kết quả phân tích tĩnh từ `Revo.Studio.Setup.1.4.3.zip` do người dùng cung cấp. Không chạy bộ cài, ứng dụng hay backend. **Đây chưa phải source gốc hoàn chỉnh và chưa phải dự án có thể build/chạy lại.**

## Kết quả

| Thành phần | Kết quả và giới hạn |
| --- | --- |
| Bộ cài | NSIS, chứa payload 7z; đã giải nén 21.721 file để phân tích. Không đưa toàn bộ runtime vào gói này. |
| Electron | Trích xuất nguyên trạng 4.580 file từ `app.asar`, bao gồm dependencies. Package ghi phiên bản 1.4.3. |
| JavaScript ứng dụng | 57 file Electron và 1 bundle giao diện; có bản định dạng dễ đọc. Nhiều file vẫn bị obfuscate; định dạng lại không khôi phục tên biến, comment hay cấu trúc TypeScript gốc. |
| Giao diện | HTML, CSS, ảnh và JavaScript build. Không thấy source map của giao diện chính; không khôi phục được cây component React/TSX nguyên bản. |
| Python backend | PyInstaller, Python 3.12; trích xuất 4.806 module bytecode, gồm 233 module thuộc `app`. |
| Dịch ngược Python | 1.313 code object hàm được dịch thành đoạn Python qua kiểm tra cú pháp; 1.498 hàm chưa dịch được. Các số này tính cả hàm lồng nhau. Không phải tỷ lệ khôi phục toàn ứng dụng. |
| Native backend | 17 module `.pyd` của ứng dụng được giữ nguyên cùng báo cáo PE. Chưa khôi phục thành Python/C/C++ source. |
| IMA2 | Giữ package `ima2-gen` kèm phần dependencies nằm bên trong package và metadata của runtime. Không kèm toàn bộ dependencies ở cấp runtime. |
| Source map IMA2 | Trích xuất 884 nội dung source từ 233 source map, chủ yếu thuộc thư viện đi kèm; không phải 884 file source riêng của RevoStudio. |

## Cấu trúc

- `recovered/app/`: nội dung nguyên trạng của `app.asar`; bắt đầu đọc ở `package.json`, `dist-electron/main.js`, `dist/index.html`.
- `recovered/backend/archive/`: nội dung archive PyInstaller, bao gồm `PYZ.pyz` và entrypoint.
- `recovered/backend/bytecode/`: bytecode `.pyc` Python 3.12; dùng cho phân tích tiếp.
- `recovered/backend/shipped/`: các thư mục `app`, `alembic`, `crawlers`, `tts2` và cấu hình được đóng gói cùng backend; gồm source có sẵn, tài nguyên và native modules.
- `recovered/ima2/`: mã/package IMA2 và metadata dependency.
- `readable/javascript/`: bản JavaScript được định dạng lại, không thay thế bản nguyên trạng.
- `readable/python-partial/`: hàm Python dịch ngược, **chỉ để tham khảo**. Chưa tái tạo đầy đủ imports, class, decorator, default arguments, closure hoặc khởi tạo module. Không nên chạy/import như backend hoàn chỉnh.
- `readable/python-disassembly/`: disassembly đầy đủ của 233 module Python `app`, dùng đối chiếu khi bản dịch ngược thiếu hoặc sai.
- `readable/ima2-sourcemaps/`: nội dung source nhúng trong source map; lưu theo map và chỉ số để tránh trùng tên.
- `reports/`: thống kê, trạng thái từng hàm, kiểm tra JavaScript, hashes đầu vào, thông tin PE và manifest các file.
- `scripts/`: script đã dùng trong phiên phân tích, sử dụng đường dẫn tương đối theo workspace ban đầu; không phải bộ build ứng dụng.

## Mở và kiểm tra

Giải nén gói ZIP rồi mở thư mục `RevoStudio` bằng VS Code. Đọc bản nguyên trạng trong `recovered/` và đối chiếu bản dễ đọc trong `readable/`.

Đã kiểm tra cú pháp bằng `node --check` cho 57 file Electron: 57/57 đạt. Các đoạn Python được đánh dấu thành công đã qua `ast.parse` riêng lẻ. Chưa kiểm thử chức năng, chưa xác minh tương đương ngữ nghĩa, chưa build và chưa kết nối các dịch vụ bên ngoài.

Để tái tạo dự án chạy được còn cần khôi phục cấu trúc frontend, backend đầy đủ (đặc biệt 17 native modules), cấu hình build và dependency/runtime tương thích. Các kiểm tra integrity, bản quyền và xác thực trong file nguyên trạng được giữ nguyên.

Các script Python dùng Python 3.12; định dạng/dịch ngược dùng `jsbeautifier` và `depyf`; giải nén payload dùng `libarchive`. Không thực thi mã trích xuất trong quá trình phân tích. Bản decompile có thể sai ngữ nghĩa dù hợp lệ về cú pháp; bytecode và disassembly là dữ liệu đối chiếu.
