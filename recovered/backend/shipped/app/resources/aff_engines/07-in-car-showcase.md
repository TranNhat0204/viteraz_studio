---
# ⚠️ ENRICHED ENGINE — nguồn tab (04_M_U_NG_I_TR_N_OTO / "MẪU NGỒI TRÊN OTO") CHỈ CÓ ~1 DÒNG STUB
# (đúng 1 câu lệnh tạo ảnh: cô gái ngồi ghế lái ô tô sang, góc từ ghế phụ hất lên, ngoài xe là phố + nhà cao tầng).
# → File này GIỮ NGUYÊN VĂN nội dung stub (mục 3 ví dụ ảnh), phần còn lại được LÀM GIÀU trung thực theo
#   cấu trúc exemplar 09-kol-koc-3scene.md + Quality Playbook §10, đồng nhất với các fashion-engine khác
#   (in-car lifestyle outfit showcase). Không mâu thuẫn với stub.
id: in-car-showcase
name: "Mẫu ngồi trên ô tô — Outfit trong xe (in-car lifestyle)"
archetype: A
video_type: "outfit-check"
niche_default: "Thời trang nữ — người mẫu ngồi ghế lái ô tô sang, khoe outfit đời thường trong xe"
niches:
  - label: "Thời trang nữ đời thường"
    fits: "váy, set đi chơi, áo khoác, đồ công sở nhẹ mặc trong xe"
  - label: "Phụ kiện & túi"
    fits: "túi xách, kính mát, đồng hồ, khăn — đặt trên đùi/ghế phụ, dễ khoe cận"
  - label: "Streetwear nam (đổi persona nam)"
    fits: "áo khoác, hoodie, set nam ngồi ghế lái"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"
final_length: "15-30s"
persona_scope: channel
faceless: false
design_lock: false
recurring_character: "{PERSONA} — nhân vật cố định của kênh (dùng lại character-sheet đã lưu, giữ y hệt mặt/tóc/dáng)"
scene_structure: "3 phân cảnh trong xe: (1) LOCKED_OFF góc ghế phụ hất lên khoe cả outfit + không gian nội thất → (2) mẫu hơi quay về camera + chỉnh lại áo/tóc (slight push-in) → (3) khoe phụ kiện (túi/kính/đồng hồ) cận nhẹ. 6-10s, camera gần như tĩnh nên AI làm rất mượt, ít lỗi."
camera_sequence: [LOCKED_OFF, PUSH_IN_SLOW, RACK_FOCUS_TO_PRODUCT]
motion_presets: [fashion_incar_3scene]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, medium-format-style film grain, natural color, warm daylight lifestyle photo,"
image_style_lock: "natural skin texture with visible pores and fine imperfections, natural human proportions, warm window daylight, shallow depth of field, vertical 9:16."
golden_rules: ["góc từ ghế phụ hất lên (low angle up)", "thấy rõ outfit + phần ghế ngồi/nội thất xe", "cửa kính xe cho ánh sáng ban ngày ấm, cozy", "ngoài xe thấy phố + nhà cao tầng làm nền bokeh", "chọn ảnh đẹp nhất mới làm video"]
lighting_default: "warm daytime sunlight through the car window from camera-side, soft wraparound on face, cozy interior ambience, gentle natural shadows"
color_look: "warm-iphone (lifted shadows, protected highlights, flattering warm skin, cozy tone)"
lut_intensity: 50
lens_default: "85mm portrait look, shallow depth of field (f/1.8), street outside window softly blurred into bokeh"
camera_angle_default: "from passenger seat, low angle tilted up toward the driver; subject in upper 1/3"
background_default: "nội thất ô tô sang (ghế da, vô-lăng); ngoài cửa kính là đường phố xe cộ + nhà cao tầng nhoè bokeh"
skin_realism: "natural skin texture with visible pores and fine imperfections, natural human proportions"
negative_constant: "morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped car interior, floating steering wheel, reflection artifacts on glass, flickering, inconsistent lighting, watermark, text overlay"
motion_strength: "subtle_to_moderate"
reference_workflow: "character-sheet 360 → keyframe 9:16 2K in-car (mask-and-place {SẢN_PHẨM} lên người) → Veo Ingredients/Kling Elements → 3 beat clip"
post_chain: "upscale 4K → interp 30fps → LUT warm → grain 8% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients/first-last) / Kling 2.5-2.6 Cinematic — image-to-video"
tts_mood: "không thoại — nhạc nền lifestyle nhẹ nhàng"
music_mood: "nhạc trend TikTok chill/vibe lái xe, beat rõ để cắt cảnh"
tags: [in-car, outfit-check, oto, koc-ao, thoi-trang, lifestyle, tiktok-shop, affiliate, ootd, xe-sang]
---

# AFF Engine — Mẫu ngồi trên ô tô · Outfit trong xe

<!-- ENRICHED: tab nguồn chỉ là stub ~1 dòng; engine này dựng đầy đủ theo exemplar + Quality Playbook §10. -->

> **Kiểu:** A (người mẫu mặc/khoe outfit) · **Dùng khi:** sản phẩm mặc/đeo được, muốn cảm giác lifestyle "sang, chill" — cô gái ngồi ghế lái xe sang, ánh nắng ấm qua cửa kính. Camera gần như tĩnh nên AI render rất mượt, ít méo.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl) + `{PERSONA}` (nhân vật cố định của kênh — dùng lại character-sheet đã lưu).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc:** 3 phân cảnh trong xe — ① camera **cố định** đặt ở **ghế phụ, hất lên** khoe toàn bộ outfit + phần ghế ngồi + nội thất xe → ② mẫu **hơi quay về phía camera**, chỉnh lại áo/tóc, camera **đẩy nhẹ (slight push-in)** → ③ **khoe phụ kiện** (túi/kính/đồng hồ) với nét chuyển về sản phẩm. **Thời lượng 6-10 giây.**
- **Sản phẩm hợp:** đồ mặc được + phụ kiện (túi, kính mát, đồng hồ, khăn). **Persona:** BẮT BUỘC dùng nhân vật cố định của kênh.
- **Vì sao mượt (ghi chú kỹ thuật):** camera **gần như tĩnh** (LOCKED_OFF / slight push-in), người ngồi ít chuyển động → cực ít biến dạng vải/tay; ánh sáng cửa kính ổn định. Chỉ cần canh **cửa kính + phố ngoài xe** để có bokeh "đắt tiền".

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền + text overlay. (Muốn voiceover review thì bật `dialogue_mode: vi_voiceover`, dùng khung Hook→Problem→Solution→CTA docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng lifestyle/khoe — ví dụ "Outfit đi cà phê hôm nay ✨", "Ngồi lên xe là auto xịn", "Set này mà giá này á?". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** điểm nhấn {SẢN_PHẨM} ngắn (chất liệu, form) + tên phụ kiện đang khoe.
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền 11 trường (docs/aff-engine.md §5.7) theo `{PERSONA}` + `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`.
- **Golden rules (từ stub + quy ước fashion-engine):** góc **từ ghế phụ hất lên** · thấy rõ **outfit + phần ghế ngồi/nội thất** · **cửa kính** cho nắng ấm cozy · ngoài xe là **phố + nhà cao tầng** nhoè bokeh.
- **Ví dụ VERBATIM (giữ nguyên câu lệnh stub, thay chỗ động bằng {biến}):**
  ```
  shot on 85mm, medium-format-style film grain, natural color, warm daylight lifestyle photo,
  Tạo hình ảnh {PERSONA: cô gái châu Á trẻ, da sáng mịn, mặt nhỏ thanh tú, tóc đen dài gợn sóng}
  ngồi trong 1 chiếc ô tô sang trọng, ở ghế lái, cô gái đang lái xe.
  Cô mặc {SẢN_PHẨM: mô tả outfit chi tiết — màu, form, chất liệu, phụ kiện đi kèm}.
  Góc chụp từ ghế phụ và hướng từ dưới lên, nhìn thấy phần ghế ngồi của cô gái,
  bên ngoài cửa kính là đường phố xe đi lại, cùng nhà cao tầng.
  Ánh sáng ban ngày ấm áp hắt qua cửa kính, không gian nội thất ấm cúng, cozy,
  shallow depth of field, phố ngoài xe nhoè bokeh nhẹ,
  natural skin texture with visible pores and fine imperfections, natural human proportions, warm window daylight, shallow depth of field, vertical 9:16.
  ```
- **Nhân bản (nếu cần thêm keyframe):** giữ NGUYÊN {PERSONA} + {SẢN_PHẨM} + nội thất xe, chỉ đổi khung ngoài cửa kính (phố ngày ↔ hoàng hôn) hoặc đổi phụ kiện khoe — làm start/end frame khác nhau.

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip** (chống méo). Giữ "cô gái mặc outfit như ảnh gốc" (reference-chaining). Bake `negative_constant` cuối mỗi prompt.
> Đây là PHẦN LÕI — 3 phân cảnh dưới là 1 menu; pipeline chọn/ghép theo beat nhạc.

**Phân cảnh 1 — Ngồi lái, camera cố định hất lên (`LOCKED_OFF` + `IN_CAR_DRIVE`):**
```
Bối cảnh: nội thất ô tô sang trọng (ghế da, vô-lăng), nắng ban ngày ấm hắt qua cửa kính, ngoài xe là phố + nhà cao tầng nhoè bokeh.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, giữ nguyên khuôn mặt/tóc/outfit.
Hành động: camera CỐ ĐỊNH ở ghế phụ, hất nhẹ lên. Cô gái ngồi ghế lái tay đặt hờ trên vô-lăng, khẽ liếc ra ngoài rồi nhìn về phía camera, biểu cảm thư thái tự tin. Chuyển động rất nhẹ, đời thường.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền lifestyle nhẹ.
[negative_constant]
```
**Phân cảnh 2 — Quay về camera, chỉnh lại outfit (`PUSH_IN_SLOW` + `ADJUST_COLLAR`):**
```
Bối cảnh: trong xe như phân cảnh trước, ánh sáng cửa kính ổn định, cozy.
Nhân vật: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: camera ĐẨY VÀO chậm. Cô gái hơi quay người về phía camera, chỉnh lại cổ áo/tà áo và vuốt nhẹ tóc, mỉm cười duyên. Vải áo chuyển động mềm mại chân thực, tay giữ đủ ngón.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
**Phân cảnh 3 — Khoe phụ kiện (`RACK_FOCUS_TO_PRODUCT` + `POINT_AT_PRODUCT`):**
```
Bối cảnh: trong xe, phụ kiện ({SẢN_PHẨM}: túi/kính/đồng hồ) đặt trên đùi hoặc ghế phụ.
Nhân vật: {PERSONA} mặc/đeo {SẢN_PHẨM} như ảnh gốc.
Hành động: camera giữ gần cố định, NÉT chuyển từ khuôn mặt sang phụ kiện. Cô gái nâng/chạm nhẹ phụ kiện khoe chất liệu, ngón tay lướt bề mặt. Nét vào sản phẩm, hậu cảnh mờ nhẹ.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```
> Kỹ thuật giữ nhân vật: **Veo first+last frame** HOẶC **Kling Elements** (2-4 ref = character-sheet + keyframe in-car + ảnh sản phẩm). Motion strength Subtle→Moderate để vải/tóc/nội thất xe không morph.
> Mở rộng menu (tùy chọn): `PAN_LR` khoe toàn cảnh nội thất; `HANDHELD_SHAKE` nhẹ cho cảm giác UGC thật. Xem enum docs/aff-engine.md §5.3-5.4.

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- Import 3 clip AI → **cắt đúng nhịp beat** nhạc trend TikTok → thứ tự ①②③; đổi độ dài shot (đừng đều 3-4s → lộ AI); hard-cut mặc định.
- Text nhẹ trong safe-zone 9:16: "Outfit đi cà phê ✨" (mở), điểm nhấn {SẢN_PHẨM} (giữa), "Link ở bio" (cuối). Caption karaoke nếu có voiceover.
- Gate chất lượng (docs/aff-engine.md §7, §10): color grade thống nhất warm-cozy, grain 8%, −14 LUFS.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped car interior, floating steering wheel, reflection artifacts on glass, flickering, inconsistent lighting, watermark, text overlay` + `no cartoon/3D render` (kế thừa §5.5).
- **DO:** góc từ ghế phụ hất lên + thấy rõ outfit & ghế ngồi; giữ NGUYÊN persona + nội thất xe qua cả 3 clip; 1 camera-move + 1 action/clip; nắng cửa kính ấm + bokeh phố ngoài xe.
- **DON'T:** đừng để camera chao/xoay mạnh trong xe (méo vô-lăng, ghế); đừng tả lại đặc điểm mặt mỗi clip (gây drift); đừng để phản chiếu cửa kính lỗi; đừng dùng "8K/HDR" (da nhựa); đừng để hero/CTA vào 20% đáy.

## 7. METADATA
- **Title** <70 ký tự: in-car outfit + điểm nhấn (vd "Set lên xe là auto sang 🤍").
- **Caption + 15-25 hashtag** ngách thời trang/lifestyle (#outfit #ootd #xesang #reviewdo #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
