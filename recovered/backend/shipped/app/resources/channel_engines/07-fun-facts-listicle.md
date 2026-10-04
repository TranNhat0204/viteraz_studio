---
id: fun-facts-listicle
name: "Sự thật thú vị / Top-List (khơi tò mò)"
niche: "Sự thật bất ngờ, top-10 đếm ngược, trivia khoa học/lịch sử/thiên nhiên — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Sự thật gây sốc"
    angle_hint: "Điều bạn chưa từng biết, khiến phải 'wow'"
  - label: "Top 10 đếm ngược"
    angle_hint: "Bảng xếp hạng, so sánh kỳ thú"
  - label: "Khoa học kỳ lạ"
    angle_hint: "Hiện tượng khoa học khó tin"
  - label: "Lịch sử & thiên nhiên lạ lùng"
    angle_hint: "Mẩu chuyện lạ, kỳ quan tự nhiên"
  - label: "So sánh & 'điều gì xảy ra nếu'"
    angle_hint: "Đối chiếu quy mô, giả định thú vị"
# Kênh TRI THỨC → bật step `research` (tra cứu dữ kiện thật trước khi viết, chống bịa).
factual: true
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "6-12 min"
narration_pov: "2nd person + energetic narrator (you / did you know / wait until you hear)"
narration_tone: "energetic, fun, upbeat, fast, playful"
visual_style: "bright bold flat vector cartoon infographic"
style_anchor: "Bright bold flat vector cartoon illustration, clean thick outlines, vivid saturated flat colors, playful infographic energy,"
style_lock: "flat 2D, simple shapes, high readability, big bold number labels, no photo, no 3d render, no gradients, no realistic faces, no gritty texture, 16:9 widescreen."
style_anchor_vi: "Minh họa hoạt hình vector 2D nổi bật tươi sáng, nét viền dày sạch sẽ, màu sắc phẳng tươi tắn rực rỡ, năng lượng đồ họa thông tin infographic vui nhộn,"
style_lock_vi: "phong cách 2D phẳng, hình khối đơn giản, độ rõ ràng cao, không ảnh chụp, không dựng hình 3D, không mảng màu chuyển gradients, không khuôn mặt tả thực, khung hình rộng 16:9."
recurring_character: "friendly flat vector mascot avatar — round simple head, big readable eyes, small smile, simple stick/blob body; reacts to each fact (surprised wide-eyes + open mouth = 'wow', dropped jaw = shock, raised eyebrow = skeptical, thumbs up = approval). Stays the same color and shape every frame."
consistency_devices: "recurring big number badges (#10 → #1) as bold rounded squares/circles; mascot reacting beside each fact; one consistent flat icon set; white background"
cast_policy:
  required: true
  min: 1
  recommended_max: 2
  hard_max: 4
  allow_crowd_without_reference: true
  portrait: {crop: "full-body", background: "plain bright neutral background", lighting: "flat even vector lighting"}
  shot_rotation: [wide fact card, medium mascot, close-up reaction, object detail, size comparison, countdown layout]
palette:
  badge_red: "#FF4757"
  bold_blue: "#2E86DE"
  sunny_yellow: "#FFC312"
  fresh_green: "#26DE81"
  pop_orange: "#FF7F2A"
  hot_pink: "#FD79A8"
  purple_pop: "#A55EEA"
  teal: "#26C6DA"
  ink_outline: "#1B2430"
  cool_gray: "#9AA5B1"
  white: "#FFFFFF"
tts_mood: "energetic, fun"
music_mood: "upbeat playful"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [fun-facts, listicle, top-10, trivia, did-you-know, weird-science, comparison, infographic, flat-vector, curiosity, educational, entertainment]
marketing:
  version: 1
  audience: "Đại chúng thích khám phá nhanh, trivia và những điều bất ngờ"
  objectives: [engagement, education, share, follow]
  formats: [listicle, quiz, fact_card, fast_reel]
  pillars: [{id: surprising_facts, weight: 45, content_class: shareable, buyer_stage: awareness, formats: [fact_card, fast_reel]}, {id: myth_vs_fact, weight: 30, content_class: both, buyer_stage: awareness, formats: [quiz, listicle]}, {id: comparison, weight: 25, content_class: searchable, buyer_stage: awareness, formats: [listicle, fact_card]}]
  hook_bank: {types: [curiosity, value, contrarian], examples: ["Sự thật này nghe như bịa, nhưng có thật.", "Bạn đoán được đáp án không?"]}
  cta: [comment, share, follow]
  avoid: [false_trivia, misleading_clickbait]
  evidence: {mode: required, allowed_claims: [verifiable_facts], prohibited_claims: [invented_statistics]}
  quality: {min_caption_chars: 100, max_promotional_share: 5}
---

<!-- body do control plane cấp theo entitlement (A5) -->
