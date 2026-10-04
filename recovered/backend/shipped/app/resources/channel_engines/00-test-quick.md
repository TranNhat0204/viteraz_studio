---
id: test-quick
name: "⚡ Test nhanh (chạy thử pipeline)"
niche: "Chủ đề bất kỳ — engine rút gọn để chạy thử pipeline cho nhanh"
language: vi
aspect_ratio: "16:9"
video_length: "~16s"
# Cờ TEST: bước script CẮT CỨNG kịch bản ≤ test_target_sec (xem script.py) → TTS ngắn theo, storyboard
# tự ra ~2 cảnh ⇒ 1 video (hook) + 1 ảnh. KHÔNG dựa vào LLM tự viết ngắn. Xoá file này là gỡ sạch.
test_mode: true
test_target_sec: 16
narration_pov: "2nd person"
narration_tone: "calm, simple"
visual_style: "hand-drawn 2D doodle cartoon animation"
style_anchor: "Hand-drawn 2D doodle cartoon animation, flat solid colors, bold black hand-drawn outlines, slightly wobbly imperfect marker lines,"
style_lock: "no gradients, no drop shadows, no photographic textures, no photorealism, no 3D render, no realistic faces, no anime, 16:9 widescreen, simple educational YouTube explainer doodle style."
style_anchor_vi: "Hoạt hình doodle 2D vẽ tay, mảng màu phẳng nguyên khối, nét vẽ chì đen đậm nét mộc mạc hơi nguệch ngoạc dạng bút dạ,"
style_lock_vi: "không hiệu ứng đổ bóng, không bóng mờ, không chất liệu ảnh chụp, không tả thực photorealism, không dựng hình 3D, không vẽ mặt tả thực, không nét vẽ anime, khung hình 16:9, phong cách doodle giải thích kiến thức YouTube đơn giản."
palette:
  orange: "#F58220"
  sky_blue: "#7FB5D5"
  grass_green: "#4E9A45"
  cream: "#F5F1E6"
  white: "#FFFFFF"
tts_mood: "calm, simple narrator"
music_mood: "subtle ambient"
recommended_image_tool: "Google Flow (Imagen)"
recommended_video_tool: "Google Flow (Veo) — image-to-video"
tags: [test, debug, quick]
---

<!-- body do control plane cấp theo entitlement (A5) -->
