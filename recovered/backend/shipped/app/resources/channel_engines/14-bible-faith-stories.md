---
id: bible-faith-stories
name: "Kinh Thánh & Đức tin (tĩnh nguyện)"
niche: "Chuyện Kinh Thánh kể lại, giải nghĩa, suy niệm, khích lệ đức tin — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Chuyện Kinh Thánh kể lại"
    angle_hint: "Câu chuyện Kinh Thánh sống động"
  - label: "Giải nghĩa Kinh Thánh"
    angle_hint: "Ý nghĩa câu chữ, bối cảnh, bài học"
  - label: "Suy niệm & tĩnh nguyện"
    angle_hint: "Phản tỉnh, cầu nguyện hằng ngày"
  - label: "Đức tin & khích lệ"
    angle_hint: "Hy vọng, an ủi, vượt thử thách"
# Kênh TRI THỨC → bật step `research` (tra cứu dữ kiện thật trước khi viết, chống bịa).
factual: true
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "8-18 min"
narration_pov: "warm 2nd person for devotionals (you / God sees you); 3rd person reverent for the retold story itself"
narration_tone: "warm, calm, reverent"
visual_style: "cinematic biblical oil-painting, Renaissance-inspired, divine light"
style_anchor: "Cinematic biblical oil-painting illustration, Renaissance-inspired composition, dramatic divine god-rays, warm reverent light,"
style_lock: "rich classical palette, painterly brushwork, holy volumetric glow, timeless ancient setting, no cartoon, no anime, no flat vector, no modern objects, no text artifacts, 16:9 widescreen."
style_anchor_vi: "Minh họa tranh sơn dầu Kinh Thánh điện ảnh, bố cục cảm hứng Phục Hưng, các tia sáng thần thánh kịch nghệ, ánh sáng ấm áp kính cẩn,"
style_lock_vi: "bảng màu cổ điển phong phú, nét vẽ sơn dầu painterly, hào quang thần thánh volumetric, bối cảnh cổ xưa vượt thời gian, không hoạt hình, không anime, không vector phẳng, không vật thể hiện đại, khung hình rộng 16:9."
recurring_character: "depicted figures rendered modestly and reverently — often back-lit, distant, or with faces softly lit; consistent ancient-Holy-Land wardrobe (simple woven robes, head coverings, sandals); recurring divine-light motif (god-rays from above)"
cast_policy:
  required: true
  min: 1
  recommended_max: 5
  hard_max: 7
  allow_crowd_without_reference: true
  portrait: {crop: "waist-up", background: "plain warm earth-tone painterly background", lighting: "soft reverent golden light"}
  shot_rotation: [epic establishing, medium group, reverent close-up, symbolic object, over-the-shoulder, crowd tableau]
palette:
  warm_gold: "#D4A437"
  deep_blue: "#1E3A5F"
  earthy_ochre: "#B0772E"
  marble_white: "#F2EDE0"
  radiant_light: "#FBF3D0"
  shadow_umber: "#3A2A1C"
  olive_green: "#6B6A3A"
  terracotta: "#A8553A"
  twilight_violet: "#3C3157"
  candle_amber: "#E8A33D"
tts_mood: "warm, calm, reverent"
music_mood: "soft worship strings / piano, gentle and uplifting"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [bible, faith, christian, devotional, scripture, encouragement, jesus, god, prayer, christianity]
marketing:
  version: 1
  audience: "Cộng đồng đức tin tìm sự suy ngẫm, bối cảnh Kinh Thánh và khích lệ"
  objectives: [community, education, engagement, follow]
  formats: [reflection, passage_context, prayer_prompt, story_reel]
  pillars: [{id: scripture_context, weight: 35, content_class: both, buyer_stage: awareness, formats: [passage_context, reflection]}, {id: daily_reflection, weight: 40, content_class: shareable, buyer_stage: community, formats: [reflection, prayer_prompt]}, {id: faith_story, weight: 25, content_class: shareable, buyer_stage: community, formats: [story_reel, passage_context]}]
  hook_bank: {types: [story, value, curiosity], examples: ["Đoạn này không chỉ nói về quá khứ.", "Một suy ngẫm nhỏ cho ngày hôm nay."]}
  cta: [comment, save, follow]
  avoid: [fear_or_shame_manipulation, denominational_attack, prosperity_guarantees]
  evidence: {mode: required, allowed_claims: [respectful_scripture_context], prohibited_claims: [fabricated_scripture_or_quote]}
  quality: {min_caption_chars: 140, max_promotional_share: 5}
---

<!-- body do control plane cấp theo entitlement (A5) -->
