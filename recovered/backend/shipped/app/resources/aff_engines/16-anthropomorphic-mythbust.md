---
id: anthropomorphic-mythbust
name: "Vật dụng nhân hoá — Bóc thói quen sai (edutainment sức khỏe/gia dụng)"
archetype: C
video_type: "anthropomorphic-mythbust"
niche_default: "Sức khỏe / gia dụng — đồ vật có mắt-miệng cartoon tự kể thói quen sai của gia chủ rồi sửa"
niches:
  - label: "Thực phẩm / bếp núc"
    fits: "cơm, canh, rau, trái cây, thức ăn thừa, dầu chiên, nước sốt, sữa, đồ đông lạnh"
  - label: "Gia dụng nhà bếp"
    fits: "nồi, chảo chống dính, bình giữ nhiệt, nồi cơm điện, nắp nồi, bình lọc nước, nồi áp suất"
  - label: "Đồ điện / vật dụng nhà"
    fits: "quạt điện, máy sấy tóc, tủ lạnh, bình nhựa, bình xịt dầu, bình đựng gia vị"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "8s"
final_length: "8-15s"
persona_scope: none
faceless: false
design_lock: false
recurring_character: "vật dụng được nhân hoá (mắt/miệng cartoon) — mỗi clip 1 món, nói ngôi thứ nhất 'tao'"
scene_structure: "6 slot cố định trong 1 clip 8s: (1) vật hiện ra có mắt/miệng → (2) Scene starts: gia chủ làm THÓI QUEN SAI vì tưởng đúng → (3) Visual consequence: hậu quả xấu hiện hình (vi khuẩn/mốc/độc tố hoạt hình) → (4) Scene corrects: cách làm đúng → (5) Environment (Kitchen/Home/Fridge...) → (6) Spoken dialogue: câu 'tao/mày' đường phố + đuôi no-text."
camera_sequence: [LOCKED_OFF]
motion_presets: [anthropomorphic_tip]
dialogue_mode: vi_voiceover
voice: anthropomorphic_street
image_style_anchor: "A 3D animated cartoon character, semi-cartoon Pixar-style, expressive anthropomorphic object with cartoon eyes and mouth, soft clean lighting,"
image_style_lock: "cute expressive anthropomorphic object, clean home/kitchen background, vertical 9:16."
golden_rules: ["mỗi clip CHỈ 1 vật được nhân hoá (mắt + miệng cartoon trên bề mặt)", "phải đủ 6 slot: hiện ra → thói quen sai → hậu quả hiện hình → sửa → environment → thoại 'tao/mày'", "câu thoại giữ NGUYÊN register đường phố 'tao/mày', ngắn gọn bắt tai", "hậu quả phải THẤY được (vi khuẩn/mốc/độc tố hoạt hình) — edutainment chứ không bán hàng"]
lighting_default: "soft even cartoon lighting, bright and friendly, gentle shadows"
color_look: "clean bright cartoon grade, warm friendly tones, natural food colors"
lut_intensity: 40
lens_default: "cartoon 3D render, subject tack-sharp, simple shallow background"
camera_angle_default: "eye-level on the object, product 45° for context"
background_default: "kitchen / home / fridge / sink environment — sạch, đơn giản, không lộn xộn"
skin_realism: "n/a — semi-cartoon anthropomorphic object, giữ mắt/miệng cartoon dễ thương, biểu cảm rõ"
negative_constant: "no text, no subtitles, no logos, no watermark, no extra characters, no morphing, no flickering, no distorted proportions, no scary/horror imagery, no real human face"
motion_strength: "subtle_to_moderate"
reference_workflow: "1 keyframe ảnh vật nhân hoá (mắt/miệng cartoon trên bề mặt) → image-to-video 1 clip 8s chạy trọn 6 slot → nhân bản đổi {VẬT} + thói quen + thoại để ra hàng loạt topic"
post_chain: "grain nhẹ 3-5% → LUT bright-clean ≤40% → VN voice 'tao/mày' −14 LUFS + nhạc trend vui"
quality_knobs: [lighting_mood, color_look, lut_intensity, background, pacing, caption_style, voice_energy]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 / Kling 2.5-2.6 (image-to-video, semi-cartoon) — 8s"
tts_mood: "giọng đường phố 'tao/mày' tưng tửng, gần gũi, hài duyên"
music_mood: "nhạc trend TikTok vui nhộn, beat nhẹ, không át thoại"
tags: [suc-khoe, gia-dung, meo-vat, nhan-hoa, cartoon, edutainment, myth-busting, tao-may, nuoi-kenh, tiktok]
---

# AFF Engine — Vật dụng nhân hoá · Bóc thói quen sai

> **Kiểu:** C (engagement / edutainment — nuôi follower quanh account aff, KHÔNG review sản phẩm trực tiếp) · **Dùng khi:** muốn nuôi kênh sức khỏe/gia dụng bằng mẹo vặt bắt tai, phủ SEO-topic, gom follower rồi mới cắm link.
> Đây là **engine TEMPLATE điền chỗ trống** (fill-in): giữ NGUYÊN bộ 6 slot cố định, chỉ thay `{VẬT}` (thực phẩm/đồ gia dụng) + thói quen sai + câu thoại. 1 schema → sinh ra được cả trăm clip topic khác nhau.
> Input: `{VẬT}` (tên đồ vật/thực phẩm) + thói quen sai phổ biến + hậu quả + cách sửa. Không cần `{PERSONA}` (persona_scope: none).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Format bóc thói quen sai (myth-bust):** một đồ vật/thực phẩm được **nhân hoá** (gắn mắt + miệng cartoon lên bề mặt) tự đứng ra kể: gia chủ đang làm **một thói quen SAI vì tưởng là đúng** → **hậu quả xấu hiện hình** (vi khuẩn/mốc/độc tố/chất thôi nhiễm vẽ kiểu hoạt hình) → **cách làm đúng**. Cuối cùng vật buông một câu **ngôi thứ nhất "tao/mày"** đường phố, tưng tửng mà thấm.
- **Cấu trúc (verbatim từ tab — 6 slot cố định / 1 clip 8s):**
  ① dòng mở tả vật `A 3D animated cartoon [VẬT] with cartoon eyes and mouth...` → ② `Scene starts with` (thói quen sai) → ③ `Visual consequence:` (hậu quả hiện hình) → ④ `Scene corrects:` (sửa) → ⑤ `<...> environment.` → ⑥ `Spoken dialogue:` (câu "tao/mày") + đuôi `No text, no subtitles, no logos, no watermark.`
- **Sản phẩm hợp / lộ mặt:** không có người, không persona cố định — nhân vật là chính đồ vật. **Độ dài:** 8s/clip, có thể đăng lẻ hoặc nối vài clip cùng chủ đề.
- **Mục đích:** **edutainment nuôi kênh** (follower-farming + phủ SEO-topic sức khỏe/gia dụng) quanh một account affiliate — KHÔNG phải video bán hàng. Bán/aff chỉ chèn sau khi kênh có follower (soft CTA tùy chọn).
- **Vì sao AI làm mượt:** semi-cartoon nên KHÔNG cần chống AI-face/da nhựa; 1 vật đứng yên + biểu cảm cartoon + hiệu ứng hậu quả đơn giản → ít drift, ít lỗi.

## 2. KỊCH BẢN & LỜI (script layer)
> Ở engine này, **câu thoại "tao/mày" CHÍNH LÀ hook** — không cần hook overlay riêng. Đây là edutainment, KHÔNG phải sales; giữ giọng đường phố, đừng lên gân quảng cáo.
- **Hook = lời tự giới thiệu của vật (0-3s):** luôn mở bằng `"Tao là [VẬT] đây."` rồi vặn ngược cái tưởng-đúng của người xem. Mẫu verbatim từ tab:
  - `"Tao là [CƠM] đây. Kín quá tưởng tốt hả? Tao bí hơi là thiu liền đó. Xới tao ra cho thở coi."`
  - `"Tao là [CHẢO] đây. Đang nóng mà tạt nước là tao tróc da đó. Để tao nguội rồi hãy rửa."`
  - `"Tao là [QUẠT] đây. Không lau là tao thổi bụi vô mặt mày đó. Lau tao đi."`
- **Thân (Problem → Solution):** hậu quả nói bằng HÌNH (slot ③) + 1 câu thoại; cách sửa gói trong vế cuối câu thoại ("...giùm tao", "...cho tao thở coi"). Ngắn, có duyên, chốt bằng lời khuyên hành động.
- **CTA (tùy chọn, soft):** engine này mặc định KHÔNG bán. Khi kênh đã đủ follower mới cắm nhẹ: "Đồ trữ mát mình để ở giỏ hàng nha" + disclosure "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)
- **Text overlay:** KHÔNG — bake `No text, no subtitles, no logos, no watermark` (đúng tab). Caption/hashtag đặt ở phần đăng bài, không cháy trên video.

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Engine C semi-cartoon: dòng mở tab CHÍNH là spec ảnh keyframe. Mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`. **Luật vàng:** mỗi ảnh CHỈ 1 vật, gắn **mắt + miệng cartoon lên bề mặt vật**, nền nhà bếp/nhà sạch.
- **Ví dụ VERBATIM (từ tab, thay {VẬT}):**
  ```
  A 3D animated cartoon [VẬT] with cartoon eyes and mouth embedded on its surface, expressive anthropomorphic style.
  <Ví dụ vị trí mắt/miệng theo vật: on rice surface / on the pan surface / on the fan head / on the leaves / floating on the liquid surface>
  Kitchen environment (hoặc Home / Fridge / Kitchen sink environment).
  cute expressive anthropomorphic object, clean home/kitchen background, vertical 9:16.
  ```
- **Nhân bản:** giữ NGUYÊN phong cách semi-cartoon, chỉ đổi `{VẬT}` + chỗ gắn mắt/miệng để ra cả loạt keyframe (mỗi topic 1 vật).

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, 1 clip 8s chạy trọn 6 slot)
> **PHẦN LÕI — đây là TEMPLATE ĐIỀN CHỖ TRỐNG.** Chép NGUYÊN bộ 6 slot cố định của tab; pipeline chỉ thay `{VẬT}` + thói quen sai + hậu quả + cách sửa + câu thoại "tao/mày". Mỗi clip = 1 vật, 8s, LOCKED_OFF, chạy tuần tự 6 slot. Bake `negative_constant` cuối.

**SCHEMA CỐ ĐỊNH (6 slot — verbatim, giữ đúng nhãn tiếng Anh của tab):**
```
A 3D animated cartoon {VẬT} with cartoon eyes and mouth {vị trí trên bề mặt: on rice surface / on the pan surface / on the leaves / floating on the liquid surface...}, expressive anthropomorphic style.
Scene starts with {THÓI QUEN SAI mà gia chủ tưởng là đúng}.
Visual consequence: {HẬU QUẢ XẤU hiện hình — vi khuẩn/mốc/độc tố/chất thôi nhiễm hoạt hình}.
Scene corrects: {CÁCH LÀM ĐÚNG}.
{Kitchen / Home / Fridge / Kitchen sink / Kitchen table} environment.
Spoken dialogue:
“Tao là {VẬT} đây. {vặn cái-tưởng-đúng, register 'tao/mày' đường phố}. {hậu quả}. {lời khuyên sửa, giọng gần gũi}.”
No text, no subtitles, no logos, no watermark.
```

**Ví dụ VERBATIM #1 — [CƠM] (Prompt 13):**
```
A 3D animated cartoon [CƠM] with cartoon eyes and mouth on rice surface.
Scene starts with cơm được đậy kín trong nồi vì nghĩ là khỏi ruồi.
Visual consequence: hơi ẩm tích tụ, cơm thiu nhanh.
Scene corrects: xới ra cho thoáng trước khi cất.
Kitchen environment.
Spoken dialogue:
“Tao là [CƠM] đây. Kín quá tưởng tốt hả? Tao bí hơi là thiu liền đó. Xới tao ra cho thở coi.”
No text, no subtitles, no logos, no watermark.
```

**Ví dụ VERBATIM #2 — [CHẢO CHỐNG DÍNH] (Prompt 26):**
```
A 3D animated cartoon [CHẢO CHỐNG DÍNH] with cartoon eyes and mouth on the pan surface.
Scene starts with chảo được xịt nước lạnh ngay khi còn nóng.
Visual consequence: lớp chống dính bong tróc.
Scene corrects: để nguội tự nhiên rồi mới rửa.
Kitchen environment.
Spoken dialogue:
“Tao là [CHẢO] đây. Đang nóng mà tạt nước là tao tróc da đó. Để tao nguội rồi hãy rửa.”
No text, no subtitles, no logos, no watermark.
```

**Ví dụ VERBATIM #3 — [QUẠT ĐIỆN] (Prompt 71):**
```
A 3D animated cartoon [QUẠT ĐIỆN] with cartoon eyes and mouth on the fan head.
Scene starts with quạt dùng lâu ngày không lau cánh.
Visual consequence: bụi bẩn bay ngược vào không khí.
Scene corrects: lau cánh quạt định kỳ.
Home environment.
Spoken dialogue:
“Tao là [QUẠT] đây. Không lau là tao thổi bụi vô mặt mày đó. Lau tao đi.”
No text, no subtitles, no logos, no watermark.
```
> Bộ placeholder hay dùng của tab (thay vào `{VẬT}`): `[THỰC PHẨM]`, `[ĐỒ UỐNG]`, `[RAU]`, `[CANH]`, `[TRÁI CÂY]`, `[SỮA]`, `[NỒI INOX]`, `[CHẢO CHỐNG DÍNH]`, `[BÌNH GIỮ NHIỆT]`, `[TỦ LẠNH]`, `[NỒI CƠM ĐIỆN]`, `[MÁY SẤY TÓC]`, `[QUẠT ĐIỆN]`, `[ĐÈN BÀN]`... — tab lặp đúng 1 schema này ~120 lần, mỗi lần 1 vật + 1 thói quen sai.
> Kỹ thuật: 1 clip chạy trọn 6 slot (không cắt 3 phân cảnh như engine fashion). LOCKED_OFF, motion Subtle→Moderate cho hiệu ứng hậu quả (vi khuẩn sinh sôi / mốc li ti) mượt, không morph.

## 5. GHÉP & XUẤT  (BƯỚC 3 — assemble/Studio/export)
- Mỗi topic thường 1 clip 8s đăng lẻ; muốn dài hơn thì nối 2-3 clip cùng chủ đề (vd trọn bộ "mẹo bếp") cắt theo beat nhạc trend vui.
- **Voice:** lồng giọng `anthropomorphic_street` ("tao/mày" tưng tửng) khớp miệng cartoon; nhạc nền vui nhẹ, không át thoại. KHÔNG burn text lên video (giữ đúng đuôi no-text).
- **Gate chất lượng** (docs/aff-engine.md §7): grade bright-clean ≤40%, grain nhẹ 3-5%, −14 LUFS; hậu quả hiện hình rõ nhưng KHÔNG kinh dị.
- **Disclosure:** chỉ cần khi có gắn link/CTA thương mại. Export 1080p 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen — verbatim tab + kế thừa §5.5):** `no text, no subtitles, no logos, no watermark` + `no extra characters, no morphing, no flickering, no distorted proportions, no scary/horror imagery, no real human face`. **LƯU Ý:** engine C giữ semi-cartoon → **KHÔNG** loại `cartoon/3D/CGI` như engine A/B.
- **DO:** đúng đủ 6 slot; mỗi clip 1 vật gắn mắt/miệng cartoon; hậu quả THẤY được; giữ NGUYÊN câu thoại "tao/mày" ngắn gọn bắt tai; mở luôn bằng `"Tao là [VẬT] đây."`.
- **DON'T:** đừng biến thành review sản phẩm/bán hàng; đừng bỏ slot Visual consequence (mất tính giáo dục); đừng đổi register "tao/mày" thành lịch sự (mất chất viral); đừng burn caption lên khung.

## 7. METADATA
- **Title** <70 ký tự: mẹo + tò mò (vd "Đậy kín nồi cơm là sai lầm 🍚", "Đừng tạt nước vào chảo đang nóng").
- **Caption + 15-25 hashtag** ngách sức khỏe/gia dụng (#meovat #suckhoe #giadung #mẹobếp #tiktoktips #{vật}).
- **CTA:** mặc định KHÔNG bán (nuôi kênh); khi cắm aff mới thêm "Link ở giỏ hàng/bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
