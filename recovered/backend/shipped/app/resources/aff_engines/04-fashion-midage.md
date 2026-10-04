---
id: fashion-midage
name: "Thời trang TRUNG NIÊN — Người mẫu ảo U50 khoe form (da thật, chống AI-face)"
archetype: A
video_type: "outfit-showcase-midage"
niche_default: "Thời trang nữ trung niên — người mẫu ảo U50 bước ra khoe dáng/khoe form trong showroom"
niches:
  - label: "Đầm/áo dài trung niên"
    fits: "đầm dự tiệc, áo dài cách tân, set áo-quần trung niên"
  - label: "Set công sở U50"
    fits: "áo sơ mi, blazer, quần âu, chân váy dáng thanh lịch"
  - label: "Áo khoác / len mùa lạnh"
    fits: "áo khoác dạ, cardigan, len — khoe form + chất liệu"
  - label: "Áo dài truyền thống"
    fits: "áo dài lụa, gấm — cần khóa hoa văn/họa tiết 100%"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-8s"
final_length: "15-30s"
persona_scope: channel
faceless: false
design_lock: false
recurring_character: "{PERSONA} — phụ nữ Việt Nam 50-55 tuổi, cao ~1m60, dáng đẹp, khuôn mặt sáng thần thái, tóc thời trang gọn gàng, DA THẬT có texture (dùng character-sheet đã lưu, giữ y hệt)"
scene_structure: "Người mẫu bước nhẹ 1-2 bước về phía camera rồi dừng → xoay người rất nhẹ 10-15° khoe form → nhìn camera cười nhẹ. Full-body chính diện, chủ thể ~80% chiều cao khung. 6-8s. Gentle motion, showroom mờ bokeh."
camera_sequence: [WALK_IN_TO_STOP, GENTLE_TURN_10_15, HOLD_SMILE_TO_CAMERA]
motion_presets: [fashion_midage_gentle_showcase]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, medium-format-style film grain, natural color, real-life documentary fashion photo, warm soft showroom light,"
image_style_lock: "real skin texture with visible pores and fine imperfections, no beauty-filter, no plastic skin, natural human proportions, warm soft showroom light, vertical 9:16."
golden_rules: ["DA THẬT có texture — TUYỆT ĐỐI không AI-face, không beauty-filter giả, không plastic skin", "GIỮ NGUYÊN 100% thiết kế/màu sắc/hoa văn/logo trang phục theo ảnh tham chiếu", "toàn thân chính diện, chủ thể chiếm ~80% chiều cao khung, chân gần chạm mép dưới", "DoF mạnh — nét căng mặt + trang phục, nền showroom mờ bokeh", "chọn ảnh đẹp nhất mới làm video"]
lighting_default: "warm soft showroom light from ceiling + side mirrors, gentle falloff, face clearly lit, no harsh shadows, real skin tone"
color_look: "warm-clean realistic (lifted shadows nhẹ, giữ highlight, da ấm THẬT, KHÔNG over-process)"
lut_intensity: 45
lens_default: "85mm portrait look, strong shallow depth of field (f/1.8), subject tack-sharp, showroom background softly blurred bokeh"
camera_angle_default: "full-body frontal, camera đặt tầm thấp trung bình ngang hông (chân tự nhiên, thân cân đối), hướng thẳng vào nhân vật"
background_default: "cửa hàng thời trang nữ trung niên cao cấp: kệ treo đồ, mannequin, gương, lọ hoa lan trắng, rèm nhung xám, ánh đèn showroom ấm — luôn mờ bokeh"
skin_realism: "real skin texture with visible pores and fine imperfections, micro-expression lines, slight under-eye texture, natural human proportions, no beauty-filter, no plastic skin"
negative_constant: "AI-face, plastic skin, beauty-filter giả, waxy airbrushed skin, morphing faces, identity change, đổi thiết kế/màu/hoa văn trang phục, logo lạ, chữ/biển quảng cáo mới, distorted hands, extra fingers, extra people, trẻ em, warped proportions, flickering, inconsistent lighting, watermark, text overlay, cartoon, CGI, 3D render"
motion_strength: "subtle"
reference_workflow: "character-sheet 360 U50 (front+45°+90°+back, DA THẬT) → keyframe 9:16 2K full-body ~80% khung → mask-and-place {SẢN_PHẨM} khóa thiết kế 100% → Veo Ingredients/Kling Elements → 3 beat gentle"
post_chain: "upscale 4K → interp 30fps → LUT warm-clean 45% → grain 8-10% → −14 LUFS + nhạc nền nhẹ"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3 Flow (Ingredients/first-last) / Kling 2.5-2.6 Cinematic — image-to-video"
tts_mood: "không thoại — nhạc nền thời trang nhẹ nhàng, sang trọng"
music_mood: "nhạc trend TikTok êm/sang, beat rõ để cắt cảnh"
tags: [thoi-trang-trung-nien, U50, nguoi-mau-ao, khoe-form, showroom, da-that, anti-ai-face, fashion, tiktok-shop, affiliate]
---

# AFF Engine — Thời trang TRUNG NIÊN · Người mẫu ảo U50 khoe form

> **Kiểu:** A (người mẫu ảo mặc/khoe trang phục) · **Dùng khi:** đồ mặc được cho phụ nữ trung niên (đầm/áo dài/set công sở/áo khoác). Tạo cảm giác một người phụ nữ U50 duyên dáng, DA THẬT tự nhiên, bước ra khoe form trong showroom cao cấp — chạm đúng tệp khách 45-60 tuổi. **Bí quyết viral & chống rẻ: da thật có texture, TUYỆT ĐỐI không AI-face/beauty-filter giả.**
> Input: `{SẢN_PHẨM}` (tên/ảnh tham chiếu/giá/chất liệu đã crawl — KHÓA thiết kế 100%) + `{PERSONA}` (nhân vật U50 cố định của kênh).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc (verbatim từ tab):** Người mẫu **bước nhẹ 1-2 bước** về phía camera rồi dừng → **xoay người rất nhẹ 10-15 độ** để khoe form → **nhìn vào camera với nụ cười nhẹ.** Tay và dáng đứng tự nhiên, không tạo dáng quá lố. Khung **full-body (đầu tới chân)**, chủ thể chiếm **~80% chiều cao khung**, chân gần chạm mép dưới. **Thời lượng 6-8 giây.**
- **Sản phẩm hợp:** đồ mặc được cho phụ nữ trung niên (đầm, áo dài, set công sở, áo khoác/len). **Persona:** BẮT BUỘC nhân vật U50 cố định của kênh (đồng bộ thương hiệu, DA THẬT có texture).
- **Vì sao mượt, ít lỗi:** chuyển động rất nhẹ nhàng (gentle) — bước ngắn + xoay nhỏ + đứng yên cười; camera handheld nhẹ (không rung mạnh); nhân vật không tạo dáng lố → ít biến dạng vải/tay. **DoF mạnh** giấu showroom, giữ nét mặt + đường may + logo.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền + text overlay. (Nếu kênh muốn voiceover review, bật `dialogue_mode: vi_voiceover`, dùng khung Hook→Problem→Solution→CTA giọng ấm trung niên ở docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng hợp tệp U50 — ví dụ "Tuổi này mặc set này là chuẩn ✨", "Đầm dự tiệc cho mẹ, sang mà nhẹ nhàng", "Dáng đẹp không kể tuổi". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** tên/điểm nhấn {SẢN_PHẨM} (chất liệu, form dáng tôn người trung niên).
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "shop có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền 11 trường theo `{PERSONA}` + `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`.
- **Golden rules (verbatim từ tab):** DA THẬT có texture · **TUYỆT ĐỐI không AI-face / không beauty-filter giả / không plastic skin** · giữ NGUYÊN 100% thiết kế/màu/hoa văn/logo trang phục theo ảnh tham chiếu · toàn thân chính diện, chủ thể **~80% chiều cao khung**, chân gần chạm mép dưới · **DoF mạnh** nền mờ.
- **Ví dụ VERBATIM (từ tab, thay chỗ động bằng {SẢN_PHẨM}/{PERSONA}):**
  ```
  Tạo ảnh người mẫu Phụ Nữ trung niên 50 tuổi khuôn mặt sáng thần thái, mái tóc thời trang,
  chiều cao khoảng 1m60 dáng đẹp, người việt nam mặc chính xác trang phục như trong ảnh tham chiếu
  ({SẢN_PHẨM} — giữ nguyên thiết kế, màu sắc và hoa văn của áo và quần).

  Bối cảnh nền phía sau... đứng trong Cửa hàng thời trang nữ cao cấp, ánh sáng ấm vàng từ trần và
  hai bên gương, hiệu ứng phản chiếu bóng mờ trên nền sàn bóng, decor gồm lọ hoa lan trắng và rèm nhung xám.

  Làm sắc nét TẬP TRUNG NỔI BẬT vào người mẫu trang phục và sáng khuôn mặt, làm mờ hậu cảnh nền phía sau.

  Góc chụp: Toàn thân chính diện, lấy trọn người từ đầu đến chân và chân gần chạm mép dưới cùng của ảnh,
  người mẫu đứng giữa khung hình.

  Tỷ lệ nhân vật: Chiếm 80% chiều cao khung hình, chiều ngang 50% bề rộng ảnh,
  phần đầu ở 1/10 phía trên, bàn chân gần chạm mép dưới.

  Máy ảnh: đặt ở tầm thấp trung bình ngang hông người chụp giúp cơ thể cân đối và chân trông tự nhiên,
  hướng thẳng về phía nhân vật, lấy chiều sâu không gian phía sau.

  Biểu cảm: Nụ cười tươi, ánh mắt nhìn về phía camera, tự tin tạo dáng đứng khoe dáng người và trang phục.

  Ánh sáng: tự nhiên, cho thấy rõ mặt của người mẫu và trang phục.

  Chất lượng: phong cách chụp đời thực, ánh sáng ấm dịu,
  real skin texture with visible pores and fine imperfections, no beauty-filter, no plastic skin,
  natural human proportions, vertical 9:16.
  ```
  > ⚠️ **Lưu ý chống AI-face:** tab gốc ghi "8K" — theo Quality Playbook §10.2, "8K/HDR/hyperrealistic" đẩy sang **da nhựa/AI-face**. Engine này **thay 8K bằng film-stock + real skin texture** (đã áp ở khối cuối trên) để giữ DA THẬT.
- **Nhân bản:** giữ NGUYÊN {PERSONA} + {SẢN_PHẨM} (khóa thiết kế 100%), chỉ đổi góc showroom để ra thêm keyframe (dùng làm start/end frame khác nhau).

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip** (chống méo). Giữ "người mẫu U50 mặc {SẢN_PHẨM} như ảnh gốc, DA THẬT" (reference-chaining). Bake `negative_constant` cuối mỗi prompt. Camera **HANDHELD_SHAKE nhẹ / slow**, motion strength **Subtle**.

**Phân cảnh 1 — Bước nhẹ 1-2 bước tiến vào (`WALK_IN_TO_STOP`):**
```
Bối cảnh: cửa hàng thời trang nữ trung niên (kệ treo đồ, mannequin, gương, ánh đèn showroom ấm), hậu cảnh luôn mờ bokeh.
Nhân vật: {PERSONA} — phụ nữ Việt Nam 50-55 tuổi, cao ~1m60, dáng đẹp, khuôn mặt sáng thần thái, DA THẬT tự nhiên (có texture da), TUYỆT ĐỐI không AI-face/không giả; mặc {SẢN_PHẨM} như ảnh gốc (giữ nguyên 100% thiết kế/màu/hoa văn/logo).
Hành động: người mẫu bước nhẹ 1-2 bước về phía camera rồi dừng lại. Tay và dáng đứng tự nhiên, không tạo dáng quá lố. Camera tầm mắt, full-body (đầu tới chân), máy quay ổn định, chuyển động rất nhẹ kiểu handheld (không rung mạnh). DoF mạnh: nét căng trên mặt và trang phục (chi tiết vải/đường may/logo rõ), nền mờ.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền thời trang nhẹ.
[negative_constant]
```
**Phân cảnh 2 — Xoay người rất nhẹ 10-15° khoe form (`GENTLE_TURN_10_15`) — quan trọng nhất:**
```
Bối cảnh: cửa hàng thời trang nữ trung niên, ánh sáng showroom mềm ổn định, hậu cảnh mờ bokeh.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, DA THẬT có texture, giữ nguyên khuôn mặt/tóc/trang phục.
Hành động: người mẫu xoay người rất nhẹ 10-15 độ để khoe form dáng trang phục, tay và dáng đứng tự nhiên, không tạo dáng quá lố. Vải chuyển động mềm mại chân thực theo cơ thể, giữ đúng chất liệu/độ rủ như ảnh tham chiếu. Camera tầm mắt full-body, chuyển động rất nhẹ handheld (không rung mạnh), DoF mạnh nét mặt + trang phục, nền mờ.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 3 — Nhìn camera cười nhẹ kết (`HOLD_SMILE_TO_CAMERA`):**
```
Bối cảnh: cửa hàng thời trang nữ trung niên giống phân cảnh trước, ánh sáng showroom ấm mềm.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM}, DA THẬT, giữ nguyên identity.
Hành động: người mẫu dừng lại, nhìn vào camera với nụ cười nhẹ, tự tin, ánh mắt ấm áp. Ánh sáng showroom mềm, mặt sáng rõ, không bóng gắt, màu da thật. Camera giữ khung full-body, chuyển động rất nhẹ handheld slow, DoF mạnh, nền mờ bokeh.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> Kỹ thuật giữ nhân vật: **Veo 3 Flow first+last frame** HOẶC **Kling `Cinematic` + Elements** (2-4 ref = character-sheet U50 + keyframe). Motion strength **Subtle** để vải/tóc + DA không morph, giữ đúng chất liệu ảnh tham chiếu. Vải nhiều hoa văn/logo → giảm motion tránh warp (§10.14).
> Mở rộng menu (tùy chọn): `fashion_midage_detail_pass` (push-in nhẹ khoe chất liệu vải/đường thêu). Xem enum docs/aff-engine.md §5.

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- Import 3 clip AI → **cắt đúng nhịp beat** nhạc trend TikTok (chọn nhạc êm/sang hợp tệp trung niên) → thứ tự ①②③; đổi độ dài shot 1-8s (đừng đều → lộ AI); hard-cut mặc định.
- Text nhẹ trong safe-zone 9:16 (TikTok 900×1492): hook U50 (mở), điểm nhấn {SẢN_PHẨM} (giữa), "Link ở bio" (cuối). Caption karaoke nếu có voiceover. KHÔNG để hero/CTA vào 20% đáy.
- **Gate chất lượng** (docs/aff-engine.md §7, §10, §10.14): color grade thống nhất warm-clean **≤75%**, grain 8-10%, −14 LUFS; check cổ áo/vai thẳng hàng, drape vải, **logo/hoa văn đúng ảnh tham chiếu**, tay/ngón đúng số, **mặt không morph & KHÔNG bị beauty-filter hóa** giữa các cắt.
- **Disclosure** AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi lần gen):** `AI-face, plastic skin, beauty-filter giả, waxy airbrushed skin, morphing faces, identity change, đổi thiết kế/màu/hoa văn trang phục, logo lạ, chữ/biển quảng cáo mới, distorted hands, extra fingers, extra people, trẻ em, warped proportions, flickering, inconsistent lighting, watermark, text overlay, cartoon, CGI, 3D render` + kế thừa NEGATIVE chung §5.5.
- **DO:** DA THẬT có texture (không AI-face/beauty-filter); giữ NGUYÊN 100% thiết kế/màu/hoa văn/logo trang phục theo ảnh tham chiếu; toàn thân chính diện ~80% khung, chân gần chạm mép dưới; DoF mạnh nét mặt + vải, nền showroom mờ; gentle motion (bước 1-2 bước + xoay 10-15° + cười nhẹ), camera handheld nhẹ; 1 camera-move + 1 action/clip.
- **DON'T:** đừng dùng "8K/HDR/hyperrealistic" (đẩy da nhựa/AI-face); đừng cho beauty-filter/làm mịn quá (mất texture da → lộ giả); đừng đổi/“cải tiến” thiết kế hay màu/hoa văn trang phục; đừng tạo dáng lố hay xoay mạnh (morph vải); đừng rung camera mạnh; đừng thêm người khác/trẻ em; đừng để chân dính đáy khung.

## 7. METADATA
- **Title** <70 ký tự: hợp tệp trung niên (vd "Set này cho mẹ U50 mặc lên sang lắm 🤍").
- **Caption + 15-25 hashtag** ngách trung niên (#thoitrangtrungnien #dodep #U50 #damdutiec #aodai #reviewdo #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · shop nhận hoa hồng qua link".
