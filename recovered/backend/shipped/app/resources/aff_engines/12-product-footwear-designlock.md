---
id: product-footwear-designlock
name: "Dép/Giày cầm tay — Design-Lock Masterclass (faceless product review)"
archetype: B
video_type: "product-review"
niche_default: "Dép lê / dép quai chéo / giày — faceless, cầm trên tay khoe design, khóa 100% form"
niches:
  - label: "Dép lê / dép quai chéo nam"
    fits: "dép da, dép quai chéo, dép lê nam có logo/đường may nổi"
  - label: "Dép/sandal nữ"
    fits: "dép quai, sandal, dép đế cao — cầm 2 chiếc khoe cạnh bên"
  - label: "Giày sneaker/lười"
    fits: "giày đế mỏng cầm được 1 tay, khoe upper + đường may"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "6-8s"
final_length: "15-30s"
persona_scope: none
faceless: true
design_lock: true
recurring_character: ""
scene_structure: "Faceless product-in-hand: (1) tay cầm cố định khoe mặt trước (LOCKED_OFF) → (2) nhấc dép từ sàn lên → xoay ngang 360 độ khoe quai/mặt trước → đặt lại vị trí cũ (ORBIT_360, PICKUP_ROTATE_REPLACE) → (3) đưa sản phẩm tiến thẳng gần camera cho mặt trước chiếm khung, nét vào sản phẩm (DOLLY_IN + RACK_FOCUS). Camera CỐ ĐỊNH tuyệt đối. 6-8s."
camera_sequence: [LOCKED_OFF, ORBIT_360, DOLLY_IN, RACK_FOCUS_TO_PRODUCT]
motion_presets: [product_360_lock, product_hand_review]
dialogue_mode: none_music
voice: none_music
image_style_anchor: "shot on 85mm, medium-format-style film grain, natural color, high-end commercial product photography,"
image_style_lock: "product tack-sharp with only a slight foreground blur on the hands, soft bokeh background, natural human hand proportions, vertical 9:16."
golden_rules: ["Giữ nguyên chính xác đôi dép và hai bàn tay như ảnh tham chiếu, khóa chặt thiết kế sản phẩm, giữ đúng form dép, tỉ lệ hai chiếc dép, không méo, không biến dạng, không thêm bớt chi tiết, không đổi chất liệu, không đổi màu, không lỗi ngón tay", "camera cố định — không lia, không rung, không motion blur mạnh", "sản phẩm chiếm ~80% khung, bố cục đối xứng đặt chính giữa", "ưu tiên show rõ MẶT TRƯỚC của dép, luôn cân đối song song ngay ngắn"]
lighting_default: "three-point studio lighting with soft key + strip-softbox rim for separation, hoặc soft ambient luxury indoor (đèn ấm shop), không bóng gắt"
color_look: "clean-airy warm (whites chuẩn, da tay ấm tự nhiên, saturation kiềm)"
lut_intensity: 50
lens_default: "85mm / macro look, shallow depth of field, product tack-sharp, background softly blurred"
camera_angle_default: "cận cảnh trực diện từ phía trước, ngang tầm mắt (không góc từ trên xuống)"
background_default: "cửa hàng bán dép cao cấp nội thất gỗ óc chó / quán cà phê vỉa hè buổi tối / sàn gỗ xám tối giản — luôn làm mờ (bokeh) để nổi sản phẩm"
skin_realism: "natural skin texture on the hands with visible pores and fine imperfections, correct finger count and proportions"
negative_constant: "ảnh mờ, chữ sai, logo sai, chữ méo, chữ ngẫu nhiên, méo hình sản phẩm, tay thừa ngón, tay biến dạng, góc chụp nghiêng, góc chụp từ trên xuống, ánh sáng gắt, bóng đổ mạnh, màu quá rực, hậu cảnh lộn xộn, phong cách hoạt hình, phong cách 3D, chất liệu nhựa giả, ảnh tối, morphing product, đổi màu, đổi chất liệu, thêm/bớt chi tiết, motion blur mạnh, flickering, watermark"
motion_strength: "subtle_to_moderate"
reference_workflow: "1 ảnh gốc ProductSpec 9:16 (2 chiếc dép + tay cầm) → design-lock làm 'absolute lock' → Veo Ingredients (Image=product) / Kling Elements @image → clip 360-lock + dolly-in reference-chaining"
post_chain: "upscale 4K → interp 30fps → LUT clean-warm ≤50% → grain 8-10% → −14 LUFS + nhạc trend"
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, background, warmth, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients, product lock) / Kling 2.5-2.6 Cinematic (@image + Motion Brush lên tay) — image-to-video"
tts_mood: "không thoại — nhạc nền product review sang trọng"
music_mood: "nhạc trend TikTok chill/luxury, beat rõ để cắt cảnh"
tags: [dep, giay, footwear, product-review, faceless, design-lock, san-pham-cam-tay, tiktok-shop, affiliate, review-do]
---

# AFF Engine — Dép/Giày cầm tay · Design-Lock Masterclass

> **Kiểu:** B (product-in-hand, faceless — chỉ tay + sản phẩm, không lộ mặt) · **Dùng khi:** đồ vật nhỏ cầm được (dép, giày, sandal). Đây là tab **DESIGN-LOCK giàu nhất** của thư viện — mục tiêu duy nhất: giữ **100% form/màu/logo/đường may** của sản phẩm qua mọi frame, quay kiểu **review thương mại cao cấp**.
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/chất liệu đã crawl — thay vào mọi chỗ động). **Không có persona** (faceless): chỉ "hai bàn tay" là chủ thể phụ, sản phẩm là chủ thể chính tuyệt đối.

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc (verbatim tinh thần tab):** tay cầm giữ mặt trước hướng thẳng camera → **nhấc dép từ sàn lên cao về phía ống kính** → **xoay ngang 360 độ** chậm khoe mặt trước + quai → **đặt lại đúng vị trí cũ trên sàn** → **đưa sản phẩm tiến thẳng gần camera** cho mặt trước chiếm khung lớn hơn (cảm giác "review sản phẩm cao cấp"). **6-8 giây, camera cố định hoàn toàn.**
- **Sản phẩm hợp:** dép/giày/sandal nhỏ cầm được. **Không lộ mặt, không persona** — thay đổi giữa các video chỉ là `{SẢN_PHẨM}` + bối cảnh.
- **Vì sao AI làm mượt, ít lỗi:** camera đứng yên + chỉ 1 chuyển động tay/1 clip + reference image gánh 100% design → ít drift; luật vàng là **design-lock** (§3, §4), motion strength Subtle→Moderate để da/đường may không morph.

## 2. KỊCH BẢN & LỜI (script layer)
> Kiểu này mặc định **không thoại** — chỉ nhạc nền + text overlay nhẹ. (Muốn voiceover review thì bật `dialogue_mode: vi_voiceover`, dùng khung Hook→Problem→Solution→CTA docs/aff-engine.md §3.)
- **Hook (text overlay 0-3s):** "Đôi dép này mà giá này á?" / "Da thật, đường may xịn — xem cận nè". (kho hook §3.4)
- **Text giữa:** điểm nhấn {SẢN_PHẨM} (chất liệu da, logo dập, quai chéo) — ngắn.
- **CTA (cuối):** "Link ở giỏ hàng màu vàng 🛒" / "Link ở bio nha" + disclosure "mình có nhận hoa hồng nếu mua qua link". (kho CTA §3.5)

> **⚠️ GHI CHÚ 2 BẢN PERSONA (đặc trưng riêng của tab này — pipeline cho user chọn 1 "mode"):**
> - **BẢN CHO NGƯỜI THÍCH REVIEW** — cầu kỳ, dàn cảnh: ảnh có **props kể chuyện** (đèn giấy xếp ly, chồng sách, lịch lật, biển tên shop "KHO GIÀY DÉP MK"), 3 nhịp motion đầy đủ (shake → rotate&zoom → nhấc-xoay-đặt), và có **10 biến thể bối cảnh** (macro khoe chất liệu · flat-lay bãi biển · cạnh hồ bơi · minimalism bóng đổ dài · trên tay trong nhà · thảm cỏ đọng sương · low-angle · gym/spa · splash tạt nước · kệ shop sang trọng). Chọn khi kênh muốn nội dung "có gu", ít bị nhàm.
> - **BẢN CHO NGƯỜI THÍCH ĂN XỔI** — tối giản để sản xuất nhanh hàng loạt: **1 câu lệnh video design-lock cố định**, chỉ **thay từng bối cảnh** ở đoạn "nhấc dép từ sàn lên → xoay nhẹ 1 vòng → đặt lại"; ảnh dùng 1 prompt lifestyle cao cấp cầm-tay, đổi mỗi {SẢN_PHẨM} + nền. Chọn khi cần đăng 15-20 video/ngày.
> → Cả 2 bản DÙNG CHUNG design-lock clause §3 và motion lõi §4; khác nhau ở độ cầu kỳ dàn cảnh, không khác kỹ thuật khóa form.

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Khung ProductSpec (docs/aff-engine.md §5.7 dạng product): **Chủ thể (2 chiếc {SẢN_PHẨM}) · Tay cầm (nữ da trắng móng french / nam da tự nhiên) · Bố cục (đối xứng, ~80% khung, chính giữa) · Góc máy (cận trực diện ngang tầm mắt, KHÔNG top-down) · Ánh sáng (studio mềm / ambient luxury) · Nền (mờ bokeh) · Color grade (clean-warm) · Ống kính (85mm/macro shallow DoF)**. Mở đầu `image_style_anchor`, kết `image_style_lock`.

- **Golden rule = DESIGN-LOCK (verbatim từ tab):** giữ nguyên chính xác đôi dép và hai bàn tay như ảnh tham chiếu, khóa chặt thiết kế sản phẩm; sản phẩm là **chủ thể chính tuyệt đối chiếm gần hết trung tâm**; chỉ thấy **một phần vừa đủ hai bàn tay** và nền phía sau; **không chụp bán thân, không lấy rộng bối cảnh**.

- **Ví dụ ẢNH VERBATIM (tab — thay chỗ động bằng {SẢN_PHẨM}):**
  ```
  Ảnh dọc tỉ lệ 9:16, chất lượng 4K, hai bàn tay nữ da trắng nõn nà, thon dài, móng tay dài sơn gel đính đá kiểu french tip thanh lịch đang cầm hai chiếc {SẢN_PHẨM: dép} giống hệt ảnh tham chiếu, đôi {SẢN_PHẨM: dép} đặt chính giữa khung hình chiếm khoảng 80% diện tích ảnh, bố cục đối xứng tuyệt đối, góc máy cận cảnh trực diện ngang tầm mắt, dép nghiêng rất nhẹ về phía trước để thấy rõ mặt trước và cạnh bên, background là cửa hàng bán dép cao cấp với nội thất gỗ óc chó, kệ trưng bày ánh vàng ấm, ánh sáng ambient luxury, hậu cảnh làm mờ nhẹ (bokeh mềm) để nổi bật sản phẩm, ánh sáng studio mềm mại làm nổi bật chất liệu dép, ảnh siêu chân thực phong cách lifestyle cao cấp, chỉ thấy một phần vừa đủ hai bàn tay và nền phía sau, không lấy rộng không gian, không chụp bán thân, không để sản phẩm nhỏ hoặc xa, không cho phép ảnh mờ, chữ sai, logo sai, chữ méo, chữ ngẫu nhiên, méo hình sản phẩm, tay thừa ngón, tay biến dạng, góc chụp nghiêng, góc chụp từ trên xuống, ánh sáng gắt, bóng đổ mạnh, màu quá rực, hậu cảnh lộn xộn, phong cách hoạt hình, phong cách 3D, chất liệu nhựa giả, ảnh tối.
  ```
- **Ví dụ ẢNH REVIEW-MODE VERBATIM (tab — có props kể chuyện):**
  ```
  Một bức ảnh chụp sản phẩm chân thực, chi tiết cao về một đôi {SẢN_PHẨM: dép lê nam quai chéo bằng da màu nâu sẫm}. Một bàn tay với tông da tự nhiên cầm một chiếc dép ở tiền cảnh, đặt góc để khoe rõ các đường may trang trí màu kem tương phản tinh tế, phần lót dép có vân nổi và chi tiết móc khóa kim loại nhỏ màu bạc. Chiếc dép thứ hai cùng bộ nằm trên sàn phía sau. Sàn nhà là gỗ công nghiệp màu xám vân gỗ. Phía sau bên trái, có một chiếc đèn bàn bằng giấy xếp ly đang bật sáng, chồng sách, và tiêu đề 'The Godfather'. Phía sau bên phải, có một bộ lịch lật vĩnh cửu màu đen và vàng tối giản hiển thị 'APR' và '30'. Bên dưới bộ lịch là một tấm biển màu đen với dòng chữ chính xác là: 'KHO GIÀY DÉP MK' cùng một logo nhỏ. Khung cảnh được chiếu sáng bởi ánh sáng mềm mại, ấm áp, tự nhiên và môi trường. Độ sâu trường ảnh nông, tập trung sắc nét vào bàn tay và chiếc dép ở tiền cảnh.
  ```
- **Nhân bản (tab dạy):** giữ NGUYÊN bố cục/góc/khung cảnh của ảnh tham chiếu, chỉ **thay đôi dép** ("Dựa trên bố cục, góc chụp, và khung cảnh của ảnh tham chiếu... Giữ nguyên bối cảnh sàn gỗ xám, đèn, sách, lịch... Thay đổi đôi dép thành: {SẢN_PHẨM}") — hoặc đổi bối cảnh theo **10 biến thể** ở §2 (macro/flat-lay biển/hồ bơi/minimalism/trong nhà/thảm cỏ/low-angle/gym-spa/splash/kệ shop).

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Sản phẩm — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip**. Sản phẩm = "như ảnh gốc" (reference-chaining). **Bake DESIGN-LOCK + `negative_constant` cuối mỗi prompt.** Camera CỐ ĐỊNH tuyệt đối.
> Đây là PHẦN LÕI — chép NGUYÊN VĂN bộ prompt của tab thành menu; pipeline chọn/ghép.

**Phân cảnh 1 — Lắc nhẹ trái–phải rồi tiến gần (`LOCKED_OFF` + `TILT_LR_THEN_DOLLY`) — VERBATIM tab:**
```
Giữ nguyên chính xác đôi dép và hai bàn tay như ảnh tham chiếu, khóa chặt thiết kế sản phẩm, giữ đúng form dép, tỉ lệ hai chiếc dép, không méo, không biến dạng, không thêm bớt chi tiết, không đổi chất liệu, không đổi màu, không lỗi ngón tay. Chuyển động tự nhiên, sang trọng, quay sản phẩm kiểu thương mại chuyên nghiệp. Hai bàn tay cầm đôi dép ở vị trí ổn định, bắt đầu giữ mặt trước sản phẩm hướng thẳng về camera, sau đó nghiêng nhẹ toàn bộ sản phẩm sang trái một góc nhỏ, dừng rất ngắn để thấy rõ mặt trước, rồi nghiêng nhẹ sang phải một góc nhỏ, chuyển động mềm mại, chậm, mượt, kiểm soát tốt, không rung giật. Sau khi hoàn thành động tác nghiêng trái phải, hai bàn tay từ từ đưa đôi dép tiến gần về phía camera theo đường thẳng, chậm và chắc, tạo cảm giác review sản phẩm cao cấp, giúp mặt trước dép chiếm khung hình lớn hơn. Toàn bộ chuyển động phải ưu tiên show rõ mặt trước của dép, giữ sản phẩm luôn cân đối, song song, ngay ngắn, không xoay lệch làm mất form. Camera cố định, không lia, không rung, không hiệu ứng, không motion blur mạnh, không nhòe, ánh sáng ổn định, hậu cảnh giữ mềm và mờ nhẹ, sản phẩm luôn sắc nét, chi tiết rõ ràng, chuyển động thực tế, tinh tế, chuyên nghiệp.
[negative_constant]
```

**Phân cảnh 2 — Micro-tilt "như đang thở" + dolly (`MICRO_TILT_LR` + `DOLLY_IN`) — VERBATIM tab:**
```
Giữ nguyên tuyệt đối đôi dép và hai bàn tay như ảnh tham chiếu, khóa chặt toàn bộ chi tiết sản phẩm: form dép, chất liệu da, độ nhăn bề mặt, đường may viền, logo dập, màu sắc, tỉ lệ hai chiếc dép, không méo, không biến dạng, không thêm bớt chi tiết, không lỗi ngón tay. Hai bàn tay cầm sản phẩm ổn định, luôn giữ mặt trước đôi dép hướng trực diện về camera, không để lộ mặt bên hay mặt dưới. Bắt đầu chuyển động bằng một nhịp xoay cực nhẹ và uyển chuyển sang trái theo dạng lắc cổ tay mềm (micro-tilt), biên độ rất nhỏ, đủ để ánh sáng lướt qua bề mặt da, làm nổi texture và logo nhưng vẫn giữ mặt trước là chủ đạo. Ngay sau đó, chuyển động liền mạch sang phải với cùng biên độ nhỏ hơn một chút, tạo cảm giác nhịp nhàng như đang "thở", chuyển động mượt, không giật, không dừng cứng, giống chuyển động slow luxury product showcase. Trong suốt quá trình, sản phẩm luôn giữ trục thẳng, không xoay lệch góc nhìn chính diện. Sau nhịp lắc trái phải, hai bàn tay giữ nguyên hướng mặt trước và từ từ đưa sản phẩm tiến gần camera theo đường thẳng, tốc độ chậm dần (ease-in), tạo cảm giác cao cấp. Khi tiến gần, mặt trước đôi dép chiếm dần khung hình, các chi tiết da, đường may, logo trở nên rõ nét hơn, nhưng vẫn giữ đúng hình dạng ban đầu, không biến dạng phối cảnh. Toàn bộ chuyển động phải mềm mại, liên tục, có kiểm soát, không rung giật, không thay đổi ánh sáng, không hiệu ứng, không motion blur mạnh. Camera cố định hoàn toàn, góc nhìn chính diện, nền phía sau mờ nhẹ, sản phẩm luôn là điểm nét duy nhất, sắc nét cao, chi tiết rõ ràng, phong cách quay sản phẩm cao cấp, tinh tế.
[negative_constant]
```

**Phân cảnh 3 — LÕI: Nhấc từ sàn → Xoay 360 → Đặt lại (`PICKUP_ROTATE_REPLACE` + `ORBIT_360`) — bản khóa-thiết-kế mạnh nhất, VERBATIM tab (Tiếng Việt):**
```
Quay phim sản phẩm thương mại cao cấp. Sử dụng hình ảnh tham chiếu làm tiêu chuẩn tuyệt đối cho thiết kế. Bàn tay nhấc chiếc {SẢN_PHẨM: dép} từ sàn gỗ lên cao về phía ống kính một cách dứt khoát. Xuyên suốt chuyển động, chiếc dép phải giữ nguyên chính xác hình dáng, tỉ lệ, màu sắc và chi tiết quai, không được méo mó hay biến dạng. Sau đó, bàn tay thực hiện động tác xoay ngang 360 độ chậm rãi để khoe mặt trước và quai dép, luôn giữ sản phẩm ở vị trí trung tâm và song song với ống kính. Kết thúc bằng việc đặt dép lại đúng vị trí ban đầu trên sàn. Camera cố định, không rung lắc, không nhòe chuyển động. Ánh sáng studio chuyên nghiệp, hậu cảnh mờ nhẹ (bokeh), hình ảnh sắc nét 4K.
[negative_constant]
```

**Phân cảnh 3 (English) — bản gốc tối ưu cho AI, VERBATIM tab:**
```
Commercial product cinematography. Using image_reference as an absolute lock for the product design. A hand decisively picks up the {SẢN_PHẨM: lime green flip-flop} from the wooden floor and brings it closer to the camera. The flip-flop must maintain its exact shape, scale, and proportions throughout the motion with zero distortion or morphing. The hand then performs a slow, controlled 360-degree horizontal rotation to showcase the front and straps, keeping the product perfectly centered and parallel to the lens. The motion ends by placing the flip-flop precisely back into its original position on the floor. Static camera, zero shake, zero motion blur. High-end studio lighting, soft bokeh background, 4k ultra-sharp details, professional advertising aesthetic.
```

> **Câu lệnh motion ngắn (tab — dùng khi cần biến thể nhanh, mỗi câu = 1 clip):**
> - Lắc nhẹ (`Shake`): `Bàn tay ở tiền cảnh lắc nhẹ chiếc {SẢN_PHẨM} sang hai bên, độ phân giải 4k, chất lượng cao.`
> - Review xoay & zoom (`ROTATE_WRIST` + `PUSH_IN_SLOW`): `Video phong cách review sản phẩm chuyên nghiệp. Bàn tay nhẹ nhàng xoay chiếc {SẢN_PHẨM} để khoe từ nhiều góc độ, làm nổi bật kết cấu và chi tiết. Camera thực hiện thao tác zoom chậm, mượt mà và lia nhẹ để tạo cảm giác điện ảnh.`
> - Nhấc–Xoay–Đặt (`PICKUP_ROTATE_REPLACE`): `Bàn tay nhấc chiếc {SẢN_PHẨM} từ sàn gỗ lên cao về phía ống kính, sau đó xoay nhẹ một vòng và đặt lại vị trí cũ trên sàn. Chuyển động dứt khoát và chuyên nghiệp.`
>
> Kỹ thuật giữ form: **Veo Ingredients** (Image = ảnh sản phẩm gốc làm lock) HOẶC **Kling `@image` + Motion Brush** (brush riêng lên tay để chỉ tay chuyển động, sản phẩm giữ nét). Motion strength **Subtle→Moderate** để da/đường may không morph. Đoạn `finger-glide` khoe texture: cho **ngón tay lướt nhẹ trên bề mặt da/quai** rồi mới dolly-in.

## 5. GHÉP & XUẤT  (BƯỚC 3 — assemble/Studio/export)
- Import clip AI → **cắt đúng beat** nhạc trend TikTok → thứ tự: lắc/xoay → nhấc-xoay-360 → dolly-in cận. Đổi độ dài shot 1-8s (đừng đều).
- Text nhẹ safe-zone 9:16: hook (mở), điểm nhấn {SẢN_PHẨM} (giữa), "Link ở bio" (cuối). Karaoke nếu có voiceover.
- Gate chất lượng (docs/aff-engine.md §7, §10): color grade thống nhất clean-warm ≤50%, grain 8-10%, −14 LUFS. **QA design-lock:** logo/đường may/quai đúng, tay đủ ngón, form không morph giữa cắt.
- Disclosure AI + hoa hồng cạnh CTA. Export **1080p/4K**, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `ảnh mờ, chữ sai, logo sai, chữ méo, méo hình sản phẩm, tay thừa ngón, tay biến dạng, góc chụp nghiêng, góc chụp từ trên xuống, ánh sáng gắt, bóng đổ mạnh, màu quá rực, hậu cảnh lộn xộn, phong cách hoạt hình, phong cách 3D, chất liệu nhựa giả, ảnh tối, morphing product, đổi màu/chất liệu, thêm/bớt chi tiết, motion blur mạnh, flickering, watermark` + kế thừa NEGATIVE chung docs/aff-engine.md §5.5 (mục Sản phẩm: giữ 100% hình/màu/logo/đường may).
- **DO:** giữ 100% design-lock qua mọi clip; sản phẩm ~80% khung, chính giữa, mặt trước hướng camera; **camera cố định tuyệt đối**; 1 camera-move + 1 action/clip; nhấc-xoay-360-đặt-lại giữ trục song song ống kính.
- **DON'T:** đừng để góc từ trên xuống (product cần trực diện/ngang mắt); đừng xoay lệch làm mất form; đừng tả lại chi tiết sản phẩm bằng chữ mỗi clip (để reference image gánh); đừng dùng "8K/HDR" (da nhựa) — dùng film-stock anchor; đừng để sản phẩm nhỏ/xa.

## 7. METADATA
- **Title** <70 ký tự: review-do + điểm nhấn (vd "Đôi dép da này mà giá này 🤯").
- **Caption + 15-25 hashtag** ngách footwear (#dep #giay #reviewdo #tiktokshop #{ngách}).
- **CTA:** "Link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
