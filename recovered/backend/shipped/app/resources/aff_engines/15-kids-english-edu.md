---
id: kids-english-edu
name: "TIẾNG ANH MẸ BÉ — Anna & Chibi 3D Pixar (song ngữ, 3 phase/clip)"
archetype: C
video_type: "kids-edu (song ngữ mẹ-bé, động từ trong ngày diễn kịch)"
niche_default: "Kênh mẹ & bé dạy tiếng Anh — mỗi clip 8s dạy 1 động từ (dig/plant/water/pick...) theo tình huống đời thường"
niches:
  - label: "Đồ chơi & học liệu mẹ&bé"
    fits: "đất nặn, khối gỗ, sách tranh, bút màu, nhạc cụ đồ chơi"
  - label: "Đồ dùng chăm bé"
    fits: "sữa tắm, khăn, kem dưỡng, bàn chải, lược, đồ ngủ"
  - label: "Đồ dùng ngoài trời & nhà bếp cho bé"
    fits: "dụng cụ làm vườn mini, bộ nướng bánh, phao bơi, lều cắm trại, đồ đi biển"
platform: "tiktok_shop"
language: vi
aspect_ratio: "9:16"
clip_length: "8s"
final_length: "35-45s"          # 5 cảnh × 8s ghép 1 chủ đề
persona_scope: none              # KHÔNG persona kênh — cast CỐ ĐỊNH Anna + Chibi
faceless: false
design_lock: false
recurring_character: "Anna (mẹ) + Chibi (bé), 3D Pixar — Anna tóc búi rối nâu, áo khoác denim; Chibi tóc xoăn + băng đô hoa, váy cam. Giữ y hệt qua mọi cảnh (dùng ảnh gốc image_0.png làm identity canon)."
scene_structure: "1 chủ đề = 5 cảnh × 8s. Mỗi clip theo schema 3 PHASE có mốc thời gian: Phase 1 (0-2s) mẹ Anna hỏi tiếng Việt → Phase 2 (3-6s) bé Chibi diễn hành động + trả lời keyword tiếng Anh → Phase 3 (7-8s) chốt cảm xúc. Mỗi phase 1 câu says: + tag (mood)."
camera_sequence: [PHASE1_QUESTION, PHASE2_ACTION_KEYWORD, PHASE3_EMOTION_CLOSE]
motion_presets: [kids_english_3phase]
dialogue_mode: vi_prompt_en_keyword
voice: "(bilingual, consistent) — Anna giọng nữ ấm ngọt; Chibi giọng cao trong trẻo ngây thơ; giữ nguyên tính cách giọng qua cả 5 cảnh (Voice Consistency)"
image_style_anchor: "3D Pixar style, cinematic 3D animation, Pixar aesthetic, cinematic lighting,"
image_style_lock: "consistent character design, high detail, high-resolution, 8k, no text, no subtitles, no logos, no watermark."
golden_rules: ["cast CỐ ĐỊNH Anna + Chibi (không đổi persona theo kênh)", "mỗi clip đúng 3 phase 0-2s / 3-6s / 7-8s", "mỗi phase 1 câu says: + 1 tag (mood)", "1 động từ tiếng Anh/clip diễn ra bằng hành động", "kèm câu Voice Consistency giữ giọng", "đuôi bắt buộc: no text, no subtitles, no logos, no watermark"]
lighting_default: "warm soft natural light (sunlit garden / cozy indoor / warm golden bedroom) tuỳ chủ đề, ấm áp thân mật"
color_look: "vibrant Pixar palette, warm friendly grade, màu tươi bão hoà vừa phải, da hồng hào"
lut_intensity: 45
lens_default: "cinematic 3D depth of field, soft bokeh background, close-up ưu tiên khuôn mặt biểu cảm bé"
camera_angle_default: "eye-level / close-up khuôn mặt bé Chibi ở 1/3 trên; hành động (tay bé) cận cảnh"
background_default: "bối cảnh đời thường theo chủ đề: vườn nắng · siêu thị · phòng ngủ ấm · phòng chơi · bãi biển · sở thú"
skin_realism: "Pixar-style rounded facial features, expressive big eyes, soft skin shading (KHÔNG realism lỗ chân lông — đây là 3D animation)"
negative_constant: "text, subtitles, captions, logos, watermark, morphing faces, inconsistent character design, distorted hands, extra fingers, extra people, flickering, blurry, creepy uncanny faces, dark scary mood"
motion_strength: "subtle_to_moderate"
reference_workflow: "keyframe ảnh bìa Anna+Chibi (image_0.png = identity canon) → mọi cảnh 'same characters Anna and Chibi from image_0.png' → image-to-video 8s theo schema 3 phase → ghép 5 cảnh 1 chủ đề"
post_chain: "giữ nét 3D → interp 30fps → warm LUT nhẹ (~45%) → grain 0-5% (animation không cần grain) → voice song ngữ −14 LUFS + nhạc nền thiếu nhi vui tươi"
quality_knobs: [lighting_mood, color_look, lut_intensity, background, pacing, caption_style_in_edit]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI (giữ 3D Pixar, KHÔNG ép realism)"
recommended_video_tool: "Veo 3.1 (image-to-video, có audio dialogue) / Kling 2.5-2.6 — 8s/clip"
tts_mood: "song ngữ: mẹ Anna ấm ngọt (VN) + bé Chibi cao trong trẻo (keyword EN)"
music_mood: "nhạc nền thiếu nhi nhẹ nhàng vui tươi, không lấn giọng"
tags: [tieng-anh-me-be, kids-english, song-ngu, 3d-pixar, anna-chibi, day-tre-hoc, dong-tu, me-va-be, tiktok-shop, affiliate, edu]
---

# AFF Engine — TIẾNG ANH MẸ BÉ · Anna & Chibi 3D Pixar (song ngữ)

> **Kiểu:** C (engagement / edu — nội dung giáo dục song ngữ cho trẻ) · **Dùng khi:** nuôi kênh **mẹ & bé** để gắn account affiliate các sản phẩm mẹ&bé (đồ chơi, học liệu, đồ chăm bé, đồ ngoài trời cho bé). Mỗi video 3D Pixar dễ thương dạy bé **1 động từ tiếng Anh** qua tình huống đời thường — mẹ hỏi tiếng Việt, bé diễn hành động rồi bật ra keyword tiếng Anh — tạo cảm giác ấm áp, hữu ích, dễ chia sẻ trong hội nhóm bố mẹ.
> Input: `{SẢN_PHẨM}` (đồ mẹ&bé đã crawl — gắn ở caption/CTA & chọn chủ đề khớp đạo cụ) · **KHÔNG có {PERSONA} kênh** — cast **CỐ ĐỊNH Anna (mẹ) + Chibi (bé)**.

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **Cast cố định (verbatim từ tab):** **Anna** — "a young mother Anna with a brown messy bun, denim jacket"; **Chibi** — "a little girl Chibi with curly hair and a floral headband wearing an orange dress". Phong cách **3D Pixar / Disney**. Giữ **y hệt** qua mọi cảnh bằng câu khoá `same characters Anna and Chibi from image_0.png` (ảnh bìa cảnh đầu = identity canon).
- **Cấu trúc thư viện:** **20 chủ đề × 5 cảnh** (Trồng cây, Đi siêu thị, Vẽ tranh, Trước khi ngủ, Chăm sóc thú cưng, Đi tắm, Màu sắc, Bốn mùa, Làm bánh, Vệ sinh buổi sáng, Dọn dẹp đồ chơi, Chơi đất nặn, Cắm trại, Tập thể dục, Đọc sách, Đi biển, Chơi đồ chơi, Đi sở thú, Nhạc cụ...). **1 video = 1 chủ đề = 5 cảnh × 8s** ghép liên tục.
- **Mỗi cảnh = 1 clip 8s theo schema 3 PHASE có mốc thời gian** (xem §4 — đây là phần lõi):
  - **Phase 1 (0-2s):** mẹ **Anna hỏi bằng tiếng Việt** (gợi mở động từ) — `says:` + `(mood)`.
  - **Phase 2 (3-6s):** bé **Chibi diễn hành động** (dig/plant/water/pick/smell...) và **trả lời keyword tiếng Anh** — `says:` + `(mood)`.
  - **Phase 3 (7-8s):** **chốt cảm xúc** (mẹ khen / bé reo vui) — `says:` + `(mood)`.
- **Động từ trong ngày (verb-of-the-day) diễn bằng hành động:** mỗi clip khoá **1 động từ** trẻ học được (Dig, Plant, Water, Pick, Smell, Push, Choose, Put, Read, Yawn, Kiss, Bake, Knead, Roll, Shape...) — bé **vừa làm vừa nói**, học qua hình ảnh chứ không đọc chữ.
- **Mục đích edu → nuôi kênh aff:** nội dung dạy tiếng Anh cho bé thu hút **bố mẹ** (đúng chân dung mua đồ mẹ&bé), video sạch, dễ tin → gắn `{SẢN_PHẨM}` mẹ&bé vào caption/CTA/ghim giỏ hàng.
- **Vì sao AI làm mượt, ít lỗi:** cast cố định + bối cảnh ấm + **mỗi phase 1 hành động rõ ràng** (không đổi nhiều thứ cùng lúc) + đuôi `no text` giúp AI không vẽ chữ sai chính tả.

## 2. KỊCH BẢN & LỜI (script layer)
> Kiểu này **CÓ thoại song ngữ** — lời nằm sẵn trong prompt video (`says:` mỗi phase), sinh trực tiếp bằng model có audio (Veo). Không cần voiceover ngoài.
- **Hook (Phase 1 cảnh 1, 0-2s):** câu **hỏi tiếng Việt** khơi tò mò gắn động từ — ví dụ "Dùng xẻng nhỏ đào một cái hố là đang làm gì nhỉ?", "Cho cây uống nước mỗi ngày gọi là gì nào?".
- **Thân (Phase 2, 3-6s):** bé Chibi **diễn hành động + đáp keyword EN** — "Dig! I dig the soil", "Water! I water the tree". Đây là điểm học chính, giữ chân người xem.
- **Chốt (Phase 3, 7-8s):** cảm xúc ấm — mẹ khen ("Giỏi quá!"), bé reo ("Mát quá!", "For you, Mom!").
- **CTA (ở khâu dựng/caption, không burn trong clip):** "Đồ chơi/học liệu cho bé link ở giỏ hàng màu vàng 🛒" + disclosure "mình có nhận hoa hồng nếu mua qua link". (kho CTA: docs/aff-engine.md §3.5)
- **Voice Consistency (bắt buộc trong prompt):** "Warm, sweet female voice for Anna; clear, innocent high-pitched voice for Chibi" — nhắc lại `Consistent voices` ở các cảnh sau để giọng không đổi.

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Tạo **ảnh bìa cảnh 1 = identity canon** (image_0.png) rồi mọi cảnh sau tham chiếu về nó. Mở đầu `image_style_anchor`, kết `image_style_lock`. **Giữ 3D Pixar — TUYỆT ĐỐI không ép "photorealistic/realism", negative KHÔNG loại 3D/cartoon.**
- **Golden rules (verbatim):** cast cố định Anna (búi tóc nâu, denim) + Chibi (tóc xoăn, băng đô hoa, váy cam) · phong cách 3D Pixar/Disney · khuôn mặt biểu cảm to tròn dễ thương · `no text, no logos, no watermark`.
- **Ví dụ ảnh bìa VERBATIM (từ tab — chủ đề Trồng cây):**
  ```
  Cinematic 3D animation, close-up of a mother Anna and her young daughter Chibi kneeling in a sun-drenched garden, the girl Chibi holding a small shovel digging into rich brown soil, mother Anna smiling encouragingly, vibrant green plants in background, soft bokeh, 8k resolution, high detail, Pixar aesthetic, no text, no logos, no watermark.
  ```
- **Nhân bản (identity-lock):** từ cảnh 2 trở đi luôn mở bằng `3D Pixar style, same characters Anna and Chibi from image_0.png. <bối cảnh/đạo cụ mới>` — chỉ đổi đạo cụ/hành động, giữ nguyên mặt/tóc/trang phục để 5 cảnh đồng nhất.

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi cảnh 1 clip 8s)
> **PHẦN LÕI.** Schema **3 PHASE có mốc thời gian** (khác archetype A/B): mỗi clip 8s = mở đầu style + cast + `Voice Consistency:` → **Phase 1 (0-2s)** / **Phase 2 (3-6s)** / **Phase 3 (7-8s)**, mỗi phase 1 câu `says:` + `(mood)`, đóng bằng đuôi `no text, no subtitles, no logos, no watermark`. Luật: **1 hành động rõ / phase**, giữ cast như ảnh gốc, bake NEGATIVE §6 (KHÔNG loại 3D).

**KHUÔN CHUẨN (điền theo chủ đề):**
```
3D Pixar style, same characters Anna and Chibi from image_0.png. <bối cảnh + đạo cụ của cảnh>. Voice Consistency: <Warm sweet Anna voice; clear innocent high-pitched Chibi voice / Consistent voices>. Phase 1 (0-2s): <Anna hành động nhỏ>, says: "<câu hỏi tiếng Việt gợi động từ>"; Phase 2 (3-6s): <Chibi diễn hành động của động từ>, says: "<Keyword! I <verb> ... (tiếng Anh)>"; Phase 3 (7-8s): <chốt cảm xúc>, says: "<câu tiếng Việt/EN + cảm xúc>"; no text, no subtitles, no logos, no watermark.
```

### Ví dụ chủ đề A — "Trồng cây" (5 cảnh VERBATIM từ tab)
**Cảnh 1 — Đào hố (verb: DIG):**
```
3D Pixar style, a young mother Anna with a brown messy bun, denim jacket, and a little girl Chibi with curly hair and a floral headband wearing an orange dress. Both wear yellow gardening gloves in a sunny garden. Voice Consistency: Warm, sweet female voice for Anna; clear, innocent high-pitched voice for Chibi. Phase 1 (0-2s): Anna points at a small shovel, says: "Dùng xẻng nhỏ đào một cái hố là đang làm gì nhỉ?"; Phase 2 (3-6s): Chibi uses the shovel to scoop soil with excitement, says: "Dig! I dig the soil"; Phase 3 (7-8s): Anna claps happily as the hole is ready, says: "Giỏi quá!"; no text, no subtitles, no logos, no watermark.
```
**Cảnh 2 — Trồng mầm (verb: PLANT):**
```
3D Pixar style, same characters Anna and Chibi from image_0.png. Anna and Chibi are looking at a small green sprout. Voice Consistency: Same warm Anna voice and innocent Chibi voice. Phase 1 (0-2s): Anna hands a small sprout to Chibi, says: "Đặt cây mầm vào đất để cây lớn lên gọi là gì con?"; Phase 2 (3-6s): Chibi carefully places the sprout into the hole and pats the soil, says: "Plant! I plant a tree"; Phase 3 (7-8s): Chibi looks up at Anna with a big smile, says: "Xong rồi ạ!"; no text, no subtitles, no logos, no watermark.
```
**Cảnh 3 — Tưới nước (verb: WATER):**
```
3D Pixar style, same characters Anna and Chibi from image_0.png. Chibi holds a blue elephant-shaped watering can. Voice Consistency: Consistent voices. Phase 1 (0-2s): Anna tilts the watering can slightly, says: "Cho cây uống nước mỗi ngày gọi là gì nào?"; Phase 2 (3-6s): Chibi pours sparkling water over the plants, water droplets glisten in the sun, says: "Water! I water the tree"; Phase 3 (7-8s): Chibi giggles as a bit of water splashes, says: "Mát quá!"; no text, no subtitles, no logos, no watermark.
```
**Cảnh 4 — Hái quả (verb: PICK):**
```
3D Pixar style, same characters Anna and Chibi from image_0.png. A bush with bright red tomatoes. Voice Consistency: Consistent voices. Phase 1 (0-2s): Anna points to a ripe tomato, says: "Quả chín rồi, con hái xuống gọi là gì nhỉ?"; Phase 2 (3-6s): Chibi gently plucks the red tomato from the vine, says: "Pick! I pick a fruit"; Phase 3 (7-8s): She shows the tomato to the camera, says: "Cà chua đỏ quá!"; no text, no subtitles, no logos, no watermark.
```
**Cảnh 5 — Ngửi hoa (verb: SMELL):**
```
3D Pixar style, same characters Anna and Chibi from image_0.png. Chibi holds a beautiful colorful flower. Voice Consistency: Consistent voices. Phase 1 (0-2s): Anna brings the flower closer to Chibi's nose, says: "Hoa thơm quá, con dùng mũi để làm gì thế?"; Phase 2 (3-6s): Chibi closes her eyes and takes a deep breath of the flower's scent, says: "Smell! I smell the flower"; Phase 3 (7-8s): Anna hugs Chibi warmly, says: "Thơm quá con nhỉ!"; no text, no subtitles, no logos, no watermark.
```

### Ví dụ chủ đề B — "Trước khi ngủ" (5 cảnh VERBATIM từ tab — lưu ý giọng đổi sang thì thầm)
**Cảnh 1 — Đọc truyện (verb: READ):**
```
3D Pixar style, a young mother Anna with a brown messy bun and a little girl Chibi with curly hair and a floral headband wearing cloud-patterned pajamas. They are sitting on a cozy bed with soft, warm golden lighting. Voice Consistency: Soft, whispered female voice for Anna; clear, gentle high-pitched voice for Chibi. Phase 1 (0-2s): Anna opens a large colorful picture book, whispers: "Trước khi ngủ mình cùng lật từng trang sách gọi là gì nhỉ?"; Phase 2 (3-6s): Chibi leans against Anna's shoulder looking at the pages, says: "Read! I read a story"; Phase 3 (7-8s): Anna turns a page slowly, says: "Đúng rồi, truyện hay quá!"; no text, no subtitles, no logos, no watermark.
```
**Cảnh 2 — Ngáp (verb: YAWN):**
```
3D Pixar style, same characters Anna and Chibi from previous scene. Chibi looks sleepy, rubbing her eyes. Voice Consistency: Same soft Anna voice and sleepy Chibi voice. Phase 1 (0-2s): Anna smiles as Chibi starts to close her eyes, says: "Ôi, con buồn ngủ quá rồi, hành động này gọi là gì nào?"; Phase 2 (3-6s): Chibi covers her mouth and lets out a big, adorable yawn, says: "Yawn! I yawn"; Phase 3 (7-8s): Anna strokes Chibi's hair, says: "Buồn ngủ lắm rồi đây!"; no text, no subtitles, no logos, no watermark.
```
**Cảnh 3 — Tắt đèn (verb: TURN OFF):**
```
3D Pixar style, same characters Anna and Chibi. Chibi reaches her small hand toward a bedside lamp. Voice Consistency: Consistent voices. Phase 1 (0-2s): Anna points to the lamp switch, says: "Để chuẩn bị đi ngủ, mình làm gì với đèn con nhỉ?"; Phase 2 (3-6s): Chibi pushes the button, the room light dims to a soft glow, says: "Turn off! I turn off the light"; Phase 3 (7-8s): Anna settles Chibi down, says: "Chúc con ngủ ngon!"; no text, no subtitles, no logos, no watermark.
```
**Cảnh 4 — Đắp chăn (verb: TUCK IN):**
```
3D Pixar style, same characters Anna and Chibi. Chibi is lying down on a soft pillow. Voice Consistency: Consistent voices. Phase 1 (0-2s): Anna pulls a fluffy blanket up to Chibi's chin, says: "Kéo chăn ấm cho con ngủ ngon gọi là gì?"; Phase 2 (3-6s): Anna tucks the edges of the blanket neatly around Chibi, says: "Tuck in! Mom tucks me in"; Phase 3 (7-8s): Chibi snuggles deeper into the blanket, says: "Ấm quá mẹ ơi!"; no text, no subtitles, no logos, no watermark.
```
**Cảnh 5 — Hôn chúc ngủ ngon (verb: KISS):**
```
3D Pixar style, same characters Anna and Chibi. The room is quiet and peaceful with soft moonlight through the window. Voice Consistency: Consistent voices. Phase 1 (0-2s): Anna leans down close to Chibi's face, says: "Hôn con một cái thật kêu gọi là gì nào?"; Phase 2 (3-6s): Anna kisses Chibi gently on the forehead, says: "Kiss! A goodnight kiss"; Phase 3 (7-8s): Chibi closes her eyes with a happy smile, says: "Con yêu mẹ!"; no text, no subtitles, no logos, no watermark.
```
> **Kỹ thuật:** mỗi phase chỉ **1 hành động**; nếu tab ghi `(mood)` ngay sau câu thoại (như chủ đề Vẽ tranh/Làm bánh) thì **giữ nguyên** `says: "... (mood)"` — đó là chỉ dẫn cảm xúc cho giọng. Cảnh 1 mỗi chủ đề đặt đầy đủ mô tả cast (làm ảnh gốc); cảnh 2-5 dùng `same characters ... from image_0.png` / `from previous scene`. Đủ 20 chủ đề trong tab, pipeline chọn 1 chủ đề → 5 cảnh.

## 5. GHÉP & XUẤT  (BƯỚC 3 — assemble/Studio/export)
- Ghép **5 clip 8s** theo đúng thứ tự cảnh của chủ đề → 1 video song ngữ ~35-45s. Cắt gọn đầu/cuối theo nhịp, hard-cut mượt (mạch câu chuyện liền).
- **KHÔNG burn chữ khi gen:** tab chốt `no text, no subtitles, no logos, no watermark` trong mọi prompt (tránh AI vẽ chữ sai). Nếu cần **phụ đề song ngữ / tên động từ**, thêm ở **khâu dựng** (overlay ngoài, safe-zone 9:16 TikTok 900×1492), không phải trong lúc sinh video.
- Audio: giữ **giọng song ngữ** từ clip (Anna VN + Chibi keyword EN) đồng nhất; thêm **nhạc nền thiếu nhi nhẹ** không lấn giọng; chuẩn −14 LUFS.
- **Gate chất lượng** (docs/aff-engine.md §7, §10): giữ nét 3D Pixar, màu ấm tươi, mặt bé **không morph** giữa các cảnh (kiểm identity), grain 0-5% (animation không cần grain nặng).
- **Disclosure** cạnh CTA (AI-generated + hoa hồng). Export 1080p/4K, 9:16.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen — LƯU Ý: KHÔNG loại 3D/cartoon vì đây LÀ 3D Pixar):** `text, subtitles, captions, logos, watermark, morphing faces, inconsistent character design, distorted hands, extra fingers, extra people, flickering, blurry, creepy uncanny faces, dark scary mood`.
- **DO:** giữ **cast cố định Anna + Chibi** y hệt qua 5 cảnh (dùng `same characters from image_0.png`); đúng **3 phase 0-2s/3-6s/7-8s**, mỗi phase 1 `says:` + `(mood)`; **1 động từ EN/clip diễn bằng hành động**; luôn kèm `Voice Consistency`; luôn đóng đuôi `no text, no subtitles, no logos, no watermark`.
- **DON'T:** đừng ép "photorealistic/8K realism/lỗ chân lông" (hỏng nét Pixar, mặt uncanny); đừng nhồi nhiều hành động trong 1 phase (méo); đừng đổi giọng/tính cách Anna-Chibi giữa chừng; đừng để clip tự sinh chữ (luôn `no text`); đừng đổi trang phục/tóc cast giữa các cảnh cùng chủ đề.

## 7. METADATA
- **Title** <70 ký tự: chủ đề + động từ (vd "Bé Chibi học từ 'Water' khi tưới cây 🌱 | Tiếng Anh mẹ bé").
- **Caption + 15-25 hashtag** ngách mẹ&bé/edu (#tienganhmebe #daybehoc #songngu #mevabe #kidsenglish #anna_chibi #tiktokshop #{chủ_đề}).
- **CTA:** "Đồ chơi & học liệu cho bé — link giỏ hàng màu vàng / bio" + **disclosure** "video có yếu tố AI · mình nhận hoa hồng qua link".
