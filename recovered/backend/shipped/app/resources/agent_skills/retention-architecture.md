# Retention architecture

What the platform actually rewards, converted into instructions a scriptwriting model can follow. Every number here goes into the master prompt as a clock position, not as advice.

---

## 1. The first thirty seconds decide the video

The intro window shows the steepest single drop on every retention curve, and the platform measures it directly as its own key moment. The practical gap: a video where ~70% of viewers survive 30 seconds is treated by distribution as a different object than one where 40% survive.

**Benchmarks to write into the prompt:**
- Past the hook: above 70% is solid, above 80% exceptional. Below 50% in the first 10–15 seconds means the hook failed.
- End-of-video: 40% is a healthy baseline, 50%+ excellent. For 15–30 minute runtimes, 30–45% average percentage viewed is strong — a 30-minute episode held to 30% is nine minutes of watch time, which is a strong signal.

**The hook clock (write these exact positions into every master prompt):**

- **0:00–0:06** — the single strongest verified fact, stated flat, no preamble, no greeting, no channel name, no "in this video". A specific noun and a number beat any adjective.
- **0:06–0:15** — the contradiction or the wrongness. This is what converts a fact into a question the viewer cannot put down.
- **0:15–0:25** — the stake. Who stood to lose what. Concrete and human.
- **0:25–0:40** — the contract. One sentence naming what the episode will actually deliver, so the viewer knows staying is worth it. Never reveal the outcome.
- **Branding, if any, sits after 0:40** and lasts under 15 seconds. A channel name in the first ten seconds is a measurable retention leak.

The hook must deliver on the exact promise of the title and thumbnail. A cliff-shaped drop at second five is almost always a mismatch between thumbnail promise and opening line, not a pacing problem.

---

## 2. The beat clock

After the hook, retention comes from **progression**, not from tension tricks. The rule to encode:

> Every 200–300 words (roughly 90–130 seconds of narration), the script must deliver at least one of: new information, a consequence, a contradiction, a decision, a revelation, a raised stake, a new question, or a re-reading of something already established.

A paragraph that does none of these is filler and gets cut. This is the single highest-leverage rule in the whole document, because "boring middle" is where 15–25 minute episodes die.

**Section-level pacing for a 15–22 minute episode:**

- 0:00–0:40 hook
- 0:40–1:30 orientation (who, where, what is at stake) — this is where the audience decides if the story is about people they can care about
- 1:30–5:00 the world before (what could be lost). Long enough that the loss lands later; if it runs past 5:30 the curve sags
- 5:00–9:00 first cracks; ends on a genuine unresolved question, not a manufactured one
- 9:00–14:00 the point of no return; **slow the narration here** — shorter sentences, more paragraph breaks, more concrete detail
- 14:00–19:00 the explanation section (what really happened / the mechanism / the finding)
- 19:00–23:00 consequences
- final 2–3 minutes meaning + close

Scale proportionally for 10–16 minute engines and 20–25 minute engines. Never scale by padding a section; drop a section instead.

---

## 3. Re-hooks

A re-hook is a sentence that re-states what is still unanswered. Not a cliffhanger, not "but what happened next".

- Place one at the end of every major section, so roughly every 3–5 minutes.
- Format: name the open question in plain words, then move. "The deed had already been transferred. What nobody in the family knew was who had signed it."
- Hard ban on empty formulas: "little did they know", "everything was about to change", "you won't believe what happened next", "but here's where it gets interesting", "the truth was much darker".
- The test: a re-hook is legitimate if the answer genuinely arrives later in the episode. If it does not, it is a lie and the comments will say so.

---

## 4. Information order is the only legitimate suspense tool

The script may **delay** a verified fact, **foreshadow** it, and **re-contextualize** it. The script may never **alter** it, and may never imply something the source does not support.

Encode the split explicitly:
- WHAT THE VIEWER KNOWS NOW
- WHAT IS BEING HELD FOR LATER

Do not summarize the whole story in the opening. The most common failure in adapted-from-article scripts is front-loading the entire article in the first two minutes, after which the remaining eighteen minutes have nothing to reveal.

---

## 5. Chapters and series coherence

- 12–22 minutes per episode is the functional sweet spot for narrative documentary; it is long enough for real depth and meaningful watch-time signals, short enough to hold.
- Chapter markers every 2–4 minutes, named as questions or stakes, never as "Part 3".
- Episodes should reference the series identity once, near the close, so the catalog reads as a show rather than a pile of one-offs.

---

## 6. Curve diagnostics to include in the master prompt

Give the model the failure signatures so it can pre-empt them:

- **Cliff** (steep drop in the first 15–30 seconds, then flat): the opening did not deliver the title's promise. Fix by cutting everything before the strongest fact.
- **Slow bleed** through the middle: the beat clock was violated. Find the 300-word stretch that delivers nothing and cut it.
- **V-dip** at a specific minute: usually a recap the audience did not need, or a section that explains something already understood.
- **Late collapse** at 70–80%: the consequences section arrived after the audience already had the answer. Move the payoff later or hold one fact back.

---

## 7. Title and thumbnail contract

The title must be defensible against the script. Encode this as a check: **every claim in the title must be supported by a line in the script within the first two minutes**, or the title is changed. A title that promises a revelation the script delivers at minute nineteen produces a cliff, not suspense.

Title shape that works for this catalog: a specific human stake + a specific decision, discovery or number + an unanswered consequence. Under 70 characters. No all-caps, no "SHOCKING", no promise the record cannot support.
