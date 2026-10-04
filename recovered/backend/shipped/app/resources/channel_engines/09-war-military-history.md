---
id: war-military-history
name: "Lịch sử Quân sự (phong cách tài liệu)"
niche: "Trận đánh nổi tiếng, chiến dịch, chiến lược, vũ khí & chiến thuật — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Trận đánh nổi tiếng"
    angle_hint: "Diễn biến, bước ngoặt, kết cục các trận lớn"
  - label: "Chiến dịch & chiến lược"
    angle_hint: "Mưu lược, hậu cần, nghệ thuật chỉ huy"
  - label: "Câu chuyện chưa kể thời chiến"
    angle_hint: "Góc khuất, số phận con người"
  - label: "Vũ khí & chiến thuật qua thời đại"
    angle_hint: "Tiến hóa vũ khí, kỹ thuật quân sự"
  - label: "Nhân vật & tướng lĩnh"
    angle_hint: "Chân dung danh tướng, quyết định lịch sử"
# Kênh TRI THỨC → bật step `research` (tra cứu dữ kiện thật trước khi viết, chống bịa).
factual: true
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "12-22 min"
narration_pov: "3rd person (authoritative documentary narrator)"
narration_tone: "authoritative, measured, sober, respectful"
visual_style: "aged documentary / vintage archival film aesthetic (history reenactment)"
style_anchor: "Aged documentary reenactment still, desaturated vintage film grain, archival war-era tones, cinematic wide framing,"
style_lock: "muted sepia-and-steel palette, period-accurate uniforms and equipment, photographic realism, smoke and atmosphere, no cartoon, no illustration, no modern objects, no anime, no graphic gore, 16:9 widescreen."
style_anchor_vi: "Cảnh tái hiện phim tài liệu lịch sử cổ điển, hạt phim hoài cổ desaturated, tông màu tư liệu chiến tranh, góc máy điện ảnh rộng,"
style_lock_vi: "bảng màu sepia và thép trầm tối, trang phục và khí tài chuẩn xác theo thời kỳ lịch sử, tính chân thực nhiếp ảnh, khói bụi và không khí chiến trường, không hoạt hình, không tranh vẽ, không vật thể hiện đại, khung hình rộng 16:9."
visual_guardrails: "HISTORICAL ACCURACY LOCK: first infer the exact year or narrow date range, region, belligerents, and historical phase from the narration; repeat the year/era and army names in every prompt containing people or equipment. Select technology only from the correct period: pre-1000 = period infantry, cavalry, bows, spears, shields, siege engines and pre-modern fortifications; 1000-1499 = medieval armor, crossbows, early gunpowder only where historically justified; 1500-1799 = pike-and-shot, matchlock/flintlock firearms, period cannon, cavalry, horses, wagons, sailing ships and era-appropriate fortifications; 1800-1850 = Napoleonic-era muskets, smoothbore cannon, cavalry, horses and period logistics; 1851-1913 = industrial-era rifles, early machine guns, railways, telegraph, ironclads and only historically available artillery; 1914-1945 = World War-era uniforms, tanks, aircraft, submarines, radios and weapons only when the date supports them; 1946-1990 = Cold War-era uniforms, jets, helicopters, armored vehicles, missiles and radios only when supported; after 1990 = contemporary equipment only when explicitly supported. Never mix technology, uniforms, flags, vehicles, architecture or roads from different periods. Never insert tanks, aircraft, assault rifles, concrete bunkers or modern machinery into an earlier era such as 1789. If the narration does not justify a vehicle, use the period's infantry, cavalry, artillery, logistics, map or landscape instead."
consistency: "keep period accuracy (uniforms, weapons, terrain per era/front); recurring map/strategy frames with arrows and front lines; faceless/wide soldier silhouettes; never show explicit close-up faces in distress"
cast_policy:
  required: false
  min: 0
  recommended_max: 5
  hard_max: 6
  allow_crowd_without_reference: true
  portrait:
    crop: "waist-up"
    background: "plain neutral grey studio background"
    lighting: "soft even documentary portrait lighting"
  shot_rotation: [wide establishing, medium action, close-up, object detail, map or diagram, over-the-shoulder]
palette:
  sepia: "#8C6A3F"
  gunmetal: "#3A4047"
  muted_olive: "#5A5E3A"
  smoke_grey: "#9A9A94"
  faded_amber: "#C39A52"
  steel_blue: "#4A5A63"
  ash_white: "#D8D4C8"
  charcoal: "#26282B"
  rust_brown: "#6E4A33"
  field_tan: "#B7A079"
  map_parchment: "#E3D8BC"
  blood_muted: "#7A3B33"
tts_mood: "grave, authoritative"
music_mood: "somber militaristic strings and drums, restrained and tense"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [history, military-history, war, battles, campaigns, strategy, documentary, archival, reenactment, weapons, tactics]
marketing:
  version: 1
  audience: "Người xem documentary quan tâm lịch sử, chiến lược và con người trong chiến tranh"
  objectives: [education, engagement, follow]
  formats: [timeline, map_carousel, archive_card, documentary_reel]
  pillars: [{id: battle_context, weight: 35, content_class: both, buyer_stage: awareness, formats: [timeline, map_carousel]}, {id: strategy_and_logistics, weight: 35, content_class: searchable, buyer_stage: awareness, formats: [archive_card, map_carousel]}, {id: human_history, weight: 30, content_class: shareable, buyer_stage: community, formats: [documentary_reel, discussion]}]
  hook_bank: {types: [story, curiosity, value], examples: ["Trận đánh này được quyết định trước khi tiếng súng đầu tiên vang lên.", "Bản đồ này giải thích toàn bộ chiến dịch."]}
  cta: [comment, save, follow]
  avoid: [glorifying_violence, extremist_praise, graphic_war_content]
  evidence: {mode: required, allowed_claims: [archival_historical_sources], prohibited_claims: [revisionism_as_fact]}
  quality: {min_caption_chars: 200, max_promotional_share: 0}
---

<!-- body do control plane cấp theo entitlement (A5) -->
