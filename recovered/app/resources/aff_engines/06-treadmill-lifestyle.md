---
id: treadmill-lifestyle
name: "Mẫu trên máy chạy bộ — KOL đi bộ khoe outfit (camera cố định)"
archetype: A
video_type: "treadmill-lifestyle"
niche_default: "Thời trang nữ Hàn — người mẫu ảo đi bộ trên máy chạy bộ, khoe outfit + gesture KOL"
niches:
  - label: "Thời trang nữ Hàn"
    fits: "set nữ tính, váy, áo len, loungewear, outfit độ tuổi 18-25 quay trong phòng"
  - label: "Athleisure / đồ tập"
    fits: "legging, áo croptop tập, giày thể thao (hợp bối cảnh máy chạy bộ)"
  - label: "Phụ kiện outfit"
    fits: "túi, mũ, giày, kính — khoe khi đi bộ toàn thân"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"
final_length: "15-30s"
persona_scope: channel
faceless: false
design_lock: false
recurring_character: "{PERSONA} — nhân vật cố định của kênh (dùng character-sheet đã lưu, giữ y hệt mặt/tóc/dáng)"
scene_structure: "Máy quay CỐ ĐỊNH góc chính diện phía trước; người mẫu đi bộ tại chỗ trên máy chạy bộ trong phòng khách retro và lần lượt đổi gesture KOL (vẫy chào → tạo tim → chữ V → tay lên ngực → vươn 2 tay). Mỗi gesture = 1 clip 6-10s, ghép thành chuỗi."
camera_sequence: [LOCKED_OFF_FRONT, LOCKED_OFF_FRONT, LOCKED_OFF_FRONT, LOCKED_OFF_FRONT, LOCKED_OFF_FRONT]
motion_presets: [treadmill_kol_gestures]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, medium-format-style film grain, natural color, lifestyle fashion lookbook photo,"
image_style_lock: "natural skin texture with visible pores and fine imperfections, natural human proportions, warm soft light, vertical 9:16."
golden_rules: ["ảnh chụp TOÀN THÂN người mẫu đứng trên máy chạy bộ", "máy quay góc chính diện cố định phía trước", "phòng khách retro nội thất gỗ ấm + gương lớn bên cạnh", "outfit rõ ràng, màu chuẩn; chọn ảnh đẹp nhất mới làm video"]
lighting_default: "warm cozy indoor lighting, soft practical lamp glow (đèn ngủ ánh sáng cam ấm), gentle shadows + soft natural window light, high-key bias sáng thoáng"
color_look: "warm-iphone (lifted shadows, protected highlights, flattering warm skin) — tông ấm phòng retro"
lut_intensity: 50
lens_default: "85mm portrait look, shallow depth of field, soft background bokeh (phòng khách blur nhẹ)"
camera_angle_default: "full-body chính diện eye-level, máy quay CỐ ĐỊNH phía trước (LOCKED_OFF), chừa head/foot room"
background_default: "phòng khách hiện đại phong cách retro: nội thất gỗ ấm, kệ trang trí + cây xanh nhỏ, đèn ngủ ánh cam ấm, TV phía sau, gương lớn bên cạnh"
skin_realism: "natural skin texture with visible pores and fine imperfections, natural human proportions"
negative_constant: "morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, camera móving/drift (giữ máy cố định), flickering, inconsistent lighting, background thay đổi, méo hình, watermark, text overlay"
motion_strength: "subtle_to_moderate"
reference_workflow: "character-sheet 360 (front+45°+90°+back) → keyframe 9:16 2K toàn thân trên máy chạy bộ (mặc {SẢN_PHẨM} bằng mask-and-place) → Veo Ingredients/Kling Elements → mỗi gesture 1 beat clip (camera locked-off)"
post_chain: "upscale 4K → interp 30fps → LUT warm → grain 8% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "ChatGPT-image (như tab) / Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients, camera locked) / Kling 2.5-2.6 Cinematic — image-to-video giữ nền tĩnh"
tts_mood: "không thoại — nhạc nền thời trang"
music_mood: "nhạc trend TikTok nữ tính, beat rõ để cắt cảnh + nhún nhảy"
tags: [treadmill, may-chay-bo, koc-ao, kol-ao, thoi-trang-han, outfit, camera-co-dinh, gesture-kol, tiktok-shop, affiliate]
---

# AFF Engine — Mẫu trên máy chạy bộ · KOL đi bộ khoe outfit

> **Kiểu:** A (người mẫu ảo mặc/khoe outfit) · **Dùng khi:** sản phẩm mặc được (set nữ Hàn, athleisure, phụ kiện). Người mẫu đi bộ tại chỗ trên máy chạy bộ trong phòng khách retro ấm cúng, máy quay **cố định phía trước**, lần lượt "diễn" các gesture KOL mạng xã hội (vẫy chào, tạo hình tim, chữ V, tay lên ngực, vươn tay). Cảm giác một KOL đang livestream/quay reel tại nhà — thân thiện, dễ viral, AI làm CỰC mượt vì **nền tĩnh + camera đứng yên**.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl) + `{PERSONA}` (nhân vật cố định của kênh — dùng lại character-sheet đã lưu).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc (verbatim tinh thần tab):** Máy quay giữ **góc chính diện cố định phía trước**, người mẫu **đi bộ tự nhiên trên máy chạy bộ** trong phòng khách hiện đại phong cách retro, rồi lần lượt đổi **gesture KOL mạng xã hội**: ① vẫy tay chào → ② tạo hình trái tim trước ngực → ③ giơ tay tạo chữ V gần mặt → ④ tay phải đặt lên ngực + quay mặt cười → ⑤ vươn 2 tay rồi chào. Mỗi gesture = 1 clip **6-10 giây**, ghép nối thành video.
- **Sản phẩm hợp:** đồ mặc được (thời trang nữ Hàn, athleisure, phụ kiện outfit). **Persona:** BẮT BUỘC dùng nhân vật cố định của kênh (đồng bộ thương hiệu).
- **Vì sao AI làm mượt, ít lỗi:** **camera đứng yên (locked-off) + nền không đổi** → mẫu chỉ vận động chân + tay tại chỗ, không có camera-move/parallax để morph nền; động tác tay đơn giản, rõ ràng từng clip. Đây là kiểu "an toàn" nhất cho AI-video.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền + text overlay. (Nếu kênh muốn voiceover review, bật `dialogue_mode: vi_voiceover` và dùng khung Hook→Problem→Solution→CTA ở docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng khoe/thân thiện — ví dụ "Vừa tập vừa khoe outfit 🏃‍♀️✨", "Set Hàn này mà giá này á?", "Chào buổi sáng nè 👋". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** tên/điểm nhấn {SẢN_PHẨM} ngắn gọn (chất liệu, form, phong cách Hàn).
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — ChatGPT-image / Nano Banana / Flow / Meta)
Điền 11 trường theo `{PERSONA}` + `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`. **Golden rules:** ảnh phải **toàn thân đứng trên máy chạy bộ** · **máy quay chính diện cố định phía trước** · **phòng khách retro (gỗ ấm + gương lớn + đèn cam)** · outfit rõ.
- **Golden rules (verbatim từ tab):** "Ảnh chụp toàn thân... đang đi bộ trên máy chạy bộ trong phòng khách hiện đại", phòng phong cách retro, nội thất gỗ ấm, đèn ngủ ánh cam ấm, TV phía sau, gương lớn bên cạnh, "góc máy thời trang lookbook", "giống ảnh quay video thời trang trên mạng xã hội".
- **Ví dụ VERBATIM (từ tab, thay chỗ động bằng {SẢN_PHẨM}/{PERSONA}):**
  ```
  Ảnh chụp toàn thân một {PERSONA: cô gái châu Á xinh đẹp, dáng cao, thanh mảnh, trang điểm nhẹ nhàng sang trọng, tóc đen thẳng, da trắng} đang đi bộ trên máy chạy bộ trong phòng khách hiện đại.
  Cô mặc {SẢN_PHẨM: mô tả outfit chi tiết — màu, form, chất liệu, phụ kiện đi kèm}.

  Phòng có:
  – phong cách retro
  – nội thất gỗ ấm, kệ trang trí và cây xanh nhỏ
  – đèn ngủ ánh sáng cam ấm
  – TV phía sau
  – một chiếc gương lớn bên cạnh

  Ánh sáng tự nhiên mềm, góc máy thời trang lookbook, ánh sáng studio tự nhiên, chi tiết sắc nét, màu sắc ấm áp, phong cách lifestyle fashion, tỉ lệ 9:16, giống ảnh quay video thời trang trên mạng xã hội.
  natural skin texture with visible pores and fine imperfections, natural human proportions, warm soft light, vertical 9:16.
  ```
  > **Lưu ý style_anchor:** tab gốc ghi "chất lượng 8K, siêu chi tiết, độ phân giải cao" — ĐÃ BỎ theo Quality Playbook §10.2 (8K/HDR/hyperrealistic đẩy sang da nhựa/AI-face). Thay bằng `shot on 85mm, medium-format-style film grain, natural color` ở đầu prompt + skin_realism ở cuối.
- **Nhân bản:** giữ NGUYÊN {PERSONA} + {SẢN_PHẨM} + phòng retro, chỉ đổi góc đứng/biểu cảm để ra thêm keyframe (dùng làm start-frame cho từng gesture clip).

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi gesture 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **máy quay CỐ ĐỊNH (locked-off) + 1 gesture / clip** (chống méo); nền phòng retro **giữ nguyên không đổi** (reference-chaining). Giữ "người mẫu mặc outfit như ảnh gốc". Bake `negative_constant` cuối mỗi prompt.
> Đây là PHẦN LÕI — mỗi gesture KOL từ tab = 1 block verbatim; pipeline chọn/ghép chuỗi.

**Phân cảnh 1 — Vẫy tay chào (`LOCKED_OFF_FRONT` + `TREADMILL_GESTURE:wave`):**
```
Bối cảnh: phòng khách hiện đại phong cách retro, nội thất gỗ ấm, đèn ngủ ánh cam ấm, gương lớn bên cạnh; ánh sáng ổn định.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc, giữ nguyên khuôn mặt/tóc/outfit.
Hành động: Người mẫu vừa đi bộ vừa giơ tay chào camera, biểu cảm thân thiện, chuyển động mượt, nền giữ nguyên, không méo hình. Máy quay giữ góc chính diện cố định.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền thời trang.
[negative_constant]
```

**Phân cảnh 2 — Tạo hình trái tim trước ngực (`LOCKED_OFF_FRONT` + `TREADMILL_GESTURE:heart`):**
```
Bối cảnh: phòng khách retro như ảnh gốc, ánh sáng cam ấm ổn định.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Người mẫu đi bộ trên máy chạy bộ và tạo hình trái tim bằng tay trước ngực, ánh mắt nhìn vào camera, phong cách KOL mạng xã hội. Máy quay giữ góc chính diện cố định.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 3 — Tạo chữ V gần mặt (`LOCKED_OFF_FRONT` + `TREADMILL_GESTURE:V`):**
```
Bối cảnh: phòng khách retro như ảnh gốc.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Người mẫu vừa đi bộ vừa giơ tay tạo hình chữ V gần mặt. Cười tươi rạng rỡ, đầu hơi nghiêng nhẹ, nhún nhảy theo nhịp nhạc. Máy quay giữ góc chính diện cố định.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 4 — Tay đặt lên ngực, quay mặt cười (`LOCKED_OFF_FRONT` + `TREADMILL_GESTURE:hand-on-chest`):**
```
Bối cảnh: phòng khách retro như ảnh gốc.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Người mẫu đi trên máy chạy bộ, tay phải đặt lên ngực, tay trái vẫy chào, sau đó quay mặt sang trái, cười tươi, tạo dáng sang trọng. Máy quay giữ góc chính diện cố định, ánh sáng ổn định.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

**Phân cảnh 5 — Vươn 2 tay rồi chào (`LOCKED_OFF_FRONT` + `TREADMILL_GESTURE:reach`):**
```
Bối cảnh: phòng khách retro như ảnh gốc.
Nhân vật/Sản phẩm: {PERSONA} mặc {SẢN_PHẨM} như ảnh gốc.
Hành động: Người mẫu đi trên máy chạy bộ, 2 tay vươn mình, đan xen vào nhau sau đó hạ tay, đưa 2 tay chào camera, biểu cảm thân thiện, chuyển động mượt, nền giữ nguyên, không méo hình. Máy quay giữ góc chính diện cố định.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant]
```

> **Clip nền (mở/đóng) — Đi bộ mỉm cười (`LOCKED_OFF_FRONT` + `TREADMILL_GESTURE:walk`):** "Người phụ nữ đang đi bộ tự nhiên trên máy chạy bộ, mỉm cười với camera, tóc chuyển động nhẹ theo bước đi, máy quay giữ góc chính diện cố định, ánh sáng ổn định, chuyển động chân thực." Dùng làm intro/outro trung tính.
> **Kỹ thuật giữ nhân vật + nền tĩnh:** dùng **Veo Ingredients** (nạp keyframe + character-sheet + sản phẩm) hoặc **Kling Elements (2-4 ref)** với `maintains exact appearance throughout`; **KHÓA camera** (`camera stays locked, no pan, no zoom`); motion strength Subtle→Moderate để vải/tóc/tay không morph. Mở rộng menu: xem enum docs/aff-engine.md §5.

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- Import các clip gesture → **cắt đúng nhịp beat** nhạc trend TikTok; xếp thứ tự vẫy chào → tim → chữ V → tay-ngực → vươn tay (hoặc mix theo beat). Đổi độ dài shot 1-8s, đừng đều → lộ AI.
- Text nhẹ trong safe-zone 9:16: hook (mở) → điểm nhấn {SẢN_PHẨM} (giữa) → "Link ở bio" (cuối). Caption karaoke nếu có voiceover.
- Gate chất lượng (docs/aff-engine.md §7, §10): color grade thống nhất warm, grain 8-10%, −14 LUFS. **QA:** kiểm tay/ngón đúng số khi tạo tim/chữ V; nền phòng không đổi giữa các cắt; mặt không morph.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `morphing faces, identity change, plastic skin, AI-face, beauty-filter giả, distorted hands, extra fingers, extra people, warped proportions, camera moving/drift, flickering, inconsistent lighting, background thay đổi, méo hình, watermark, text overlay` + `no cartoon/3D render` (kế thừa §10.9).
- **DO:** ảnh toàn thân trên máy chạy bộ + phòng retro đúng props (gỗ ấm/đèn cam/gương lớn); **giữ máy quay CỐ ĐỊNH** + nền không đổi mọi clip; 1 gesture/clip; kiểm tay/ngón ở gesture tim & chữ V.
- **DON'T:** đừng cho camera pan/zoom (mất lợi thế "nền tĩnh"); đừng tả lại đặc điểm mặt mỗi clip (gây drift); đừng làm gesture quá nhanh (morph tay/vải); đừng dùng "8K/HDR" (da nhựa); đừng để chân dính đáy khung / CTA vào 20% đáy.

## 7. METADATA
- **Title** <70 ký tự: treadmill + khoe outfit (vd "Vừa đi bộ vừa flex outfit Hàn 🏃‍♀️🤍").
- **Caption + 15-25 hashtag** ngách thời trang Hàn (#outfit #ootd #thoitranghan #reviewdo #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
