---
id: gallery-projector
name: "Gallery Backdrop — Mẫu đứng trước chân dung khổng lồ của chính mình (editorial)"
archetype: A
video_type: "gallery-editorial-standing"
niche_default: "Thời trang nữ cao cấp — người mẫu đứng giữa gallery, sau lưng là panel in chân dung khổng lồ của chính cô"
niches:
  - label: "Thời trang nữ cao cấp"
    fits: "set công sở thanh lịch, blouse, quần ống rộng, blazer, đầm editorial"
  - label: "Phụ kiện luxury"
    fits: "túi da, đồng hồ, trang sức — nhấn khi kết cả outfit"
  - label: "Thời trang nam lịch lãm"
    fits: "suit, sơ mi, set smart-casual (đổi persona nam)"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"
final_length: "15-30s"
persona_scope: channel
faceless: false
design_lock: false
recurring_character: "{PERSONA} — nhân vật cố định của kênh (dùng character-sheet đã lưu, giữ y hệt mặt/tóc/dáng; chân dung khổng lồ trên panel là ẢNH của CHÍNH persona này)"
scene_structure: "Người mẫu đứng chính giữa gallery, phía sau là panel triển lãm khổng lồ in chân dung mờ của chính cô. 5 phân cảnh chuyển động nhẹ: (1) push-in chậm vào chủ thể → (2) xoay người nhẹ khoe outfit → (3) point/chạm sản phẩm → (4) reveal panel chân dung phía sau → (5) chốt tư thế editorial. 6-10s/clip. Chỉ 1 chuyển động camera + 1 action/clip nên AI làm rất mượt."
camera_sequence: [SLOW_PUSH_IN, SLIGHT_TURN_SHOWCASE, POINT_AT_PRODUCT, PULL_BACK_REVEAL_PANEL, HOLD_EDITORIAL_POSE]
motion_presets: [gallery_editorial_5scene]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, medium-format-style film grain, natural color, high-end fashion editorial campaign photo,"
image_style_lock: "natural skin texture with visible pores and fine imperfections, natural human proportions, soft even commercial light, vertical 9:16."
golden_rules: ["phải toàn thân (head-to-toe) canh giữa đối xứng", "panel chân dung khổng lồ phía sau = ẢNH CHÍNH persona (mờ/pastel, không nét hơn chủ thể)", "chủ thể sắc nét, panel hơi mềm để tách lớp", "outfit rõ màu chuẩn", "chọn ảnh đối xứng đẹp nhất mới làm video"]
lighting_default: "soft commercial lighting, diffused frontal light, very soft shadows, high-key but not overexposed, luxury fashion campaign look (option low-key: single directional light + deep shadows cho SKU luxury)"
color_look: "clean pastel luxury grade — soft white / blush pink / beige / cream / nude, low-to-medium contrast, refined and airy"
lut_intensity: 45
lens_default: "70-85mm lens look, mild background softness (panel mềm), full subject crisp, realistic perspective no distortion"
camera_angle_default: "eye-level, full-body centered symmetrical editorial composition; chủ thể sharp focus giữa khung"
background_default: "gallery/bảo tàng nghệ thuật hiện đại tối giản, sàn sáng bóng, panel triển lãm trắng khổng lồ in chân dung mờ pastel của chính persona, vài bóng người xa mờ ở rìa, không gian mở sang trọng"
skin_realism: "natural skin texture with visible pores and fine imperfections, natural human proportions"
negative_constant: "morphing faces, identity change, plastic skin, waxy, airbrushed, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people crowding subject, warped proportions, flickering, inconsistent lighting, panel sharper than subject, duplicated face merging, watermark, text overlay, cartoon, 3D render, oversaturated"
motion_strength: "subtle_to_moderate"
reference_workflow: "character-sheet 360 → keyframe 9:16 2K gallery (chủ thể + panel chân dung cùng persona, mask-and-place {SẢN_PHẨM}) → Veo Ingredients/Kling Elements (2-4 ref) → 5 beat clip"
post_chain: "upscale 4K → interp 30fps → LUT pastel-luxury ≤45% → grain 8% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients/first-last) / Kling 2.5-2.6 Cinematic — image-to-video"
tts_mood: "không thoại — nhạc nền editorial sang"
music_mood: "nhạc trend TikTok chậm rãi/sang, beat rõ để cắt cảnh"
tags: [gallery-backdrop, editorial, chan-dung-khong-lo, thoi-trang-cao-cap, luxury-campaign, koc-ao, tiktok-shop, affiliate, ootd]
---

# AFF Engine — Gallery Backdrop · Mẫu đứng trước chân dung khổng lồ của chính mình

> **Kiểu:** A (người mẫu mặc/khoe outfit) · **Dùng khi:** SKU thời trang/luxury muốn look **aspirational/editorial** — người mẫu đứng giữa gallery, phía sau là panel triển lãm in **chân dung khổng lồ của chính cô** làm nền. Cảm giác "campaign tạp chí cao cấp", nâng tầm thương hiệu → viral vì sang và lạ mắt.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl) + `{PERSONA}` (nhân vật cố định của kênh — dùng lại character-sheet đã lưu; **chân dung trên panel cũng là persona này**).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc:** người mẫu đứng **chính giữa** một gallery nghệ thuật tối giản, phía sau là **panel triển lãm trắng khổng lồ** in **chân dung mờ/pastel của chính cô**. 5 phân cảnh chuyển động nhẹ để ghép thành 1 clip quảng cáo outfit: ① push-in chậm → ② xoay người nhẹ khoe outfit → ③ point/chạm sản phẩm → ④ pull-back reveal panel chân dung → ⑤ giữ pose editorial chốt. **6-10 giây/clip.**
- **Sản phẩm hợp:** đồ mặc được cao cấp (set công sở, blouse, blazer, đầm editorial) + phụ kiện luxury. **Persona:** BẮT BUỘC nhân vật cố định của kênh (mặt trên panel phải trùng persona).
- **Vì sao AI làm mượt, ít lỗi:** chủ thể đứng gần như tĩnh, mỗi clip chỉ 1 chuyển động camera + 1 action nhỏ → ít biến dạng vải/mặt; nền gallery phẳng, sạch, dễ giữ nhất quán qua các clip.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền editorial + text overlay nhẹ. (Nếu kênh muốn voiceover review, bật `dialogue_mode: vi_voiceover` và dùng khung Hook→Problem→Solution→CTA ở docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng sang/tò mò — ví dụ "Set này như bước ra từ campaign ✨", "Đứng đâu cũng là nhân vật chính", "Outfit đi làm mà sang như triển lãm". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** điểm nhấn {SẢN_PHẨM} ngắn gọn (chất liệu, form, màu).
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền 11 trường theo `{PERSONA}` + `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`.
- **Golden rules (verbatim):** toàn thân canh giữa đối xứng · **panel chân dung khổng lồ phía sau = ẢNH của CHÍNH persona** (mờ/pastel, KHÔNG nét hơn chủ thể) · chủ thể sharp, panel mềm để tách lớp · outfit rõ màu chuẩn · chọn ảnh đối xứng đẹp nhất mới làm video.
- **Ví dụ VERBATIM (từ tab, thay chỗ động bằng {PERSONA}/{SẢN_PHẨM}):**
  ```
  A highly realistic full-body fashion portrait of {PERSONA: a young East Asian woman} standing in the center of a minimalist modern art gallery, in front of a massive white exhibition panel featuring a huge soft faded portrait of herself in the background. She is around 24 years old, slim build, fair smooth skin, oval face, delicate feminine features, soft natural makeup, subtle pink lips, gentle confident smile, looking directly at the camera.

  She wears {SẢN_PHẨM: a light pastel pink button-up blouse with rolled sleeves, elegant high-waisted wide-leg beige trousers with an asymmetric layered front panel, nude open-toe heels, a small black leather shoulder bag on her left shoulder, minimal jewelry including small earrings, a thin necklace, and a wristwatch or bracelet}. Her long dark brown hair is styled half-up with soft face-framing strands falling in front, neat and feminine.

  Pose: standing still, body facing mostly forward, head slightly tilted, right hand gently touching under her chin, left arm relaxed down naturally, legs close together with one foot slightly forward.

  Camera: eye-level shot, full-body composition, centered framing, symmetrical editorial composition, subject in sharp focus.

  Background: bright clean indoor gallery, polished light floor, huge rectangular white display wall behind her, large pastel-toned portrait of the same woman softly printed or projected on it, faint distant figures at far edges of the gallery, minimal clutter, elegant open space.

  Lighting: soft commercial lighting, diffused frontal light, very soft shadows, high-key but not overexposed, smooth skin rendering, luxury fashion campaign look.

  Color palette: soft white, blush pink, beige, cream, nude, light warm neutral tones, clean pastel luxury grading, low-to-medium contrast, refined and airy.

  Style: high-end fashion editorial, luxury lifestyle campaign, polished commercial photography, Korean fashion advertisement aesthetic, ultra-detailed, realistic fabric texture, realistic skin, natural proportions, premium magazine quality.

  Lens and depth of field: 70mm to 85mm lens look, mild background softness, full subject crisp and clear, realistic perspective, no distortion.

  ultra realistic, photographic, 8k, premium editorial, natural pose, clean composition, museum gallery atmosphere, sophisticated feminine elegance
  ```
- **Nhân bản:** giữ NGUYÊN {PERSONA} + {SẢN_PHẨM} + panel chân dung; chỉ đổi bối cảnh gallery (màu panel, ánh sáng) để ra thêm keyframe làm start/end frame khác nhau.
> Lưu ý style_anchor engine dùng **film-stock 85mm** (không "8K/HDR") để chống da nhựa — chuỗi "8k" chỉ còn ở đuôi prompt tab verbatim; nếu ra da nhựa hãy bỏ "8k, ultra-detailed" và giữ `medium-format-style film grain` (docs/aff-engine.md §10.2).

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip** (chống méo). Giữ "cô gái mặc outfit + panel chân dung như ảnh gốc" (reference-chaining). Bake `negative_constant` cuối mỗi prompt.
> Tab chỉ đưa meta-lệnh ("đóng vai nhà trình diễn thời trang, viết 5 câu lệnh chuyển động ghép thành 1 video quảng cáo bộ đồ") → dưới đây là **menu 5 phân cảnh** dựng đúng tinh thần đó; pipeline chọn/ghép.

**Phân cảnh 1 — Push-in chậm vào chủ thể (`SLOW_PUSH_IN`):**
```
Bối cảnh: gallery nghệ thuật hiện đại tối giản, sàn sáng bóng, panel triển lãm trắng khổng lồ in chân dung mờ pastel của chính cô phía sau. Ánh sáng thương mại mềm, high-key.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, giữ nguyên khuôn mặt/tóc/outfit; panel chân dung phía sau vẫn là mặt cô.
Hành động: camera TỪ TỪ push-in chậm từ toàn cảnh vào chủ thể, giữ bố cục đối xứng canh giữa. Cô gái đứng yên tự tin, tay phải chạm nhẹ dưới cằm, mắt nhìn thẳng camera, biểu cảm thanh lịch cuốn hút.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền editorial sang.
[negative_constant]
```
**Phân cảnh 2 — Xoay người nhẹ khoe outfit (`SLIGHT_TURN_SHOWCASE`):**
```
Bối cảnh: gallery như phân cảnh trước, panel chân dung khổng lồ giữ nguyên phía sau.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: camera giữ cố định eye-level, cô gái xoay người nhẹ ~30-45 độ khoe form và chất liệu outfit rồi quay lại nhìn camera, tà áo/quần chuyển động mềm mại chân thực theo cơ thể, tóc lay nhẹ tự nhiên.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 3 — Point/chạm sản phẩm (`POINT_AT_PRODUCT`):**
```
Bối cảnh: gallery tối giản, ánh sáng ổn định, panel chân dung phía sau.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: camera push-in nhẹ về chi tiết; cô gái đưa tay chạm/chỉ vào điểm nhấn của {SẢN_PHẨM} (túi da trên vai / cổ tay / gấu áo), ánh mắt hướng nhẹ về sản phẩm rồi trở lại camera. Chuyển động tay chậm, tự nhiên, ngón tay đúng tỉ lệ.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 4 — Pull-back reveal panel chân dung (`PULL_BACK_REVEAL_PANEL`):**
```
Bối cảnh: gallery mở, panel triển lãm trắng khổng lồ in chân dung mờ pastel của chính cô, vài bóng người xa mờ ở rìa.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc; chân dung trên panel trùng khớp mặt cô.
Hành động: camera TỪ TỪ pull-back / kéo lùi ra sau, để lộ dần toàn bộ panel chân dung khổng lồ phía sau chủ thể, tạo cảm giác "cô đứng giữa campaign của chính mình". Cô gái đứng yên tư thế editorial, đầu hơi nghiêng.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 5 — Giữ pose editorial chốt (`HOLD_EDITORIAL_POSE`):**
```
Bối cảnh: gallery cân đối đối xứng, panel chân dung làm nền, ánh sáng high-key luxury.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM}.
Hành động: camera gần như tĩnh (drift rất nhẹ), cô gái giữ tư thế editorial cuối — thân hướng thẳng, một chân hơi bước tới, mắt nhìn camera tự tin, nụ cười nhẹ. Frame chốt sạch để cắt CTA.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> Kỹ thuật giữ nhân vật: **Veo Ingredients / first-last frame** HOẶC **Kling Elements (2-4 ref = character-sheet + keyframe gallery)** với `maintains exact appearance throughout`. Motion strength Subtle→Moderate để vải/tóc và **chân dung trên panel** không morph. Đặt cinematography ở ĐẦU prompt Veo (docs/aff-engine.md §10.10-10.11).

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- Import các clip AI → **cắt đúng nhịp beat** nhạc trend TikTok (chọn 3-5 cảnh); đổi độ dài shot 1-8s, đừng đều 3-4s.
- Text nhẹ trong safe-zone 9:16: hook (mở) → điểm nhấn {SẢN_PHẨM} (giữa) → "Link ở bio" (cuối). Caption karaoke nếu có voiceover.
- Gate chất lượng (docs/aff-engine.md §7, §10): color grade pastel-luxury thống nhất ≤45%, grain 8%, −14 LUFS. **QA gallery:** panel chân dung KHÔNG nét hơn chủ thể, mặt trên panel không morph, tay/ngón đúng số.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `morphing faces, identity change, plastic skin, waxy, airbrushed, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people crowding subject, warped proportions, flickering, inconsistent lighting, panel sharper than subject, duplicated face merging, watermark, text overlay` + `cartoon, anime, 3D render, CGI, oversaturated, over-sharpened`.
- **DO:** chủ thể sharp canh giữa đối xứng · **panel chân dung = mặt persona, mờ/pastel để tách lớp** · giữ NGUYÊN persona + outfit qua cả 5 clip · 1 camera-move + 1 action/clip · panel làm nền aspirational nhưng không hút mắt khỏi outfit.
- **DON'T:** đừng để panel nét/sáng hơn chủ thể (rối lớp) · đừng để 2 khuôn mặt (thật + panel) morph/dính vào nhau · đừng tả lại đặc điểm mặt mỗi clip (gây drift) · đừng để chân dính đáy khung / CTA vào 20% đáy · đừng ép "8K/HDR" (da nhựa) — giữ film-stock 85mm.

## 7. METADATA
- **Title** <70 ký tự: editorial/campaign + điểm nhấn (vd "Set đi làm mà sang như triển lãm 🤍").
- **Caption + 15-25 hashtag** ngách thời trang cao cấp (#outfit #ootd #editorial #reviewdo #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
