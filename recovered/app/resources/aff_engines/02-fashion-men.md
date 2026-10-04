---
id: fashion-men
name: "Thời trang NAM — Người mẫu nam mặc outfit (camera tĩnh, khoe form)"
archetype: A
video_type: "outfit-check-men"
niche_default: "Thời trang nam — người mẫu nam ảo mặc outfit, camera giữ cố định khoe form"
niches:
  - label: "Thời trang nam"
    fits: "set nam, áo sơ mi, áo khoác, quần tây, streetwear nam"
  - label: "Menswear công sở / smart-casual"
    fits: "sơ mi, blazer, quần âu, giày tây — nhấn form phẳng phiu"
  - label: "Phụ kiện nam"
    fits: "túi, thắt lưng, giày, đồng hồ — khoe khi mặc cả bộ"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"
final_length: "15-30s"
persona_scope: channel
faceless: false
design_lock: false
recurring_character: "{PERSONA} — nhân vật nam cố định của kênh (dùng character-sheet đã lưu, giữ y hệt mặt/tóc/dáng)"
scene_structure: "Menswear thiên CAMERA TĨNH: đa số cảnh 'camera giữ cố định / đứng im', nhân vật nam tự vận động (bước tới, xoay 360, quay 45-90°, tay vào túi, chỉnh áo, pose). Chỉ 1 dạng có camera lia (từ dưới chân lên mặt). 6-10s. Dạng này AI tạo rất mượt, ít lỗi — chuyển động chậm, dứt khoát, nam tính."
camera_sequence: [TILT_UP_BODY_TO_FACE, LOCKED_OFF, ORBIT_360, TURN_45_90, FOLLOW_WALK]
motion_presets: [fashion_walk_showcase, fashion_kol_3scene]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, medium-format-style film grain, natural color, menswear editorial lifestyle photo,"
image_style_lock: "natural skin texture with visible pores and fine imperfections, natural human proportions, soft even light, no color shift, vertical 9:16."
golden_rules: ["phải toàn thân (head-to-toe), form áo/quần rõ", "dáng thẳng, vai mở, phong thái nam tính tự tin", "outfit rõ ràng, màu chuẩn, đường may sắc nét", "camera giữ cố định là mặc định — để nhân vật vận động", "chọn ảnh đẹp nhất mới làm video"]
lighting_default: "soft diffused window light from camera-side + subtle rim light for separation, even and stable (không lóe, không đổi màu)"
color_look: "neutral-clean masculine (cân trắng chuẩn, contrast vừa, da khỏe không ngả cam; có thể lệch cool nhẹ cho menswear/streetwear)"
lut_intensity: 45
lens_default: "85mm portrait look, shallow depth of field, soft background bokeh"
camera_angle_default: "full-body slightly low angle (kéo dáng cao); talking/turn eye-level; adjust-collar chuyển trung-cận"
background_default: "hành lang căn hộ hiện đại / góc 2 tường tối giản sáng / showroom menswear neutral, sàn sạch, bokeh nhẹ"
skin_realism: "natural skin texture with visible pores and fine imperfections, natural human proportions"
negative_constant: "morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, flickering, inconsistent lighting, color shift, watermark, text overlay"
motion_strength: "subtle_to_moderate"
reference_workflow: "character-sheet 360 (front+45°+90°+back) → keyframe 9:16 2K full-body menswear → (mặc {SẢN_PHẨM} bằng mask-and-place) → Veo Ingredients/Kling Elements → clip theo menu §4"
post_chain: "upscale 4K → interp 30fps → LUT neutral-cool → grain 8% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (first-last frame / camera locked) / Kling 2.5-2.6 Cinematic (roll 360) — image-to-video"
tts_mood: "không thoại — nhạc nền menswear/streetwear"
music_mood: "nhạc trend TikTok beat rõ, tông cool/chắc để cắt cảnh"
tags: [outfit-check, koc-ao-nam, thoi-trang-nam, menswear, xoay-360, ootd-men, tiktok-shop, affiliate, streetwear]
---

# AFF Engine — Thời trang NAM · Người mẫu nam mặc outfit (camera tĩnh)

> **Kiểu:** A (người mẫu nam ảo mặc/khoe outfit) · **Dùng khi:** sản phẩm menswear mặc được (set nam/sơ mi/áo khoác/quần/phụ kiện nam). Tạo cảm giác một người mẫu nam thật đứng khoe form — phong thái nam tính, dứt khoát. Khác bản nữ ở chỗ **camera phần lớn ĐỨNG IM**, nhân vật tự vận động → AI làm cực mượt, ít morph.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl) + `{PERSONA}` (nhân vật nam cố định của kênh — dùng lại character-sheet đã lưu).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc (verbatim từ tab):** menswear thiên **camera tĩnh** — hầu hết prompt ghi rõ *"Camera giữ cố định / Camera đứng im / Camera không rung / Camera quay đứng yên"*. Nhân vật nam tự tạo chuyển động: **bước tới tự tin → xoay 360° → quay nhẹ 45-90° → bỏ tay vào túi quần → chỉnh/kéo áo → bước ngang khung → dừng lại pose 2-3 tư thế**. Chỉ dạng mở đầu là camera lia **từ chân/dưới lên mặt** để làm rõ trang phục và gương mặt. **Thời lượng 6-10 giây.** "Dạng này AI tạo rất mượt — ít lỗi."
- **Sản phẩm hợp:** đồ nam mặc được (set/sơ mi/khoác/quần/phụ kiện nam). **Persona:** BẮT BUỘC nhân vật nam cố định của kênh (đồng bộ thương hiệu).
- **Vì sao mượt:** menswear ít động tác bay-bổng (không hair-flip/váy xoè); camera locked-off + 1 chuyển động cơ thể chậm/dứt khoát → gần như không morph vải/tóc. Ít biến thể hơn bản nữ, nhưng chắc nét.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền + text overlay. (Nếu kênh muốn voiceover review, bật `dialogue_mode: vi_voiceover` và dùng khung Hook→Problem→Solution→CTA ở docs/aff-engine.md §3, giọng `vi_male_warm`.)
- **Hook (text overlay 0-3s):** 1 dòng khoe chất/form nam — ví dụ "Set này mặc lên là auto ngầu 🔥", "Form chuẩn menswear", "Giá này mà chất này á?". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** tên/điểm nhấn {SẢN_PHẨM} ngắn gọn (chất liệu, form, phom dáng).
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền 11 trường theo `{PERSONA}` + `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`. **Luật vàng menswear:** toàn thân (head-to-toe) · dáng thẳng vai mở nam tính · form áo/quần + đường may rõ · màu chuẩn.
> **11 trường (docs/aff-engine.md §5.7):** ① Chủ thể (nam) · ② Outfit ({SẢN_PHẨM}) · ③ Tóc · ④ Tư thế (đứng thẳng, vai mở / tay vào túi) · ⑤ Biểu cảm (điềm tĩnh, tự tin) · ⑥ Góc máy & cỡ cảnh (full-body hơi thấp hất lên) · ⑦ Ánh sáng (soft window + rim, đều, không đổi màu) · ⑧ Môi trường/nền (hành lang/showroom neutral) · ⑨ Color grade (neutral-clean, cool nhẹ) · ⑩ Phong cách nhiếp ảnh (menswear editorial film) · ⑪ Ống kính & DoF (85mm f/1.8 bokeh) + tỉ lệ 9:16.
- **Lưu ý nguồn:** tab NAM là bộ **motion prompt** (image→video, "từ bức ảnh tham chiếu") — không có prompt keyframe riêng. Keyframe dưới đây dựng theo chuẩn 11 trường + Quality Playbook §10, giữ nam tính:
  ```
  shot on 85mm, medium-format-style film grain, natural color, menswear editorial lifestyle photo,
  Một {PERSONA: chàng trai châu Á, gương mặt góc cạnh nam tính, da khỏe có texture thật, tóc undercut gọn}.
  Anh mặc {SẢN_PHẨM: mô tả outfit nam chi tiết — màu, form, chất liệu, phụ kiện/giày đi kèm}.
  Đứng toàn thân, dáng thẳng, vai mở, một tay hơi đưa vào túi quần, biểu cảm điềm tĩnh tự tin nhìn thẳng camera.
  Góc chụp hơi thấp hất lên nhẹ (kéo dáng cao), lấy trọn head-to-toe, form áo/quần và đường may rõ.
  Bối cảnh {background_default: hành lang căn hộ hiện đại / showroom menswear tối giản, sàn sạch, tường neutral}.
  Ánh sáng window mềm từ bên + rim tách nền, đều ổn định không đổi màu, shallow depth of field, bokeh nền nhẹ,
  natural skin texture with visible pores and fine imperfections, natural human proportions, soft even light, no color shift, vertical 9:16.
  ```
- **Nhân bản:** giữ NGUYÊN {PERSONA} + {SẢN_PHẨM}, chỉ đổi bối cảnh/tư thế tay để ra thêm keyframe (dùng làm start/end frame khác nhau).

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip**. Giữ "nhân vật nam mặc outfit như ảnh gốc" (reference-chaining). Bake `negative_constant` cuối mỗi prompt.
> Đây là PHẦN LÕI — menu chép NGUYÊN VĂN prompt tiếng Việt từ tab NAM; pipeline chọn/ghép 3-5 cảnh. **Menswear = camera tĩnh chủ đạo**, chỉ Phân cảnh 1 có camera lia lên.

**Phân cảnh 1 — Camera lia từ dưới chân lên mặt (`TILT_UP_BODY_TO_FACE` + `WALK_TOWARD`):**
```
Bối cảnh: hành lang căn hộ hiện đại, ánh sáng mềm đều, không gian sang trọng tối giản.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, giữ nguyên khuôn mặt/tóc/outfit.
Hành động (verbatim tab): "Tạo video dọc 9:16 từ bức ảnh tham chiếu. Nhân vật bước đi tự tin, dáng người thẳng và nụ cười tự nhiên. Camera chuyển động mượt từ dưới lên, làm rõ chi tiết trang phục và gương mặt. Giữ ánh sáng mềm, đều, không chói và đảm bảo màu sắc ổn định trong suốt cảnh quay."
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền menswear.
[negative_constant]
```

**Phân cảnh 2 — Camera cố định, bước tới trước tự tin (`LOCKED_OFF` + `WALK_TOWARD`):**
```
Bối cảnh: hành lang / showroom neutral, ánh sáng ổn định.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động (verbatim tab): "Tạo video dọc 9:16. Nhân vật nam bước tới trước tự tin, dáng người thẳng và nét mặt thoải mái. Camera giữ cố định và bắt trọn outfit khi nhân vật tiến gần." (biến thể: "Nhân vật nam tiến về phía trước với phong thái tự tin, vai mở và bước đều. Camera giữ ổn định và làm rõ từng chi tiết trang phục.")
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 3 — Camera đứng im, xoay người 360° (`ORBIT_360`/`SPIN_360`, camera locked):**
```
Bối cảnh: hành lang căn hộ hiện đại sang trọng, ánh sáng đều.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động (verbatim tab): "Nhân vật nam xoay tròn 360° để khoe trọn form quần áo. Camera đứng im, giữ toàn thân trong khung hình." (biến thể: "Nhân vật nam xoay 360° chậm, giữ tư thế thẳng và phong thái lịch sự. Camera quay đứng yên." / "Cho nhân vật nam xoay 360° với tốc độ tự nhiên, dừng lại ở mặt trước. Camera bắt rõ outfit từ đầu đến chân.")
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 4 — Camera cố định, chỉnh áo / kéo áo (`LOCKED_OFF` + `ADJUST_COLLAR`/`ADJUST_SLEEVE`):**
```
Bối cảnh: góc 2 tường tối giản, ánh sáng mềm, cỡ cận thân trên.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động (verbatim tab): "Nhân vật nam dùng hai tay chỉnh lại vạt áo nhẹ nhàng. Camera lấy cận thân trên, ánh sáng mềm." (biến thể: "Cho nhân vật nam kéo nhẹ phần cổ áo để làm rõ chất liệu. Camera giữ cố định, không rung." / "Nhân vật nam dùng tay vuốt áo từ trên xuống để tạo sự phẳng phiu. Camera bắt nét rõ form áo.")
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 5 — Camera cố định, bỏ tay vào túi quần (`LOCKED_OFF` + `HANDS_IN_POCKETS`):**
```
Bối cảnh: hành lang / showroom neutral, ánh sáng mềm đều.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động (verbatim tab): "Nhân vật nam bước nhẹ và đưa một tay vào túi quần, phong thái tự nhiên. Camera ghi toàn thân." (biến thể: "Tạo video 9:16. Nhân vật cho hai tay vào túi quần, đứng pose tự tin. Camera giữ cố định." / "Cho nhân vật nam tạo dáng với hai tay trong túi quần. Camera đứng im, outfit rõ nét.")
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 6 — Camera cố định, quay nhẹ 45°–90° trái/phải (`LOCKED_OFF` + `TURN_45_90`):**
```
Bối cảnh: góc 2 tường / showroom neutral, ánh sáng đều.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động (verbatim tab): "Nhân vật nam quay người 45° sang phải để khoe form áo. Camera giữ trung cảnh." (biến thể: "Cho nhân vật nam xoay nhẹ 90° sang trái và giữ dáng vài giây. Camera rõ outfit." / "Nhân vật nam xoay 90° sang trái rồi quay lại chính diện. Camera giữ nét, không rung.")
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 7 — Camera cố định, liếc mắt / quay đầu rồi nhìn lại camera (`LOCKED_OFF` + `WAVE_GREET`/glance):**
```
Bối cảnh: hành lang / góc tường sáng, ánh sáng đều, cỡ trung cảnh giữ nét gương mặt.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động (verbatim tab): "Nhân vật nam nhìn sang trái, sau đó quay lại nhìn camera. Camera trung cảnh." (biến thể: "Nhân vật liếc nhẹ sang phải rồi nhìn lại ống kính. Camera giữ nét gương mặt." / "Nhân vật nam quay đầu sang phải rồi trở lại chính diện. Camera ổn định.")
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 8 — Camera cố định, bước ngang qua khung hình (`LOCKED_OFF` + `WALK_ACROSS`):**
```
Bối cảnh: hành lang / showroom neutral, ánh sáng mềm đều.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động (verbatim tab): "Nhân vật nam bước ngang qua khung hình từ trái sang phải. Camera đứng im." (biến thể: "Nhân vật đi ngang qua ống kính chậm rãi để thể hiện form quần áo." / "Camera đứng im, nhân vật bước ngang và giữ ánh sáng mềm.")
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 9 — Camera cố định, dừng lại và pose 2–3 tư thế (`LOCKED_OFF` + `POSE_HOLD_2_3`):**
```
Bối cảnh: hành lang / góc tường tối giản, ánh sáng đều.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động (verbatim tab): "Nhân vật nam dừng lại và tạo 2 tư thế pose tự tin. Camera ghi toàn thân." (biến thể: "Nhân vật nam dừng lại tạo dáng với tay trong túi rồi đổi sang khoanh tay." / "Nhân vật đứng pose 2–3 kiểu để làm rõ trang phục. Camera trung cảnh.")
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

> Kỹ thuật giữ nhân vật: menswear ưu tiên **Veo camera locked / first+last frame** HOẶC **Kling `roll 360` + Elements** (2-4 ref = character-sheet + keyframe). Motion strength Subtle→Moderate để vải/đường may không morph. Chuyển động cơ thể chậm, dứt khoát — hợp phong thái nam.
> Ghép tối thiểu 3 cảnh (vd: ①TILT_UP → ③XOAY_360 → ⑨POSE) theo beat; thêm ⑥TURN_45_90 / ⑤HANDS_IN_POCKETS để đủ 5 cảnh.

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- Import 3-5 clip AI → **cắt đúng nhịp beat** nhạc trend TikTok; mở bằng TILT_UP, giữ chân bằng XOAY_360, kết bằng POSE/TURN.
- Text nhẹ trong safe-zone 9:16: hook nam tính (mở), điểm nhấn {SẢN_PHẨM} — chất liệu/form (giữa), "Link ở bio" (cuối). Caption karaoke nếu có voiceover.
- Gate chất lượng (docs/aff-engine.md §7, §10): color grade thống nhất neutral/cool nhẹ, grain 8%, −14 LUFS; **đổi độ dài shot 1-8s** (đừng đều 3-4s → lộ AI).
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, flickering, inconsistent lighting, color shift, watermark, text overlay` + `no cartoon/3D render`.
- **DO:** ảnh toàn thân + form/đường may rõ + dáng thẳng vai mở nam tính; **camera giữ cố định là mặc định** (chỉ Phân cảnh 1 lia lên); giữ NGUYÊN persona qua mọi clip; 1 camera-move + 1 action/clip; chuyển động cơ thể chậm dứt khoát.
- **DON'T:** đừng tả lại đặc điểm mặt mỗi clip (gây drift); đừng cho camera động cùng lúc với xoay người (kép chuyển động → warp); đừng để chân dính đáy khung / CTA vào 20% đáy; đừng dùng "8K/HDR" (da nhựa); đừng grade ngả cam quá (menswear giữ da khỏe, cool nhẹ).

## 7. METADATA
- **Title** <70 ký tự: outfit-check nam + điểm nhấn (vd "Set nam này mặc lên xịn hơn giá 🔥").
- **Caption + 15-25 hashtag** ngách menswear (#outfitnam #menswear #ootdmen #thoitrangnam #reviewdo #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
