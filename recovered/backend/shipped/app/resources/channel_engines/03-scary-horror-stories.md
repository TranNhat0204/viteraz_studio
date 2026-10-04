---
id: scary-horror-stories
name: "Kể chuyện kinh dị (giọng rùng rợn)"
niche: "Truyện kinh dị ngôi thứ nhất, truyền thuyết đô thị, chuyện 'có thật' rợn người — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Truyện kinh dị ngôi thứ nhất"
    angle_hint: "Trải nghiệm rùng rợn nosleep, hồi hộp tăng dần"
  - label: "Truyền thuyết đô thị"
    angle_hint: "Đồn đại, hiện tượng lạ nơi quen thuộc"
  - label: "Chuyện có thật rùng rợn"
    angle_hint: "'Dựa trên sự kiện có thật', ám ảnh"
  - label: "Ma quái & siêu nhiên"
    angle_hint: "Nhà ma, bóng đè, thực thể vô hình"
  - label: "Sinh vật trong bóng tối"
    angle_hint: "Quái vật dân gian, săn đuổi trong đêm"
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "8-20 min"
narration_pov: "1st person (I / me / my) — intimate near-whisper survivor's account"
narration_tone: "low, intimate, slow-building dread; psychological, not gory"
visual_style: "dark moody cinematic horror illustration"
style_anchor: "Dark cinematic horror illustration, gritty texture, heavy shadow, low-key lighting, film grain,"
style_lock: "gothic desaturated palette, deep blacks, eerie volumetric haze, painterly dread, faces hidden or shadowed, no bright cheerful colors, no cute, no clean flat vector, no daylight, no graphic gore, 16:9 widescreen."
style_anchor_vi: "Minh họa kinh dị điện ảnh u tối, chất liệu thô ráp u ám, bóng tối bao trùm, ánh sáng low-key rùng rợn, hạt phim u uất,"
style_lock_vi: "tông màu u tối u ám, bóng đêm thăm thẳm, sương mờ khối ma mị, nỗi sợ mang tính hội họa, khuôn mặt ẩn mờ trong bóng tối, không màu sắc tươi sáng vui vẻ, không nét vẽ phẳng vector, không ánh sáng ban ngày, khung hình rộng 16:9."
visual_guardrails: "LOCATION CONTINUITY LOCK: infer the country, region, climate, settlement type, architecture and time period from the story, then keep that same real-world setting in every scene unless the narration explicitly moves elsewhere. Do not interpret the word gothic in the color/style lock as permission to invent European Gothic architecture. When the story is set in Vietnam, show recognizably Vietnamese environments appropriate to the stated region: modest rural tile-roof or corrugated-roof houses, plaster or weathered brick walls, narrow lanes, courtyards, wells, bamboo or tropical vegetation, humid rain, local utility poles and region-appropriate interiors. Absolutely no European castle, Victorian manor, cathedral, Western cemetery, wrought-iron estate gate, medieval tower, Western overcoat or foreign streets unless explicitly present in the narration. Preserve the same house silhouette, roof material, gate, courtyard, well, road and surrounding vegetation across consecutive scenes at that location."
recurring_mood: "single light source in darkness, drifting fog, long empty corridors, distant shadowed silhouettes; any human figure kept faceless or shadowed"
cast_policy:
  required: true
  min: 1
  recommended_max: 3
  hard_max: 5
  allow_crowd_without_reference: true
  portrait: {crop: "waist-up", background: "plain near-black background", lighting: "single soft low-key light, face readable but restrained"}
  shot_rotation: [wide isolation, medium suspense, close-up reaction, obscured threat, object detail, point-of-view]
palette:
  near_black: "#0B0C0E"
  ink_charcoal: "#15181C"
  cold_blue: "#243B55"
  steel_blue: "#3A5A78"
  sickly_green: "#3F5B43"
  muted_teal: "#2C4A4A"
  blood_muted_red: "#6E2B2B"
  rust_red_accent: "#8A3A2E"
  bone_gray: "#7C7E80"
  ash_white: "#B9BCC0"
  fog_gray: "#5A6066"
  amber_lamp: "#7A5A2A"
tts_mood: "low intimate whisper, slow, restrained; long pauses, breath before the reveal"
music_mood: "minimal sustained drone, sub-bass swell, sudden silence at the turn"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video, slow push-ins"
tags: [horror, scary stories, nosleep, creepypasta, true scary stories, urban legend, narration, dark, atmospheric, faceless]
marketing:
  version: 1
  audience: "Fan truyện rùng rợn, urban legend và không khí bí ẩn"
  objectives: [engagement, community, follow]
  formats: [micro_story, poll, lore_card, horror_reel]
  pillars: [{id: original_microfiction, weight: 45, content_class: shareable, buyer_stage: community, formats: [micro_story, horror_reel]}, {id: urban_legend, weight: 30, content_class: both, buyer_stage: awareness, formats: [lore_card, poll]}, {id: audience_prompt, weight: 25, content_class: shareable, buyer_stage: community, formats: [poll, discussion]}]
  hook_bank: {types: [story, curiosity, contrarian], examples: ["Đúng 3:17 sáng, điện thoại của cô ấy reo.", "Đừng đọc dòng cuối nếu bạn ở một mình."]}
  cta: [comment, share, follow]
  avoid: [graphic_gore, self_harm_detail, panic_misinformation]
  evidence: {mode: optional, allowed_claims: [fiction_labeled, folklore_context], prohibited_claims: [fiction_presented_as_verified_news]}
  quality: {min_caption_chars: 140, max_promotional_share: 10}
---

<!-- body do control plane cấp theo entitlement (A5) -->
