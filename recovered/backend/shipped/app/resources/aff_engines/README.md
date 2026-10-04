# AFF Engines — Thư viện "kiểu video" cho AI Affiliate

Mỗi file `.md` ở đây = **1 KIỂU VIDEO AFFILIATE** (1 "bộ não" prompt). Chia folder **giống `channel_engines/`**, nhưng **cấu trúc bên trong KHÁC** — bám đúng cách thư viện prompt affiliate thực chiến vận hành: **ảnh keyframe (11 trường) → prompt video từng phân cảnh → ghép**.

Khi user tạo video ở tab **AI Affiliate**, họ chọn **1 engine (kiểu video)** ở đây. Engine giữ NGUYÊN cách quay/dựng/giọng của kiểu đó, chỉ thay `{SẢN_PHẨM}` (crawl từ link) + `{PERSONA}` (nhân vật cố định của kênh, chỉ archetype A).

- **Cấu trúc chuẩn 1 file:** xem [`_TEMPLATE.md`](./_TEMPLATE.md).
- **Chuẩn chất lượng + constants dùng chung (NEGATIVE, DESIGN_LOCK, enum camera/action, hook/cta library, Quality Playbook §10):** [`../../../../docs/aff-engine.md`](../../../../docs/aff-engine.md).
- **Kế hoạch tính năng tổng:** [`../../../../docs/ai-affiliate-plan.md`](../../../../docs/ai-affiliate-plan.md).
- **Pipeline ChatGPT keyframe → Grok image-to-video:** [`../../../../docs/chatgpt-grok-affiliate-image-to-video.md`](../../../../docs/chatgpt-grok-affiliate-image-to-video.md).
- **Nguồn:** thư viện prompt affiliate VN thực chiến "PROMT AI - HỮU ĐẠT MMO" (17 tab Google Sheet) — mỗi tab → 1 engine (chép prompt verbatim) — cộng research thị trường VN/thế giới + prompting Veo/Kling/Nano Banana.

## 3 ARCHETYPE (route theo loại sản phẩm)
- **A — Model-wears-product:** người mẫu/KOC ảo mặc/dùng sản phẩm. Có `{PERSONA}` cố định của kênh. Cốt lõi: consistency nhân vật + camera tilt-up/orbit.
- **B — Product-in-hand (faceless):** review cầm tay, không lộ mặt. Cốt lõi: **DESIGN-LOCK** (khoá 100% hình/màu/logo/đường may), camera cố định.
- **C — Engagement/edu:** nội dung nuôi follower quanh account aff (mascot/kids/nhân hoá). Không gắn sản phẩm trực tiếp.

## Danh mục engine (16)

| # | id | Archetype | Kiểu video | Tab nguồn |
|---|---|---|---|---|
| 01 | `fashion-women` | A | Thời trang nữ — thư viện motion đầy đủ (walk/hair-flip/360/detail...) | THỜI TRANG NỮ |
| 02 | `fashion-men` | A | Thời trang nam — camera tĩnh, khoe form | THỜI TRANG NAM |
| 03 | `fashion-kids` | A | Trẻ em — mirror-selfie mẹ bế bé, micro-expression | THỜI TRANG TRẺ EM |
| 04 | `fashion-midage` | A | Trung niên U50 — da thật, chống AI-face | THỜI TRANG TRUNG NIÊN |
| 05 | `mirror-selfie` | A | Che mặt trước gương — faceless on-ramp (11-field đầy đủ) | MẪU CHE MẶT TRƯỚC GƯƠNG |
| 06 | `treadmill-lifestyle` | A | Trên máy chạy bộ — KOL gesture, camera cố định | MẪU TRÊN MÁY CHẠY BỘ |
| 07 | `in-car-showcase` | A | Ngồi ô tô — outfit trong xe *(enrich từ stub)* | MẪU NGỒI TRÊN OTO |
| 08 | `gallery-projector` | A | Gallery backdrop — chân dung khổng lồ, editorial | Mẫu đứng phía sau máy chiếu |
| 09 | `kol-koc-3scene` | A | ⭐ Outfit-check 3 phân cảnh (viral chuẩn) — **file mẫu gold** | TẠO KOL KOC ẢO |
| 10 | `product-hat` | B | Mũ — cầm tay faceless, 3 bước nhân bản | MŨ |
| 11 | `product-phonecase` | B | Ốp điện thoại — 10 prompt video thực chiến | ỐP ĐIỆN THOẠI |
| 12 | `product-footwear-designlock` | B | Dép/giày — Design-Lock Masterclass (VI+EN), "review vs ăn xổi" | MẪU CÂU LỆNH DÉP |
| 13 | `mannequin-to-model` | B | Ma-nơ-canh → người mẫu / orbit 360 sản phẩm | MANOCANH |
| 14 | `engagement-wealth-mascot` | C | Tăng FL — linh vật/Phật/Thần Tài rải vàng | DẠNG TĂNG FL TIKTOK |
| 15 | `kids-english-edu` | C | Tiếng Anh mẹ bé — Anna & Chibi 3D Pixar, 3 phase/clip | TIẾNG ANH MẸ BÉ |
| 16 | `anthropomorphic-mythbust` | C | Vật dụng nhân hoá — bóc thói quen sai (sức khỏe/gia dụng) | SỨC KHỎE GIA DỤNG |

*(Tab "MẸ CHỒNG NÀNG DÂU" trống trong sheet → chưa dựng; là dạng skit/tiểu phẩm, bổ sung sau khi có nội dung.)*

## Cấu trúc 1 file engine (7 mục — xem `_TEMPLATE.md`)
1. **Tổng quan & cấu trúc phân cảnh** — dùng khi nào, sản phẩm hợp, chuỗi phân cảnh, độ dài.
2. **Kịch bản & lời** — hook + Hook→Problem→Solution→CTA + CTA "giỏ hàng màu vàng" + disclosure (fashion no-thoại thì chỉ hook overlay).
3. **Prompt ảnh keyframe** — 11 trường + golden rules / design-lock + **ví dụ verbatim** (chèn `{SẢN_PHẨM}`/`{PERSONA}`).
4. **Thư viện prompt motion** ⭐lõi — **prompt verbatim từng phân cảnh** của tab (schema *Bối cảnh–Nhân vật–Hành động–Lời thoại–Giọng*), pipeline chọn/ghép.
5. **Ghép & xuất** — beat, safe-zone 9:16, gate chất lượng, disclosure.
6. **Negative & chốt** — DO/DON'T + negative riêng kiểu.
7. **Metadata** — title/caption/hashtag/CTA/disclosure.

## Quality baseline (mọi engine kế thừa — docs/aff-engine.md §10)
- **style_anchor = chỉ định máy/film cụ thể**, KHÔNG "8K/HDR/hyperrealistic" (gây da nhựa/AI-face).
- **skin_realism** (visible pores...) + **2 nguồn sáng** + **shallow DoF/bokeh** + **nền sạch**.
- Gu VN: **high-key + warm + tôn da sáng**; low-key chỉ luxury. **LUT ≤ 75%**.
- Reference workflow: **character-sheet 360 → keyframe 2K → mask-and-place sản phẩm → Veo Ingredients / Kling Elements → beat**.
- Post: upscale 4K → interp 30fps → LUT → grain 5-12% → −14 LUFS.

## Thêm engine mới
Copy `_TEMPLATE.md` → `NN-slug.md`, đặt `id` = slug (= tên file bỏ số), điền frontmatter (archetype/camera_sequence/motion_presets/quality defaults) + 7 mục body. Nếu có tab prompt thực chiến → chép **verbatim** vào mục 4. Loader đọc frontmatter + body làm system-prompt cho pipeline AI Affiliate (mirror cách `channel_engines` được nạp).
