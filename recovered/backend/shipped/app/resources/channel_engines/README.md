# Channel Engines — "Bộ não AI" cho từng kiểu kênh YouTube

> Mỗi file trong thư mục này là **một "channel engine"** = một system-prompt hoàn chỉnh dạy AI cách *nghĩ ý tưởng → viết kịch bản → sinh prompt ảnh cho Google Flow → viết metadata YouTube* theo đúng DNA của một **ngách (niche) + phong cách hình ảnh** cụ thể.
>
> Đây là tài sản **quyết định chất lượng** của tính năng **AI Studio** (xem [ai-studio-automation-plan-v2.2.md](../ai-studio-automation-plan-v2.2.md)). Khi user tạo **profile kênh**, họ chọn 1 engine ở đây làm "bộ não"; engine đó được nạp làm system prompt cho `ideation_service` (Idea Chain) và step `script` / `storyboard` / `flow_generate`.

## 1. Engine plug vào đâu trong app

```
Tạo profile kênh ──► chọn 1 Channel Engine (file .md này)
        │
        ▼
frontmatter  ──► fields máy-đọc (style_anchor, style_lock, palette, aspect, voice…)
                 → nạp nhanh vào ScheduleConfig.channel_profile + config Flow/TTS
body (system prompt) ──► nạp vào make_primary_client() cho:
   • Idea Chain   (Stage 1 — sinh ý tưởng theo Viral Topic Angles của ngách)
   • step `script`   (Stage 2 — viết kịch bản đúng Script DNA)
   • step `storyboard`+`flow_generate` (Stage 3 — sinh image prompt đúng Visual Style DNA)
   • metadata     (Stage 4 — title/description/tags)
```

> **Khác với prompt H2DEV gốc (chạy thủ công trong ChatGPT, chờ user reply từng stage):** trong app, 4 stage được pipeline tự chạy nối tiếp (preset `ai_studio_full`). Phần "wait for user reply / download file / paste timestamp" ở prompt gốc → thay bằng *bước duyệt trên Dashboard/Telegram* và *truyền dữ liệu giữa các step qua DB*, KHÔNG hỏi lại user giữa chừng. Body engine vẫn giữ đủ 4 stage để: (a) chạy được standalone trong ChatGPT/Gemini nếu cần, (b) làm nguồn chân lý cho từng step trích đúng phần của mình.

## 2. Cấu trúc chuẩn của MỖI engine (skeleton — bắt buộc giống nhau)

Mọi file engine PHẢI theo đúng khung này (xem [_TEMPLATE.md](_TEMPLATE.md) và bản mẫu [01-ancient-humans-doodle.md](01-ancient-humans-doodle.md)):

```
--- (YAML frontmatter: id, name, niche, style_anchor, style_lock, palette, voice, aspect…) ---

# <Tên engine>

## CHANNEL KNOWLEDGE BASE (Pre-loaded — Do Not Ask Again)
   ### CONTENT & SCRIPT DNA      (niche, format, hook formula, rhythm, narrative arc, evidence rule)
   ### PROVEN VIRAL TOPIC ANGLES (5–7 mẫu tiêu đề viral của ngách)
   ### VISUAL STYLE DNA          (art style, nhân vật/chủ thể, background theo cảm xúc, on-screen text,
                                  signature devices, color palette hex, aspect ratio)

## STAGE 1 — GENERATE 5 VIRAL TOPIC IDEAS        (bảng 5 ý tưởng)
## STAGE 2 — GENERATE FULL NARRATION SCRIPT      (rule độ dài/giọng/nhịp/evidence/hook/ending)
## STAGE 3 — GENERATE IMAGE PROMPTS PER TIMESTAMP (style anchor đầu + style lock cuối + batching 20)
## STAGE 4 — GENERATE FINAL VIRAL METADATA       (title <70 ký tự, description+hashtags, tags)

## OPERATOR RULES (Always Active)
```

**Nguyên tắc bất biến (mọi engine đều có):**
- **Visual Style DNA + style-lock + character string** = nguồn chân lý duy nhất; MỌI image prompt ở Stage 3 phải kế thừa → cả kênh đồng nhất một phong cách (đây là cơ chế lõi của thể loại này).
- **Style anchor** mở đầu mỗi prompt ảnh; **style lock (negative phrasing)** đóng cuối — vì Google Flow/Imagen **không có ô negative**, exclusions phải viết dạng khẳng định ("flat 2D, no photographic texture").
- **Aspect ratio set trong UI Flow** (16:9 / 9:16), KHÔNG dùng cờ `--ar` (đó là cú pháp Midjourney).
- **Consistent character:** giữ một chuỗi mô tả nhân vật cố định + tạo 1 ảnh "character reference" làm *ingredient* trong Flow (tối đa 3 ref, đặt ảnh định-danh-mạnh-nhất đầu tiên).
- **Evidence/uy tín:** ngách kiến thức phải chèn nguồn/người/sự kiện CÓ THẬT (không bịa tên).

## 3. Catalog engine (mỗi dòng = 1 option khi tạo profile kênh)

| File | Ngách | Phong cách hình ảnh | Giọng/POV |
|---|---|---|---|
| [01-ancient-humans-doodle.md](01-ancient-humans-doodle.md) | Người cổ đại / tiền sử / tiến hoá | Doodle 2D vẽ tay | Ngôi 2, calm |
| [02-true-crime-cinematic.md](02-true-crime-cinematic.md) | True crime / điều tra / bí ẩn | Điện ảnh tả thực (reenactment) | Kể chuyện căng thẳng |
| [03-scary-horror-stories.md](03-scary-horror-stories.md) | Truyện kinh dị / nosleep | Minh hoạ horror tối, hạt phim | Thì thầm, rùng rợn |
| [04-space-cosmos-science.md](04-space-cosmos-science.md) | Vũ trụ / thiên văn / khoa học | Ảnh vũ trụ tả thực (JWST) | Trầm hùng, kỳ vĩ |
| [05-stoicism-philosophy.md](05-stoicism-philosophy.md) | Stoicism / triết học / động lực | Điện ảnh + tượng cổ, low-key | Ngôi 2, uy nghiêm |
| [06-personal-finance-money.md](06-personal-finance-money.md) | Tài chính cá nhân / tiền bạc | Editorial 2D nhân vật cao cấp | Rõ ràng, thực dụng |
| [07-fun-facts-listicle.md](07-fun-facts-listicle.md) | Sự thật thú vị / top-list | Vector phẳng / doodle vui | Nhanh, năng lượng cao |
| [08-mythology-folklore.md](08-mythology-folklore.md) | Thần thoại / dân gian | Tranh sơn dầu sử thi | Kể sử thi, trang trọng |
| [09-war-military-history.md](09-war-military-history.md) | Lịch sử quân sự / chiến tranh | Tư liệu vintage / điện ảnh | Tư liệu, nghiêm |
| [10-psychology-your-mind.md](10-psychology-your-mind.md) | Tâm lý học / não bộ / hành vi | Doodle / flat giải thích | Ngôi 2, thân mật |
| [11-sleep-bedtime-stories.md](11-sleep-bedtime-stories.md) | Truyện ngủ / thư giãn | Màu nước mơ màng, pastel | Rất chậm, êm |
| [12-kids-fairy-tales.md](12-kids-fairy-tales.md) | Truyện cổ tích trẻ em | Storybook màu nước / 3D mềm | Ấm áp, kể chuyện |
| [13-tech-ai-future.md](13-tech-ai-future.md) | Công nghệ / AI / tương lai | 3D sạch / futuristic phẳng | Sắc bén, hiện đại |
| [14-bible-faith-stories.md](14-bible-faith-stories.md) | Kinh thánh / đức tin | Sơn dầu điện ảnh, ánh sáng thần | Trầm ấm, thành kính |
| [25-doi-song-2d-vector.md](25-doi-song-2d-vector.md) | Đời sống / tiền bạc / xã hội | Editorial 2D điện ảnh có host | Ấm, dí dỏm, thẳng |
| [26-cinematic-human-stories.md](26-cinematic-human-stories.md) | Chuyện người thật / nghề nghiệp | Documentary 35mm tự nhiên | Ấm, quan sát, tiết chế |
| [27-premium-3d-explainer.md](27-premium-3d-explainer.md) | Business / hệ thống / công nghệ | Isometric 3D editorial | Sắc gọn, phân tích |
| [28-medical-body-3d.md](28-medical-body-3d.md) | Sức khoẻ / cơ thể / fitness | Medical CGI chính xác | Bình tĩnh, khoa học |
| [29-food-travel-culture-cinematic.md](29-food-travel-culture-cinematic.md) | Ẩm thực / du lịch / văn hoá | Documentary cảm quan | Gần gũi, giàu cảm giác |
| [30-product-brand-film.md](30-product-brand-film.md) | Sản phẩm / thương hiệu / chế tạo | Commercial macro premium | Tinh gọn, kỹ thuật |
| [31-geopolitics-map-desk.md](31-geopolitics-map-desk.md) | Địa chính trị / thương mại / logistics | Editorial map desk | Trung lập, sắc, điềm tĩnh |
| [32-education-language-visual-lab.md](32-education-language-visual-lab.md) | Dạy học / tiếng Anh / ngoại ngữ / kiến thức | Cinematic visual learning lab | Rõ, khích lệ, hội thoại |

> **49 (Vox Collage) không còn ở bundle này** — đã gỡ sang server-only cùng đợt với 33–50, xem [`admin/resources/channel_engines/49-vox-paper-collage-explainer.md`](../../../../admin/resources/channel_engines/49-vox-paper-collage-explainer.md).

> **49 khác mọi engine còn lại ở một điểm: THEME CLAUSE.** Cơ học giấy cắt dán (mép xé, băng dính,
> halftone, nền phẳng) là phần BẤT BIẾN nên nằm trong `style_anchor`/`style_lock`; còn palette + kiểu
> chữ + finish + mức năng lượng chuyển động là **10 theme** (american-retro, punk-zine,
> newsprint-editorial, gilded-deco…) — Stage 3 chọn ĐÚNG MỘT theme mỗi video rồi lặp nguyên văn câu
> đó ở mọi prompt. Một cỗ máy, nhiều diện mạo, thay vì 10 file engine gần trùng nhau. Engine dùng
> chung cho cả 16:9 và 9:16 (Stage 3 có khối bố cục dọc riêng). Xem
> [`docs/plan-engine-vox-paper-collage.md`](../../../../docs/plan-engine-vox-paper-collage.md).

> Danh sách mở rộng được: thêm engine mới = thêm 1 file theo `_TEMPLATE.md`, thêm 1 dòng vào bảng này. Gợi ý mở rộng tương lai: geography/comparison (infographic bản đồ), mythbusting/khoa học thường thức, lịch sử nghệ thuật, ẩm thực, true-history "weird facts", ASMR.

### 3b. PREMIUM PACK — `premium-us-midlife` (33–47, khoá theo entitlement)

15 engine nhắm **khán giả Mỹ 40–60**, RPM cao, viết **100% tiếng Anh** (kể cả `name`/`niches`) vì output phục vụ view ngoại. Khác pack thường ở 4 điểm: `prompt_grammar: v2` (grammar 12 trường + anti-AI-look), `anonymity_lock`/`likeness_lock`, `format_variation_min` (chống "mass-produced"), và evidence rule cứng theo từng ngách.

> ⚠️ **33–50 KHÔNG còn nằm trong bundle backend** (`app/resources/channel_engines/`) — đã gỡ khỏi đây, chỉ còn ở [`admin/resources/channel_engines/`](../../../../admin/resources/channel_engines/) (nguồn `prisma/seed.ts` đẩy lên DB). App desktop nhận các engine này qua `GET /api/desktop/engines` → `POST /internal/engines` → `apply_server_overlay` theo entitlement (tier), không phải từ file cục bộ nữa — máy chưa đăng nhập gói hợp lệ sẽ không có "bộ não" các engine này. Link cột File bên dưới trỏ sang thư mục admin.

| File (ở `admin/resources/channel_engines/`) | Ngách | RPM band | Khoá đặc thù |
|---|---|---|---|
| [33-cold-case-dossier.md](../../../../admin/resources/channel_engines/33-cold-case-dossier.md) | Hồ sơ vụ án nguội (cold case) | high | factual · anonymity |
| [34-courtroom-verdict-drama.md](../../../../admin/resources/channel_engines/34-courtroom-verdict-drama.md) | Drama crime / phiên toà | top | chỉ vụ đã xử xong · anonymity |
| [35-fraud-exposed-files.md](../../../../admin/resources/channel_engines/35-fraud-exposed-files.md) | Lừa đảo & bóc trần dòng tiền | top | cấm hướng dẫn thao tác lừa đảo |
| [36-memory-lane-americana.md](../../../../admin/resources/channel_engines/36-memory-lane-americana.md) | Hồi tưởng Americana 1955–1989 | mid | `era_lock` · mọi giá/số phải có nguồn |
| [37-where-are-they-now.md](../../../../admin/resources/channel_engines/37-where-are-they-now.md) | What happened to / Old Hollywood | mid | **likeness lock** (cấm sinh mặt người thật) |
| [38-retirement-money-after-50.md](../../../../admin/resources/channel_engines/38-retirement-money-after-50.md) | Tiền bạc sau tuổi 50 | top | YMYL · cấm khuyên cá nhân |
| [39-family-secrets-drama.md](../../../../admin/resources/channel_engines/39-family-secrets-drama.md) | Bí mật gia đình / thừa kế | mid | dramatized + bắt buộc disclosure |
| [40-declassified-history.md](../../../../admin/resources/channel_engines/40-declassified-history.md) | Hồ sơ giải mật / Chiến tranh Lạnh | high | cấm conspiracy framing |
| [41-medical-mystery-after-50.md](../../../../admin/resources/channel_engines/41-medical-mystery-after-50.md) | Bí ẩn y khoa & sức khoẻ 50+ | high | YMYL nặng · cấm chẩn đoán/kê đơn |
| [42-faith-second-chances.md](../../../../admin/resources/channel_engines/42-faith-second-chances.md) | Đức tin & cơ hội thứ hai | mid | phi giáo phái · cấm miracle claim |
| [43-air-disaster-investigation.md](../../../../admin/resources/channel_engines/43-air-disaster-investigation.md) | Điều tra tai nạn hàng không/hàng hải | high | cấm hình ảnh nạn nhân · livery-free |
| [44-business-empire-collapse.md](../../../../admin/resources/channel_engines/44-business-empire-collapse.md) | Doanh nghiệp thịnh–suy | high | cấm logo thương hiệu trong ảnh |
| [45-ai-and-your-money.md](../../../../admin/resources/channel_engines/45-ai-and-your-money.md) | AI & công việc/tiền bạc | top | cấm hình sci-fi (robot/não phát sáng) |
| [46-real-estate-relocation.md](../../../../admin/resources/channel_engines/46-real-estate-relocation.md) | Nhà ở, chi phí sống & chuyển vùng | top | YMYL · cấm dự báo giá |
| [47-survival-grid-down.md](../../../../admin/resources/channel_engines/47-survival-grid-down.md) | Sinh tồn & mất điện diện rộng | mid | cấm vũ khí/tactical/doomsday |
| [48-news-real-life-consequences.md](../../../../admin/resources/channel_engines/48-news-real-life-consequences.md) | **Story từ bài báo** (gắn feat/News) | high | `transformation_lock` + likeness lock + cấm logo |

> **48 khác 33–47 ở 2 điểm:** (a) nguồn là **bài báo** do `news_import_service` crawl về, nên engine bắt buộc **transformation test** — cấm đọc/tóm tắt lại bài, phải thêm ≥3 thứ bài báo không có (cơ chế pháp lý/tài chính được giải thích, chronology dựng lại, chi phí lượng hoá, hậu quả kéo dài sau bài); (b) pipeline chèn **ảnh thật từ bài báo** xen ảnh AI, nên visual style cố tình **trung tính kiểu phóng sự** — cấm màu phim, cấm teal-orange, cấm bokeh điện ảnh, để khung AI đứng cạnh ảnh thật không lộ.

Chi tiết kiến trúc, gating theo tier và QC gate: [`docs/plan-premium-cinematic-engine-pack.md`](../../../../docs/plan-premium-cinematic-engine-pack.md).

### 3c. JP SERVER-ONLY PACK (50–51) — engine nhắm khán giả Nhật, chỉ Team

| File (ở `admin/resources/channel_engines/`) | Ngách | Ngôn ngữ | Phong cách hình ảnh | Khoá |
|---|---|---|---|---|
| [50-japan-corporate-decisions.md](../../../../admin/resources/channel_engines/50-japan-corporate-decisions.md) | 日本企業の決断史 — doanh nghiệp Nhật thịnh–suy qua 1 quyết định kinh doanh, đối chiếu 有価証券報告書 | `ja` | Business-editorial 2D illustration (không phải ảnh thật, không phải manga/webtoon) | `team` |
| [51-japan-senior-health.md](../../../../admin/resources/channel_engines/51-japan-senior-health.md) | 健康長寿ラボ — sức khỏe tổng hợp cho người Nhật 40-70 tuổi (dấu hiệu cơ thể, thói quen, phòng lão hoá, giấc ngủ, ăn uống, phòng bệnh) | `ja` | Warm 2D editorial illustration đời thường + sơ đồ cơ thể tối giản (không 3D y khoa, không photoreal, không kiểu yukkuri/mascot) | `team` |

Khác các engine ở mục 3 (bundle) ở 3 điểm: (a) `language: ja`, thân bài viết bằng tiếng Anh nhưng output (tiêu đề, kịch bản, metadata) bắt buộc tiếng Nhật — riêng Stage 3 (prompt ảnh) luôn tiếng Anh cho model ảnh; (b) mỗi engine đi kèm 1 **master prompt viết kịch bản riêng, 100% tiếng Nhật** ở `master_prompts/` (`50-japan-corporate-decisions.master.md`, `51-japan-senior-health.master.md`) — cố ý lệch quy ước "master prompt tiếng Anh" của skill `channel-master-prompt` vì phần văn phong/âm đọc (です・ます調, cách đọc số, nhịp câu tiếng Nhật) chỉ chính xác khi viết thẳng bằng tiếng Nhật; (c) **server-only ngay từ đầu, cả 2 khoá `min_tier: team`/`allowed_tiers: [team]`** — chỉ tài khoản Team thấy được, chặt hơn cả nhóm 33–48 (đang khoá `max`+`team`).

**51 (health) là engine YMYL rủi ro cao nhất repo** — sức khỏe là nhóm YouTube soi kỹ nhất, và đúng khán giả (người Nhật 60+) đang là mục tiêu của làn sóng kênh "bác sĩ AI giả" bị YouTube truy quét 2026. Rào chắn cứng: **không nhân vật/host nào được đóng vai bác sĩ/y tá/chuyên gia** (không áo blouse trắng, không ống nghe, không bối cảnh phòng khám), mọi claim y tế phải bám nguồn công khai (MHLW, e-ヘルスネット, nghiên cứu bình duyệt), cấm chẩn đoán/kê đơn/claim chữa khỏi, disclaimer bắt buộc mỗi video. Xem nghiên cứu + quyết định đã chốt: [`docs/plan-engine-japan-corporate-decisions.md`](../../../../docs/plan-engine-japan-corporate-decisions.md) (50) và [`docs/plan-engine-japan-senior-health.md`](../../../../docs/plan-engine-japan-senior-health.md) (51).

### 3d. GLOBAL 2D MARKET PACK (52–56) — 1 "key" đáng làm nhất mỗi thị trường, chỉ Team

| File (ở `admin/resources/channel_engines/`) | Thị trường | Ngách | Ngôn ngữ | Phong cách hình ảnh |
|---|---|---|---|---|
| [52-us-revenge-storytime.md](../../../../admin/resources/channel_engines/52-us-revenge-storytime.md) | 🇺🇸 US | Malicious compliance / petty revenge storytime (hư cấu, dán nhãn) | `en` | Flat 2D vector storytime, nét viền dày, biểu cảm cường điệu |
| [53-france-true-crime-illustre.md](../../../../admin/resources/channel_engines/53-france-true-crime-illustre.md) | 🇫🇷 Pháp | True crime / faits divers có dossier thật, presomption d'innocence nghiêm ngặt | `fr` | Noir editorial illustration kiểu tạp chí "Détective" cổ điển |
| [54-es-misterio-paranormal.md](../../../../admin/resources/channel_engines/54-es-misterio-paranormal.md) | 🇪🇸 Tây Ban Nha | Misterio/paranormal — **motor DUAL** (MODO LEYENDA nhẹ fact-gate vs MODO SUCESO DOCUMENTADO nặng fact-gate) | `es` | Minh hoạ khí quyển tối + texture "terror analógico" (VHS/scan-line) |
| [55-kr-life-reversal-drama.md](../../../../admin/resources/channel_engines/55-kr-life-reversal-drama.md) | 🇰🇷 Hàn Quốc | 인생반전사연 — đảo ngược số phận, "사이다" comeuppance (hư cấu, dán nhãn) | `ko` | Webtoon Hàn hiện đại sạch (không phải "커뮤체") |
| [56-japan-sukatto-comeuppance.md](../../../../admin/resources/channel_engines/56-japan-sukatto-comeuppance.md) | 🇯🇵 Nhật Bản | スカッとする話 — trả đũa sảng khoái (hư cấu, dán nhãn) | `ja` | Manga panel-style, tương phản biểu cảm mạnh "trước/sau" |

Cả 5 đều **server-only ngay từ đầu**, `min_tier: team`/`allowed_tiers: [team]`, và đều có **master prompt riêng đầy đủ 26 mục** ở `master_prompts/52..56-*.master.md` (viết bằng đúng ngôn ngữ output của từng kênh, không phải tiếng Anh).

**Rủi ro kiếm tiền đã research kỹ trước khi build (52/55/56 — nhóm "storytime hư cấu"):** đợt truy quét 1/2026 của YouTube xoá 11 kênh/35 triệu sub, nêu đích danh 2 kiểu chết — (a) sản xuất hàng loạt giống khuôn không có tiếng nói riêng, (b) kể chuyện hư cấu nhưng nguỵ trang như chuyện thật. Hoạt hình 2D rõ ràng không tả thực được MIỄN dán nhãn "synthetic content" của chính sách 2026 (chỉ bắt dán nhãn nội dung dễ gây nhầm là cảnh quay thật). → cả 3 engine đều ghim cứng: `dramatized: true` + disclosure, cấm lấy cốt truyện verbatim từ Reddit/2ch/커뮤니티, bắt buộc `format_variation_min`, nhân vật là archetype gốc không mô phỏng IP có bản quyền.

**53 (Pháp) và 54 (Tây Ban Nha)** giữ kỷ luật factual y hệt engine 33/50 vì đụng tới sự việc/con người thật — 53 nhấn mạnh riêng nguyên tắc "présomption d'innocence" (luật Pháp); 54 phải tự phân loại đúng chế độ tin cậy (huyền thoại vs sự việc có thật) trước khi viết, không được trộn 2 mức mà không nói rõ.

Xem nghiên cứu + phong cách hình ảnh từng thị trường: [`docs/plan-engine-global-2d-market-pack.md`](../../../../docs/plan-engine-global-2d-market-pack.md).

## 4. Quy ước file
- Tên: `NN-slug.md` (NN số thứ tự 2 chữ số). `_TEMPLATE.md` = khung trống.
- Frontmatter YAML chuẩn (giống mọi file) cho backend parse nhanh.
- Body = system prompt tiếng Anh (vì script/prompt/metadata đầu ra tiếng Anh; engine vẫn có thể override `language` ở frontmatter cho kênh tiếng Việt/tiếng Nhật — xem 25/26 cho ví dụ thân bài tiếng Việt, 50 cho ví dụ thân bài tiếng Anh nhưng output tiếng Nhật).
