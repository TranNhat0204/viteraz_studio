---
id: <slug>
name: "<Tên engine hiển thị>"
niche: "<mô tả ngách MẶC ĐỊNH 1 dòng — chỉ là ví dụ; kênh có thể chọn ngách khác bên dưới>"
# Catalog NGÁCH con dùng chung "kiểu video" (vibe) này. Khi tạo KÊNH, user chọn 1 ngách (hoặc tự nhập)
# → AI giữ NGUYÊN format/visual/giọng của engine nhưng sinh nội dung theo ngách đã chọn. 1 engine → nhiều kênh.
# Có thể bỏ trống. Dạng list chuỗi, hoặc list dict {label, angle_hint} để gợi ý góc khai thác.
niches:
  - label: "<Ngách con 1>"
    angle_hint: "<góc khai thác / nhấn mạnh cho ngách này>"
    angles:    # (tùy chọn) angle bank — các khuôn tiêu đề/góc viral để ideation xoay vòng, tránh lặp
      - "<Khuôn góc 1, dùng ___ cho chỗ thay đổi>"
      - "<Khuôn góc 2>"
  - label: "<Ngách con 2>"
    angle_hint: "<...>"
# series_mode: "anthology" = mỗi tập là 1 CHỦ ĐỀ MỚI đứng độc lập (vụ án/câu chuyện/chủ đề khác nhau);
# ideation KHÔNG nối tiếp cùng một chủ đề, chỉ giữ chung phong cách/format/giọng/nhận diện kênh.
# ("serial" = kể tiếp cùng nhân vật/cốt truyện nhiều tập — chỉ dùng cho kênh kể chuyện dài kỳ.)
series_mode: anthology
language: en
aspect_ratio: "16:9"            # hoặc 9:16 cho Shorts
video_length: "<vd 7-12 min>"
narration_pov: "<vd 2nd person / 3rd person narrator>"
narration_tone: "<vd calm, intelligent>"
visual_style: "<vd hand-drawn 2D doodle>"
style_anchor: "<câu mở đầu MỌI image prompt>"
style_lock: "<câu khoá phong cách + negative-phrasing + 16:9, đặt cuối MỌI image prompt>"
style_anchor_vi: "<câu mở đầu MỌI image prompt bằng Tiếng Việt (tùy chọn cho kênh tiếng Việt)>"
style_lock_vi: "<câu khoá phong cách bằng Tiếng Việt (tùy chọn cho kênh tiếng Việt)>"
recurring_character: "<chuỗi mô tả nhân vật/chủ thể cố định — để giữ đồng nhất; '' nếu ngách không có nhân vật>"
cast_policy:
  required: true
  min: 1
  recommended_max: 4
  hard_max: 6
  allow_crowd_without_reference: true
  portrait:
    crop: "waist-up"
    background: "plain neutral studio background"
    lighting: "soft even studio lighting"
  shot_rotation: [wide establishing, medium action, close-up, object detail, map or diagram, over-the-shoulder]
palette:
  <ten_mau>: "#RRGGBB"
tts_mood: "<gợi ý giọng đọc>"
music_mood: "<gợi ý nhạc nền>"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [<seo>, <keywords>]
---

<!-- body do control plane cấp theo entitlement (A5) -->
