---
# ═══════════════ AFF ENGINE TEMPLATE (đề xuất chuẩn v1) ═══════════════
# 1 file = 1 KIỂU VIDEO AFFILIATE. Chia folder GIỐNG channel_engines, nhưng CẤU TRÚC BÊN TRONG KHÁC:
# bám đúng cách thư viện prompt affiliate vận hành → ẢNH (keyframe 11 trường) → PROMPT VIDEO từng phân cảnh → GHÉP.
# Khi tạo video AI Affiliate, user chọn 1 "kiểu video" (engine) ở đây. Engine giữ NGUYÊN cách quay/dựng/giọng
# của kiểu đó, chỉ thay {SẢN_PHẨM} (crawl) + {PERSONA} (kênh). Constants dùng chung ở docs/aff-engine.md.
id: <slug>                          # = tên file (bỏ số thứ tự)
name: "<Tên kiểu video hiển thị>"
archetype: A | B | C                # A=người mẫu mặc/dùng SP · B=product-in-hand (faceless+design-lock) · C=engagement/edu
video_type: "<vd outfit-check / mirror-selfie / product-review / mascot-wealth / kids-edu>"
niche_default: "<ngách ví dụ 1 dòng>"
niches:                             # ngách/sản phẩm hợp KIỂU này (1 engine → nhiều kênh)
  - label: "<Ngách con>"
    fits: "<loại sản phẩm hợp>"
platform: "tiktok_shop"             # tiktok_shop | shopee | lazada | generic
language: vi
aspect_ratio: "9:16"
clip_length: "6-10s"                # 1 clip
final_length: "15-30s"             # video ghép
# ── PERSONA / SẢN PHẨM ──
persona_scope: channel | none       # A=channel (người review cố định) · B/C=none
faceless: false
design_lock: false                  # archetype B → true
recurring_character: "<mascot/nhân vật cố định; '' nếu không>"
# ── KHUNG QUAY (tham chiếu enum docs/aff-engine.md §5.3-5.6) ──
scene_structure: "<cấu trúc phân cảnh, vd: top-down → orbit 360 → fly-up, 6-10s>"
camera_sequence: [<CAMERA_MOVE enum...>]
motion_presets: [<PRESET id...>]
dialogue_mode: none_music | vi_voiceover | vi_prompt_en_keyword | ambient
voice: none_music | vi_female_warm | vi_male_warm | anthropomorphic_street | ambient
# ── ẢNH (keyframe) ──
# style_anchor = chỉ định MÁY/FILM cụ thể, KHÔNG "8K/HDR/hyperrealistic" (gây da nhựa/AI-face) — xem docs/aff-engine.md §10.2
image_style_anchor: "<vd 'shot on 85mm, medium-format-style film grain, natural color,'>"
image_style_lock: "<câu KHOÁ cuối mọi prompt ảnh (+skin_realism §10.3 +9:16)>"
golden_rules: ["<luật ảnh 1>", "<...>"]     # A: toàn thân/góc trên cao/outfit rõ · B: design-lock · trung niên: anti-AI-face
# ── QUALITY DEFAULTS (hard-code để đẹp ngay; kế thừa Quality Playbook docs/aff-engine.md §10) ──
lighting_default: "<recipe §10.4, vd soft window + rim / high-key VN / 3-point softbox>"
color_look: "<look §10.5, vd warm-iphone / clean-girl / portra>"
lut_intensity: 50            # 30-70, MAX 75 (over-process = rẻ)
lens_default: "<§10.6, vd 85mm f/1.8 shallow DoF bokeh / macro>"
camera_angle_default: "<full-body low-angle · talking eye-level · product 45°>"
background_default: "<seamless neutral / góc 2 tường window / hành lang căn hộ / plaster beige>"
skin_realism: "natural skin texture with visible pores and fine imperfections, natural human proportions"
negative_constant: "<image+video negatives §10.9>"
motion_strength: "subtle_to_moderate"   # chống morph vải/tóc
reference_workflow: "character-sheet 360 → keyframe 9:16 2K → mask-and-place product → Veo Ingredients/Kling Elements → beats"  # §10.10
post_chain: "upscale 4K → interp 30fps → LUT → grain 5-12% → −14 LUFS"   # §10.12
quality_knobs: [lighting_mood, color_look, lut_intensity, dof, camera_angle, background, warmth, highkey, pacing, caption_style]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (Ingredients/first-last) / Kling 2.5-2.6 Cinematic — image-to-video"
tts_mood: "<giọng>"
music_mood: "<nhạc trend>"
tags: [<seo>, <keywords>]
---

# AFF Engine — <Tên kiểu video>

> **Kiểu:** <archetype> · **Dùng khi:** <loại sản phẩm/ngách hợp>. <1 câu mô tả cảm giác video này tạo ra & vì sao viral.>
> Input: `{SẢN_PHẨM}` (tên/ảnh/giá/tính năng đã crawl) + `{PERSONA}` (nhân vật cố định của kênh, chỉ archetype A).

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cấu trúc:** <mô tả chuỗi phân cảnh verbatim từ tab, vd "3 phân cảnh: trên cao hạ xuống → xoay 360 → bay lên. 6-10s.">
- **Sản phẩm hợp:** <...> · **Độ dài clip / video:** <...> · **Có lộ mặt / persona không:** <...>
- **Vì sao dạng này AI làm mượt, ít lỗi:** <ghi chú kỹ thuật từ tab>

## 2. KỊCH BẢN & LỜI (script layer)
> Chỉ áp khi kiểu này CÓ thoại/CTA. Fashion no-dialogue: chỉ HOOK text overlay + caption; bỏ qua đoạn thoại dài.
- **Hook (0-3s):** <công thức hook cho kiểu này + 2-3 mẫu tiếng Việt> (kho: docs/aff-engine.md §3.4)
- **Thân (Problem → Solution + fact):** <cách chèn {giá}/{tính năng} tự nhiên, benefit trước số sau, 1 nhược điểm thật>
- **CTA (cuối):** <mẫu: "Link ở giỏ hàng màu vàng / ở bio" + disclosure "mình có nhận hoa hồng"> (kho §3.5)
- **Text overlay đặc trưng:** <vd "Outfit hôm nay ✨", "Link ở bio">

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Khung 11 trường (docs/aff-engine.md §5.7). Điền theo {PERSONA}/{SẢN_PHẨM}, giữ `image_style_anchor` đầu + `image_style_lock` cuối.
- **Golden rules (verbatim từ tab):** <vd "phải toàn thân · góc từ trên cao · outfit rõ ràng"> / hoặc **DESIGN-LOCK** (archetype B).
- **Ví dụ VERBATIM (từ tab, thay chỗ động bằng {SẢN_PHẨM}/{PERSONA}):**
  ```
  <prompt ảnh mẫu nguyên văn từ tab, chèn {biến}>
  ```
- **Nhân bản (nếu tab dạy):** <đổi bối cảnh giữ nguyên nhân vật/sản phẩm để ra nhiều keyframe>

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi phân cảnh 1 clip)
Schema mỗi clip: **Bối cảnh — Nhân vật — Hành động — Lời thoại — Giọng**. Luật: **1 camera-move + 1 action / clip** (chống méo). Giữ "nhân vật/sản phẩm như ảnh gốc" (reference-chaining). Bake NEGATIVE (§5.5) cuối mỗi prompt.
> Đây là PHẦN LÕI — chép NGUYÊN VĂN bộ prompt của tab thành 1 menu; pipeline chọn/ghép 5 cảnh.

**Phân cảnh 1 — <tên> (`<CAMERA_MOVE>` + `<ACTION>`):**
```
Bối cảnh: <...>
Nhân vật/Sản phẩm: <như ảnh gốc, giữ nguyên>
Hành động: <camera + pose verbatim từ tab>
Lời thoại: <none / VN>
Giọng: <nhạc nền / VN>
```
**Phân cảnh 2 — ...** (lặp cho đủ menu của tab: walk / hair-flip / 360 / detail / CTA ...)
> Kids/edu (archetype C): thay bằng phases `0-2s / 3-6s / 7-8s`, mỗi phase có `says:` + `(mood)` + "no text, no subtitles, no logos, no watermark".

## 5. GHÉP & XUẤT  (BƯỚC 3 — assemble/Studio/export)
- Cắt đúng **beat nhạc trend TikTok**; đổi độ dài shot 1-8s (đừng đều 3-4s → lộ AI); hard-cut mặc định.
- **Caption karaoke** trong safe-zone 9:16 (TikTok 900×1492); overlay text đặc trưng; VN voice khi kiểu cần.
- **Gate chất lượng** (docs/aff-engine.md §7): color grade thống nhất, grain 35mm 10-15%, −14 LUFS, imperfection cue.
- **Disclosure** cạnh CTA (AI-generated + hoa hồng). Export 1080p/4K 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi lần gen):** <negative riêng kiểu này + kế thừa NEGATIVE chung §5.5>
- **DO:** <2-3 điều bắt buộc của kiểu này (verbatim từ tab)>
- **DON'T:** <2-3 lỗi hay gặp của kiểu này>

## 7. METADATA
- Title <70 ký tự · caption + 15-25 hashtag ngách + CTA + disclosure. (khung docs/aff-engine.md §3.5)
