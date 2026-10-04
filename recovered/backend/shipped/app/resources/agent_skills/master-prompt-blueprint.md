# Master prompt blueprint — the 26 required sections

Order is fixed. Every section appears in every master prompt, filled with **this channel's** specifics. A section that could be pasted unchanged into another engine's master prompt has not been written yet.

Formatting rules for the artifact: plain text, numbered sections with `====` rules, no markdown tables, no frontmatter, English only, second person to the model.

---

**1. SYSTEM ROLE**
Who the model is for this channel, in two or three sentences: the job title, the show, the audience, and the one sentence that defines the channel's promise. State the core workflow as an arrow chain (source → skeleton → conflict → angle → controlled release → consequence → meaning → signature), adapted to this genre.

**2. INPUT CONTRACT**
The exact placeholder(s) the operator will fill: `{{SOURCE}}`, `{{TOPIC}}`, `{{REPORT}}`, `{{PLACE_A}} / {{PLACE_B}}`, `{{OCCUPATION}}`, and so on — chosen per the source-contract table in SKILL.md. Delimited clearly with START/END markers. If the engine needs two inputs, define both.

**3. PRIMARY OBJECTIVE**
Runtime, word band computed at 140 wpm from the engine's `video_length`, and three "must feel like" / three "must not feel like" comparisons written in this genre's terms.

**4. CHANNEL DNA**
The engine's identity compressed to a three-line creed plus what the channel explores that the headline does not. State explicitly that brand recognition comes from voice and discipline, not from repeating a tagline.

**4B. BRAND IDENTITY AND PLACEMENT**
Mandatory. The `{{CHANNEL_NAME}}` placeholder, the channel's internal brand compass, the three tiers of recognition named for this engine, the brand bridge window and its three jobs, the mid-episode rule and its forbidden zones, the signature window, the two-mention budget, and the single-CTA rule. Full specification in `brand-identity.md`. A master prompt without this section produces strong episodes for an unnamed channel.

**5. SOURCE QUALITY GATE**
The reject rule. List the eight to fourteen elements that make a source usable for this genre, the minimum count required, the categories to reject outright, and the exact rejection output format.

**6. FACT MAP (silent)**
The list of entities the model must extract before writing, tuned to the genre — for a trial: charges, elements, exhibits, rulings, verdict, sentence, appeal. For a benefits episode: rule, year, thresholds, exceptions, penalties, deadlines. Never output the map.

**7. FACT LEVELS A / B / C**
Verbatim mechanics from `fact-integrity.md`, with this genre's own attribution verbs.

**8. ZERO-HALLUCINATION INVENTORY**
The genre's specific never-invent list, twenty to forty items, concrete. Plus the "never manufacture a better ending" rule.

**9. PEOPLE POLICY**
Real names, anonymity, presumption of innocence, no merging, no invented characters, POV default, privacy limits, likeness lock if the engine sets one.

**10. QUOTATION AND FAIRNESS**
Quotation-mark discipline, paraphrase preference, attribution verbs, mandatory inclusion of relevant denials or competing accounts.

**11. STORY ENGINE (silent)**
Seven to nine questions the model answers silently before writing, ending with "what question should remain in the viewer's mind". Then a list of the deep conflicts this genre legitimately carries — choose only what the source supports.

**12. NARRATOR VOICE**
A person, not an adjective list: age, temperament, what they have seen, what they refuse to do. Then the "do not sound like" list, written with this genre's failure modes named.

**13. SIGNATURE EMOTIONAL STYLE**
The register rule. For most engines in this pack: the more extreme the facts, the plainer the sentence. State the "plainest sentence at the emotional peak" rule explicitly, and ban the genre's adjective crutches by name.

**14. WRITING FOR THIS AUDIENCE**
Who they are as people, what they already know, what they will not forgive. Priorities and prohibitions in their own vocabulary.

**15. SIGNATURE STORY DEVICES**
Three to five devices, each with a use condition and an abuse warning. The small detail that changes meaning. The moment of no return. The second meaning. Plus at least one device unique to this genre (the document line, the element-by-element, the two-place same-hour comparison, the task decomposition, the silence frame, the object at the peak).

**16. THE MANDATORY SIGNATURE BEAT**
The engine's one non-negotiable beat, with its clock position and its failure condition. This is the section that makes the channel recognizable. Never omit, never move.

**17. RETENTION ENGINE**
The hook clock (0:00–0:06, 0:06–0:15, 0:15–0:25, 0:25–0:40), the beat clock (one meaningful development per 200–300 words), re-hook placement and format, and the banned formula list.

**18. INFORMATION RELEASE**
The knows-now versus held-for-later split, the ban on front-loading, and the rule that delay is legitimate but alteration is not.

**19. EPISODE STRUCTURE**
Section-by-section with clock ranges and word budgets that add up to the target band, ±20%. Each section states its **function**, not required events. Explicit instruction: never invent an event to fill a section; if the source cannot support a section, compress or drop it.

**20. NARRATION AND DELIVERY LAYER**
The part almost every master prompt is missing. Sentence architecture for the ear, punctuation as pacing markup, number and pronunciation hygiene, the read-aloud gate, and the requirement to output a short NARRATION DIRECTION block outside the script body.

**21. ANTI-AI WRITING FILTER**
The numeric thresholds from `human-voice.md` plus this channel's own eight-to-fourteen-phrase blacklist. Include the sentence-spread rule, the opener rule, the em dash limit, the triad limit, the false-contrast ban.

**22. NO FILLER RULE**
Every paragraph performs at least one listed function or is deleted. Name the functions for this genre.

**23. SENSITIVITY SAFEGUARD**
Genre-specific: victims, families, illness, death, minors, financial ruin, faith, disability. What is described, what is implied, what is never depicted.

**24. TITLE ENGINE**
Generate candidates silently, output one. The shape that works for this genre, the character limit, the defensibility rule, and the genre's banned title patterns by example.

**25. FINAL AUDIT (silent, can fail)**
The rubric applied to the draft: the ten dimensions abbreviated into pass/fail questions, plus the auto-fail list, plus the ending swap test. Explicit instruction: if any check fails, rewrite before output — do not ship with a note.

**26. STRICT OUTPUT FORMAT**
Exactly two permitted outputs. Rejection form, or:

```
TITLE: [final title]

SCRIPT:

[complete narration]

--- END OF SCRIPT ---

NARRATION DIRECTION:
[3-6 lines, outside the script body]
```

Then the explicit "output nothing else" list: no analysis, no fact map, no planning, no alternative titles, no word counts, no visual or music notes, no citations, no commentary.

Close with a final principle line, one sentence, written for this channel.

---

## Section length guidance

Sections 1–5 and 24–26 are short and mechanical. Sections 12–21 are where the channel's quality actually lives — spend the words there. Section 19 is the longest single section.

## The differentiation test

Before writing the file, take any three sections and ask: could this paragraph appear unchanged in a different engine's master prompt? If yes for more than two sections out of twenty-six, the document is generic and must be localized further.
