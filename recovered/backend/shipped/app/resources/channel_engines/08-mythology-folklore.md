---
id: mythology-folklore
name: "Thần thoại & Truyền thuyết (sử thi)"
niche: "Thần thoại Hy Lạp/Bắc Âu/Ai Cập, huyền thoại, quái vật, anh hùng — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Thần thoại Hy Lạp"
    angle_hint: "Các vị thần, anh hùng, bi kịch Olympus"
  - label: "Thần thoại Bắc Âu"
    angle_hint: "Odin, Thor, Ragnarok, chín cõi"
  - label: "Thần thoại Ai Cập & thế giới"
    angle_hint: "Thần Ai Cập, huyền thoại các nền văn minh"
  - label: "Quái vật & sinh vật huyền thoại"
    angle_hint: "Rồng, quái thú, sinh vật dân gian"
  - label: "Sử thi anh hùng"
    angle_hint: "Hành trình anh hùng, trận chiến thần thoại"
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "10-20 min"
narration_pov: "3rd person (rich storyteller — the gods, the hero, the people)"
narration_tone: "grand, immersive, dramatic storyteller"
visual_style: "epic painterly oil-painting fantasy illustration"
style_anchor: "Epic painterly fantasy illustration, dramatic oil-painting brushwork, mythological grandeur, golden volumetric light,"
style_lock: "rich saturated classical palette, sweeping cinematic composition, divine atmosphere, no photo, no 3d render, no flat vector, no anime, no modern objects, 16:9 widescreen."
style_anchor_vi: "Minh họa sử thi huyền ảo mang tính hội họa painterly, nét vẽ sơn dầu kịch tính kịch nghệ, vẻ tráng lệ thần thoại, ánh sáng khối vàng óng volumetric,"
style_lock_vi: "bảng màu cổ điển đậm đà phong phú, bố cục điện ảnh bao la tráng lệ, không khí thần thánh, không ảnh chụp, không dựng hình 3D, không vector phẳng, không anime, không vật thể hiện đại, khung hình rộng 16:9."
recurring_character: "keep each god/hero's defining attributes constant across every scene — e.g. Zeus = mature bearded king, white-and-gold robes, crackling lightning bolt; Thor = red-bearded warrior, winged helm, short-handled hammer Mjolnir; Anubis = jackal-headed figure in gold-and-black; Athena = helmeted maiden with spear, shield and owl. Build one reference frame per recurring figure."
cast_policy:
  required: true
  min: 1
  recommended_max: 5
  hard_max: 7
  allow_crowd_without_reference: true
  portrait: {crop: "waist-up", background: "plain painterly neutral background", lighting: "soft golden character-study lighting"}
  shot_rotation: [epic wide, medium confrontation, heroic close-up, artifact detail, over-the-shoulder, crowd tableau]
palette:
  divine_gold: "#D4AF37"
  deep_crimson: "#8C1C1C"
  marble_white: "#F2EDE0"
  storm_grey: "#4A4E5A"
  divine_glow: "#FBE7A8"
  bronze: "#9C6B3C"
  aegean_blue: "#2E5A78"
  shadow_black: "#1A1714"
  ember_orange: "#D9772E"
  laurel_green: "#3F6B4A"
  royal_purple: "#5B3A6E"
tts_mood: "rich, dramatic storyteller"
music_mood: "epic orchestral"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [mythology, folklore, greek-mythology, norse-mythology, egyptian-mythology, legends, gods, heroes, epic, storytelling]
marketing:
  version: 1
  audience: "Người yêu thần thoại, văn hóa dân gian và biểu tượng cổ"
  objectives: [education, engagement, follow]
  formats: [story, character_card, compare_carousel, poll]
  pillars: [{id: god_and_hero, weight: 35, content_class: shareable, buyer_stage: community, formats: [story, character_card]}, {id: symbol_and_origin, weight: 35, content_class: both, buyer_stage: awareness, formats: [compare_carousel, story]}, {id: myth_comparison, weight: 30, content_class: searchable, buyer_stage: awareness, formats: [compare_carousel, poll]}]
  hook_bank: {types: [story, curiosity, value], examples: ["Vị thần này không giống điều bạn vẫn nghĩ.", "Biểu tượng cổ này từng mang một ý nghĩa rất khác."]}
  cta: [comment, save, follow]
  avoid: [religious_mockery, invented_historical_sources]
  evidence: {mode: required, allowed_claims: [clearly_labeled_myth_or_folklore], prohibited_claims: [myth_presented_as_historical_fact]}
  quality: {min_caption_chars: 160, max_promotional_share: 5}
---

<!-- body do control plane cấp theo entitlement (A5) -->
