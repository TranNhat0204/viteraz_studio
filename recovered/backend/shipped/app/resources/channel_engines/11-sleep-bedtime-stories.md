---
id: sleep-bedtime-stories
name: "Truyện ngủ ngon (thư giãn, êm dịu)"
niche: "Truyện kể ru ngủ, thư giãn có dẫn dắt, hành trình êm dịu — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Truyện kể ngủ ngon"
    angle_hint: "Câu chuyện êm dịu, nhịp chậm đưa vào giấc ngủ"
  - label: "Hành trình thư giãn có dẫn dắt"
    angle_hint: "Tưởng tượng dẫn dắt, thả lỏng cơ thể"
  - label: "Âm thanh & khung cảnh êm dịu"
    angle_hint: "Mưa rơi, rừng đêm, biển cả ru ngủ"
  - label: "Thiền & hít thở trước ngủ"
    angle_hint: "Buông bỏ căng thẳng, an dịu tâm trí"
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "20-60+ min"
narration_pov: "2nd person, soft warm guide (you drift / imagine you / let yourself)"
narration_tone: "very slow, soft, soothing, low, reassuring, monotonously gentle"
visual_style: "soft dreamy watercolor, low-contrast, pastel"
style_anchor: "Soft dreamy watercolor illustration, gentle pastel washes, blurred cozy edges, delicate paper texture, serene low-contrast light,"
style_lock: "calm muted palette, soft diffused glow, tranquil storybook serenity, slow gentle imagery, no harsh lines, no high contrast, no photo, no 3d render, no neon, no scary elements, 16:9 widescreen."
style_anchor_vi: "Minh họa màu nước mộng mơ êm dịu, mảng màu pastel dịu nhẹ, đường nét mờ ấm áp, chất liệu giấy tinh tế, ánh sáng tương phản thấp thanh bình,"
style_lock_vi: "bảng màu dịu nhẹ bình yên, ánh sáng khuếch tán mềm mại, vẻ thanh tĩnh như trang sách truyện ru ngủ, không nét vẽ sắc nhọn, không độ tương phản cao, không ảnh chụp, không dựng hình 3D, không màu dạ quang neon, khung hình rộng 16:9."
recurring_visuals: "moonlit meadows, soft rain on cabin windows, drifting clouds, warm cozy cabins, still lakes, lantern-lit paths; slow barely-moving scenes; uniformly soft pastel palette"
cast_policy:
  required: false
  min: 0
  recommended_max: 2
  hard_max: 4
  allow_crowd_without_reference: true
  portrait: {crop: "waist-up", background: "plain soft pastel wash", lighting: "gentle diffused moonlight"}
  shot_rotation: [wide tranquil landscape, medium traveler, soft profile close-up, cozy object detail, over-the-shoulder, sky insert]
palette:
  muted_lavender: "#C7BEDC"
  soft_blue: "#A9C4DC"
  warm_cream: "#F3ECDD"
  dusty_rose: "#D8B7B5"
  pale_gold_moonlight: "#E8DBA6"
  misty_grey_blue: "#B7C2C9"
  soft_sage: "#BFCBB6"
  deep_dusk_blue: "#6E7C9B"
tts_mood: "very slow, soft, soothing, low; long pauses; gentle near-whisper, never bright"
music_mood: "ambient pad, soft rain, gentle low drones; no beats, no swells, no melody peaks"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video, very gentle drift"
tags: [sleep, sleep story, bedtime story, relaxation, guided meditation, calm, insomnia, rain sounds, asmr, deep sleep, soothing]
marketing:
  version: 1
  audience: "Người trưởng thành muốn thư giãn, ngủ ngon và có ritual buổi tối"
  objectives: [community, engagement, follow]
  formats: [evening_prompt, calm_story, ritual_card, ambient_reel]
  pillars: [{id: bedtime_ritual, weight: 40, content_class: shareable, buyer_stage: implementation, formats: [ritual_card, evening_prompt]}, {id: calming_story, weight: 35, content_class: shareable, buyer_stage: community, formats: [calm_story, ambient_reel]}, {id: mindful_pause, weight: 25, content_class: both, buyer_stage: awareness, formats: [evening_prompt, ritual_card]}]
  hook_bank: {types: [story, value, curiosity], examples: ["Tối nay, hãy cho mình 30 giây để chậm lại.", "Một câu chuyện nhỏ trước khi bạn ngủ."]}
  cta: [save, comment, follow]
  avoid: [sleep_cure_claims, urgency, fear_based_copy]
  evidence: {mode: optional, allowed_claims: [gentle_wellness_education], prohibited_claims: [medical_treatment_claims]}
  quality: {min_caption_chars: 90, max_promotional_share: 5}
---

<!-- body do control plane cấp theo entitlement (A5) -->
