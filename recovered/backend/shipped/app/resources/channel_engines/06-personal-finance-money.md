---
id: personal-finance-money
name: "Tài chính cá nhân (giải thích đời thường)"
niche: "Ngân sách, tiết kiệm, đầu tư cơ bản, lãi kép, tâm lý tiền bạc — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách finance-explainer — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Tâm lý tiền bạc"
    angle_hint: "Vì sao ta tiêu sai, thói quen chi tiêu, cảm xúc và tiền — góc hành vi"
    angles:   # angle bank (Phase 3) — ideation xoay vòng các khuôn góc viral
      - "Vì sao bạn luôn hết tiền (lý do thật sự)"
      - "Sai lầm ___ đang khiến bạn nghèo đi"
      - "Sự thật về ___ mà không ai nói cho bạn"
      - "[N] quy tắc tiền bạc trường học không dạy"
      - "Não bộ đánh lừa bạn tiêu tiền như thế nào"
  - label: "Đầu tư cơ bản cho người mới"
    angle_hint: "Lãi kép, quỹ chỉ số, rủi ro/lợi nhuận — giáo dục, không khuyến nghị cá nhân"
  - label: "Thoát nợ & quản lý chi tiêu"
    angle_hint: "Ngân sách, trả nợ, quỹ khẩn cấp, kiểm soát dòng tiền hằng tháng"
  - label: "Tự do tài chính & nghỉ hưu sớm"
    angle_hint: "Tỷ lệ tiết kiệm, thu nhập thụ động, tư duy FIRE cho người Việt"
  - label: "Bẫy tài chính & lừa đảo thường gặp"
    angle_hint: "Đa cấp, vay nặng lãi, FOMO đầu tư — nhận diện và phòng tránh"
# Kênh TRI THỨC → bật step `research` (tra cứu dữ kiện thật trước khi viết, chống bịa).
factual: true
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "6-12 min"
narration_pov: "2nd person (you / your money / your future)"
narration_tone: "clear, friendly, confident, brisk, practical"
visual_style: "high-quality 2D digital comic book and webtoon cartoon illustration with dynamic financial storytelling"
style_anchor: "Premium 2D editorial digital comic book and webtoon art illustration frame, appealing expressive characters with thick clean black outlines, clear vibrant cel-shaded color block fills, detailed character design with expressive large eyes and detailed hair, dynamic natural poses, cinematic composition, lively emotional visual storytelling,"
style_lock: "polished modern manhwa vector style, crisp hard-edge shadows, detailed realistic environments and props, rich vivid color palette with bright contrasts, clear focus on characters and their facial expressions, no generic infographic template, no simple line art, no thin minimalistic stick figures, no sketchy drawings, no faceless shapes, no corporate clip-art or simple infographic icons, no photorealism, no 3d render, no watermark, 16:9 widescreen."
style_anchor_vi: "Khung hình minh họa truyện tranh digital 2D cao cấp, nhân vật đẹp mắt biểu cảm với nét viền đen sạch sẽ sắc nét, mảng màu tô phẳng cel-shaded tươi sáng, thiết kế nhân vật chi tiết với đôi mắt to biểu cảm,"
style_lock_vi: "phong cách truyện tranh webtoon manhwa hiện đại trau chuốt, đổ bóng nét viền cứng cáp sắc sảo, bối cảnh và đạo cụ chi tiết sinh động, bảng màu phong phú rực rỡ tương phản sáng rõ, tập trung vào nhân vật và biểu cảm nét mặt, không mẫu đồ họa infographic chung chung, không nét vẽ hình que tối giản, không ảnh chụp tả thực, không dựng hình 3D, khung hình rộng 16:9."
# Existing proposed ideas can still carry the former cheap infographic contract. Runtime removes/migrates
# these literal fragments before applying the current anchor+lock, so "Tạo lại" improves old ideas too.
legacy_style_fragments:
  - "Flat vector infographic illustration, minimalist design, clean bold lines, limited 3-4 color palette, simple geometric shapes and icons,"
  - "flat solid colors, crisp edges, generous negative space, clear data-viz icon style, no photo, no 3d render, no gradient mesh, no realistic faces, no heavy drop shadows, 16:9 widescreen."
  - "Flat 2D vector cartoon illustration, bold clean black outlines, saturated flat cel-fill colors, simple rounded shapes, expressive caricature faces, clean uncluttered composition on a light background,"
  - "crisp vector explainer art, flat colors only, no gradients, no gradient mesh, no drop shadows, no photorealism, no photographic texture, no 3d render, no realistic faces, no anime, no gritty texture, no watermark, 16:9 widescreen."
legacy_prompt_replacements:
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
  "flat solid colors": "layered cel colors with subtle shading"
  "clear data-viz icon style": "integrated financial details that support the story"
  "flat 2D vector cartoon illustration": "premium editorial 2D character illustration"
  "simple rounded shapes": "appealing natural stylized anatomy"
  "clean uncluttered composition on a light background": "cinematic character-led composition in a believable everyday environment"
  "no gradients": "restrained value transitions"
  "no drop shadows": "soft contact shadows"
  "no realistic faces": "expressive appealing stylized faces"
recurring_character: "a consistent relatable protagonist designed in a clean modern 2D webtoon comic art style, with a highly expressive face, detailed hair and clothing, clear black linework, vibrant cel-shaded details, natural expressive eyes, and dynamic physical gestures; they actively interact with their environment and story props"
cast_policy:
  required: true
  min: 1
  recommended_max: 3
  hard_max: 4
  allow_crowd_without_reference: true
  portrait: {crop: "waist-up", background: "warm neutral editorial background", lighting: "soft directional cel lighting with subtle rim light"}
  shot_rotation: [cinematic wide story scene, expressive medium character shot, emotional face close-up, over-the-shoulder financial decision, tactile object detail, environmental comparison]
palette:
  money_green: "#2EA56A"
  deep_green: "#1B7A4B"
  navy: "#1F2A44"
  navy_soft: "#33415C"
  white: "#FFFFFF"
  off_white: "#F4F6F8"
  warning_orange: "#F2772E"
  warning_red: "#E0463B"
  cool_gray: "#9AA5B1"
  light_mint: "#CBE9D8"
tts_mood: "clear, upbeat-practical narrator"
music_mood: "light corporate / lofi, motivating but unobtrusive"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [finance, personal-finance, money, budgeting, saving, investing, compound-interest, debt, financial-literacy, infographic, motion-graphic, explainer]
marketing:
  version: 1
  audience: "Người đi làm muốn kiểm soát chi tiêu, nợ và kiến thức đầu tư cơ bản"
  objectives: [education, engagement, save, follow]
  formats: [checklist, explainer, calculator_card, carousel]
  pillars: [{id: money_basics, weight: 35, content_class: both, buyer_stage: awareness, formats: [explainer, carousel]}, {id: spending_behavior, weight: 30, content_class: shareable, buyer_stage: awareness, formats: [checklist, discussion]}, {id: debt_and_safety, weight: 20, content_class: searchable, buyer_stage: implementation, formats: [checklist, calculator_card]}, {id: investing_literacy, weight: 15, content_class: searchable, buyer_stage: awareness, formats: [explainer, carousel]}]
  hook_bank: {types: [contrarian, value, curiosity], examples: ["Một thói quen nhỏ đang âm thầm làm bạn thiếu tiền.", "Trước khi đầu tư, hãy kiểm tra con số này."]}
  cta: [save, comment, follow]
  avoid: [individual_financial_advice, guaranteed_returns, urgency_to_invest]
  evidence: {mode: required, allowed_claims: [general_financial_education], prohibited_claims: [personal_recommendation, fabricated_returns]}
  quality: {min_caption_chars: 180, max_promotional_share: 10}
---

<!-- body do control plane cấp theo entitlement (A5) -->
