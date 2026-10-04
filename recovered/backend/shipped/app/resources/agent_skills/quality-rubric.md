# The 10-dimension rubric

Used twice: the skill scores the **master prompt** it writes, and the master prompt makes the scriptwriting model score its own **script** before output. Same scale, different subject.

Score each dimension 0–10. Publish only at **total ≥ 90 with no dimension below 8**. Anything else is rewritten, not shipped with an apology.

---

## D1 — Hook integrity (weight: highest)
- 10: First six seconds are one verified, specific fact with a number or a proper noun. No preamble, no greeting, no channel name. Contradiction by 0:15, stake by 0:25, contract by 0:40. Title promise visible in the first two minutes.
- 6: Hook is interesting but generic, or the strongest fact arrives at 0:20.
- 3: Opens with orientation, branding, or a rhetorical question.
- 0: Opens with "In this video" or a greeting.

## D2 — Factual discipline
- 10: Every claim traces to the source. Attributions spoken naturally with year and origin. Allegation and fact are visibly separated. Gaps are stated, not filled.
- 6: Mostly sourced, one or two unattributed generalizations.
- 3: A detail, quote, or figure appears that the source does not support.
- 0: An invented case, person, document, statistic, or outcome. **Auto-fail regardless of total.**

## D3 — Structural progression
- 10: Every 200–300 words delivers new information, a consequence, a contradiction, a decision, a revelation, a raised stake, or a re-reading. No paragraph is decorative.
- 6: One flat stretch of 400+ words.
- 3: Two or more flat stretches, or a mid-episode recap the audience did not need.
- 0: The article's whole content is spent in the first three minutes.

## D4 — Human voice (prose)
- 10: Sentence-length spread passes (a ≤6-word and a ≥25-word sentence in every 200), opener check passes, zero blacklist phrases, ≤1 em dash per 1,000 words, ≤1 triad per 1,000 words, zero false-contrast constructions.
- 6: Passes most, two or three tells survive.
- 3: Uniform cadence, visible triads, several blacklist phrases.
- 0: Reads as unedited model output.

## D5 — Narration performance (the ear)
- 10: Every sentence speakable in one breath at 140 wpm. Contractions used at the channel's register. No semicolons, parentheses, symbols, or bare numerals. Numbers spelled as spoken. Paragraph breaks placed as beats. A NARRATION DIRECTION block is present and specific.
- 6: A few long clauses; delivery notes generic.
- 3: Written for the eye. Symbols and long nested sentences survive.
- 0: Unreadable aloud without rewriting.

## D6 — Emotional calibration
- 10: The most dramatic moment carries the plainest sentence. No adjective does work a fact could do. The audience is never told whom to hate. Restraint scales with the severity of the material.
- 6: Occasional editorializing.
- 3: Adjective-driven drama, moral instruction to the viewer.
- 0: Tabloid register, victim degradation, or mockery.

## D7 — Channel identity
- 10: The engine's signature mandatory beat is present, in position, and doing real work. Register, POV, tense discipline and vocabulary all match the engine. A returning viewer would recognize the show from any two minutes of it.
- 6: Identity present but thin; the beat is perfunctory.
- 3: Could be any channel in the genre.
- 0: Contradicts the engine (wrong POV, wrong tense, banned content present).

## D8 — Audience fit
- 10: Written for a competent 40–65-year-old. Nothing over-explained, nothing condescended to. No youth slang, no fake outrage, no rhetorical-question padding. Concerns named in their real terms (money, family, security, reputation, health, time).
- 6: Register slips once or twice.
- 3: Reads like short-form social content stretched long.
- 0: Talks down to the audience.

## D9 — Ending quality
- 10: The close belongs to this story alone. Factual status stated, the human meaning named without preaching, one specific question that invites reasonable disagreement. **Swap test: if this ending could close ten other episodes, it scores 0 on this dimension.**
- 6: Case-specific but generic in phrasing.
- 3: Moral lecture or motivational close.
- 0: Copy-paste outro.

## D10 — Compliance and safety
- 10: Every engine-level lock is honored — anonymity, likeness, YMYL disclaimers, dramatization disclosure, no operational harm detail, no defamation, no medical or legal or investment advice, respectful handling of victims.
- 6: A lock is honored in spirit but not stated where it must be stated.
- 3: A disclosure or disclaimer is missing.
- 0: A lock is violated. **Auto-fail regardless of total.**

---

## Auto-fail list

Any one of these forces a rewrite no matter what the numeric total says:

1. Invented fact, name, quote, document, figure, or outcome.
2. An allegation narrated as established fact.
3. A missing mandatory disclosure (dramatized, YMYL, likeness, sources).
4. A recognizable real-person likeness requested in imagery, where the engine locks it.
5. Operational instructions that would help someone commit the harm being described.
6. Graphic content the engine bans (gore, casualty depiction, injury detail).
7. Output that is not exactly one of the two permitted formats.
8. The word count is hit by padding rather than by material.

---

## Scoring the master prompt itself

When the skill scores the artifact it just wrote, the same dimensions apply, read as "does this document force the behavior":

- D1 → does it give exact clock positions, or just say "start strong"?
- D2 → does it define fact levels and name the channel's specific fabrication risk?
- D3 → is the beat clock a number?
- D4 → are the anti-AI limits numeric and is there a channel-specific blacklist?
- D5 → is there a narration layer at all? (Most master prompts have none. This is the easiest place to win.)
- D6 → is restraint defined behaviorally, with the plain-sentence-at-the-peak rule?
- D7 → is the engine's signature beat mandatory and positioned?
- D8 → is the audience described as people, not as a demographic bracket?
- D9 → is the swap test present?
- D10 → is every lock from the engine reproduced, with its reason?
