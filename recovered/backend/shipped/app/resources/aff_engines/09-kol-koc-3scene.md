---
id: kol-koc-3scene
name: "KOL/KOC ảo — Outfit Check 3 phân cảnh (viral chuẩn)"
archetype: A
video_type: "outfit-check"
niche_default: "Thời trang nữ — người mẫu ảo mặc outfit, xoay khoe dáng"
niches:
  - label: "Thời trang nữ"
    fits: "váy, set đồ, áo khoác, phụ kiện mặc được"
  - label: "Thời trang nam"
    fits: "set nam, áo khoác, streetwear (đổi persona nam)"
  - label: "Phụ kiện outfit"
    fits: "túi, mũ, giày — nhấn mạnh khi mặc cả bộ"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"
final_length: "15-30s"
persona_scope: channel
faceless: false
design_lock: false
recurring_character: "{PERSONA} — nhân vật cố định của kênh (dùng character-sheet đã lưu, giữ y hệt mặt/tóc/dáng)"
scene_structure: "3 phân cảnh: (1) góc trên cao hạ xuống ngang mắt → (2) camera xoay 360 quanh người → (3) camera bay lên kết thúc. 6-10s. Dạng này AI tạo rất mượt, ít lỗi."
camera_sequence: [CRANE_DOWN_TOP_TO_EYE, ORBIT_360, CRANE_UP_DRONE_OUT]
motion_presets: [fashion_kol_3scene]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, medium-format-style film grain, natural color, high-fashion editorial lifestyle photo,"
image_style_lock: "natural skin texture with visible pores and fine imperfections, natural human proportions, soft even light, vertical 9:16."
golden_rules: ["phải toàn thân (head-to-toe)", "góc chụp từ trên cao (top view) rồi hạ xuống", "outfit rõ ràng, màu chuẩn", "chọn ảnh đẹp nhất mới làm video"]
lighting_default: "soft diffused window light from camera-side + subtle rim light for separation, bright airy high-key"
color_look: "warm-iphone (lifted shadows, protected highlights, flattering warm skin)"
lut_intensity: 50
lens_default: "85mm portrait look, shallow depth of field, soft background bokeh"
camera_angle_default: "full-body slightly low angle tilted up (leg-lengthening); crane down from top view"
background_default: "hành lang căn hộ hiện đại / góc 2 tường sáng tối giản, sàn sáng, bokeh nhẹ"
skin_realism: "natural skin texture with visible pores and fine imperfections, natural human proportions"
negative_constant: "morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, flickering, inconsistent lighting, watermark, text overlay"
motion_strength: "subtle_to_moderate"
reference_workflow: "character-sheet 360 (front+45°+90°+back) → keyframe 9:16 2K outfit-check → (mặc {SẢN_PHẨM} bằng mask-and-place) → Veo Ingredients/Kling Elements → 3 beat clip"
post_chain: "upscale 4K → interp 30fps → LUT warm → grain 8% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (first-last frame front→back) / Kling 2.5-2.6 Cinematic (roll 360) — image-to-video"
tts_mood: "không thoại — nhạc nền thời trang"
music_mood: "nhạc trend TikTok, beat rõ để cắt cảnh"
tags: [outfit-check, koc-ao, kol-ao, thoi-trang, xoay-360, fashion, tiktok-shop, affiliate, ootd]
---

# AFF Engine — KOL/KOC ảo · Outfit Check 3 phân cảnh

> **Kiểu:** A (người mẫu ảo mặc/khoe outfit) · **Dùng khi:** sản phẩm mặc được (váy/set/áo khoác/phụ kiện). Tạo cảm giác một reviewer thời trang thật xoay khoe dáng — dạng viral nhất, AI làm mượt ít lỗi.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl) + `{PERSONA}` (nhân vật cố định của kênh — dùng lại character-sheet đã lưu).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc (verbatim):** Video gồm **3 phân cảnh** — ① góc nhìn từ trên cao hạ xuống ngang tầm mắt → ② camera xoay **360 độ** quanh người (đoạn quan trọng nhất, giữ chân người xem) → ③ camera **bay lên** trở lại top view kết thúc. **Thời lượng 6-10 giây.** "Dạng này AI tạo rất mượt — ít lỗi."
- **Sản phẩm hợp:** đồ mặc được (thời trang nữ/nam, phụ kiện outfit). **Persona:** BẮT BUỘC dùng nhân vật cố định của kênh (đồng bộ thương hiệu).
- **Vì sao mượt:** chỉ 1 chuyển động camera liên tục/cảnh + nhân vật đứng pose (ít biến dạng); ghép 3 clip ngắn theo beat nhạc.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền + text overlay. (Nếu kênh muốn có voiceover review, bật `dialogue_mode: vi_voiceover` và dùng khung Hook→Problem→Solution→CTA ở docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng tò mò/khoe — ví dụ "Outfit hôm nay ✨", "Set này mà giá này á?", "Dáng xinh mặc đẹp". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** tên/điểm nhấn {SẢN_PHẨM} ngắn gọn (chất liệu, form).
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền 11 trường theo `{PERSONA}` + `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`. **3 luật vàng:** toàn thân · góc từ trên cao · outfit rõ.
- **Ví dụ VERBATIM (chỉnh từ tab, thay chỗ động bằng biến):**
  ```
  shot on 85mm, medium-format-style film grain, natural color, high-fashion editorial lifestyle photo,
  Một {PERSONA: cô gái châu Á trẻ tuổi xinh đẹp, da trắng mịn, khuôn mặt nhỏ thanh tú, mắt to, tóc đen dài gợn sóng}.
  Cô mặc {SẢN_PHẨM: mô tả outfit chi tiết — màu, form, chất liệu, phụ kiện đi kèm}.
  Góc chụp từ trên cao nhìn xuống (top view), cô gái ngước mặt nhìn thẳng vào camera, tạo dáng toàn thân.
  Bối cảnh {background_default: hành lang căn hộ hiện đại, sàn sáng, tường tối giản sang trọng}.
  Ánh sáng tự nhiên mềm mại từ bên, high-key sáng thoáng, shallow depth of field, bokeh nền nhẹ,
  natural skin texture with visible pores and fine imperfections, natural human proportions, soft even light, vertical 9:16.
  ```
- **Nhân bản:** giữ NGUYÊN {PERSONA} + {SẢN_PHẨM}, chỉ đổi bối cảnh để ra thêm keyframe (dùng làm start/end frame khác nhau).

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip**. Giữ "cô gái mặc outfit như ảnh gốc" (reference-chaining). Bake `negative_constant` cuối mỗi prompt.

**Phân cảnh 1 — Camera từ trên cao hạ xuống (`CRANE_DOWN_TOP_TO_EYE`):**
```
Bối cảnh: hành lang căn hộ hiện đại, ánh sáng tự nhiên mềm, không gian sang trọng tối giản.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, giữ nguyên khuôn mặt/tóc/outfit.
Hành động: camera bắt đầu từ góc nhìn trên cao nhìn xuống khuôn mặt, sau đó TỪ TỪ hạ thấp xuống ngang tầm mắt. Cô gái đứng yên tự tin, mắt nhìn theo camera, biểu cảm nhẹ nhàng cuốn hút.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền thời trang.
[negative_constant]
```
**Phân cảnh 2 — Xoay camera 360 độ (`ORBIT_360`) — quan trọng nhất:**
```
Bối cảnh: hành lang căn hộ hiện đại sang trọng, ánh sáng ổn định.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: camera xoay vòng 360 độ quanh cô gái một cách mượt mà, điện ảnh, giống drone vòng quanh người mẫu. Cô gái đứng tạo dáng tự tin, tay hơi di chuyển nhẹ, tóc bay nhẹ tự nhiên; quần áo chuyển động mềm mại chân thực theo cơ thể.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 3 — Camera bay lên kết thúc (`CRANE_UP_DRONE_OUT`):**
```
Bối cảnh: hành lang căn hộ hiện đại giống phân cảnh trước.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM}.
Hành động: camera từ từ bay lên cao trở lại góc nhìn từ trên xuống như lúc đầu. Cô gái hơi ngẩng đầu nhìn theo camera. Chuyển động mượt mà, điện ảnh.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> Kỹ thuật giữ nhân vật: dùng **Veo first+last frame** (front→back cho đoạn xoay) HOẶC **Kling `roll 360` + Elements** (2-4 ref = character-sheet + keyframe). Motion strength Subtle→Moderate để vải/tóc không morph.
> Mở rộng menu (tùy chọn thêm cảnh): `fashion_walk_showcase` (bước tới + hair-flip), `fashion_detail_pass` (push-in khoe chất liệu + point-at-product). Xem enum docs/aff-engine.md §5.

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- Import 3 clip AI → **cắt đúng nhịp beat** nhạc trend TikTok → thứ tự ①②③.
- Text nhẹ trong safe-zone 9:16: "Outfit hôm nay ✨" (mở), điểm nhấn {SẢN_PHẨM} (giữa), "Link ở bio" (cuối). Caption karaoke nếu có voiceover.
- Gate chất lượng (docs/aff-engine.md §7, §10): color grade thống nhất warm, grain 8%, −14 LUFS.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, flickering, inconsistent lighting, watermark, text overlay` + `no cartoon/3D render`.
- **DO:** ảnh phải toàn thân + góc trên cao + outfit rõ; giữ NGUYÊN persona qua cả 3 clip; 1 camera-move + 1 action/clip; đoạn 360 mượt là điểm giữ chân.
- **DON'T:** đừng tả lại đặc điểm mặt mỗi clip (gây drift); đừng xoay quá nhanh (morph vải); đừng để chân dính đáy khung / CTA vào 20% đáy; đừng dùng "8K/HDR" (da nhựa).

## 7. METADATA
- **Title** <70 ký tự: outfit-check + điểm nhấn (vd "Set này mặc lên xịn hơn giá 🤍").
- **Caption + 15-25 hashtag** ngách thời trang (#outfit #ootd #reviewdo #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
