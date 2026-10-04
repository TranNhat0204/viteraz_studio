---
id: space-cosmos-science
name: "Vũ trụ & Khoa học (giải thích trực quan)"
niche: "Thiên văn, vũ trụ học, hố đen, hành tinh, quy mô vũ trụ — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Hố đen & vật thể cực đoan"
    angle_hint: "Hố đen, sao neutron, nghịch lý vật lý"
  - label: "Hệ Mặt Trời & hành tinh"
    angle_hint: "Các hành tinh, mặt trăng, sứ mệnh thám hiểm"
  - label: "Ngoài hành tinh & sự sống"
    angle_hint: "Exoplanet, khả năng có sự sống, tìm kiếm"
  - label: "Quy mô vũ trụ & 'điều gì xảy ra nếu'"
    angle_hint: "Kích thước vũ trụ, kịch bản giả định"
  - label: "Lịch sử thiên văn & sứ mệnh"
    angle_hint: "Các sứ mệnh không gian, khám phá lớn"
# Kênh TRI THỨC → bật step `research` (tra cứu dữ kiện thật trước khi viết, chống bịa).
factual: true
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "8-15 min"
narration_pov: "calm authoritative 3rd person, occasional 2nd person ('imagine you...')"
narration_tone: "grand, wondering, awe-driven, deep and patient"
visual_style: "photorealistic cosmic / astrophotography (JWST / Hubble telescope quality)"
style_anchor: "Hyper-detailed photorealistic astrophotography, James Webb / Hubble telescope quality, deep-space cinematic capture,"
style_lock: "crisp dense star fields, rich nebula color, ultra-high dynamic range, scientifically plausible, vast cosmic scale, no cartoon, no illustration, no halftone, no painterly, no text artifacts, 16:9 widescreen."
style_anchor_vi: "Chụp ảnh thiên văn siêu chi tiết photorealistic, chất lượng kính thiên văn James Webb / Hubble, khung hình điện ảnh không gian sâu vũ trụ,"
style_lock_vi: "dải sao dày đặc sắc nét, màu sắc tinh vân phong phú, dải tương phản rộng ultra-high, quy mô vũ trụ bao la, không hoạt hình, không minh họa tranh vẽ, không kỹ xảo 3D, khung hình rộng 16:9."
recurring_character: "no human character; recurring SCALE ANCHORS — a single tiny astronaut silhouette OR a small spacecraft/probe silhouette in lower frame to convey scale; accurate, scientifically plausible planet/star/nebula appearances"
cast_policy:
  required: false
  min: 0
  recommended_max: 1
  hard_max: 2
  allow_crowd_without_reference: true
  portrait: {crop: "full-body", background: "plain deep-space black background", lighting: "clean rim light preserving suit silhouette"}
  shot_rotation: [extreme wide scale, orbital wide, medium spacecraft, scientific close-up, diagram, point-of-view]
palette:
  deep_space_black: "#04060D"
  void_blue_black: "#0A1326"
  nebula_amber: "#F2A03D"
  nebula_cyan: "#36C9D9"
  nebula_magenta: "#C94FB0"
  nebula_teal: "#1F8C8C"
  ember_orange: "#E0681F"
  stellar_red: "#C8402E"
  cold_blue: "#5C8CE0"
  star_white: "#FBFBFF"
  dust_violet: "#6A4F9E"
  ice_pale: "#D9E6F2"
  gold_starlight: "#E8C66A"
tts_mood: "calm, awe, deep"
music_mood: "ambient orchestral swells, slow, vast, wondering"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [space, astronomy, cosmology, universe, black holes, exoplanets, nasa, jwst, science, explainer, photorealistic]
marketing:
  version: 1
  audience: "Người yêu thiên văn muốn hiểu vũ trụ bằng ngôn ngữ dễ tiếp cận"
  objectives: [education, engagement, follow]
  formats: [explainer, scale_carousel, fact_card, science_reel]
  pillars: [{id: cosmic_scale, weight: 35, content_class: shareable, buyer_stage: awareness, formats: [scale_carousel, science_reel]}, {id: discovery_explainer, weight: 40, content_class: both, buyer_stage: awareness, formats: [explainer, fact_card]}, {id: myth_vs_science, weight: 25, content_class: searchable, buyer_stage: awareness, formats: [explainer, discussion]}]
  hook_bank: {types: [curiosity, value, social_proof], examples: ["Nếu ánh sáng có thể kể chuyện, nó sẽ nói gì về vũ trụ?", "Khoảng cách này lớn hơn bạn tưởng rất nhiều."]}
  cta: [save, comment, follow]
  avoid: [unsupported_space_claims, doomsday_clickbait]
  evidence: {mode: required, allowed_claims: [peer_reviewed_or_agency_sources], prohibited_claims: [speculation_as_discovery]}
  quality: {min_caption_chars: 180, max_promotional_share: 10}
---

<!-- body do control plane cấp theo entitlement (A5) -->
