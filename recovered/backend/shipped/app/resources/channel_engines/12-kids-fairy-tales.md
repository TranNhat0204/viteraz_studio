---
id: kids-fairy-tales
name: "Truyện thiếu nhi / Cổ tích (hoạt hình)"
niche: "Cổ tích, ngụ ngôn loài vật, truyện đạo đức nhẹ nhàng cho bé — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Cổ tích kinh điển kể lại"
    angle_hint: "Truyện cổ quen thuộc, lời kể nhẹ nhàng"
  - label: "Truyện ngụ ngôn loài vật"
    angle_hint: "Bài học đạo đức qua con vật"
  - label: "Truyện mới về lòng tốt"
    angle_hint: "Câu chuyện gốc dạy điều hay lẽ phải"
  - label: "Phiêu lưu kỳ diệu cho bé"
    angle_hint: "Thế giới thần tiên, an toàn và ấm áp"
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "5-12 min"
narration_pov: "3rd person storyteller (Once upon a time… / our little friend…)"
narration_tone: "warm, friendly, animated, gentle storyteller"
visual_style: "whimsical children's storybook illustration (soft watercolor & gouache)"
style_anchor: "Whimsical children's storybook illustration, soft watercolor and gouache, rounded friendly shapes, warm cozy lighting,"
style_lock: "bright cheerful pastel palette, gentle daylight, hand-painted picture-book look, big expressive friendly characters, no photo, no realistic faces, no dark or scary elements, no gritty texture, 16:9 widescreen."
style_anchor_vi: "Minh họa sách tranh truyện thiếu nhi kỳ diệu, màu nước mỏng nhẹ và màu bột gouache, đường nét tròn trịa thân thiện, ánh sáng ấm áp áp áp,"
style_lock_vi: "bảng màu pastel tươi vui rực rỡ, ánh sáng ban ngày dịu dàng, vẻ đẹp sách tranh vẽ tay, nhân vật to biểu cảm thân thiện, không ảnh chụp, không khuôn mặt tả thực, không yếu tố u uất đáng sợ, khung hình rộng 16:9."
recurring_character: "designs are LOCKED per story — each character's species, exact colors, clothing, and proportions are fixed in the first prompt and restated verbatim in every later prompt; recurring cozy storybook world (sunny meadow, round little cottage, friendly forest, soft blue sky)"
cast_policy:
  required: true
  min: 1
  recommended_max: 5
  hard_max: 7
  allow_crowd_without_reference: true
  portrait: {crop: "full-body", background: "plain warm storybook cream background", lighting: "soft cheerful daylight"}
  shot_rotation: [wide storybook scene, medium group, close-up expression, magical object detail, over-the-shoulder, playful action]
palette:
  warm_pastel_cream: "#FBF3E3"
  sky_blue: "#A7D4F0"
  meadow_green: "#A8D78A"
  sunny_yellow: "#FCE38A"
  soft_pink: "#F7C5C5"
  gentle_lavender: "#D9C7F0"
  peach: "#FBD3A8"
  cocoa_brown: "#B98B68"
  leaf_green: "#7FB069"
  warm_white: "#FFFDF7"
tts_mood: "warm, animated, gentle storyteller"
music_mood: "playful gentle storybook music"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [kids, children, fairy-tales, bedtime, moral-stories, fables, storybook, animated, made-for-kids, family-friendly]
marketing:
  version: 1
  audience: "Phụ huynh tìm nội dung kể chuyện an toàn, tích cực cho trẻ"
  objectives: [education, community, follow]
  formats: [parent_carousel, story_card, activity_prompt, kids_reel]
  pillars: [{id: gentle_moral_story, weight: 45, content_class: shareable, buyer_stage: community, formats: [story_card, kids_reel]}, {id: parent_activity, weight: 30, content_class: both, buyer_stage: implementation, formats: [parent_carousel, activity_prompt]}, {id: character_kindness, weight: 25, content_class: shareable, buyer_stage: awareness, formats: [story_card, parent_carousel]}]
  hook_bank: {types: [story, value, curiosity], examples: ["Một câu chuyện nhỏ để cả nhà cùng kể tối nay.", "Bé sẽ học được điều gì từ bạn thỏ này?"]}
  cta: [save, share, follow]
  avoid: [child_data_collection, fear_or_shame, direct_purchase_pressure_to_children, unsafe_behavior]
  evidence: {mode: optional, allowed_claims: [parent_facing_educational_copy], prohibited_claims: [developmental_guarantees]}
  quality: {min_caption_chars: 100, max_promotional_share: 0}
---

<!-- body do control plane cấp theo entitlement (A5) -->
