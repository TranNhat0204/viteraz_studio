---
id: fashion-kids
name: "Thời trang TRẺ EM — Mirror-selfie mẹ bế bé (micro-expression)"
archetype: A
video_type: "mirror-selfie"
niche_default: "Đồ trẻ em — bé 1.5-3 tuổi được mẹ bế, mẹ che mặt bằng điện thoại, khoe outfit qua gương"
niches:
  - label: "Váy/set bé gái"
    fits: "váy voan/tulle, set bé gái, đồ công chúa, họa tiết bướm/nơ"
  - label: "Đồ mặc nhà / pajama bé"
    fits: "bộ thun mặc nhà, pajama, đồ họa tiết nhân vật (Minnie...)"
  - label: "Phụ kiện bé"
    fits: "kẹp tóc nơ, cột tóc, mũ, giày nhỏ — khoe khi mặc cả bộ"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-8s"
final_length: "15-30s"
persona_scope: channel
faceless: true
design_lock: false
recurring_character: "{PERSONA} = bé (1.5-3 tuổi, châu Á, má phúng phính, mắt to đen láy) + MẸ bế bé (chỉ lộ thân/áo trơn, MẶT MẸ BỊ ĐIỆN THOẠI CHE HOÀN TOÀN) — giữ y hệt qua mọi clip"
scene_structure: "Mirror-selfie giữ NGUYÊN 1 bố cục: mẹ đứng bế bé, giơ điện thoại che mặt quay qua gương; bé ĐỨNG YÊN trong tay mẹ, CHỈ đổi MICRO-EXPRESSION (chớp mắt/cười ngại/phồng má/nghiêng đầu/vẫy tay...) từng clip 6-8s. Camera khóa cứng, background & khung hình không đổi."
camera_sequence: [LOCKED_OFF, MICRO_TILT_LR]
motion_presets: [kids_mirror_microexpression]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on iPhone Pro front camera, mirror selfie, medium-format-style soft film grain, natural color, everyday lifestyle candid photo,"
image_style_lock: "soft natural baby skin, subtle rosy cheeks, natural human proportions, warm pastel tone, raw phone photo (not studio), vertical 9:16."
golden_rules: ["MẶT MẸ luôn bị điện thoại che kín (faceless)", "bé ĐỨNG YÊN trong tay mẹ — không đi/không tạo dáng người lớn", "giữ NGUYÊN bố cục mirror-selfie qua gương + điện thoại ở mép khung", "outfit bé rõ màu & họa tiết", "raw-phone đời thường, KHÔNG quá studio/8K"]
lighting_default: "soft diffused window + ambient room light, front catchlight in baby eyes, high-key bright/airy, low contrast, no harsh shadow"
color_look: "warm pastel lifestyle (Asian phone-cam natural filter): hồng phấn + nâu gỗ, saturation dịu, warm-clean skin"
lut_intensity: 40
lens_default: "24-26mm smartphone wide (deep DoF, mọi thứ nét — raw phone look); tùy chọn 50-85mm shallow DoF nếu muốn xóa phông nền gỗ"
camera_angle_default: "mirror-selfie ngang tầm mắt mẹ, hơi cao hơn bé chút; bé là trung tâm, điện thoại + tay/mẹ ở mép khung"
background_default: "trong nhà: tường/cửa ốp gỗ có phào chỉ (hoặc vách inox thang máy); giữ NGUYÊN, không đổi"
skin_realism: "soft natural baby skin, subtle rosy chubby cheeks, catchlight in eyes, natural human proportions, no plastic skin, no heavy beauty-filter"
negative_constant: "mẹ lộ mặt / mất điện thoại che mặt, bé bước đi (no walking), bé tạo dáng người lớn, đổi bố cục/góc máy, morphing baby face, identity change, plastic skin, AI-face, distorted hands, extra fingers, extra people, warped proportions, flickering, inconsistent lighting, watermark, text overlay, cartoon/3D render, over-saturated, over-sharpened, studio look"
motion_strength: "subtle"
reference_workflow: "keyframe mirror-selfie 9:16 2K (bé + mẹ-che-mặt) → giữ facial tokens của bé → Veo Ingredients / Kling Elements (2-4 ref: keyframe + bé) → mỗi clip 1 micro-expression, LOCKED_OFF"
post_chain: "upscale 4K nhẹ → interp 30fps → LUT warm-pastel ~40% → grain 6-10% → −14 LUFS + nhạc nhẹ dễ thương"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (image-to-video, camera locked) / Kling 2.5-2.6 Cinematic (motion Subtle) — image-to-video"
tts_mood: "không thoại — nhạc nền dễ thương nhẹ nhàng"
music_mood: "nhạc trend cute/lo-fi ấm, beat nhẹ để cắt cảnh"
tags: [thoi-trang-tre-em, do-be, mirror-selfie, me-be, be-yeu, kids-fashion, tiktok-shop, affiliate, vay-be-gai, pajama-be]
---

# AFF Engine — Thời trang TRẺ EM · Mirror-selfie mẹ bế bé

> **Kiểu:** A faceless-ish (mẹ bế bé, MẶT MẸ bị điện thoại che) · **Dùng khi:** đồ trẻ em mặc được (váy/set/pajama/phụ kiện bé). Tạo cảm giác một khoảnh khắc gia đình đời thường, mẹ quay bé qua gương — đáng yêu, chân thật, dễ viral vì "thật như ảnh nhà chụp".
> Input: `{SẢN_PHẨM}` = đồ trẻ em (tên/ảnh/giá/chất liệu đã crawl) + `{PERSONA}` = bé (nhân vật cố định của kênh — bé + mẹ-che-mặt, dùng lại reference đã lưu).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc (verbatim từ tab):** Ảnh gốc là **mirror-selfie** — mẹ đứng bế bé, một tay đỡ bé, tay kia **giơ điện thoại lên ngang mặt che khuất HOÀN TOÀN mặt mẹ**, chụp/quay qua gương. Bé là **trung tâm** khung hình. Video = **giữ nguyên bố cục đó**, bé **đứng yên trong vòng tay mẹ**, mỗi clip chỉ đổi **một micro-expression** (chớp mắt, cười ngại, phồng má chu môi, nghiêng đầu, ngáp dụi mắt, vẫy tay...). **Background & bố cục mirror-selfie GIỮ NGUYÊN.**
- **Sản phẩm hợp:** đồ trẻ em mặc được (bé 1.5-3 tuổi). **Persona:** bé cố định của kênh; **mẹ luôn faceless** (điện thoại che mặt).
- **Vì sao AI làm mượt, ít lỗi:** bé **KHÔNG đi/không tạo dáng** → không có chuyển động toàn thân dễ morph; camera **khóa cứng** (LOCKED_OFF), chỉ vi-biểu-cảm mặt + tóc/váy lay nhẹ → cực ít biến dạng, giữ identity bé tốt.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền dễ thương + text overlay. (Nếu kênh muốn voiceover mẹ bỉm review, bật `dialogue_mode: vi_voiceover` và dùng khung Hook→Problem→Solution→CTA ở docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng cưng/khoe — ví dụ "Bé mặc lên iu xỉu 🥹", "Set này bé nhà mình mê lắm", "Đồ bé mà xinh dữ vậy trời". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** tên/điểm nhấn {SẢN_PHẨM} ngắn (chất liệu cotton mềm, form, size theo cân nặng).
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha các mẹ" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)
- **Text overlay đặc trưng:** "Bé nhà mình 🥰", điểm nhấn {SẢN_PHẨM}, "Link ở bio".

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Khung **11 trường** (docs/aff-engine.md §5.7), điền theo `{PERSONA}` (bé) + `{SẢN_PHẨM}` (đồ bé), mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`.
- **Golden rules (verbatim từ tab):** MẶT MẸ bị điện thoại che HOÀN TOÀN · bé là trung tâm khung · chụp **mirror-selfie qua gương** · outfit bé rõ màu/họa tiết · **raw photo điện thoại**, KHÔNG color grading cầu kỳ, KHÔNG "studio".
- **11 trường (full spec từ tab):**
  1. **Chủ thể:** bé gái châu Á 1.5-3 tuổi, mặt bầu bĩnh, **mắt to tròn đen láy**, hai má phúng phính ửng hồng, mũi nhỏ, môi chúm chím hồng. **Chủ thể phụ:** mẹ bế bé — chỉ lộ thân áo thun trơn, tay đỡ bé, tay kia cầm điện thoại (iPhone Pro / ốp MagSafe) **che kín mặt mẹ**.
  2. **Tư thế:** bé đứng/lơ lửng trong tay mẹ, thân hướng trực diện; một bàn tay mẹ ôm bụng/đùi giữ bé; mẹ đứng thẳng giơ điện thoại ngang mặt.
  3. **Biểu cảm:** ngây thơ, trong trẻo, hơi tò mò, điềm tĩnh; mắt nhìn thẳng vào gương HOẶC liếc nhẹ sang bên.
  4. **Góc máy/khung:** mirror-selfie ngang tầm mắt mẹ (hơi cao hơn bé); cỡ **cận trung** (medium close-up), lấy từ đỉnh đầu tới bụng/eo bé; bé trung tâm/hơi lệch, điện thoại + tay/mẹ ở mép.
  5. **Ánh sáng:** soft light — cửa sổ hắt + đèn phòng; **catchlight rõ trong mắt bé**; high-key, tương phản thấp, không bóng gắt.
  6. **Môi trường/nền:** trong nhà — tường/cửa ốp gỗ có phào chỉ (hoặc vách inox thang máy có bảng nút bấm); giữ nguyên.
  7. **Màu/grade:** tông ấm **pastel** (hồng phấn + nâu gỗ), saturation dịu, **raw photo phone-cam**, không grade cầu kỳ.
  8. **Phong cách nhiếp ảnh:** lifestyle candid + **smartphone mirror selfie**.
  9. **Ống kính/DoF:** **DEEP DoF** — wide 24-26mm điện thoại, mọi thứ nét, không bokeh nhân tạo (variant raw-phone). *(Knob: đổi 50-85mm shallow DoF nếu muốn xóa phông nền gỗ.)*
  10. **Tâm trạng:** đáng yêu, trong trẻo, bình yên, lưu giữ khoảnh khắc gia đình.
  11. **Chất lượng/realism:** mặt bé sắc nét, photorealistic — nhưng giữ **da bé mềm tự nhiên**, tránh over-sharp.
- **Ví dụ VERBATIM (từ tab, thay chỗ động bằng {SẢN_PHẨM}/{PERSONA}):**
  ```
  shot on iPhone Pro front camera, mirror selfie, medium-format-style soft film grain, natural color, everyday lifestyle candid photo,
  Một {PERSONA: bé gái châu Á khoảng 1.5-3 tuổi, khuôn mặt bầu bĩnh, mắt to tròn đen láy, hai má phúng phính ửng hồng, môi chúm chím hồng, tóc buộc hai chỏm nhỏ hai bên}.
  Bé mặc {SẢN_PHẨM: mô tả đồ bé chi tiết — vd váy voan tulle hồng phấn không tay xếp bèo, đính họa tiết bướm hồng 3D; hoặc bộ pajama cộc tay in họa tiết}.
  Một người lớn (mẹ) đang bế bé: chỉ lộ phần thân mặc áo thun trơn, một tay ôm giữ bụng/đùi bé, tay kia CẦM ĐIỆN THOẠI iPhone Pro (ốp MagSafe) GIƠ LÊN NGANG MẶT — điện thoại CHE KHUẤT HOÀN TOÀN khuôn mặt của mẹ.
  Ảnh chụp thẳng qua GƯƠNG (mirror selfie), góc ngang tầm mắt mẹ, cỡ cận trung từ đỉnh đầu tới bụng bé. Bé là trung tâm khung hình, mắt nhìn thẳng vào gương.
  Bối cảnh {background_default: trong nhà, tường/cửa ốp gỗ có phào chỉ phía sau}.
  Ánh sáng mềm tự nhiên từ cửa sổ + đèn phòng, catchlight rõ trong mắt bé, high-key sáng thoáng, tương phản thấp, tông ấm pastel hồng phấn, raw photo điện thoại (không grading cầu kỳ, không studio), deep depth of field mọi thứ nét,
  soft natural baby skin, subtle rosy cheeks, natural human proportions, warm pastel tone, raw phone photo (not studio), vertical 9:16.
  ```
- **Nhân bản:** giữ NGUYÊN {PERSONA} (bé) + mẹ-che-mặt + bố cục mirror-selfie, chỉ đổi {SẢN_PHẨM} (bằng mask-and-place, giữ facial tokens bé) để ra thêm keyframe cho outfit khác.

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi clip 1 micro-expression) — PHẦN LÕI
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật cứng của kiểu này: **camera LOCKED_OFF** (hoặc MICRO_TILT_LR cực nhẹ), **bé ĐỨNG YÊN trong tay mẹ**, **1 micro-expression / clip**, **mẹ luôn cầm điện thoại che mặt quay qua gương**, **background & bố cục GIỮ NGUYÊN**. Giữ "bé + mẹ như ảnh gốc" (reference-chaining). Bake `negative_constant` cuối mỗi prompt.
> Đây là menu **CHÉP NGUYÊN VĂN** 20 câu lệnh micro-motion từ tab — pipeline chọn 3-5 câu ghép thành 1 video. Với mỗi câu, đặt trước bằng khối `Bối cảnh/Nhân vật`, đặt sau bằng `Lời thoại: không · Giọng: nhạc nền · [negative_constant]`.

**Khối cố định gắn ĐẦU mỗi clip:**
```
Bối cảnh: trong nhà, tường/cửa gỗ có phào chỉ phía sau, ánh sáng mềm tự nhiên, mirror selfie qua gương, giữ NGUYÊN bố cục & góc máy.
Nhân vật/Sản phẩm: {PERSONA: bé} mặc {SẢN_PHẨM} như ảnh gốc; mẹ bế bé, một tay giữ bé, tay kia cầm điện thoại che kín mặt mẹ, quay qua gương. Giữ nguyên mặt/tóc/outfit bé.
Camera: LOCKED_OFF (khóa cứng, không di chuyển) — hoặc MICRO_TILT_LR cực nhẹ.
```

**Menu micro-motion (`LOCKED_OFF` + 1 micro-expression, verbatim từ tab):**
```
1.  Em bé đứng yên trong vòng tay mẹ, mắt chớp liên tục rồi bất ngờ nở nụ cười ngại ngùng cực đáng yêu, mẹ vẫn cầm điện thoại selfie trước gương, bối cảnh phòng gỗ phía sau giữ nguyên, ánh sáng mềm mại tự nhiên, phong cách video đời thường siêu chân thực.
2.  Em bé nghiêng đầu nhẹ sang một bên, đôi mắt to tròn nhìn tò mò vào điện thoại rồi mím môi cười, hai tay khẽ cử động đáng yêu nhưng vẫn đứng yên tại chỗ, mẹ tiếp tục cầm điện thoại quay trước gương, background không thay đổi.
3.  Em bé phồng má rồi chu môi ngơ ngác như đang suy nghĩ, tóc đung đưa nhẹ, váy chuyển động tự nhiên, mẹ vẫn ôm bé và quay mirror selfie, bối cảnh gỗ phía sau giữ nguyên, video 4K photorealistic.
4.  Em bé chớp mắt chậm rãi rồi bật cười nhẹ, ánh mắt đảo sang trái phải đầy tò mò, cơ thể vẫn đứng yên trong tay mẹ, điện thoại vàng champagne vẫn xuất hiện ở mép khung hình, hậu cảnh mờ nhẹ giữ nguyên.
5.  Em bé đưa tay nhỏ lên chạm nhẹ vào váy rồi nhìn sang bên cạnh với biểu cảm ngây thơ, mẹ vẫn cầm điện thoại quay trước gương, khung hình dọc 9:16, ánh sáng mềm và tone màu ấm pastel.
6.  Em bé cười khúc khích không thành tiếng, hai má hồng phúng phính rung nhẹ, đôi mắt long lanh phản chiếu ánh sáng cửa sổ, mẹ vẫn giữ nguyên tư thế quay mirror selfie, background gỗ không đổi.
7.  Em bé ngơ ngác nhìn xung quanh rồi bất ngờ mở to mắt như phát hiện điều thú vị, tóc mai bay nhẹ tự nhiên, đứng yên trong vòng tay mẹ, bối cảnh và góc máy giữ nguyên hoàn toàn.
8.  Em bé mím môi, nghiêng đầu nhẹ rồi nở nụ cười đáng yêu, đôi chân không di chuyển, mẹ tiếp tục cầm điện thoại quay trước gương, phong cách smartphone photography chân thực như video gia đình.
9.  Em bé chớp mắt liên tục rồi che miệng cười nhẹ, hai tay cử động nhỏ đầy tự nhiên, váy có chuyển động mềm mại, mẹ vẫn ôm bé và quay bằng điện thoại, background gỗ mờ phía sau giữ nguyên.
10. Em bé nhìn chằm chằm vào camera vài giây rồi bất ngờ quay mắt sang bên với biểu cảm tò mò, ánh sáng dịu phản chiếu rõ trong mắt, mẹ vẫn cầm điện thoại selfie, khung cảnh không thay đổi.
11. Em bé cắn môi nhẹ rồi cười tươi, đôi má đỏ hồng nổi bật, tóc buộc hai bên lắc nhẹ tự nhiên, đứng yên tại chỗ trong vòng tay mẹ, mirror selfie indoor photorealistic.
12. Em bé khẽ lắc đầu đáng yêu rồi mở to mắt nhìn mẹ, bàn tay nhỏ nắm nhẹ váy, mẹ vẫn cầm điện thoại quay trước gương, hậu cảnh gỗ nâu mờ giữ nguyên, video cinematic đời thường.
13. Em bé nhìn sang phải rồi chớp mắt cười nhẹ như đang chơi với mẹ, cơ thể giữ nguyên vị trí, mẹ vẫn ôm bé bằng một tay và cầm điện thoại quay bằng tay còn lại, ánh sáng mềm tự nhiên.
14. Em bé ngáp nhẹ cực đáng yêu rồi dụi mắt bằng tay nhỏ, sau đó cười ngại ngùng, vẫn đứng yên trong vòng tay mẹ, background và bố cục mirror selfie không đổi.
15. Em bé đưa mắt nhìn điện thoại rồi nghiêng đầu cười nhẹ, tóc con bay mềm mại, váy chuyển động tinh tế, mẹ vẫn quay video selfie trước gương, tone màu pastel ấm áp.
16. Em bé mở to mắt ngạc nhiên rồi khẽ bật cười, hai má phúng phính rung nhẹ, mẹ vẫn giữ điện thoại ở góc trái khung hình, bối cảnh gỗ phía sau mờ đẹp như ảnh thật.
17. Em bé khẽ nhún vai đáng yêu rồi chu môi, ánh mắt long lanh nhìn sang bên cạnh, đứng yên tại chỗ trong tay mẹ, video smartphone quality ultra realistic vertical 9:16.
18. Em bé cười tươi rồi đưa tay nhỏ vẫy nhẹ về phía gương, vẫn giữ nguyên vị trí trong vòng tay mẹ, điện thoại vàng champagne vẫn xuất hiện ở mép trái khung hình, background giữ nguyên.
19. Em bé ngơ ngác nhìn lên trên rồi chớp mắt chậm, môi chúm chím tự nhiên, mẹ tiếp tục quay mirror selfie trong căn phòng ánh sáng ấm, hậu cảnh gỗ mờ không thay đổi.
20. Em bé nhẹ nhàng lắc lư phần đầu theo nhịp vui vẻ rồi cười đáng yêu, đôi mắt to phản chiếu ánh sáng rất đẹp, mẹ vẫn cầm điện thoại quay trước gương, toàn bộ bố cục và bối cảnh giữ nguyên, phong cách video đời thường chân thực tuyệt đối.
```
```
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền dễ thương nhẹ nhàng.
[negative_constant]  ← bake cuối MỖI clip (gồm: no walking, giữ bố cục, mẹ giữ điện thoại che mặt)
```
> Kỹ thuật giữ nhân vật: nạp **keyframe + bé (facial tokens)** làm **Veo Ingredients / Kling Elements (2-4 ref)**, `maintains exact appearance throughout`; **motion strength Subtle** để da/tóc/váy bé không morph. Camera phải khóa — thêm `(thats where the camera is)` cho Veo để không trôi khung.

## 5. GHÉP & XUẤT  (BƯỚC 3 — Studio/export)
- Import 3-5 clip micro-expression AI → **cắt đúng nhịp beat** nhạc cute/lo-fi trend TikTok; xen câu chớp mắt → cười → vẫy tay để giữ chân người xem; hard-cut, đổi độ dài shot 1-6s (đừng đều nhau).
- Text nhẹ trong safe-zone 9:16: "Bé nhà mình 🥰" (mở), điểm nhấn {SẢN_PHẨM} (giữa), "Link ở bio" (cuối); tránh đè lên mặt bé (1/3 trên) và 20% đáy.
- Gate chất lượng (docs/aff-engine.md §7, §10): grade warm-pastel ≤40%, grain 6-10%, −14 LUFS + nhạc nền; giữ **look raw-phone**, đừng over-sharpen/over-saturate.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `mẹ lộ mặt / mất điện thoại che mặt, bé bước đi (no walking), bé tạo dáng người lớn, đổi bố cục/góc máy, morphing baby face, identity change, plastic skin, AI-face, distorted hands, extra fingers, extra people, warped proportions, flickering, inconsistent lighting, watermark, text overlay` + `no cartoon/3D render, no over-saturation, no studio look`.
- **DO:** mẹ LUÔN faceless (điện thoại che mặt) · bé **đứng yên**, chỉ micro-expression · **1 micro-expression + camera khóa / clip** · giữ NGUYÊN bố cục mirror-selfie + background gỗ + điện thoại ở mép khung · outfit bé rõ màu.
- **DON'T:** đừng cho bé đi/xoay/tạo dáng (morph ngay); đừng để lộ mặt mẹ; đừng đổi góc máy/nền giữa các clip (mất tính "cùng 1 khoảnh khắc"); đừng dùng "8K/HDR/studio" (mất chất raw-phone, da bé thành nhựa); đừng over-grade (giữ pastel dịu).

## 7. METADATA
- **Title** <70 ký tự: đồ bé + cưng (vd "Bé mặc set này iu xỉu 🥹 đồ mềm mà xinh").
- **Caption + 15-25 hashtag** ngách mẹ & bé (#dobe #thoitrangtreem #mevabe #beyeu #reviewdobe #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio nha các mẹ" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
