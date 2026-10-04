---
id: mirror-selfie
name: "Mẫu che mặt trước gương — Mirror Selfie (faceless on-ramp)"
archetype: A
video_type: "mirror-selfie"
niche_default: "Thời trang nữ — người mẫu ảo tạo dáng selfie trước gương, điện thoại che mặt (không lộ mặt)"
niches:
  - label: "Thời trang nữ"
    fits: "váy maxi/bodycon, set đồ, đầm, áo khoác — tôn form dáng"
  - label: "Phụ kiện đi kèm outfit"
    fits: "túi xách, vòng tay, ốp điện thoại — khoe trong bố cục mirror-selfie"
  - label: "Loungewear / clean-girl"
    fits: "đồ mặc nhà đẹp, set thanh lịch, chất vải rủ mềm"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"
final_length: "15-30s"
persona_scope: channel
faceless: true
design_lock: false
recurring_character: "{PERSONA} — nhân vật cố định của kênh (character-sheet đã lưu). FACELESS: điện thoại luôn che mặt nên KHÔNG cần lo drift mặt giữa các clip — lợi thế lớn cho người không muốn lộ mặt."
scene_structure: "Chuỗi mirror-selfie 6-10s: bước lại gần gương → xoay 15-30° khoe form → vuốt thân áo/kéo nhẹ khoe chất vải → nghiêng điện thoại trái-phải → đưa điện thoại sát gương, focus texture vải rồi fade out. Điện thoại đưa ngang mặt che khuất khuôn mặt suốt cả video."
camera_sequence: [FOLLOW_WALK, TURN_45_90, MICRO_TILT_LR, PUSH_IN_SLOW, RACK_FOCUS_TO_PRODUCT]
motion_presets: [mirror_selfie_face_cover]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on smartphone standard lens 24-28mm, vertical mirror selfie, medium-format-style fine film grain, natural color, lifestyle social-media photo,"
image_style_lock: "natural skin texture with visible pores and fine imperfections, natural human proportions, soft diffused window light, deep depth of field (background sharp), vertical 9:16."
golden_rules: ["điện thoại đưa ngang mặt che khuất hoàn toàn khuôn mặt (faceless)", "toàn thân từ đỉnh đầu tới sát gót (cắt nhẹ gấu váy)", "chủ thể center composition, chụp thẳng vào gương eye-level", "phòng gọn gàng sạch sẽ, bỏ mọi UI TikTok để AI tạo hình sạch", "outfit rõ form + màu chuẩn"]
lighting_default: "soft diffused window light from camera-left through sheer voan curtain, gentle rim light on left arm and side, low contrast, airy"
color_look: "clean-girl airy warm-pastel (trắng/kem/xanh dương nhạt/xám nhạt, contrast thấp, tôn da sáng)"
lut_intensity: 45
lens_default: "smartphone standard 24-28mm equivalent, deep depth of field (cả chủ thể và nền đều nét, không xóa phông)"
camera_angle_default: "eye-level chụp thẳng vào gương, full-body center composition, chừa head/foot room"
background_default: "phòng ngủ hiện đại thanh lịch gọn gàng: rèm voan trắng + rủ nâu/be bên trái, giường ga xám nhạt + nightstand đen viền vàng + cây thủy sinh bên phải, sàn gỗ nâu ấm"
skin_realism: "natural skin texture with visible pores and fine imperfections, natural human proportions"
negative_constant: "morphing body, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, phone screen showing a face, flickering, inconsistent lighting, messy cluttered room, TikTok UI overlay, watermark, text overlay"
motion_strength: "subtle_to_moderate"
reference_workflow: "character-sheet body 360 (front+45°+90°+back, mặt che bởi phone) → keyframe 9:16 2K mirror-selfie 11 trường → (mặc {SẢN_PHẨM} bằng mask-and-place giữ nguyên tư thế cầm phone) → Veo Ingredients/Kling Elements → 5 beat clip chuyển động"
post_chain: "upscale 4K → interp 30fps → LUT clean-airy ~45% → grain 8% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients/first-last) / Kling 2.5-2.6 Cinematic — image-to-video"
tts_mood: "không thoại — nhạc nền thời trang nhẹ"
music_mood: "nhạc trend TikTok clean-girl, beat rõ để cắt cảnh"
tags: [mirror-selfie, che-mat, faceless, koc-ao, thoi-trang, chup-guong, clean-girl, tiktok-shop, affiliate, ootd]
---

# AFF Engine — Mẫu che mặt trước gương (Mirror Selfie)

> **Kiểu:** A (người mẫu ảo mặc/khoe outfit) nhưng **FACELESS on-ramp** — cầm điện thoại đưa ngang mặt tạo dáng mirror-selfie, mặt bị điện thoại che khuất. **Dùng khi:** chủ kênh KHÔNG muốn lộ mặt mà vẫn muốn khoe outfit người thật đứng trước gương (clean-girl aesthetic đang viral). Vì mặt luôn bị che → AI không lo morph mặt, rất ổn định.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl) + `{PERSONA}` (nhân vật cố định của kênh — dùng lại character-sheet đã lưu; chỉ cần khoá dáng người/tóc/tay, không cần khoá mặt).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc (verbatim từ tab):** chuỗi mirror-selfie 6-10s — ① **bước nhẹ từ xa lại gần gương** (váy bay nhẹ, vải mềm thoáng) → ② **xoay người 15-30° chậm rãi** (tà áo lay động, khoe độ rủ) → ③ **vuốt/kéo nhẹ thân áo** (khoe độ mịn, co giãn, form dáng) → ④ **nghiêng điện thoại trái-phải** (outfit chuyển động nhẹ theo góc quay) → ⑤ **đưa điện thoại sát gương, focus vào texture vải rồi fade out**. Điện thoại đưa ngang mặt che khuất khuôn mặt suốt video.
- **Sản phẩm hợp:** đồ mặc được tôn form (váy maxi/bodycon, set, đầm, loungewear) + phụ kiện đi kèm (túi, vòng). **Persona:** nhân vật cố định của kênh nhưng **FACELESS** — chỉ khoá dáng/tóc/tay cầm phone.
- **Vì sao mượt, ít lỗi:** mặt bị điện thoại che → bỏ hẳn rủi ro "morph mặt mỗi 12 frame" (lỗi AI phổ biến nhất); mỗi clip chỉ 1 camera-move + 1 action; nhân vật đứng/xoay nhẹ nên vải ít warp. Đây là on-ramp an toàn nhất cho người mới, không cần character-sheet mặt.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền + text overlay. (Muốn voiceover review thì bật `dialogue_mode: vi_voiceover`, dùng khung Hook→Problem→Solution→CTA ở docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng tò mò/khoe không lộ mặt — ví dụ "Outfit hôm nay nhưng giấu mặt 🙈", "Set này chụp gương xịn hơn tưởng ✨", "Mặc đồ này đi đâu cũng auto sang". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** điểm nhấn {SẢN_PHẨM} ngắn (chất liệu rủ mềm, form bodycon, màu pastel).
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)
- **Text overlay đặc trưng:** "Outfit hôm nay ✨" (mở) · "Link ở bio" (cuối).

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền **11 trường** theo `{PERSONA}` + `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`. Đây là tab có spec ảnh ĐẦY ĐỦ nhất — dùng nguyên khung 11 trường:

1. **Chủ thể:** giới tính (nữ), chủng tộc (châu Á Á Đông), tuổi (~20-25), ngoại hình (dáng thon thả thanh mảnh, vai gầy, da trắng sáng).
2. **Quần áo / Outfit:** {SẢN_PHẨM} tả chi tiết — kiểu dáng, form, màu nền + họa tiết, thiết kế cổ/dây/bèo, phụ kiện đi kèm (vòng tay, túi xách).
3. **Kiểu tóc:** tóc nâu đen búi cao messy bun, lọn mai uốn nhẹ buông hai bên má và gáy.
4. **Tư thế & vị trí cơ thể:** đứng thẳng tạo dáng selfie trước gương, hông đẩy nhẹ sang phải tạo đường cong; tay trái cầm điện thoại (ốp sáng, cụm 3 camera) đưa **ngang mặt** để chụp, khuỷu tay trái móc quai túi; tay phải giang nhẹ thả lỏng; hướng trực diện vào gương/camera.
5. **Biểu cảm khuôn mặt:** **khuôn mặt BỊ CHE KHUẤT HOÀN TOÀN bởi điện thoại** (faceless) — phong cách MXH điệu đà nhưng tự nhiên, thư giãn.
6. **Góc máy & cỡ cảnh:** eye-level chụp thẳng vào gương; **toàn thân** (đỉnh đầu → sát gót, cắt nhẹ gấu váy); center composition, tỉ lệ dọc.
7. **Ánh sáng:** ánh sáng tự nhiên từ cửa sổ bên **trái** + ánh dịu môi trường; rất mềm (khuếch tán qua rèm voan), rim light nhẹ ở cánh tay/lườn trái; **low contrast** dịu mắt bồng bềnh.
8. **Môi trường & nền:** phòng ngủ hiện đại thanh lịch — trái: rèm 2 lớp (voan trắng + rủ nâu/be); phải sau: giường ga xám nhạt + nightstand đen viền vàng + cây thủy sinh nhỏ; sàn gỗ nâu ấm. **Nền rõ ràng, gọn gàng, KHÔNG lộn xộn; bỏ mọi UI TikTok để AI tạo hình sạch.**
9. **Màu sắc & color grading:** tông pastel nhẹ tươi sáng (trắng/kem/xanh dương nhạt/xám nhạt), contrast thấp; airy, soft, **clean girl aesthetic**, thiên warm pastel.
10. **Phong cách nhiếp ảnh:** Lifestyle + Fashion + Social media mirror selfie.
11. **Ống kính & DoF:** camera tiêu chuẩn điện thoại (~24-28mm), **KHÔNG xóa phông**, **deep depth of field** (cả chủ thể lẫn nền đều sắc nét). + **Mức độ realism:** ảnh chụp thật (photorealistic), đời thường, độ phân giải kiểu video MXH; tỉ lệ **9:16**.

- **Golden rules (verbatim):** điện thoại đưa ngang mặt **che kín mặt** · **toàn thân** đỉnh đầu→gót · center + eye-level chụp thẳng gương · phòng **gọn gàng sạch** (bỏ UI TikTok) · outfit rõ form + màu chuẩn. Khác biệt rẻ↔premium ở đây = **ánh sáng mềm (soft window) + nền gọn**, KHÔNG phải "8K/HDR".
- **Ví dụ VERBATIM (mirror-selfie, thay chỗ động bằng {biến}):**
  ```
  shot on smartphone standard lens 24-28mm, vertical mirror selfie, medium-format-style fine film grain, natural color, lifestyle social-media photo,
  Một {PERSONA: cô gái châu Á Á Đông khoảng 20-25 tuổi, dáng thon thả thanh mảnh, vai gầy, da trắng sáng}, tóc nâu đen búi cao messy bun với vài lọn mai uốn nhẹ buông hai bên má và gáy.
  Cô mặc {SẢN_PHẨM: mô tả outfit chi tiết — kiểu dáng, form, màu nền + họa tiết, thiết kế cổ/dây/bèo}, đeo một chiếc vòng tay vàng mỏng tay phải và xách túi da be/trắng sữa khoá kim loại.
  Cô đứng thẳng tạo dáng selfie trước gương, hông đẩy nhẹ sang phải tạo đường cong; tay trái cầm điện thoại (ốp sáng, cụm 3 camera) đưa NGANG MẶT để chụp — KHUÔN MẶT BỊ ĐIỆN THOẠI CHE KHUẤT HOÀN TOÀN; khuỷu tay trái móc quai túi; tay phải giang nhẹ thả lỏng gần rèm cửa.
  Góc eye-level chụp thẳng vào gương, toàn thân từ đỉnh đầu tới sát gót (cắt nhẹ ở gấu váy), center composition.
  Bối cảnh {background_default: phòng ngủ hiện đại thanh lịch — trái có rèm voan trắng + lớp rủ nâu/be; phải sau có giường ga xám nhạt, nightstand đen viền vàng, cây thủy sinh nhỏ; sàn gỗ nâu ấm; nền gọn gàng sạch sẽ không lộn xộn}.
  Ánh sáng tự nhiên mềm từ cửa sổ bên trái qua rèm voan, rim light nhẹ ở cánh tay và lườn trái, low contrast dịu mắt; tông pastel airy clean-girl (trắng/kem/xanh dương nhạt/xám nhạt); deep depth of field cả chủ thể và nền đều nét,
  natural skin texture with visible pores and fine imperfections, natural human proportions, soft diffused window light, deep depth of field (background sharp), vertical 9:16.
  ```
- **Nhân bản:** giữ NGUYÊN {PERSONA} + {SẢN_PHẨM} + tư thế cầm phone che mặt, chỉ đổi bối cảnh (đổi phòng/gương/ánh sáng) để ra thêm keyframe làm start/end frame khác nhau.

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip** (chống méo). Giữ "cô gái mặc outfit + cầm phone che mặt như ảnh gốc" (reference-chaining). Bake `negative_constant` cuối mỗi prompt.
> PHẦN LÕI — chép NGUYÊN VĂN bộ prompt chuyển động của tab thành 1 menu; pipeline chọn/ghép 5 cảnh. Điểm nhấn faceless: **điện thoại LUÔN che mặt suốt mọi clip** (`MIRROR_SELFIE_FACE_COVER`).

**Phân cảnh 1 — Bước lại gần gương (`FOLLOW_WALK` + `MIRROR_SELFIE_FACE_COVER`):**
```
Bối cảnh: phòng ngủ hiện đại thanh lịch, ánh sáng cửa sổ mềm bên trái qua rèm voan, nền gọn gàng.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, tay trái cầm điện thoại đưa ngang mặt che khuất mặt, giữ nguyên dáng/tóc/tay.
Hành động: nhân vật bước nhẹ từ xa lại gần gương, váy bay nhẹ theo chuyển động, tạo cảm giác vải mềm và thoáng. Điện thoại giữ nguyên che mặt.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền thời trang.
[negative_constant]
```
**Phân cảnh 2 — Xoay người 15-30° khoe form (`TURN_45_90` + `MIRROR_SELFIE_FACE_COVER`):**
```
Bối cảnh: giống phân cảnh trước, ánh sáng ổn định.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, điện thoại vẫn che mặt.
Hành động: xoay người 15-30 độ chậm rãi, tà áo lay động tự nhiên để làm nổi bật độ rủ của chất vải; sau đó vuốt nhẹ phần thân áo thể hiện độ mịn và mềm mại của chất liệu.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 3 — Kéo nhẹ khoe co giãn & form (`PUSH_IN_SLOW` + `STRETCH_FABRIC`):**
```
Bối cảnh: trước gương, ánh sáng mềm không lóa.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, điện thoại che mặt.
Hành động: nhân vật hơi nghiêng người, kéo nhẹ phần áo để cho thấy độ co giãn và form dáng thoải mái; camera tiến chậm lại gần khoe chất liệu.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 4 — Nghiêng điện thoại trái-phải (`MICRO_TILT_LR` + `MIRROR_SELFIE_FACE_COVER`):**
```
Bối cảnh: trước gương, phản chiếu ánh sáng làm nổi bật bề mặt vải.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, điện thoại che mặt.
Hành động: nhân vật cầm điện thoại, hơi nghiêng máy sang trái phải, outfit chuyển động nhẹ theo góc quay; ánh sáng phản chiếu trên gương lấp lánh trên bề mặt vải.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 5 — Đưa phone sát gương → focus texture → fade out (`RACK_FOCUS_TO_PRODUCT`):**
```
Bối cảnh: sát mặt gương, ánh sáng mềm.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, điện thoại che mặt.
Hành động: kết thúc bằng việc đưa điện thoại sát gương, camera focus vào texture vải (thớ vải, độ rủ, độ mịn cao cấp) rồi từ từ fade out.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> **Lấy thêm câu lệnh (tab dạy):** ① Tải ảnh keyframe mirror-selfie lên ChatGPT → ② nhập "tạo cho tôi 20 câu lệnh chuyển động của nhân vật để quảng cáo cho bộ quần áo đang mặc và chất vải" → ③ dùng câu lệnh mới kèm ảnh cho vào Veo 3 tạo video. Chọn ~5 câu hợp nhịp làm menu clip.
> Kỹ thuật giữ nhân vật: **Veo first+last frame** hoặc **Kling Elements (2-4 ref = character-sheet body + keyframe)**; motion strength **Subtle→Moderate** để vải/tóc không morph. Vì mặt bị che nên không cần khoá facial tokens — nhẹ gánh identity.

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- Import 5 clip AI → **cắt đúng nhịp beat** nhạc trend TikTok clean-girl → thứ tự ①②③④⑤; đổi độ dài shot 1-8s (đừng đều 3-4s → lộ AI); hard-cut mặc định.
- Text nhẹ trong safe-zone 9:16 (chừa top 10% / bottom 20% / right 10%): "Outfit hôm nay ✨" (mở), điểm nhấn {SẢN_PHẨM} (giữa), "Link ở bio" (cuối).
- Gate chất lượng (docs/aff-engine.md §7, §10): color grade thống nhất clean-airy warm ~45%, grain 8%, −14 LUFS.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `morphing body, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, phone screen showing a face, flickering, inconsistent lighting, messy cluttered room, TikTok UI overlay, watermark, text overlay` + kế thừa NEGATIVE chung §5.5 (`no text/subtitles/logos/watermark`, `giữ 100% hình/màu/logo/đường may sản phẩm`) + `no cartoon/3D render`.
- **DO:** điện thoại **luôn che kín mặt** qua cả 5 clip (faceless); ảnh phải toàn thân + eye-level chụp thẳng gương; phòng **gọn gàng sạch** (bỏ UI TikTok); 1 camera-move + 1 action/clip; giữ nguyên outfit/dáng/tay cầm phone.
- **DON'T:** đừng để lộ mặt hay để màn hình điện thoại hiện ra một khuôn mặt; đừng xoay/nghiêng quá nhanh (morph vải); đừng để phòng bừa bộn hay lọt UI TikTok; đừng dùng "8K/HDR" (da nhựa); đừng để chân dính đáy khung / CTA vào 20% đáy.

## 7. METADATA
- **Title** <70 ký tự: mirror-selfie che mặt + điểm nhấn (vd "Chụp gương giấu mặt mà outfit vẫn auto sang 🤍").
- **Caption + 15-25 hashtag** ngách thời trang/clean-girl (#outfit #ootd #mirrorselfie #reviewdo #cleangirl #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
