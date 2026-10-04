---
id: doi-song-2d-vector
name: "Đời sống & Góc nhìn — hoạt hoạ 2D có người dẫn"
niche: "Chuyện đời sống, người trẻ, tiền bạc, xã hội — giải thích bằng hoạt hoạ 2D có host dẫn chuyện"
# Ngách con dùng chung phong cách 2D + host của engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Chuyện người trẻ"
    angle_hint: "Trưởng thành, áp lực, hoang mang, lựa chọn của tuổi trẻ"
    angles:
      - "Vì sao người trẻ ngày càng ___?"
      - "Sự thật về ___ mà không ai nói với bạn ở tuổi 20"
      - "Điều bạn ước mình hiểu sớm hơn về ___"
      - "___ ở tuổi trẻ: bình thường hay đáng lo?"
  - label: "Tiền bạc & tài chính cá nhân"
    angle_hint: "Tiết kiệm, nợ, đầu tư, bẫy tiêu dùng — kiểu kênh tài chính hoạt hoạ"
    angles:
      - "Họ sợ bạn ___!"
      - "Vì sao lương ___ vẫn thua lương ___?"
      - "___ loại ___ giúp bạn ___ trong khủng hoảng"
      - "Cái bẫy ___ đang lấy tiền của bạn mỗi tháng"
  - label: "Tâm lý & cảm xúc đời thường"
    angle_hint: "Sợ hãi, trì hoãn, cô đơn, động lực"
    angles:
      - "Vì sao ta sợ ___ dù biết nó vô lý?"
      - "Lý do thật khiến bạn cảm thấy ___"
      - "Vì sao chúng ta ___ những điều đã qua?"
  - label: "Gia đình & các mối quan hệ"
    angle_hint: "Cha mẹ, tình thân, tình yêu, khoảng cách thế hệ"
    angles:
      - "Vì sao cha mẹ và con cái ngày càng ___?"
      - "Điều ta hiểu ra về ___ khi đã muộn"
  - label: "Xã hội & mổ xẻ thương hiệu"
    angle_hint: "Vì sao xã hội/doanh nghiệp hành xử thế này; bài học phía sau"
    angles:
      - "Tôi mổ xẻ ___ để bạn hiểu vì sao họ ___"
      - "Vì sao cả một thế hệ đang ___?"
      - "___: cơ hội hay rủi ro?"
# Có phần phân tích THẬT (tiền bạc/thương hiệu/xã hội) → bật research chống bịa số liệu. Ngách thuần
# chiêm nghiệm có thể tắt research per-kênh (channel_profile.research_enabled=false).
factual: true
series_mode: anthology
language: vi
aspect_ratio: "16:9"
video_length: "6-11 min"
narration_pov: "2nd person (bạn) — host xưng 'tôi', gọi người xem là 'bạn'"
narration_tone: "ấm, dí dỏm, thẳng thắn, dễ hiểu; như người anh/chú từng trải giảng giải"
visual_style: "premium editorial 2D character animation with cinematic everyday storytelling"
# ── HỢP ĐỒNG PHONG CÁCH (ràng buộc runtime, ép vào MỌI ảnh: cảnh + thumbnail + chân dung nhân vật).
style_anchor: "Premium editorial 2D animation frame, hand-crafted character art, expressive appealing caricature faces with natural anatomy and hands, varied ink line weight, sophisticated cel color and subtle texture, cinematic everyday storytelling composition,"
style_lock: "broadcast-quality polished 2D illustration, subtle cel shading and restrained paper grain, warm skin tones with deep navy jade coral and ochre accents, strong focal hierarchy, emotionally specific eyes gestures and body language, one coherent environmental metaphor, no generic infographic template, no floating icon collage, no blank geometric face, no corporate clip-art, no crude vector mascot, no oversized text covering the scene, no photorealism, no 3d render, no anime, no watermark, 16:9 widescreen."
style_anchor_vi: "Khung hình hoạt hình 2D biên tập cao cấp, nghệ thuật nhân vật vẽ tay, khuôn mặt châm biếm biểu cảm với giải phẫu và bàn tay tự nhiên, nét mực độ dày linh hoạt, màu cel tinh tế và cấu trúc nhẹ, bố cục kể chuyện đời sống điện ảnh,"
style_lock_vi: "phong cách minh họa 2D chất lượng cao trau chuốt, đổ bóng cel nhẹ nhàng, tông màu da ấm áp với các điểm nhấn san hô và ngọc bích, mắt và cử chỉ ngôn ngữ cơ thể biểu cảm, không dùng mẫu infographic chung chung, không ảnh chụp tả thực, không kỹ xảo 3D, không nét vẽ anime, khung hình rộng 16:9."
legacy_style_fragments:
  - "Flat 2D vector cartoon illustration, bold clean black outlines, saturated flat cel-fill colors, simple rounded shapes, expressive caricature faces, clean uncluttered composition on a light background,"
  - "crisp vector explainer art, flat colors only, no gradients, no gradient mesh, no drop shadows, no photorealism, no photographic texture, no 3d render, no realistic faces, no anime, no gritty texture, no watermark, 16:9 widescreen."
  - "Flat vector infographic illustration, minimalist design, clean bold lines, limited 3-4 color palette, simple geometric shapes and icons,"
  - "flat solid colors, crisp edges, generous negative space, clear data-viz icon style, no photo, no 3d render, no gradient mesh, no realistic faces, no heavy drop shadows, 16:9 widescreen."
legacy_prompt_replacements:
  "flat 2D vector cartoon illustration": "premium editorial 2D character illustration"
  "simple rounded shapes": "appealing natural stylized anatomy"
  "clean uncluttered composition on a light background": "cinematic character-led composition in a believable everyday environment"
  "flat colors only": "layered cel colors with subtle shading"
  "no gradients": "restrained value transitions"
  "no drop shadows": "soft contact shadows"
  "no realistic faces": "expressive appealing stylized faces"
  "flat vector infographic illustration": "premium editorial 2D character illustration"
  "minimalist design": "cinematic editorial visual storytelling"
  "limited 3-4 color palette": "sophisticated controlled color palette"
  "simple geometric shapes and icons": "character-led scene with integrated financial symbolism"
  "simple geometric head": "appealing stylized face with expressive eyes and eyebrows"
  "round minimal head with one dot eye and a small line expression": "appealing stylized oval face with expressive eyes, eyebrows, and a readable emotional expression"
  "round minimal head with one dot eye and a simple line expression": "appealing stylized oval face with expressive eyes, eyebrows, and a readable emotional expression"
  "no realistic facial details": "expressive stylized facial features"
  "represented by simple geometric blocks": "designed with clean appealing shapes and natural silhouette"
  "represented by simple geometric shapes": "designed with clean appealing shapes and natural silhouette"
  "clear data-viz icon style": "integrated financial details that support the story"
# Host mặc định — khối "Character DNA" viết theo THỨ TỰ TOKEN CỐ ĐỊNH (tuổi → tóc → kính → trang phục →
# dáng → nét mặt). Dán NGUYÊN VĂN vào mọi prompt có host để khoá nhận diện. User có thể đổi host riêng
# ở mục "Nhân vật đại diện kênh" (import ảnh hoặc AI tạo) — engine chỉ cấp bản mặc định.
recurring_character: "Chú Tài — middle-aged man in his late 40s, neat salt-and-pepper side-parted hair, square black glasses, navy blue suit jacket over a warm white shirt with a muted coral tie, friendly round build, appealing expressive caricature face with clearly designed eyes eyebrows nose and smile lines, natural five-finger hands, varied ink line weight and subtle cel shading; premium editorial 2D character animation, always the same face, hair, glasses, proportions and outfit in every frame"
cast_policy:
  required: true
  min: 1
  recommended_max: 3
  hard_max: 4
  allow_crowd_without_reference: true
  portrait: {crop: "waist-up", background: "warm neutral editorial background", lighting: "soft directional cel lighting with subtle rim light"}
  shot_rotation: [cinematic everyday wide, expressive host medium, emotional face-and-hands close-up, host interacting with one symbolic prop, over-the-shoulder decision, tactile object detail]
palette:
  paper_white: "#FFFFFF"
  ink_outline: "#1A1A1A"
  alert_red: "#E03131"
  money_green: "#2F9E44"
  trust_blue: "#1971C2"
  warm_skin: "#F1C27D"
  gold_accent: "#F59F00"
  soft_gray: "#DEE2E6"
tts_mood: "ấm, dí dỏm, rõ ràng, nhịp vừa"
music_mood: "nhạc nền vui nhẹ, tiết tấu đều, không lấn giọng"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [đời sống, người trẻ, tài chính cá nhân, tiền bạc, tâm lý, giải thích, hoạt hoạ 2d, vector, explainer, gen-z, vietnam]
marketing:
  version: 1
  audience: "Người trẻ Việt quan tâm đời sống, tiền bạc, tâm lý và góc nhìn xã hội"
  objectives: [engagement, save, follow, share]
  formats: [explainer, reflection, story, carousel]
  pillars:
    - {id: nguoi_tre, weight: 30, content_class: shareable, buyer_stage: awareness, formats: [reflection, story]}
    - {id: tien_bac, weight: 30, content_class: both, buyer_stage: awareness, formats: [explainer, carousel]}
    - {id: cam_xuc_tam_ly, weight: 20, content_class: shareable, buyer_stage: community, formats: [reflection]}
    - {id: xa_hoi_thuong_hieu, weight: 20, content_class: both, buyer_stage: awareness, formats: [explainer]}
  hook_bank:
    types: [curiosity, contrarian, relatable, value]
    examples: ["Họ sợ bạn có 1 tỷ.", "Lương 50 triệu vẫn thua lương 15 triệu — vì sao?"]
  cta: [save, comment, follow, share]
  avoid: [phán xét, dạy đời, hứa làm giàu nhanh, khẳng định tuyệt đối]
  evidence: {mode: required, allowed_claims: [general_education, public_business_facts], prohibited_claims: [investment_guarantee, fabricated_statistics]}
  quality: {min_caption_chars: 170, max_promotional_share: 10}
---

<!-- body do control plane cấp theo entitlement (A5) -->
