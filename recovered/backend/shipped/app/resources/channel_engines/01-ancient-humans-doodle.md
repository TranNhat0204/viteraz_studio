---
id: ancient-humans-doodle
name: "Hoạt hình Doodle vẽ tay (giải thích kiến thức)"
niche: "Người tiền sử, tiến hóa, nhân học, sinh tồn — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách doodle-explainer — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Sinh tồn thời tiền sử"
    angle_hint: "Săn bắt, giữ lửa, sống sót qua Kỷ Băng Hà, đối mặt thú dữ và đói khát"
    angles:   # angle bank (Phase 3) — ideation xoay vòng các khuôn góc viral
      - "Người tiền sử sống sót qua ___ như thế nào?"
      - "Vì sao bạn không trụ nổi 1 ngày ở ___ thời tiền sử"
      - "Thứ nguy hiểm nhất người tiền sử phải đối mặt: ___"
      - "POV: bạn là người tiền sử đang ___"
      - "Điều gì xảy ra nếu người tiền sử không biết ___?"
  - label: "Đời sống thường nhật của người cổ đại"
    angle_hint: "Ngủ nghỉ, nuôi con, vệ sinh, ăn uống, đời sống bộ lạc"
  - label: "Tiến hóa loài người"
    angle_hint: "Cơ thể, bộ não, ngôn ngữ, vì sao con người thắng các loài khác"
  - label: "Y học & vệ sinh cổ đại"
    angle_hint: "Cách người xưa chữa bệnh, sinh đẻ, giữ vệ sinh — góc trung thực, gần gũi"
  - label: "Niềm tin, nghi lễ & nghệ thuật hang động"
    angle_hint: "Tín ngưỡng, chôn cất, tranh hang, biểu tượng đầu tiên của loài người"
# Kênh TRI THỨC → bật step `research` (tra cứu dữ kiện thật trước khi viết, chống bịa).
factual: true
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "7-12 min"
narration_pov: "2nd person (you / your ancestors / your body)"
narration_tone: "calm, intelligent, curious"
visual_style: "hand-drawn 2D doodle cartoon animation"
style_anchor: "Hand-drawn 2D doodle cartoon animation, flat solid colors, bold black hand-drawn outlines, slightly wobbly imperfect marker lines,"
style_lock: "no gradients, no drop shadows, no photographic textures, no photorealism, no 3D render, no realistic faces, no anime, 16:9 widescreen, simple educational YouTube explainer doodle style."
style_anchor_vi: "Hoạt hình doodle 2D vẽ tay, mảng màu phẳng nguyên khối, nét vẽ chì đen đậm nét mộc mạc hơi nguệch ngoạc dạng bút dạ,"
style_lock_vi: "không hiệu ứng đổ bóng, không bóng mờ, không chất liệu ảnh chụp, không tả thực photorealism, không dựng hình 3D, không vẽ mặt tả thực, không nét vẽ anime, khung hình 16:9, phong cách doodle giải thích kiến thức YouTube đơn giản."
recurring_character: "round white-headed stick figure with spiky bright ORANGE hair; ancient humans = messy brown hair; neutral modern = bald white head; elder = gray hair in a bun + colored dress"
cast_policy:
  required: true
  min: 1
  recommended_max: 4
  hard_max: 6
  allow_crowd_without_reference: true
  portrait: {crop: "waist-up", background: "plain warm off-white background", lighting: "soft even illustrated lighting"}
  shot_rotation: [wide establishing, medium group, close-up reaction, object detail, over-the-shoulder, diagram]
palette:
  orange: "#F58220"
  sky_blue: "#7FB5D5"
  cave_light_blue: "#ABD3E5"
  grass_green: "#4E9A45"
  sand_tan: "#D2B488"
  dirt_brown: "#8B5A2B"
  wood_brown: "#7A4F2A"
  rock_gray: "#8A8A8A"
  night_navy: "#283A6E"
  deep_indigo: "#322B5E"
  red_text: "#E0302B"
  yellow_fire: "#F4C430"
  purple_mauve: "#8B7CB0"
  cream: "#F5F1E6"
  white: "#FFFFFF"
tts_mood: "calm, intelligent narrator"
music_mood: "subtle ambient, contemplative"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [history, prehistory, evolution, anthropology, educational, doodle, explainer]
marketing:
  version: 1
  audience: "Người tò mò về nguồn gốc loài người và lịch sử tiền sử"
  objectives: [education, engagement, follow]
  formats: [how_to, fact_card, carousel, quiz]
  pillars: [{id: human_origins, weight: 40, content_class: both, buyer_stage: awareness, formats: [how_to, carousel]}, {id: survival_and_tools, weight: 35, content_class: shareable, buyer_stage: community, formats: [fact_card, quiz]}, {id: myth_vs_evidence, weight: 25, content_class: searchable, buyer_stage: awareness, formats: [how_to, fact_card]}]
  hook_bank: {types: [curiosity, value, contrarian], examples: ["Bạn có biết tổ tiên chúng ta từng…?", "Điều nhiều người tin về người tiền sử là sai."]}
  cta: [save, comment, follow]
  avoid: [invented_archaeology, unsupported_evolution_claims]
  evidence: {mode: required, allowed_claims: [archaeological_consensus], prohibited_claims: [fabricated_sources]}
  quality: {min_caption_chars: 180, max_promotional_share: 10}
---

<!-- body do control plane cấp theo entitlement (A5) -->
