---
id: fashion-women
name: "Thời trang NỮ — Người mẫu ảo mặc/khoe outfit (thư viện motion đầy đủ)"
archetype: A
video_type: "outfit-check / fashion-showcase"
niche_default: "Thời trang nữ — người mẫu ảo mặc outfit, đi/xoay/khoe chi tiết vải"
niches:
  - label: "Thời trang nữ (váy/set/đầm)"
    fits: "váy, đầm, set đồ, áo khoác, jumpsuit mặc được toàn thân"
  - label: "Áo/topwear nữ"
    fits: "áo thun, sơ mi, áo len, áo khoác — nhấn chất liệu, độ co giãn"
  - label: "Phụ kiện outfit nữ"
    fits: "túi xách, mũ, giày — khoe khi mặc cả bộ (túi làm điểm nhấn phụ)"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"
final_length: "15-30s"
persona_scope: channel
faceless: false
design_lock: false
recurring_character: "{PERSONA} — nhân vật nữ cố định của kênh (dùng character-sheet đã lưu, giữ y hệt mặt/tóc/dáng)"
scene_structure: "Chọn/ghép từ THƯ VIỆN 8 nhóm motion nữ: bước đi tự tin → vuốt tóc → xoay 360 → chỉnh cổ/tay áo → cầm túi → kéo giãn vải → chỉ tay vào sản phẩm → bước lại gần camera. Mỗi clip 1 camera-move + 1 action, 6-10s, ghép 3-5 cảnh theo beat nhạc."
camera_sequence: [TILT_UP_TRACK, PUSH_IN_SLOW, ORBIT_360, PAN_LR, DOLLY_IN, HANDHELD_SHAKE]
motion_presets: [fashion_walk_showcase, fashion_kol_3scene, fashion_detail_pass]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, medium-format-style film grain, natural color, high-fashion editorial lifestyle photo,"
image_style_lock: "natural skin texture with visible pores and fine imperfections, natural human proportions, soft even light, vertical 9:16."
golden_rules: ["phải toàn thân (head-to-toe)", "góc chụp từ trên cao (top view) rồi hạ xuống", "outfit rõ ràng, màu chuẩn, không méo vải", "chọn ảnh đẹp nhất mới làm video"]
lighting_default: "soft diffused window light from camera-side + subtle rim light for separation, bright airy high-key (gu VN)"
color_look: "warm-iphone (lifted shadows, protected highlights, flattering warm skin, clean whites)"
lut_intensity: 50
lens_default: "85mm portrait look, shallow depth of field (f/1.8), soft background bokeh"
camera_angle_default: "full-body slightly low angle tilted up (leg-lengthening); close-up cổ/tay áo ở eye-level"
background_default: "hành lang căn hộ hiện đại / góc 2 tường sáng tối giản, sàn sáng, bokeh nhẹ"
skin_realism: "natural skin texture with visible pores and fine imperfections, natural human proportions"
negative_constant: "morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, flickering, inconsistent lighting, warp/biến dạng vải, đổi màu vải, watermark, text overlay"
motion_strength: "subtle_to_moderate"
reference_workflow: "character-sheet 360 (front+45°+90°+back) → keyframe 9:16 2K outfit-check → mặc {SẢN_PHẨM} bằng mask-and-place → Veo Ingredients/Kling Elements → chọn 3-5 clip từ thư viện motion"
post_chain: "upscale 4K → interp 30fps → LUT warm ≤75% → grain 8% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients/first-last) / Kling 2.5-2.6 Cinematic (roll 360) — image-to-video"
tts_mood: "không thoại — nhạc nền thời trang"
music_mood: "nhạc trend TikTok, beat rõ để cắt cảnh"
tags: [thoi-trang-nu, outfit-check, koc-ao, fashion, ootd, xoay-360, vuot-toc, keo-gian-vai, tiktok-shop, affiliate]
---

# AFF Engine — Thời trang NỮ · Người mẫu ảo mặc/khoe outfit

> **Kiểu:** A (người mẫu nữ mặc/khoe outfit) · **Dùng khi:** sản phẩm mặc được cho nữ (váy/đầm/set/áo/áo khoác/phụ kiện). Tạo cảm giác một KOC nữ thật đi catwalk, xoay khoe dáng, chỉnh áo, kéo giãn vải khoe chất liệu — **thư viện motion GIÀU nhất bộ engine** (8 nhóm hành động), ghép 3-5 cảnh cho ra clip viral chuẩn thời trang.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl) + `{PERSONA}` (nhân vật nữ cố định của kênh — dùng lại character-sheet đã lưu).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc:** không cố định 3 cảnh như KOL-3scene, mà **chọn/ghép từ THƯ VIỆN 8 nhóm motion** (§4): ① bước đi tự tin về phía trước → ② vuốt tóc → ③ xoay 360° → ④ chỉnh cổ/tay áo → ⑤ cầm túi (nhấn trang phục) → ⑥ kéo giãn vải khoe co giãn → ⑦ chỉ tay vào sản phẩm/tag giá → ⑧ bước lại gần camera. Mỗi clip **6-10s**, ghép **3-5 cảnh** theo beat nhạc. Mở bằng walk/approach, giữ chân bằng 360, chốt bằng detail-pass (kéo giãn/chỉ tay).
- **Sản phẩm hợp:** đồ mặc được cho nữ + phụ kiện outfit. **Persona:** BẮT BUỘC dùng nhân vật nữ cố định của kênh (đồng bộ thương hiệu).
- **Vì sao mượt, ít lỗi:** mỗi clip chỉ **1 chuyển động camera + 1 action**; nhân vật đứng/đi pose đơn giản (ít biến dạng); nhóm "detail" (chỉnh áo, kéo giãn, chỉ tay) là cận cảnh vải nên khoe chất liệu cực tốt mà AI khó lỗi.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền + text overlay. (Muốn có voiceover review thì bật `dialogue_mode: vi_voiceover` và dùng khung Hook→Problem→Solution→CTA ở docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng khoe/tò mò — ví dụ "Outfit hôm nay ✨", "Set này mà giá này á?", "Chất vải co giãn xịn thật sự". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** điểm nhấn {SẢN_PHẨM} ngắn gọn (chất liệu, form, độ co giãn) — nhất là khi ghép cảnh kéo giãn/chỉ tay.
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)
- **Text overlay đặc trưng:** "Outfit hôm nay ✨" (mở) · tên/chất liệu {SẢN_PHẨM} (giữa) · "Link ở bio" (cuối).

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền 11 trường theo `{PERSONA}` + `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`. **3 luật vàng:** toàn thân · góc từ trên cao · outfit rõ.
- **Golden rules (verbatim):** *phải toàn thân (head-to-toe) · góc chụp từ trên cao (top view) rồi hạ xuống · outfit rõ ràng, màu chuẩn · chọn ảnh đẹp nhất mới làm video.*
- **Ví dụ VERBATIM (chỉnh từ tab, thay outfit bằng {SẢN_PHẨM}):**
  ```
  shot on 85mm, medium-format-style film grain, natural color, high-fashion editorial lifestyle photo,
  Một cô gái châu Á trẻ đẹp {PERSONA: da trắng mịn, khuôn mặt nhỏ thanh tú, mắt to, tóc đen dài gợn sóng},
  mặc {SẢN_PHẨM: ví dụ — váy đen ôm body, áo khoác tweed màu be, đội mũ nồi đen, đi bốt trắng cao cổ}.
  Góc chụp từ trên cao nhìn xuống (top view), cô gái ngước mặt nhìn thẳng vào camera, tạo dáng toàn thân.
  Bối cảnh {background_default: hành lang căn hộ hiện đại, ánh sáng tự nhiên mềm mại, không gian sang trọng tối giản}.
  Ánh sáng tự nhiên mềm mại từ bên, high-key sáng thoáng, shallow depth of field, bokeh nền nhẹ,
  natural skin texture with visible pores and fine imperfections, natural human proportions, soft even light, vertical 9:16.
  ```
- **Nhân bản:** giữ NGUYÊN {PERSONA} + {SẢN_PHẨM}, chỉ đổi bối cảnh để ra thêm keyframe (dùng làm start/end frame khác nhau cho từng clip trong thư viện motion).

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip** (chống méo). Giữ "cô gái mặc outfit như ảnh gốc" (reference-chaining). Bake `negative_constant` cuối mỗi prompt.
> Đây là PHẦN LÕI — chép NGUYÊN VĂN 8 nhóm motion nữ của tab thành 1 menu; pipeline chọn/ghép 3-5 cảnh. Mỗi nhóm có ~15 biến thể trong tab; dưới đây là bản đại diện verbatim (đổi biến thể để ra nhiều clip cùng loại).

**Phân cảnh 1 — Bước đi tự tin về phía trước (`TILT_UP_TRACK` + `WALK_TOWARD`):**
```
Bối cảnh: không gian sang trọng tối giản, ánh sáng mềm mại đồng đều.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, giữ nguyên khuôn mặt/tóc/outfit.
Hành động: Cô gái bước đi tự tin với dáng người thẳng và nụ cười tự nhiên, sang trọng. Camera di chuyển mượt mà từ dưới lên, bắt trọn chi tiết trang phục và gương mặt. Giữ ánh sáng mềm mại, đồng đều, không bị chói trên khuôn mặt hay trang phục, đảm bảo màu sắc ổn định trong suốt chuyển động.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền thời trang.
[negative_constant]
```

**Phân cảnh 2 — Vuốt tóc nhẹ nhàng (`PUSH_IN_SLOW` + `HAIR_FLIP`):**
```
Bối cảnh: không gian sáng dịu, có làn gió nhẹ.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Cô gái mỉm cười tự nhiên, nhẹ nhàng đưa tay vuốt tóc từ trước ra sau. Gió thổi nhẹ làm tóc bay mềm mại. Camera bắt đầu ở phần trên cơ thể và zoom dần vào gương mặt để nhấn mạnh thần thái tươi sáng.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 3 — Xoay người 360° (`ORBIT_360` + `SPIN_360`) — giữ chân người xem:**
```
Bối cảnh: không gian sáng dịu, sàn sáng, hậu cảnh tối giản.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Cô gái mỉm cười tự nhiên, xoay người chậm rãi 360°, dáng điệu thanh lịch. Camera lia theo vòng xoay, bắt trọn từng chi tiết bộ trang phục mà không làm biến dạng hay thay đổi màu sắc.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 4 — Chỉnh cổ áo / tay áo (`PUSH_IN_SLOW` + `ADJUST_COLLAR`/`ADJUST_SLEEVE`):**
```
Bối cảnh: không gian sang trọng, ánh sáng mềm ổn định.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Cô gái mỉm cười sang trọng, dùng một tay chỉnh nhẹ cổ áo. Camera zoom cận vào phần cổ áo để làm nổi bật chi tiết may và chất liệu, ánh sáng mềm mại, không bị chói.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> Biến thể tay áo (tab): "Cô gái chỉnh lại tay áo, động tác dứt khoát nhưng sang trọng. Camera zoom vào phần tay áo, nhấn mạnh độ co giãn và form ôm vừa vặn."

**Phân cảnh 5 — Cầm túi xách nhưng nhấn mạnh trang phục (`TILT_UP_BODY_TO_FACE` + `HOLD_BAG`):**
```
Bối cảnh: không gian sang trọng, ánh sáng chân thực.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, tay cầm túi.
Hành động: Cô gái mỉm cười nhẹ nhàng, tay cầm túi thả lỏng tự nhiên. Camera bắt đầu từ túi, lia lên toàn thân, nhấn mạnh bộ quần áo gọn gàng và màu sắc chân thực. Trang phục là điểm nhấn chính, túi chỉ làm phụ.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 6 — Kéo giãn áo khoe chất liệu (`PUSH_IN_SLOW` macro + `STRETCH_FABRIC`):**
```
Bối cảnh: ánh sáng ổn định, đều, không lóa.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Cô gái mỉm cười tự nhiên, dùng hai tay kéo nhẹ phần ống tay áo để thể hiện độ co giãn. Camera zoom cận vào phần tay áo, ánh sáng ổn định, màu sắc vải giữ nguyên, không bị biến dạng.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> Biến thể eo áo (tab): "Một tay cô gái giữ cố định, tay kia kéo nhẹ phần eo áo để làm nổi bật khả năng co giãn. Camera di chuyển từ góc chéo cận chi tiết vải, đảm bảo giữ đúng màu sắc và chất liệu."

**Phân cảnh 7 — Chỉ tay vào sản phẩm / tag giá (`RACK_FOCUS_TO_PRODUCT`/`PULL_OUT` + `POINT_AT_PRODUCT`):**
```
Bối cảnh: ánh sáng mềm mại và ổn định.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Cô gái mỉm cười nhẹ, dùng một tay chỉ vào logo trên áo. Camera zoom cận logo rồi từ từ lùi ra toàn thân, ánh sáng mềm mại và ổn định.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> Biến thể tag giá (tab): "Cô gái khẽ chỉ vào tag giá trên áo, cười thoải mái. Camera zoom cận thẻ giá và chất vải xung quanh." — hợp khi muốn khoe {giá} bằng hình.

**Phân cảnh 8 — Bước lại gần camera đầy tự tin (`DOLLY_IN` + `HANDHELD_SHAKE` + `APPROACH_CLOSE`):**
```
Bối cảnh: không gian sang trọng, ánh sáng ổn định giữ nguyên chi tiết và màu sắc.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Cô gái bước chậm rãi về phía camera, nụ cười sang trọng và tự tin. Camera hơi rung nhẹ để tạo cảm giác gần gũi, ánh sáng ổn định giữ nguyên chi tiết và màu sắc trang phục.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**(Tùy chọn) Phân cảnh 9 — Tạo dáng trước gương (`LOCKED_OFF` + `MICRO_TILT_LR`):**
```
Bối cảnh: trước gương, không gian thời trang toàn thân.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Video thời trang toàn thân của cô gái đang tạo dáng trước gương, cô gái xoay nhẹ hông và vai sang hai bên trước gương. Camera cố định, bắt trọn chuyển động mềm mại của bộ trang phục.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> Kỹ thuật giữ nhân vật: **Veo first+last frame** (đứng→xoay cho SPIN_360) HOẶC **Kling `roll 360` + Elements** (2-4 ref = character-sheet + keyframe). Motion strength **Subtle→Moderate** để vải/tóc không morph. Vải nhiều họa tiết/logo → giảm motion tránh warp (docs/aff-engine.md §10.14).

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- Import 3-5 clip AI đã chọn từ thư viện → **cắt đúng nhịp beat** nhạc trend TikTok. Thứ tự gợi ý: mở bằng walk/approach → giữ chân bằng 360 → chốt bằng detail-pass (kéo giãn/chỉ tay).
- **Đổi độ dài shot 1-8s** (đừng đều 3-4s → lộ AI); hard-cut mặc định. Text nhẹ trong safe-zone 9:16: "Outfit hôm nay ✨" (mở), chất liệu {SẢN_PHẨM} (giữa), "Link ở bio" (cuối). Caption karaoke nếu có voiceover.
- Gate chất lượng (docs/aff-engine.md §7, §10): color grade thống nhất warm, LUT ≤75%, grain 8%, −14 LUFS.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, flickering, inconsistent lighting, warp/biến dạng vải, đổi màu vải, watermark, text overlay` + `no cartoon/3D render`.
- **DO:** ảnh phải toàn thân + góc trên cao + outfit rõ; giữ NGUYÊN persona + màu/chất vải qua mọi clip; 1 camera-move + 1 action/clip; nhóm detail (kéo giãn/chỉ tay/chỉnh áo) là cận cảnh khoe chất liệu — bảo toàn 100% màu & đường may.
- **DON'T:** đừng tả lại đặc điểm mặt mỗi clip (gây drift); đừng xoay/kéo quá nhanh (morph vải); đừng để chân dính đáy khung / CTA vào 20% đáy; đừng dùng "8K/HDR" (da nhựa).

## 7. METADATA
- **Title** <70 ký tự: outfit-check nữ + điểm nhấn (vd "Set này mặc lên xịn hơn giá 🤍", "Chất vải co giãn khỏi chê").
- **Caption + 15-25 hashtag** ngách thời trang nữ (#outfit #ootd #reviewdo #thoitrangnu #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
