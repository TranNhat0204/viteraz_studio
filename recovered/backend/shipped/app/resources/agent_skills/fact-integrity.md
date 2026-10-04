# Fact integrity

The layer that keeps a channel alive. Platform enforcement in this category is no longer theoretical: a true-crime channel with millions of views was terminated for fabricating cases, and channels built on mass-produced, low-value uploads have been removed from monetization in waves. Every master prompt carries this layer, worded for its own genre.

---

## 1. Fact levels

Every master prompt defines three levels and requires the model to sort each claim before writing.

- **Level A — established.** The source presents it as fact. May be narrated directly.
- **Level B — attributed.** "Police alleged", "the lawsuit claims", "the report concluded", "her attorney denied", "the filing states". **Must keep its attribution in the narration.** Stripping the attribution to make a sentence flow is the most common integrity failure in adapted scripts.
- **Level C — unknown.** The source does not establish it. It may be named as unknown. It may never be narrated as fact, implied by juxtaposition, or filled with a plausible guess.

The Level C rule needs teeth: **the model must state at least one thing the record does not answer** in every episode. A story with no acknowledged gaps has almost certainly been smoothed over.

## 2. Zero-hallucination inventory

Write the genre's own list. Generic bans get paraphrased away; specific ones survive. For each engine, enumerate what must never be invented — dialogue, motives, internal thoughts, phone calls, messages, meetings, memos, transfers, documents, witnesses, investigators, evidence, rulings, sentences, diagnoses, test results, altitudes, callouts, tax rates, premiums, prices, casualty counts, store counts, benchmark scores.

And the rule that catches everything else:

> Never create a more satisfying ending. Never manufacture justice. Never force karma. If the documented outcome is unresolved, unfair, or anticlimactic, that is the ending.

## 3. Named people

- If the source names them publicly, keep the real name. Never rename real people into recurring fictional characters.
- If the source withholds identity, preserve it.
- Never merge two people into one. Never add a person who is not in the source.
- Presumption of innocence is absolute for anyone not convicted: "person of interest", "named as a suspect", "questioned and released", "never charged", "was acquitted". Never "got away with it".
- No private addresses, workplaces, or current locations for living private individuals.
- Default POV is third-person documentary. Never invent first-person narration in a real person's voice.

## 4. Quotations

Quotation marks only for wording the source actually contains. Everything else is paraphrase, and where the substance matters, say so: "in substance", "according to the filing". Fabricated dialogue is the fastest way to lose a knowledgeable audience, and in these genres the audience is knowledgeable.

Include materially relevant denials and competing accounts that the source contains. Do not use ambiguity to make someone look guiltier than the record supports.

## 5. Dramatized channels

For engines that are explicitly fiction (39, 42):

- Fully invented names, towns, businesses, and details. No resemblance to a real identifiable person, family, town, church, company, or event.
- **Disclosure inside the first 45 seconds** of narration, phrased so it does not break the spell, and again in the description.
- Never present the story as a specific real case, and never use real place names attached to invented crimes or disputes.
- Composite stories built from documented patterns are permitted only when labeled as such.

## 6. YMYL engines

For money, health, and housing (38, 41, 46, and the money-adjacent parts of 35, 44, 45):

- Every rule, threshold, bracket, premium, and figure carries **its year and its issuing body**, spoken naturally.
- Anything that changes annually is flagged as changing annually.
- **Scenarios are explicitly illustrative** — "consider someone with…" — never presented as a real person or a testimonial.
- No individualized advice. No promised returns, cures, or appreciation. No product, supplement, ticker, or service recommendation.
- One plain disclaimer inside the script and one in the description. Not a wall of legal text; one clear sentence.
- For health: never diagnose, never dose, never frame medicine as the enemy, always include the guideline-sourced "when to seek care" beat.

## 7. Likeness and imagery

Where the engine sets `likeness_lock`, the master prompt must state it for the script layer too: never describe an image of a real identifiable person, never request a lookalike, never write "in the style of [real person]". Platform likeness detection scans uploads for synthetic depictions of enrolled faces, and the enrolled population now includes millions of creators plus public figures and journalists.

Where the engine sets `anonymity_lock`, the script must be written so it never requires a face to work: subjects are described by role, action, and place.

## 8. Harm boundaries

- **Fraud engines:** describe cons at the level of recognition and defense. Never scripts, tools, platforms, or steps that would help someone run one.
- **Disaster and crime engines:** no casualty description, no injury detail, no impact recreation. Numbers stated once, respectfully.
- **Survival engines:** no treatment protocols, no weapons, no collapse advocacy. Defer to official guidance where it exists.
- **All engines:** no content that invites harassment of a named person, and no juxtaposition that implies guilt the record does not carry.

## 9. The source gate

Every master prompt opens with a gate that can reject. This is what separates a professional prompt from a content mill: the willingness to output nothing.

The gate checks that the source contains enough documented narrative material to sustain the target runtime honestly. If it does not, the only permitted output is:

```
STATUS: REJECTED
REASON: [one concise line]
```

And the rule that must appear immediately after it:

> Never invent material to reach the word count. A short, honest episode is a business problem. A padded, invented one is an existential one.
