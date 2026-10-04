# Human voice: anti-AI prose + narration that survives TTS

Two problems, one solution layer. A script can fail by **reading** like a machine wrote it, or by **sounding** like a machine reads it. Every master prompt must carry both defenses, with numbers.

---

## Part 1 — The measurable AI tells

The single strongest signal is not vocabulary. It is **cadence uniformity**: sentence after sentence landing in the same length band. Detectors call the inverse "burstiness"; a reader just calls it flat. Everything below is a threshold you can put in a prompt and check.

### Thresholds to write into every master prompt

1. **Sentence-length spread.** In any 200-word stretch there must be at least one sentence of 6 words or fewer AND at least one of 25 words or more. Three consecutive sentences in the 17–23 word band is a defect.
2. **Sentence openers.** Across any 10 consecutive sentences, no more than 3 may begin with "The", "This", "It", "In", "But", or "And". Count them.
3. **Em dashes: at most 1 per 1,000 words.** Not because readers care, but because TTS handles them badly and they are the crutch that replaces real sentence structure. Use a period, a comma, or two sentences.
4. **Rule of three.** At most one three-item list per 1,000 words. The reflex triad ("the money, the house, the marriage") is the most common structural tell in narrative AI prose.
5. **Paragraph shape.** No more than two consecutive paragraphs with the same internal recipe (claim → example → restatement). At least one single-sentence paragraph per major section, used for weight — not more than one, or it becomes a tic.
6. **No false-contrast constructions.** "It wasn't about X, it was about Y" and its cousins ("not the money, the trust") say nothing while sounding profound. Hard ban. State the claim directly.
7. **No manufactured punchline stacks.** Three or more same-shape fragments in a row, each posed for drama, is a hard ban. Keep the one that lands.
8. **Hedge stacking.** "could potentially", "may eventually", "seems to suggest" — pick one modal or drop both.
9. **Vocabulary blacklist (global).** delve, tapestry, testament, realm, crucial, underscore, multifaceted, navigate (abstract), foster, elevate, unleash, resonate, seamless, robust, leverage (verb), pivotal moment, watershed, unprecedented (without naming the precedent), in today's world, at the end of the day, needless to say, it is worth noting, the reality is that.
10. **Transition blacklist.** Moreover, Furthermore, Additionally, In conclusion, When it comes to, That said (as a paragraph opener).

### Per-channel blacklist (this is the part everyone skips)

Every master prompt must add **8–14 genre-specific phrases** that mark the low-trust tier of that exact niche. Examples:

- True crime / cold case: chilling, sinister, evil, monster, horrifying, "what happened next will shock you", "little did she know", "the case that gripped the nation", "authorities were baffled".
- Courtroom: "justice was served", "got away with it", "the trial of the century", "airtight case", "smoking gun" (unless the record uses it).
- Fraud: "you won't believe how easy it was", "genius scheme", "mastermind", "brilliant con", any admiring adjective for the perpetrator.
- Nostalgia: "simpler times", "back when things made sense", "kids today", "they don't make them like they used to", "the good old days".
- Finance/retirement: "secret the banks don't want you to know", "financial freedom", "wealth hack", "guaranteed", "explode your savings".
- Medical: "doctors were stunned", "miracle", "one weird trick", "big pharma", "cure".
- Aviation/disaster: "final terrifying moments", "plunged", "doomed flight", "horror in the skies".
- Business: "genius move", "destroyed the competition", "the fall of an empire" (as a phrase, not as a subject), "greedy executives".
- AI/tech: "game-changer", "revolutionize", "the future is here", "will replace all jobs", "sentient".
- Faith/inspirational: "never gave up on her dreams", "everything happens for a reason", "God had a plan", "against all odds".
- Survival: "SHTF", "when society collapses", "sheeple", "the coming collapse".

### What must never be injected while "humanizing"

Do not add fake first person, manufactured stakes, invented specifics, forced contrarianism, or staccato conversion (chopping sentences purely for rhythm). Those replace one machine signature with another.

---

## Part 2 — Narration craft: writing for a voice, not a page

These scripts are read by a TTS engine and heard at 1x or 1.25x by a 40–65-year-old. The script is a **performance score**, not an essay.

### Sentence architecture for the ear

1. **One idea per sentence.** Nested clauses are where synthetic delivery collapses — the model flattens the intonation and the listener loses the thread.
2. **Hard ceiling of ~28 words**, and only occasionally; the working range is 8–20. Anything the writer cannot say aloud in one breath must be split.
3. **Active voice by default.** "The board approved it" beats "It was approved by the board" — shorter, and the stress lands on the actor.
4. **Contractions on**, unless the channel's register forbids them (declassified and courtroom engines use fewer; nostalgia and inspirational use many). Contractions are the fastest single fix for stilted delivery.
5. **Front-load the subject.** Long introductory clauses make the voice sound like it is waiting for the point. So does the listener.

### Punctuation is pacing markup

- **Period** — full stop, full breath. Use more of them than prose instinct suggests.
- **Comma** — short break. Do not stack more than two per sentence.
- **Ellipsis** — one deliberate trailing pause. At most 2–3 per script, or it becomes a tic.
- **Em dash** — avoid; most engines render it as an unpredictable gap.
- **Semicolon** — banned in narration. It has no audible form.
- **Parentheses** — banned. The voice cannot signal them.
- **Paragraph break** — the longest reliable pause available. Use breaks structurally: one beat, one paragraph.
- **ALL CAPS and bold** — never inside the narration body; they leak into some engines as shouting or get read aloud.

### Pronunciation and number hygiene

- Spell out numbers as they are spoken: "sixty-two", "two hundred and eleven thousand dollars", "nineteen seventy-eight", "nine forty-seven p.m."
- Never leave bare symbols: no `%`, `$`, `&`, `#`, `/`, `→`.
- Expand or respell anything a voice will mangle: acronyms that are spoken as letters get spaced ("F B I"), acronyms spoken as words stay solid ("NASA"). Unusual surnames and place names get a phonetic respelling on first use in a pronunciation note **outside** the script body — never inside it.
- Dates, model numbers, and flight numbers are written the way a narrator says them, not the way a document prints them.

### Rhythm devices that read as human

- **The short line after the long one.** One 25-word sentence carrying three facts, then a four-word sentence that lands it.
- **The repeated exact word.** Human writers repeat the right noun; machines cycle synonyms. If it is a ledger, call it a ledger every time.
- **The concrete over the abstract.** "Eleven thousand dollars a year" beats "a significant expense". "A screen door" beats "the family home".
- **Earned silence.** A paragraph break before the most important sentence of the episode does more than any adjective.
- **Understatement at the peak.** The most emotionally loaded moment gets the plainest sentence in the script. This is the single most reliable marker of a mature narrator.

### Delivery notes block

Every master prompt ends its script section with a **NARRATION DIRECTION** requirement: 3–6 lines that tell the voice engine or voice actor the register, the pace in words per minute, where to slow down, and the two or three places to leave a longer pause. These lines are delivered **outside** the script body so they are never spoken.

---

## Part 3 — The read-aloud gate

Before output, the model must silently perform this pass and rewrite anything that fails:

1. Read the first 30 seconds aloud in your head at 140 words per minute. If any sentence needs a second breath, split it.
2. Check three random 200-word windows against the sentence-spread and opener thresholds above.
3. Search the draft for every phrase on the global and per-channel blacklists. Zero tolerance.
4. Count em dashes, triads, and false contrasts. Apply the limits.
5. Find the emotional peak. Confirm it is the plainest sentence in the script, not the most decorated one.
6. Confirm at least one repeated exact keyword instead of synonym cycling.

A draft that fails any check is rewritten, not shipped with a caveat.
