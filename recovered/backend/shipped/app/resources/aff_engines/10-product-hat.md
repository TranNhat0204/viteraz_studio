---
id: product-hat
name: "MŨ — Review cầm tay faceless (design-lock, 3 bước nhân bản)"
archetype: B
video_type: "product-review"
niche_default: "Mũ/nón thời trang — cầm tay khoe chi tiết, không lộ mặt"
niches:
  - label: "Mũ thời trang"
    fits: "mũ lưỡi trai, bucket, nón bo viền, mũ len — có thêu/logo/đường may"
  - label: "Phụ kiện cầm tay nhỏ"
    fits: "ốp điện thoại, ví, phụ kiện nhỏ khoe chất liệu/logo (giữ design-lock)"
  - label: "Quà tặng / SKU thêu chữ"
    fits: "sản phẩm có chi tiết thêu/in cần cận cảnh chứng minh chất liệu"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-8s"
final_length: "15-30s"
persona_scope: none
faceless: true
design_lock: true
recurring_character: ""
scene_structure: "1 ảnh gốc / sản phẩm → nhân bản đổi bối cảnh → clip cầm tay: giữ ổn định → nghiêng 15° trái↔phải ('như đang thở') → đầu ngón lướt mặt/thêu → dolly tiến gần → xoay cổ tay khoe góc → ORBIT_360. 6-8s/clip."
camera_sequence: [LOCKED_OFF, DOLLY_IN, MICRO_TILT_LR, ORBIT_360]
motion_presets: [product_hand_review, product_360_lock]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, high-end commercial product photography, medium-format-style fine grain, natural color, premium lifestyle aesthetic,"
image_style_lock: "soft studio + warm ambient interior light, no harsh shadows, shallow depth of field, product tack-sharp, vertical 9:16."
golden_rules: ["DESIGN-LOCK: giữ 100% hình/màu/logo/đường may/chất liệu sản phẩm như ảnh gốc", "camera cận cảnh trực diện ngang tầm mắt, hơi thấp hơn tâm sản phẩm", "sản phẩm chiếm gần hết trung tâm khung, chỉ thấy một phần vừa đủ hai bàn tay", "mỗi sản phẩm chỉ cần 1 ảnh gốc rồi nhân bản"]
lighting_default: "soft studio key 45° + fill, ánh sáng ambient trung tính hơi ấm, không bóng gắt, đèn trần tạo bokeh tròn nhẹ hậu cảnh"
color_look: "clean-airy warm (whites chuẩn, da tay ấm, contrast mềm)"
lut_intensity: 50
lens_default: "85mm product look (ảnh) / 50mm mirrorless (video), shallow DoF, hậu cảnh mờ mịn"
camera_angle_default: "product 45° hero / cận cảnh trực diện ngang tầm mắt, hơi thấp hơn tâm sản phẩm"
background_default: "studio hiện đại tường bê tông xám nhạt, kính lớn khung kim loại đen, sàn đá tối giản, vài cây xanh + nội thất nghệ thuật, bokeh nền mờ"
skin_realism: "natural hand skin texture, móng thon sơn màu, bàn tay thon dài tự nhiên, đúng số ngón, không biến dạng"
negative_constant: "méo/biến dạng sản phẩm, đổi hình/màu/logo/đường may, thêm bớt chi tiết, chữ sai, chữ méo, logo sai, tay thừa ngón, tay biến dạng, góc chụp từ trên xuống, ánh sáng gắt, bóng đổ mạnh, màu quá rực, hậu cảnh lộn xộn, phong cách hoạt hình, phong cách 3D, chất liệu nhựa giả, ảnh tối, ảnh mờ, watermark, text overlay"
motion_strength: "subtle_to_moderate"
reference_workflow: "1 ảnh gốc sản phẩm (design-lock) → nhân bản đổi bối cảnh (cùng sản phẩm) → i2v cầm tay từ ảnh nhân bản (Veo Ingredients=product / Kling Elements @image + Motion Brush cho tay)"
post_chain: "upscale 4K → interp 30fps → LUT warm-clean → grain 8% → −14 LUFS + nhạc trend nhẹ"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients=sản phẩm) / Kling 2.5-2.6 Cinematic (@image + Motion Brush tay) — image-to-video"
tts_mood: "không thoại — nhạc nền sang, nhẹ (tùy chọn voiceover VN ấm)"
music_mood: "nhạc trend TikTok sang/chill, beat nhẹ để cắt cảnh"
tags: [mu, non, product-review, faceless, design-lock, cam-tay, product-in-hand, tiktok-shop, affiliate, review-san-pham]
---

# AFF Engine — MŨ · Review cầm tay faceless (design-lock)

> **Kiểu:** B (product-in-hand, không lộ mặt) · **Dùng khi:** đồ vật nhỏ cầm được cần khoe chi tiết/chất liệu/logo (mũ, ốp, ví, phụ kiện thêu). Tạo cảm giác một người đang nâng niu ngắm sản phẩm cao cấp trong tay — không cần nhân vật, AI ít lỗi vì chỉ có tay + sản phẩm.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl). **Không dùng persona/nhân vật** (faceless). Constants dùng chung ở docs/aff-engine.md.

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Quy trình 3 bước clone (verbatim từ tab):**
  - **Bước 1: Tạo ảnh 1** — *"Mỗi sản phẩm chỉ cần 1 ảnh"* (ảnh gốc cầm-tay, design-lock).
  - **Bước 2: Tạo ảnh nhân bản** — giữ nguyên sản phẩm, **đổi bối cảnh** để ra keyframe khác (trung tâm thương mại, cửa hàng đồ nam/nữ, cửa hàng… hoặc lấy gợi ý trên ChatGPT), góc cận cảnh, ngẫu nhiên khác biệt chi tiết.
  - **Bước 3: Làm video từ ảnh tạo từ bước 2** — image-to-video từ ảnh nhân bản.
- **Sản phẩm hợp:** đồ vật nhỏ cầm tay (mũ/nón, ốp, ví, phụ kiện thêu-in). **Persona:** KHÔNG — faceless, chỉ hai bàn tay + sản phẩm.
- **Độ dài:** clip 6-8s · video ghép 15-30s.
- **Vì sao AI làm mượt, ít lỗi:** khung hình chỉ có tay + sản phẩm (không mặt người để morph), camera gần như cố định + 1 chuyển động nhẹ/clip; **design-lock** khoá 100% sản phẩm nên ít drift. Điểm sống-còn là **giữ nguyên sản phẩm y hệt ảnh gốc**.

## 2. KỊCH BẢN & LỜI
> Kiểu này mặc định **không thoại** — chỉ nhạc nền sang + text overlay. (Tùy chọn: bật `dialogue_mode: vi_voiceover`, voiceover VN ấm đọc top-3 điểm nhấn theo khung Hook→Problem→Solution→CTA docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** 1 dòng tò mò/khoe — ví dụ "Chiếc mũ này mà giá này á? 🧢", "Đoán xem thứ này giá bao nhiêu?", "Chi tiết thêu này xịn thật sự". (kho hook: docs/aff-engine.md §3.4)
- **Text giữa video:** điểm nhấn {SẢN_PHẨM} ngắn gọn (chất liệu vải, đường may, chi tiết thêu) — khoe bằng cận cảnh, không đọc thông số.
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure nhẹ "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Điền 11 trường (docs/aff-engine.md §5.7) theo `{SẢN_PHẨM}`, mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`.
- **DESIGN-LOCK (archetype B — docs/aff-engine.md §5.6, verbatim):** *"Giữ nguyên 100% hình dạng, màu sắc, logo, đường may, chất liệu của sản phẩm như ảnh gốc. Không morph, không biến dạng, không thêm/bớt chi tiết, không lỗi ngón tay. Camera cố định."* → append vào MỌI prompt ảnh + video.
- **Golden rules (verbatim từ tab):** sản phẩm là chủ thể chính tuyệt đối, chiếm gần hết trung tâm ảnh · góc cận cảnh trực diện từ trước, ngang tầm mắt, hơi thấp hơn tâm sản phẩm · chỉ thấy một phần vừa đủ hai bàn tay và nền phía sau, không để sản phẩm bị nhỏ/bị xa · mỗi sản phẩm chỉ cần 1 ảnh gốc.
- **Ví dụ VERBATIM ẢNH 1 (từ tab, thay chỗ động bằng `{SẢN_PHẨM}`):**
  ```
  Ảnh chụp sản phẩm theo phong cách lifestyle cao cấp, siêu chân thực, sản phẩm ở ảnh tham chiếu
  ({SẢN_PHẨM: chiếc mũ, giữ nguyên hình/màu/logo/đường may như ảnh crawl}) được cầm bởi hai bàn tay nữ
  có da trắng nõn nà, bàn tay thon dài, móng tay dài và thon sơn màu đen sang chảnh, ống tay voan bo viền
  xoè to bồng bềnh tiểu thư màu đen cầm mũ ở phần mép dưới bên trái và bên phải của mũ.
  Góc máy chụp cận cảnh trực diện từ phía trước, ngang tầm mắt, hơi thấp hơn tâm mũ một chút, mũ chiếm phần
  lớn khung hình, bố cục đối xứng và đặt chính giữa tuyệt đối, mũ nghiêng tự nhiên rất nhẹ về phía trước để
  thấy rõ phần mặt trước và vành mũ.
  Không gian studio sáng tạo hiện đại với tường bê tông xám nhạt, kính lớn và khung kim loại đen, sàn đá tối
  giản, một vài cây xanh lớn và nội thất nghệ thuật đặt rải rác, bố cục sang trọng và hiện đại. Ánh sáng
  trong nhà mềm giống ảnh quảng cáo cao cấp, ánh sáng ambient trung tính hơi ấm, không bóng gắt. Các đèn
  trần tạo bokeh tròn nhẹ trong hậu cảnh. Độ sâu trường ảnh nông, hậu cảnh mờ mịn. Có một vệt ánh sáng prism
  cầu vồng rất nhẹ phía trên khung hình. Phong cách nhiếp ảnh thương mại cao cấp, cực kỳ chân thực với ánh
  sáng mềm studio + ambient interior, 85mm lens look, shallow depth of field, high-end editorial photography,
  premium luxury aesthetic.
  Máy ảnh đặt rất gần mũ, ảnh chụp cận gần, không chụp bán thân không gian, không lấy rộng bối cảnh. Mũ là chủ
  thể chính tuyệt đối và phải chiếm gần hết trung tâm ảnh. Chỉ thấy một phần vừa đủ của hai bàn tay và nền
  phía sau, không để sản phẩm bị nhỏ hoặc bị xa.
  Không cho phép các lỗi sau: ảnh mờ, chữ sai, logo sai, chữ méo, chữ ngẫu nhiên, méo hình sản phẩm, tay bị
  thừa ngón, tay bị biến dạng, góc chụp nghiêng, góc chụp từ trên xuống, ánh sáng gắt, bóng đổ mạnh, màu quá
  rực, hậu cảnh lộn xộn, phong cách hoạt hình, phong cách 3D, chất liệu nhựa giả, ảnh tối.
  ```
- **Nhân bản (BƯỚC 2 — verbatim từ tab):** *"Đổi bối cảnh của ảnh tham chiếu thành (ghi bối cảnh mình muốn: trung tâm thương mại, cửa hàng đồ nam, cửa hàng đồ nữ, cửa hàng… hoặc lấy gợi ý trên ChatGPT) ngẫu nhiên khác biệt chi tiết (góc cận cảnh)."* → GIỮ NGUYÊN `{SẢN_PHẨM}` + design-lock, CHỈ đổi bối cảnh để ra thêm keyframe.

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 3 — image-to-video từ ảnh nhân bản, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Sản phẩm — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip** (chống méo). Giữ "sản phẩm như ảnh gốc" (reference-chaining). Bake `negative_constant` (design-lock) cuối mỗi prompt.
> Đây là PHẦN LÕI — bộ prompt cầm-tay verbatim từ tab, gộp thành 1 clip liền hoặc tách menu theo camera-move; pipeline chọn/ghép.

**Phân cảnh chính — Cầm tay ổn định → nghiêng 15° trái↔phải → lướt ngón → dolly (`LOCKED_OFF` + `MICRO_TILT_LR` → `DOLLY_IN`), verbatim:**
```
Bối cảnh: studio/cửa hàng như ảnh nhân bản, ánh sáng mềm ambient hơi ấm, hậu cảnh mờ nhẹ.
Sản phẩm: {SẢN_PHẨM} như ảnh gốc, giữ NGUYÊN 100% hình/màu/logo/đường may/chất liệu.
Hành động: Ban đầu chiếc mũ được giữ ổn định trước camera. Sau đó camera di chuyển nhẹ và quay chậm sang bên
trái khoảng 15 độ rồi quay lại sang bên phải khoảng 15 độ, tạo cảm giác người đang quan sát sản phẩm từ nhiều
góc. Trong khi đó tay phải nhẹ nhàng lướt các đầu ngón tay trên phần mặt trước của mũ, vuốt nhẹ qua phần thêu
chữ để thể hiện chất liệu vải và chi tiết thêu. Ngón tay di chuyển chậm rãi từ trái sang phải trên bề mặt mũ.
Sau đó tay vuốt nhẹ xuống phần vành mũ. Hai tay tiếp tục giữ mũ cân đối ở trung tâm khung hình, chiếc mũ hơi
nghiêng rất nhẹ để ánh sáng phản chiếu lên bề mặt vải. Video cực kỳ chân thực như quay bằng máy ảnh mirrorless
với ống kính 50mm, độ sâu trường ảnh nông, hậu cảnh mờ nhẹ, chuyển động tay và camera tự nhiên như video
review sản phẩm cao cấp.
Lời thoại: không có.
Giọng: không có giọng, chỉ nhạc nền sang nhẹ.
[negative_constant: giữ 100% hình/màu/logo/đường may sản phẩm, không méo/biến dạng, tay đủ ngón no extra fingers]
```
> Ghi chú "như đang thở": nghiêng 15° trái↔phải là nhịp thở nhẹ của clip — giữ MICRO_TILT_LR êm, đừng lia gắt.

**Phân cảnh phụ (tùy chọn thêm cảnh) — Xoay cổ tay khoe góc + xoay 360 (`ROTATE_WRIST` → `ORBIT_360`):**
```
Bối cảnh: giống ảnh nhân bản, ánh sáng ổn định.
Sản phẩm: {SẢN_PHẨM} như ảnh gốc, design-lock 100%.
Hành động: hai tay xoay nhẹ cổ tay khoe các góc mặt trước và vành mũ, sau đó camera xoay chậm 360 độ quanh
chiếc mũ một cách mượt mà điện ảnh; ánh sáng lướt trên bề mặt vải và chi tiết thêu để thấy rõ chất liệu.
Chuyển động chậm rãi, cận cảnh, sản phẩm luôn ở trung tâm khung.
Lời thoại: không có.
Giọng: chỉ nhạc nền.
[negative_constant: giữ 100% hình/màu/logo/đường may sản phẩm, không méo/biến dạng, tay đủ ngón no extra fingers]
```
> Kỹ thuật giữ sản phẩm: **Veo Ingredients = ảnh sản phẩm** HOẶC **Kling `@image` + Motion Brush** (brush riêng cho bàn tay, khoá phần sản phẩm). Motion strength **Subtle→Moderate** để vải/thêu không warp. Preset: `product_hand_review` (cầm tay + lướt ngón) / `product_360_lock` (xoay khoe góc).

## 5. GHÉP & XUẤT  (assemble / Studio / export)
- Import clip AI → **cắt đúng beat** nhạc trend TikTok; đổi độ dài shot 1-8s (đừng đều 3-4s → lộ AI); hard-cut mặc định.
- Text nhẹ trong safe-zone 9:16 (900×1492): hook (mở) · điểm nhấn {SẢN_PHẨM} (giữa) · "Link ở bio" (cuối). Caption karaoke nếu có voiceover.
- **Gate chất lượng** (docs/aff-engine.md §7, §10): color grade thống nhất warm-clean, grain 35mm 8-12%, −14 LUFS; QA design-lock (logo/đường may/chất liệu không đổi giữa các clip).
- **Disclosure** cạnh CTA (AI-generated + hoa hồng). Export 1080p/4K 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi lần gen — design-lock):** `giữ 100% hình/màu/logo/đường may/chất liệu sản phẩm, không morph/biến dạng/thêm bớt chi tiết, chữ không sai/không méo, logo không sai, tay đủ ngón (no extra fingers), tay không biến dạng, không góc chụp từ trên xuống, không ánh sáng gắt/bóng mạnh, không màu quá rực, hậu cảnh không lộn xộn, không hoạt hình/3D, không nhựa giả, không ảnh tối/mờ, no watermark, no text overlay` + kế thừa NEGATIVE chung docs/aff-engine.md §5.5.
- **DO:** giữ NGUYÊN sản phẩm y hệt ảnh gốc qua mọi clip (design-lock); camera cận cố định, chỉ 1 chuyển động nhẹ/clip; sản phẩm chiếm trung tâm, chỉ lộ vừa đủ hai bàn tay; nghiêng 15° trái↔phải êm "như đang thở".
- **DON'T:** đừng để sản phẩm bị nhỏ/xa hoặc lấy rộng bối cảnh; đừng lia/xoay gắt (warp vải-thêu); đừng lộ mặt người; đừng dùng "8K/HDR/hyperrealistic" (da nhựa/nhựa giả); đừng góc từ trên xuống.

## 7. METADATA
- **Title** <70 ký tự: review mũ + điểm nhấn (vd "Chiếc mũ này mà giá này thì xịn thật 🧢").
- **Caption + 15-25 hashtag** ngách phụ kiện/mũ (#mu #non #reviewsanpham #tiktokshop #phukien #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
