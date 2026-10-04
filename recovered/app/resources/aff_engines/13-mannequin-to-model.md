---
id: mannequin-to-model
name: "MANOCANH — Ma-nơ-canh → Người mẫu / Orbit 360 sản phẩm"
archetype: B
video_type: "product-focus / mannequin-orbit"
niche_default: "Thời trang nam — áo/quần trên ma-nơ-canh, camera xoay 360 khoe chi tiết"
niches:
  - label: "Thời trang nam"
    fits: "áo sơ mi, áo khoác, quần tây, set đồ trưng trên ma-nơ-canh"
  - label: "Thời trang nữ"
    fits: "đầm, áo, set nữ trên ma-nơ-canh (đổi tông ma-nơ-canh)"
  - label: "Phụ kiện đi kèm outfit"
    fits: "đồng hồ, vòng cổ, thắt lưng — bắt cận khi orbit"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"
final_length: "15-30s"
persona_scope: none
faceless: true
design_lock: true
recurring_character: ""
scene_structure: "1 clip liền: camera orbit 360 độ chậm quanh ma-nơ-canh + dolly-in zoom từ xa lại gần khoe chất liệu. 6-10s. Sản phẩm là chủ thể duy nhất — không lộ mặt người."
camera_sequence: [DRONE_ORBIT, DOLLY_IN, ORBIT_360]
motion_presets: [mannequin_orbit]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm macro, medium-format-style film grain, natural color, professional product catalog photo,"
image_style_lock: "shallow depth of field, fabric weave tack-sharp, soft diffused boutique light, no visible face, vertical 9:16."
golden_rules: ["giữ NGUYÊN 100% thiết kế/hoạ tiết/màu sản phẩm (design-lock)", "giữ drape/nếp vải đổ tự nhiên như ảnh tham chiếu", "giữ ánh sáng & góc quay nhất quán khi ma-nơ-canh→người", "shallow DoF tập trung vào kết cấu vải dệt"]
lighting_default: "soft diffused boutique/store light, gentle wraparound falloff, subtle rim for garment separation"
color_look: "clean-airy warm grade (accurate whites, natural fabric color, low contrast)"
lut_intensity: 45
lens_default: "85mm macro look, shallow depth of field (f/1.8), background softly blurred"
camera_angle_default: "low-angle medium shot hất lên ngang cổ, ma-nơ-canh xoay 3/4"
background_default: "không gian cửa hàng / boutique mờ, seamless neutral, bokeh nền"
skin_realism: "natural fabric texture with visible weave and stitching, realistic drape and folds, no plastic sheen"
negative_constant: "warping product, morphing pattern, color shift, deformed garment, distorted logo, melting fabric, extra sleeves, flickering, wobble, motion blur smear, plastic sheen, watermark, text overlay, extra people, visible face"
motion_strength: "subtle"
reference_workflow: "ảnh sản phẩm/flatlay tham chiếu → keyframe ma-nơ-canh 9:16 2K (mask-and-place giữ facial-free design) → Veo Ingredients/Kling Elements (product ref) → 1 clip orbit+zoom (§10.10)"
post_chain: "upscale 4K → interp 30fps → LUT clean-warm ≤45% → grain 6-10% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, orbit_speed, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients=product) / Kling 2.5-2.6 Cinematic (roll 360 + zoom) — image-to-video"
tts_mood: "không thoại — nhạc nền thời trang/product"
music_mood: "nhạc trend TikTok, beat rõ để cắt vào nhịp zoom"
tags: [manocanh, mannequin, product-focus, orbit-360, thoi-trang-nam, design-lock, faceless, tiktok-shop, affiliate, review-do]
---

# AFF Engine — MANOCANH · Ma-nơ-canh → Người mẫu / Orbit 360 sản phẩm

> **Kiểu:** B (product-focused, faceless + design-lock) · **Dùng khi:** chỉ có ảnh sản phẩm/flatlay và muốn khoe outfit "trên form" mà không cần diễn viên. Chuyển ảnh sản phẩm trên ma-nơ-canh (hoặc trải phẳng) thành một **shot điện ảnh xoay 360 + zoom** khoe chất liệu, giữ NGUYÊN thiết kế — cảm giác "cửa hàng thật, hàng thật".
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl). **Không có `{PERSONA}`** — sản phẩm là chủ thể duy nhất.

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc (verbatim từ tab):** **1 video kết hợp cả 2 chuyển động** — camera **quay 360 độ** chậm rãi quanh sản phẩm (giống drone vòng quanh ma-nơ-canh) **kết hợp zoom từ xa lại gần từ từ** khoe kết cấu vải. Yêu cầu cứng: *"không rung không lắc không méo không biến dạng, giữ nguyên 100% chi tiết, hoạ tiết, màu sắc"*. **6-10 giây.**
- **Sản phẩm hợp:** đồ trưng được trên ma-nơ-canh (áo/quần/set nam-nữ, phụ kiện đi kèm). **Faceless:** ma-nơ-canh không đầu → không cần persona/diễn viên.
- **Kỹ thuật swap ma-nơ-canh → người (mask-and-place, giữ fabric drape):** đây là biến thể "trên form" của workflow §10.10 — upload ảnh **base (ma-nơ-canh/người mẫu không mặt)** + **object (ảnh {SẢN_PHẨM})** → lệnh "combine/mặc lên form", **giữ nguyên facial-free + mọi token thiết kế** (đường may, hoạ tiết, màu, đồng hồ/vòng cổ). Vì không có khuôn mặt để morph và chỉ 1 chuyển động camera liên tục, AI làm **rất mượt, ít lỗi** — miễn khóa chặt design + để motion **Subtle**.
- **Vì sao mượt:** không mặt người → hết drift danh tính; chủ thể đứng yên, chỉ camera chuyển động → vải chỉ đổ nhẹ theo trọng lực; design-lock + orbit chậm giữ hoạ tiết không warp.

## 2. KỊCH BẢN & LỜI
> Kiểu này **không thoại** — chỉ nhạc nền + text overlay. (Nếu kênh muốn voiceover review chất liệu, bật `dialogue_mode: vi_voiceover` và dùng khung Hook→điểm nhấn→CTA ở docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng khoe form/chất — ví dụ "Áo này lên form là hết nước chấm 🔥", "Chất vải này mà giá này?", "Zoom vào coi đường may nè". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** điểm nhấn {SẢN_PHẨM} ngắn (chất liệu, form dáng, phối đồ).
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền 11 trường theo `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`. **DESIGN-LOCK (archetype B):** ảnh tham chiếu là "chân lý" — bắt AI mặc ĐÚNG chi tiết áo (đường may, hoạ tiết, màu), không tự chế.
- **Golden rules (verbatim ý tab):** giữ đúng chi tiết áo của ảnh tham chiếu · shallow DoF tập trung kết cấu vải · ma-nơ-canh **không đầu**, góc thấp hất lên ngang cổ.
- **Ví dụ VERBATIM (từ tab, thay chỗ động bằng {SẢN_PHẨM}):**
  ```
  shot on 85mm macro, medium-format-style film grain, natural color, professional product catalog photo,
  Bức ảnh chụp chi tiết chuyên nghiệp của một ma-nơ-canh nam màu đen mờ, không đầu, góc quay thấp (low-angle),
  trung cảnh (medium shot), chụp hất lên ngang tầm cổ. Ma-nơ-canh được đặt theo góc nhìn 3/4 xoay sang bên phải.
  Ma-nơ-canh đang mặc {SẢN_PHẨM: một chiếc áo của ảnh tham chiếu — yêu cầu ĐÚNG chi tiết, đường may, hoạ tiết, màu}.
  Đi kèm là một chiếc quần tây xếp ly (pleated trousers) màu be nhạt (tan) dệt thô. Có một chiếc đồng hồ đeo tay
  kim loại màu bạc mặt vuông trên cổ tay trái, được đút vào túi quần tây màu be. Một vòng cổ bạc mảnh với mặt dây
  chuyền tròn nằm ngay dưới cổ trụ của áo. Khung hình bao gồm phần thân và vùng đùi trên. Chiều sâu trường ảnh nông,
  tập trung vào kết cấu vải dệt của cả áo và quần, ánh sáng cửa hàng mềm mại và khuếch tán. Hậu cảnh là một không
  gian cửa hàng mờ.
  shallow depth of field, fabric weave tack-sharp, soft diffused boutique light, no visible face, vertical 9:16.
  ```
- **Nhân bản (giữ design-lock):** giữ NGUYÊN {SẢN_PHẨM} + phối đồ, chỉ đổi góc xoay ma-nơ-canh (3/4 phải → chính diện → 3/4 trái) hoặc bối cảnh cửa hàng để ra thêm keyframe làm start/end frame cho clip orbit.

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, 1 clip kết hợp)
Schema mỗi clip: **Bối cảnh — Sản phẩm — Hành động — Lời thoại — Giọng**. Luật: giữ "sản phẩm như ảnh gốc" (reference-chaining), motion **Subtle** để vải không morph. Bake `negative_constant` cuối mỗi prompt. Đây là **PHẦN LÕI** — chép NGUYÊN VĂN prompt video của tab (orbit 360 + zoom gộp 1 clip).

**Phân cảnh LÕI — MANNEQUIN_ORBIT_ZOOM (`ORBIT_360` + `DOLLY_IN`):**
```
Bối cảnh: không gian cửa hàng / boutique mờ, ánh sáng studio mềm mại khuếch tán, chiều sâu rõ ràng.
Sản phẩm: {SẢN_PHẨM} trên ma-nơ-canh như ảnh gốc, giữ nguyên 100% form dáng, hoạ tiết, màu sắc, chất liệu.
Hành động (VERBATIM tab): Tạo video camera quay xung quanh sản phẩm, camera quay tốc độ từ từ quay 360 độ,
chuyên nghiệp. Không rung không lắc không méo không biến dạng, giữ nguyên 100% chi tiết, hoạ tiết, màu sắc
không biến đổi. Góc quay zoom từ xa lại gần từ từ. Giữ nguyên 100% form dáng, màu sắc, chất liệu và mọi chi
tiết của áo, chuyển động mượt, không méo sản phẩm, không lỗi form. Tỷ lệ 9:16, chất lượng 4K Ultra HD, hình
ảnh sắc nét, ánh sáng studio mềm mại, chiều sâu rõ ràng.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền thời trang.
[negative_constant]
```
> **Tách 2 beat (tùy chọn, nếu muốn 2 clip ghép thay vì 1):** ① `ORBIT_360` — orbit chậm 1 vòng khoe toàn thân outfit; ② `DOLLY_IN` — push-in macro vào đường may/hoạ tiết/đồng hồ khoe chất liệu. Ghép ① → ② theo nhịp nhạc.
> **Kỹ thuật giữ sản phẩm:** Veo **Ingredients = ảnh {SẢN_PHẨM}** (+ keyframe ma-nơ-canh) HOẶC Kling **Elements** (2-4 ref) với `roll 360` + `maintains exact appearance throughout`. Motion strength **Subtle** (§10.11) để hoạ tiết/vải không warp. Start↔End frame phải **cùng tông sáng/màu** (không Kling sẽ morph).

## 5. GHÉP & XUẤT  (BƯỚC 3 — CapCut/Studio/export)
- 1 clip orbit+zoom là đủ; nếu tách 2 beat → cắt vào **nhịp nhạc trend** ngay lúc zoom chạm chất liệu.
- Text nhẹ trong safe-zone 9:16: hook (mở), điểm nhấn {SẢN_PHẨM} (giữa), "Link ở bio" (cuối). CTA **không** để trong 20% đáy.
- Gate chất lượng (docs/aff-engine.md §7, §10.14): kiểm drape vải · hoạ tiết/logo đúng · đường may/măng-sét thẳng · không warp giữa orbit. Grade ≤45%, grain 6-10%, −14 LUFS.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p hoặc 4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `warping product, morphing pattern, color shift, deformed garment, distorted logo, melting fabric, extra sleeves, flickering, wobble, motion blur smear, plastic sheen, watermark, text overlay, extra people, visible face` + kế thừa NEGATIVE chung §10.9.
- **DO:** design-lock — giữ NGUYÊN 100% thiết kế/hoạ tiết/màu; orbit **chậm + mượt**, motion Subtle; shallow DoF vào kết cấu vải; ma-nơ-canh không đầu / faceless.
- **DON'T:** đừng để AI tự chế hoạ tiết hay đổi màu áo; đừng orbit nhanh (warp vải + méo form); đừng thêm người/mặt vào khung; đừng dùng "8K/HDR" (làm vải bóng nhựa).

## 7. METADATA
- **Title** <70 ký tự: khoe form/chất (vd "Áo này lên form xịn hơn giá 🤍").
- **Caption + 15-25 hashtag** ngách thời trang (#reviewdo #thoitrangnam #outfit #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".

> **Ghi chú enrichment:** Tab gốc rất ngắn (chỉ 1 prompt ảnh ma-nơ-canh nam + 1 prompt video orbit-360-kèm-zoom). Prompt ảnh §3 và motion LÕI §4 giữ **NGUYÊN VĂN** tab. Phần frontmatter chất lượng, ghi chú mask-and-place ma-nơ-canh→người (§10.10), tách-beat tùy chọn, kịch bản/CTA/metadata là **mở rộng hợp lý** theo Quality Playbook — không mâu thuẫn với tab.
