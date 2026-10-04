---
id: psychology-your-mind
name: "Tâm lý học & Hành vi (khám phá bản thân)"
niche: "Tâm lý con người, thiên kiến, thói quen, cảm xúc, mối quan hệ — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Thiên kiến nhận thức"
    angle_hint: "Não đánh lừa ta như thế nào"
  - label: "Thói quen & động lực"
    angle_hint: "Vì sao ta làm/không làm, cách thay đổi"
  - label: "Cảm xúc & sức khỏe tinh thần"
    angle_hint: "Lo âu, hạnh phúc, chữa lành"
  - label: "Tâm lý các mối quan hệ"
    angle_hint: "Tình yêu, gắn bó, giao tiếp"
  - label: "Hành vi xã hội"
    angle_hint: "Đám đông, thuyết phục, vì sao ta hành xử vậy"
# Kênh TRI THỨC → bật step `research` (tra cứu dữ kiện thật trước khi viết, chống bịa).
factual: true
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "7-13 min"
narration_pov: "2nd person (you / your brain / your mind)"
narration_tone: "warm, intelligent, curious, insightful"
visual_style: "clean flat 2D explainer illustration (friendly concept art)"
style_anchor: "Clean flat 2D explainer illustration, bold simple outlines, soft friendly flat colors, clear conceptual metaphors,"
style_lock: "minimalist concept-art style, flat shapes, calm readable composition, no photo, no 3d render, no gradient mesh, no realistic faces, no gritty texture, 16:9 widescreen."
style_anchor_vi: "Minh họa đồ họa 2D giải thích sạch sẽ, đường nét đơn giản đậm rõ, màu sắc phẳng dịu dàng thân thiện, ẩn dụ khái niệm rõ ràng,"
style_lock_vi: "phong cách nghệ thuật khái niệm tối giản, mảng hình phẳng, bố cục bình yên dễ đọc, không ảnh chụp, không dựng hình 3D, không mảng màu chuyển gradients, không khuôn mặt tả thực, khung hình rộng 16:9."
recurring_character: "a simple friendly flat human avatar as 'you' — rounded head, dot eyes, soft smile, simple flat clothing, no realistic facial detail; consistent look every frame"
cast_policy:
  required: true
  min: 1
  recommended_max: 3
  hard_max: 5
  allow_crowd_without_reference: true
  portrait: {crop: "full-body", background: "plain soft cream background", lighting: "flat even illustrated lighting"}
  shot_rotation: [wide concept, medium interaction, close-up emotion, symbolic object, split comparison, diagram]
palette:
  soft_teal: "#5FBDB0"
  warm_coral: "#F4856B"
  cream: "#F6EFE2"
  muted_purple: "#8C7DB5"
  bright_accent: "#FFC94D"
  ink_outline: "#2E2A39"
  calm_blue: "#7FA8D6"
  soft_gray: "#C9C5CE"
  white: "#FFFFFF"
tts_mood: "warm, curious, calm"
music_mood: "gentle thoughtful lofi"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [psychology, cognitive-bias, human-behavior, your-brain, habits, emotions, relationships, mental-models, educational, explainer, flat-illustration]
marketing:
  version: 1
  audience: "Người muốn hiểu hành vi, cảm xúc và thói quen hằng ngày"
  objectives: [education, engagement, save, follow]
  formats: [explainer, reflection, checklist, carousel]
  pillars: [{id: cognitive_bias, weight: 35, content_class: both, buyer_stage: awareness, formats: [explainer, carousel]}, {id: habit_and_behavior, weight: 35, content_class: shareable, buyer_stage: implementation, formats: [checklist, reflection]}, {id: relationships, weight: 30, content_class: shareable, buyer_stage: community, formats: [reflection, discussion]}]
  hook_bank: {types: [curiosity, contrarian, value], examples: ["Não bộ đang dùng lối tắt này mà bạn không nhận ra.", "Bạn không lười như bạn nghĩ."]}
  cta: [save, comment, follow]
  avoid: [diagnosis, therapy_claims, manipulation_tactics]
  evidence: {mode: required, allowed_claims: [general_psychology_education], prohibited_claims: [medical_diagnosis]}
  quality: {min_caption_chars: 170, max_promotional_share: 10}
---

<!-- body do control plane cấp theo entitlement (A5) -->
