# Khối bất biến của master prompt — DO CODE GHÉP, KHÔNG CHO MODEL GÕ LẠI

Ba khối dưới đây là **hợp đồng kỹ thuật giữa master prompt và phần mềm**. `master_prompt.parse_output`
bóc kết quả dựa đúng vào chúng, và `validate_generated` từ chối bản thiếu bất kỳ marker nào.

Trước đây skill dặn model "chép NGUYÊN VĂN, không sửa một ký tự". Nhưng model *sinh* văn bản chứ không
*chép* file: thiếu một marker là hỏng cả bài, phải retry 10k token, và đôi khi retry vẫn thiếu. Đó là
đánh cược một hằng số vào xác suất.

Nay agent **cắt hẳn phần này khỏi việc của model**: model được dặn "các mục 2, 20 và 26 đã có sẵn,
đừng viết", còn bước Assemble chèn nguyên văn từ file này vào đúng vị trí. Đổi một bug ngẫu nhiên lấy
một hằng số.

Định dạng file: mỗi khối nằm giữa hai dòng `<<<BLOCK:tên>>>` và `<<<END>>>`. Code đọc theo tên khối.

<<<BLOCK:input>>>
CHANNEL NAME:

{{CHANNEL_NAME}}

=== SOURCE START ===

{{SOURCE_MATERIAL}}

=== SOURCE END ===

Everything inside the markers is the universe of established fact. You may add general, verifiable
context about how a system or process works, because that context is the transformation. You may never
add facts about these specific people or events.
<<<END>>>

<<<BLOCK:spoken>>>
- Spell every number as spoken: "two hundred and eleven thousand dollars", "nine days", "nineteen
  eighty-three". Never emit raw digits.
- No symbols at all: no dollar sign, percent sign, ampersand, slash, or arrow.
- The SCRIPT section contains narration and nothing else: no headings, no timestamps, no stage
  directions, no speaker labels, no bracketed cues.
- Every sentence must be speakable in one breath at 140 words per minute. No semicolons, no
  parentheses, no nested clauses that force the narrator to backtrack.
<<<END>>>

<<<BLOCK:output>>>
STRICT OUTPUT FORMAT

IF REJECTED:

STATUS: REJECTED
REASON: [one concise line]

IF ACCEPTED:

TITLE: [final title]

SCRIPT:

[complete narration script, plain text, no headings, no timestamps, no stage directions]

--- END OF SCRIPT ---

NARRATION DIRECTION:
[3 to 6 lines: register, target words per minute, the two places to slow down, phonetic notes for any
name or place]

Output NOTHING else. No analysis, no planning, no alternative titles, no word counts, no visual or
music instructions, no commentary.
<<<END>>>
