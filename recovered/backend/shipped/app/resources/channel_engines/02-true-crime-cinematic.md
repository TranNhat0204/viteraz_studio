---
id: true-crime-cinematic
name: "Phá án / Bí ẩn — phong cách điện ảnh"
niche: "Vụ án chưa có lời giải, điều tra, mất tích, bí ẩn pháp y — ngách MẶC ĐỊNH, có thể đổi"
# Ngách con dùng chung phong cách engine này — chọn 1 khi tạo kênh (hoặc tự nhập ngách riêng).
niches:
  - label: "Án mạng chưa có lời giải"
    angle_hint: "Hồ sơ giết người bí ẩn, nghi phạm, manh mối lạnh"
  - label: "Mất tích bí ẩn"
    angle_hint: "Người biến mất không dấu vết, giả thuyết, cuộc tìm kiếm"
  - label: "Khoa học hình sự"
    angle_hint: "Pháp y, ADN, dấu vết phá án"
  - label: "Kẻ sát nhân hàng loạt"
    angle_hint: "Chân dung tội phạm, động cơ, hành trình bị bắt"
  - label: "Lừa đảo & án kinh tế"
    angle_hint: "Mưu mô, sụp đổ, vạch trần"
# Kênh TRI THỨC → bật step `research` (tra cứu dữ kiện thật trước khi viết, chống bịa).
factual: true
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"
video_length: "10-18 min"
narration_pov: "3rd person (investigative narrator)"
narration_tone: "measured, suspenseful, restrained, respectful; present-tense reconstruction"
visual_style: "cinematic photorealistic documentary reenactment"
style_anchor: "Cinematic photorealistic film still, shot on 35mm, shallow depth of field, moody documentary lighting,"
style_lock: "naturalistic muted color grade, volumetric light, film grain, faces obscured or shadowed for anonymity, no cartoon, no illustration, no anime, no cgi, no plastic skin, no graphic gore, 16:9 widescreen."
style_anchor_vi: "Khung hình phim điện ảnh chân thực photorealistic, quay bằng máy ảnh 35mm, độ sâu trường ảnh nông, ánh sáng phim tài liệu huyền bí u uất,"
style_lock_vi: "tông màu phim 35mm hoài cổ tự nhiên desaturated, ánh sáng khối volumetric, hạt phim mịn, khuôn mặt che bóng mờ ẩn danh, không hoạt hình, không tranh vẽ, không anime, không kỹ xảo CGI, khung hình rộng 16:9."
recurring_motifs: "case-file folder, cork board with red string, evidence bag, rain-streaked window, redacted document; every depicted person kept faceless / shadowed / back-of-head for anonymity and policy"
cast_policy:
  required: false
  min: 0
  recommended_max: 4
  hard_max: 6
  allow_crowd_without_reference: true
  portrait: {crop: "waist-up", background: "plain dark neutral background", lighting: "soft side light with identity-safe shadow"}
  shot_rotation: [wide establishing, medium reenactment, silhouette close-up, evidence detail, over-the-shoulder, document insert]
palette:
  noir_teal: "#1E3A3F"
  amber_glow: "#C8884A"
  deep_shadow: "#12161A"
  ash_gray: "#5A6066"
  cold_steel_blue: "#2C3E50"
  muted_olive: "#4A4A38"
  evidence_red: "#9B2226"
  paper_cream: "#D9CDB8"
  redaction_black: "#0A0A0A"
  fog_gray: "#8A8F94"
  sodium_lamp: "#B5803C"
  desk_brown: "#3B2F26"
  rain_blue: "#3A4A5A"
  highlight_white: "#E8E4DC"
tts_mood: "low, measured, suspenseful narrator"
music_mood: "tense ambient drone"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [true-crime, mystery, unsolved, cold-case, disappearance, forensics, investigation, documentary, cinematic, faceless]
marketing:
  version: 1
  audience: "Người xem documentary điều tra muốn hiểu bối cảnh và chứng cứ"
  objectives: [education, engagement, follow]
  formats: [timeline, case_file, discussion, documentary_reel]
  pillars: [{id: case_timeline, weight: 40, content_class: both, buyer_stage: awareness, formats: [timeline, case_file]}, {id: forensic_literacy, weight: 35, content_class: searchable, buyer_stage: awareness, formats: [case_file, discussion]}, {id: scam_awareness, weight: 25, content_class: shareable, buyer_stage: community, formats: [discussion, documentary_reel]}]
  hook_bank: {types: [curiosity, story, social_proof], examples: ["Một chi tiết nhỏ đã thay đổi toàn bộ hồ sơ.", "Hồ sơ này vẫn còn một câu hỏi chưa có lời đáp."]}
  cta: [comment, save, follow]
  avoid: [graphic_detail, victim_blaming, naming_unconvicted_people_as_guilty, sensational_fear]
  evidence: {mode: required, allowed_claims: [verified_case_records], prohibited_claims: [speculation_as_fact]}
  quality: {min_caption_chars: 220, max_promotional_share: 0}
---

<!-- body do control plane cấp theo entitlement (A5) -->
