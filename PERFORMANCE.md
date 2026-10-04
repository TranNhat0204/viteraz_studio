# Performance audit — 2026-10-02

## Kết quả đo

- Frontend là một bundle tải sẵn khoảng 5.2 MB; riêng bước parse cú pháp bằng Node mất khoảng 0.4 giây.
- Backend executable khoảng 30 MB; đọc và tính SHA-256 mất khoảng 0.1–0.3 giây mỗi lần.
- `.runtime/user-data` đang dùng khoảng 2.50 GB. Trong đó có khoảng 695 MB cache có thể xóa an toàn, hoặc khoảng 1.03 GB nếu tính cả Chromium component/model caches.
- Một phiên Viteraz đang chạy dùng khoảng 1.36 GB working set, gồm Electron, renderer, GPU/audio/video utilities và backend. Chrome thông thường đang mở là tiến trình ngoài Viteraz và không được tính vào nguyên nhân của ứng dụng.
- Renderer ChatGPT ẩn có thể dùng hơn 300 MB và CPU đáng kể khi endpoint kiểm tra trạng thái gọi `getStatusWarm()`. Chưa thay đổi hành vi này vì warm window còn dùng để lấy session/header phục vụ đăng nhập và request ChatGPT.

## Thay đổi đã áp dụng

- Fast launch không còn hash backend hai lần. `npm run doctor` vẫn kiểm tra đầy đủ; Electron main vẫn xác minh integrity trước khi spawn backend.
- Cửa sổ chính được tạo ngay sau khi backend sẵn sàng, không còn chờ license manager, Telegram relay và updater hoàn tất.
- Thêm audit định lượng và công cụ dọn cache có dry-run, chặn symlink/path escape, và từ chối xóa nếu không xác minh được ứng dụng đã đóng.

## Lệnh sử dụng

```powershell
npm run perf:audit
npm run perf:clean-cache
```

Hai lệnh trên chỉ đọc dữ liệu. Muốn xóa cache tái tạo được, đóng Viteraz Studio rồi chạy:

```powershell
npm run perf:clean-cache -- --apply
```

Tùy chọn sâu hơn sẽ xóa thêm Chromium component/model caches; chúng có thể được tải hoặc tạo lại ở lần chạy sau:

```powershell
npm run perf:clean-cache -- --deep --apply
```

## Nút thắt còn lại

- Bundle frontend đã build và obfuscate thành một file lớn, không có source component gốc để code-split/tree-shake an toàn.
- Electron bật `disable-renderer-backgrounding` và `disable-backgrounding-occluded-windows`. Điều này cần cho automation chạy nền nhưng khiến CPU/RAM không hạ nhiều khi cửa sổ bị ẩn.
- Bốn local bridge được khởi tạo tuần tự. Có thể song song hóa ở bản source gốc, nhưng sửa trực tiếp bundle obfuscate có rủi ro làm sai thứ tự cấp port/token cho backend.
- Warm renderer của ChatGPT nên được chuyển sang on-demand hoặc có idle timeout ở lần refactor source kế tiếp; cần regression test login, Cloudflare và generation trước khi bật mặc định.
