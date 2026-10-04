---
id: engagement-wealth-mascot
name: "Tăng FL TikTok — Linh vật/Phật/Thần Tài rải vàng (engagement)"
archetype: C
video_type: "mascot-wealth"
niche_default: "Nuôi follower quanh account aff — linh vật vàng/Phật/Thần Tài, spectacle tài lộc, ghép nhạc trend"
niches:
  - label: "Linh vật tài lộc"
    fits: "rồng/phượng/hổ/lân... phủ vàng-kim cương tiến tới người xem rồi phun tiền xu"
  - label: "Đức Phật dạy"
    fits: "Phật đi/thiền, hào quang hóa giải yêu ma thành sen — kênh tâm linh/an yên"
  - label: "Thần Tài — Thổ Địa"
    fits: "Thần Tài/Thổ Địa giáng từ mây vàng ban lộc — kênh phong thủy/Tết/buôn bán"
platform: "generic"
language: vi
aspect_ratio: "9:16"
clip_length: "2-3s"
final_length: "15-30s"
persona_scope: none
faceless: true
design_lock: false
recurring_character: "Linh vật/Thần (rồng vàng, phượng, Phật, Thần Tài, Thổ Địa) — nhân vật hoạt hình/mascot, KHÔNG persona người thật, KHÔNG sản phẩm"
scene_structure: "Mỗi clip 1 one-shot điện ảnh 2-3s (linh vật tiến tới → phun/rải tiền xu · Phật đi/thiền → hào quang hóa giải · Thần Tài giáng mây vàng rải lộc). Tạo HÀNG LOẠT clip → tăng tốc, cắt bớt → ghép 5-10 clip → RIP nhạc trend TikTok chồng lên."
camera_sequence: [CINEMATIC_ONE_SHOT_LOCKED]
motion_presets: [mascot_wealth]
dialogue_mode: ambient
voice: ambient
image_style_anchor: "cinematic one-shot, stylized 3D render, gold-and-gemstone material, volumetric divine light, vertical 9:16,"
image_style_lock: "Cinematic one-shot, 9:16, Ambient sound only."
golden_rules: ["1 linh vật/thần duy nhất/clip, tiến TỚI người xem", "vàng-kim cương phủ khắp + hào quang", "kết bằng burst/rain tiền xu (hoặc hào quang hóa giải với dạng Phật)", "giữ đúng đuôi câu 'Cinematic one-shot, 9:16, Ambient sound only.'"]
lighting_default: "warm divine glow + volumetric god-rays, rim light tách khối linh vật khỏi nền kho báu"
color_look: "warm gold-rich fantasy grade, glowing highlights, deep treasure shadows"
lut_intensity: 55
lens_default: "cinematic wide-to-medium, subject tiến tới camera, shallow-ish DoF nền bokeh"
camera_angle_default: "hero low-angle nhìn lên linh vật/thần (uy nghi); Phật eye-level tĩnh tại"
background_default: "hành lang cung điện/kho báu phát sáng · hang núi nứt ánh vàng · mây vàng thần thánh · rừng sương / gốc bồ đề (dạng Phật)"
skin_realism: "n/a — mascot/linh vật hoạt hình 3D, không phải người thật"
negative_constant: "morphing shape, extra limbs, flickering, distortion, compression artifacts, inconsistent lighting, watermark, text overlay, human product, logo"
motion_strength: "moderate"
reference_workflow: "keyframe linh vật/thần 9:16 (Nano Banana/Flow/Meta) → image-to-video one-shot 2-3s (Veo/Kling) mỗi prompt → gen HÀNG LOẠT → tăng tốc/cắt → ghép 5-10 → rip nhạc trend"
post_chain: "gen loạt → speed-up (mỗi clip lấy 2-3s) → ghép 5-10 clip hard-cut theo beat → RIP audio trend TikTok chồng lên → export 9:16"
quality_knobs: [lighting_mood, color_look, lut_intensity, camera_angle, subject_type, coin_burst_style, pacing, audio_trend]
recommended_image_tool: "Nano Banana (Gemini) 2K 9:16 / Google Flow / Meta AI"
recommended_video_tool: "Veo 3.1 (image-to-video one-shot) / Kling 2.5-2.6 Cinematic"
tts_mood: "không thoại — RIP âm thanh trend TikTok"
music_mood: "âm thanh trích từ video Linh vật/Phật/Thần Tài nhiều view trên TikTok"
tags: [tang-follower, tiktok, linh-vat, than-tai, tho-dia, phat-day, tai-loc, rai-vang, engagement, faceless, nuoi-account, aff]
---

# AFF Engine — Tăng FL TikTok · Linh vật / Phật / Thần Tài rải vàng

> **Kiểu:** C (engagement / nuôi follower — KHÔNG review sản phẩm trực tiếp) · **Dùng khi:** cần **nuôi follower quanh account affiliate** bằng spectacle thị giác tài lộc/tâm linh, để account có tương tác trước khi gắn link. Cảm giác viral: linh vật vàng uy nghi tiến tới phun tiền xu / Phật hóa giải yêu ma thành sen / Thần Tài giáng mây vàng ban lộc — dễ share, dễ lưu, hợp nhạc trend.
> Input: KHÔNG cần `{SẢN_PHẨM}` / `{PERSONA}` — engine tự chọn linh vật/thần từ menu prompt bên dưới. Chỉ chọn **sub-genre** + **nhạc trend** để rip.

## 1. TỔNG QUAN & CẤU TRÚC PHÂN CẢNH
- **3 sub-genre (verbatim từ tab):**
  1. **DẠNG LINH VẬT** — linh vật/con vật (rồng, phượng, hổ, lân, voi, rùa vàng...) phủ vàng & kim cương **đi/bay tiến tới người xem** rồi **thở/phun/rải cơn mưa tiền xu**. Bước 1: copy câu lệnh để tạo Video. Bước 2: **Trích xuất âm thanh** của video nhiều view trên TikTok để ghép vào video ở bước 1.
  2. **DẠNG ĐỨC PHẬT DẠY** — Phật đi chân trần/ngồi thiền, **hào quang tỏa ra hóa giải yêu ma/bóng tối thành hoa sen / ánh sáng**. Bước 1 (verbatim): *"tạo hàng loạt rồi ghép 5-10 video thành 1 video, tăng tốc độ, cắt bớt, mỗi video chỉ lấy 2-3s"*. Bước 2: lấy video về Phật dạy nhiều view trên TikTok, **trích xuất lấy âm thanh** ghép vào video đã tạo ở bước 1.
  3. **THẦN TÀI — THỔ ĐỊA** — Thần Tài/Thổ Địa **giáng từ mây vàng**, rải/ban tiền xu & lộc trên nền đền chùa/chợ cổ/đồng quê phát sáng.
- **Workflow lõi (verbatim):** *tạo hàng loạt rồi ghép 5-10 video thành 1 video, tăng tốc độ, cắt bớt, mỗi video chỉ lấy 2-3s* → sau đó **RIP âm thanh trending TikTok** (trích xuất từ video nhiều view) chồng lên bản ghép.
- **Độ dài:** mỗi clip gốc là one-shot điện ảnh, khi ghép **chỉ lấy 2-3s/clip**; video cuối ~15-30s.
- **Có lộ mặt / persona / sản phẩm không:** KHÔNG — faceless hoàn toàn, nhân vật là linh vật/thần hoạt hình, không gắn sản phẩm vào khung hình.
- **Vì sao dạng này AI làm mượt:** mỗi clip là **1 one-shot ngắn (2-3s), 1 chuyển động** (tiến tới + 1 hành động phun/rải/hóa giải) → ít biến dạng; gen số lượng lớn rồi lọc clip đẹp.

## 2. MỤC ĐÍCH & HOOK  (engagement — KHÔNG phải bán hàng)
> Đây là engine **nuôi follower**, không phải review bán hàng. Không có Problem→Solution→giá. HOOK = **spectacle thị giác** ngay từ frame đầu.
- **Mục đích (account-farming):** nuôi tương tác/follower **quanh account affiliate** — account có nội dung viral tài lộc/tâm linh trước, để về sau gắn link aff/giới thiệu sản phẩm có sẵn tệp người theo dõi.
- **Hook (0-2s) = hình ảnh, không phải chữ:** linh vật vàng khổng lồ **lù lù tiến thẳng vào camera** / Phật mở mắt hào quang bùng sáng / Thần Tài rẽ mây vàng — burst tiền xu ngay giây đầu để giữ chân.
- **CTA (nhẹ/tùy chọn):** engagement nên CTA **mềm** — "Chúc bạn 2026 tiền vào như nước 🧧", "Lưu về lấy vía tài lộc", "Follow nhận lộc mỗi ngày". **Không** ép mua. Khi account đã lên tệp mới cân nhắc gắn link + disclosure ở caption.
- **Text overlay đặc trưng:** câu chúc tài lộc/an yên ngắn ("Lộc về tận cửa", "Bình an", "Vía Thần Tài") — đặt trong safe-zone, đừng che linh vật.

## 3. PROMPT ẢNH KEYFRAME  (BƯỚC 1 — Nano Banana / Flow / Meta)
Tạo keyframe linh vật/thần 9:16 làm frame đầu cho image-to-video. **Golden rules:** 1 linh vật/thần duy nhất, phủ vàng-kim cương/hào quang, hướng tiến tới camera, nền kho báu/mây vàng. Mở đầu bằng `image_style_anchor`, kết bằng `image_style_lock`.
> Lưu ý: engine này **được phép render 3D/stylized** (linh vật thần thoại) — KHÁC các engine người thật, nên negative **KHÔNG loại "3D render / CGI"** ở đây.
- **Ví dụ VERBATIM (rút từ menu motion của tab, dùng luôn làm mô tả keyframe):**
  ```
  cinematic one-shot, stylized 3D render, gold-and-gemstone material, volumetric divine light, vertical 9:16,
  A golden dragon covered in diamonds emerges from a glowing mountain crevice, scales shimmering under warm light,
  treasure-filled palace corridor background, hero low-angle looking up, glowing highlights, deep treasure shadows.
  Cinematic one-shot, 9:16, Ambient sound only.
  ```
  ```
  cinematic one-shot, stylized 3D render, gold-and-gemstone material, volumetric divine light, vertical 9:16,
  Thần Tài, the Vietnamese God of Wealth, emerging from a golden cloud holding a bag of coins,
  ancient temple background glowing with divine light.
  Cinematic one-shot, 9:16, Ambient sound only.
  ```
- **Nhân bản:** đổi linh vật/thần + bối cảnh (hang núi / hành lang cung điện / mây vàng), giữ nguyên công thức tiến-tới + burst tiền xu → ra hàng loạt keyframe để gen nhiều clip.

## 4. THƯ VIỆN PROMPT MOTION  (BƯỚC 2 — image-to-video, mỗi prompt = 1 clip one-shot 2-3s)
Luật: **1 camera-move + 1 action / clip** (tiến tới + phun/rải/hóa giải). Giữ NGUYÊN đuôi câu `Cinematic one-shot, 9:16, Ambient sound only.` (dạng Thần Tài dùng `ambient temple/natural sounds only`). Prompt là **tiếng Anh — chép NGUYÊN VĂN**.
> Đây là PHẦN LÕI — menu prompt verbatim từ tab. Gen HÀNG LOẠT, lọc clip đẹp, rồi ghép.

**Sub-genre 1 — MASCOT_APPROACH_EMIT_COINS (linh vật tiến tới → phun/rải tiền xu):**
```
Cinematic one-shot, 9:16 aspect ratio. A golden dragon covered in diamonds emerges from a glowing mountain crevice, walking majestically toward the viewer, its scales shimmering under warm light, then exhales a burst of golden coins that rain across the floor. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A radiant phoenix made of gold and rubies spreads its wings inside a treasure-filled palace hallway, gliding forward gracefully before releasing a shower of sparkling gold dust and coins. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A white tiger adorned with gold and diamonds strides powerfully through a corridor of glowing treasure, approaching the camera and roaring as golden coins spill from its mouth. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden lion with jewel-encrusted mane walks from a mountain crack toward the viewer, roaring proudly before releasing a brilliant burst of golden light and coins. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A majestic qilin covered in gemstones steps through golden mist from a cave, walking forward with grace, glowing brighter, and then breathing out a wave of gold coins. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A massive golden elephant draped in jewels walks through a glowing temple corridor, its trunk swinging forward as it sprays shining gold coins into the air. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A phoenix made of molten gold flies through a palace corridor lined with treasure, soaring toward the viewer and releasing a cascade of coins and glowing embers. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden bull with diamond horns emerges from a mountain cave, stomping the ground as it charges toward the viewer, gold coins erupting from beneath its hooves. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A glowing dragon horse of gold and jade gallops through a corridor filled with floating jewels, running toward the viewer as golden mist and coins burst around it. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden serpent slithers gracefully from a treasure pit, moving toward the camera and exhaling a glowing stream of coins that scatter across the ground. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A celestial deer with diamond antlers walks gently through a shining palace, approaching the viewer and glowing intensely before releasing a shower of golden coins. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A radiant peacock with golden and sapphire feathers struts proudly down a hall of treasure, spreading its tail and scattering coins toward the viewer. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A powerful dragon turtle glowing with emerald and gold climbs from a cave, walks toward the camera, and exhales shimmering coins into the air. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden fox with ruby eyes runs swiftly from a cave toward the viewer, its fur sparkling before it opens its mouth to release flying coins. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A phoenix of pure gold rises from a pile of treasure, flying toward the viewer as radiant light bursts from its wings along with streams of coins. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A mighty lion with sapphire eyes steps from a glowing mountain crack, walking slowly toward the camera and releasing coins with each breath. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A silver unicorn with a golden horn gallops through a golden palace corridor toward the viewer, glowing brighter and releasing coins in a spiral. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A white crane with golden feathers lands in a treasure hall, then walks toward the viewer and opens its beak to drop glittering gold coins. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden tortoise with diamond patterns on its shell crawls from a cave, glowing brightly and spitting out a stream of coins that roll toward the camera. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden stag with radiant antlers steps from a treasure-filled hallway, walking forward as golden dust swirls and coins spill from its mouth. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A dragon horse covered in flame-like gold patterns gallops through a glowing corridor toward the viewer, its mane scattering coins in the air. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden carp swims through air inside a palace corridor toward the viewer, leaving behind trails of light and coins. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden tiger with diamond stripes prowls toward the camera, growling as coins fall from its jaws. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A golden dragon rises from a mountain of treasure and flies toward the viewer, roaring as coins rain down from the sky. Ambient sound only.
```
> Menu đầy đủ tab còn ~25 biến thể nữa (rồng molten gold, kỳ lân jade, sư tử celestial, phượng ruby-flame, ngựa rồng, rùa rồng, cá chép hóa rồng...) — cùng công thức "linh vật vàng tiến tới → burst/rain coins". Gen loạt, lọc clip mượt nhất.

**Sub-genre 2 — BUDDHA_MEDITATE_WALK (Phật đi/thiền → hào quang hóa giải yêu ma thành sen):**
```
Cinematic one-shot, 9:16 aspect ratio. Gautama Buddha walks barefoot through a misty forest at dawn, sunlight breaking through the trees. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha sits beneath the Bodhi tree in deep meditation as golden leaves slowly fall. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Siddhartha leaves the palace under moonlight, stepping into a new life of renunciation. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha walks calmly along a riverbank, his reflection rippling on the surface. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha meditates in a mountain cave illuminated by a soft ray of light. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha sits cross-legged under heavy rain, unmoved, his calm presence radiating stillness. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. The Buddha meditates under the Bodhi tree as golden light spreads from his body. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha walks across a bridge over a calm lake covered in lotus flowers. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. A close-up shot of Buddha’s hands forming the meditation mudra as sunlight glows on them. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha sits on a lotus platform floating in calm water surrounded by mist. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Surrounded by ghostly dragons, Buddha raises his hand and they dissolve into beams of light. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha meditates as the ground cracks beneath him; golden energy heals the earth. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha’s aura grows as shadows flee from his presence, leaving the world in pure tranquility. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Amidst the chaos of hellish creatures, Buddha’s golden glow restores balance and silence. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Mara sends temptations and fears toward Buddha; his steady light dissolves them into emptiness. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha’s meditation radiates light that transforms a dark forest into a blooming paradise. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Surrounded by monstrous faces, Buddha’s compassion turns each into a smiling being. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha sits still as waves of darkness crash; each wave turns golden upon touching him. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Surrounded by dark illusions, Buddha’s compassion manifests as countless glowing lotuses. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha’s meditation under the Bodhi tree glows, scattering every demon in silence. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Mara’s illusions of beauty and fear vanish as Buddha opens his eyes in wisdom. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha walks through illusionary fire; every step leaves behind glowing lotus blooms. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha’s radiance transforms demons into falling lotus petals drifting in air. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Mara’s army turns to dust as Buddha’s golden light covers the land. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. Buddha’s meditation radiates golden peace, dissolving every trace of evil around him. Ambient sound only.
Cinematic one-shot, 9:16 aspect ratio. From darkness rises Buddha’s glow, transforming night into eternal dawn. Ambient sound only.
```
> Menu đầy đủ tab có ~90 prompt (Phật đi rừng tre/ruộng vàng/ven sông/bậc đền · thiền dưới bồ đề/hang/thác/mưa · và loạt "hóa giải yêu ma/bóng tối thành sen & ánh sáng"). Chọn 5-10 để ghép 1 video.

**Sub-genre 3 — DEITY_BLESS (Thần Tài / Thổ Địa giáng mây vàng → ban lộc/rải tiền xu):**
```
A cinematic one-shot of Thần Tài, the Vietnamese God of Wealth, emerging from a golden cloud holding a bag of coins, ancient temple background glowing with divine light, ambient temple sounds only.
A cinematic one-shot of Thổ Địa, the Earth God, smiling warmly beside a small altar filled with fruits and incense smoke swirling gently, peaceful countryside background, natural ambient sounds.
A cinematic one-shot of Thần Tài descending from the sky onto a busy ancient marketplace, showering gold coins as people bow with gratitude, soft wind and crowd ambiance only.
A cinematic one-shot of Thổ Địa sitting under a sacred banyan tree, holding a fan, watching over villagers farming, sunlight filtering through leaves, birds chirping softly.
A cinematic one-shot of Thần Tài appearing inside an old wooden shop, placing a golden ingot on the counter to bless the owner with prosperity, soft bell and wind chime sounds.
A cinematic one-shot of Thổ Địa and Thần Tài sitting side by side on a stone bench at sunset, exchanging smiles as incense smoke drifts around, calm ambient sound of evening.
A cinematic one-shot of Thần Tài walking across a golden bridge in the clouds, each step leaving shimmering trails of light, distant thunder and wind ambiance.
A cinematic one-shot of Thổ Địa emerging from the soil surrounded by blooming flowers, symbolizing his connection with the land, soft rustling leaves and earth sounds.
A cinematic one-shot of Thần Tài arriving at a villager’s home during Tết, blessing them with gold and luck, glowing lanterns around, festive background ambiance.
A cinematic one-shot of Thổ Địa guiding children planting trees near an ancient shrine, representing harmony with nature, peaceful countryside ambient sound.
A cinematic one-shot of Thần Tài transforming from a golden statue into a living deity in a temple full of light, candles flickering, faint temple bells echoing.
A cinematic one-shot of Thổ Địa walking through a green rice field at dawn, touching the crops that turn greener instantly, sound of morning breeze and insects.
A cinematic one-shot of Thần Tài riding on a golden dragon flying over a sea of clouds, spreading coins of fortune below, sound of wind and dragon roars in distance.
A cinematic one-shot of Thổ Địa standing before an ancient gate, his staff glowing as he blesses the land to stay fertile, echoing chants and natural wind sound.
A cinematic one-shot of Thần Tài and Thổ Địa appearing together in a glowing mist, exchanging golden ingots and smiling kindly toward the viewer, calm spiritual ambient sound.
```

## 5. GHÉP & XUẤT + RIP AUDIO TREND  (BƯỚC 3 — assemble/Studio/export)
- **Gen hàng loạt** clip theo menu §4 → lọc clip mượt (không morph, coin-burst đẹp).
- **Tăng tốc + cắt:** *tăng tốc độ, cắt bớt, mỗi video chỉ lấy 2-3s* → **ghép 5-10 clip** thành 1 video (hard-cut theo beat).
- **RIP âm thanh trend:** trích xuất **âm thanh từ video Linh vật / Phật dạy / Thần Tài nhiều view trên TikTok** → chồng lên bản ghép (đây là "nhạc/tiếng" quyết định lượt view của dạng này). Không dùng thoại tự sinh.
- **Đổi độ dài shot** (đừng đều nhau → lộ AI); overlay câu chúc tài lộc/an yên trong safe-zone 9:16.
- **Gate chất lượng:** grade vàng thống nhất, hào quang/coin-burst rõ; export **1080p/4K, 9:16**.
- **Disclosure:** engine engagement, không bán trực tiếp → chưa cần. Khi account gắn link aff về sau mới thêm disclosure ở caption.

## 6. NEGATIVE & CHỐT
- **Negative (bake mọi gen):** `morphing shape, extra limbs, flickering, distortion, compression artifacts, inconsistent lighting, watermark, text overlay, human product, logo`. **KHÔNG** loại "3D render/CGI" ở engine này (linh vật thần thoại được phép stylized/rendered).
- **DO:** 1 linh vật/thần/clip tiến TỚI camera; kết bằng burst/rain tiền xu (hoặc hào quang hóa giải với dạng Phật); giữ đúng đuôi `Cinematic one-shot, 9:16, Ambient sound only.`; gen loạt rồi lọc; RIP audio trend TikTok.
- **DON'T:** đừng nhồi 2 linh vật/nhiều hành động 1 clip (morph); đừng để clip đều 3s (lộ AI); đừng thêm thoại tự sinh (phá "ambient + audio trend"); đừng gắn sản phẩm/persona người vào khung.

## 7. METADATA
- **Title** <70 ký tự: câu chúc tài lộc/an yên (vd "Rồng vàng rải lộc — xem là hên cả năm 🧧").
- **Caption + 15-25 hashtag** ngách tài lộc/tâm linh (#thantai #tholdia #phatday #tailoc #maylanman #linhvat #fyp #xuhuong).
- **CTA mềm:** "Lưu lấy vía · Follow nhận lộc mỗi ngày". (Chỉ thêm disclosure hoa hồng khi account bắt đầu gắn link aff.)
