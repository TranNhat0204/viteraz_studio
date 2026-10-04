# From a channel portrait → CONFIGURATION for a NEW channel

You are given the portrait of a channel that works, plus the catalogue of "engines" (video formats)
the software supports. Your job is to **decide** the configuration for a new channel that learns from
that way of working.

The previous step *described what exists*. This step *decides what will be made*. They are different
jobs — do not simply restate the portrait.

Write every descriptive field in the output language named in the request. These instructions stay in
English; the answer follows the channel's language.

## Copyright boundary — read this before you write

The new channel **learns the method**; it does not **take the place**. Concretely:

- The niche may overlap. The way of telling may be learned. **Specific subjects, people and facts may
  not be carried over.**
- Do not name or describe the new channel in a way that evokes the source channel.
- If the portrait contains signature wording (a slogan, a greeting, a sign-off), **do not reuse it**.
  Describe its *function* ("there is a sign-off line in the final 30 seconds") and let the new channel
  invent its own.

## How to decide

1. **`niche` must be narrow enough to exclude things.** "Finance" is useless. "US retirement benefits
   for people over 50, explained through real case files" is usable.
2. **`channel_orientation` is what will steer idea generation later** — write it for a machine to
   follow: which angles to favour, which emotions to aim for, which themes recur, and what is banned.
3. **`engine_match` may only be chosen from the supplied catalogue.** If nothing fits, return
   `id: null` and say why, so the user can choose. Inventing an id breaks the channel-creation flow.
4. **`target_sec` follows the typical duration in the portrait**, rounded to a sensible production
   figure.
5. Anything the portrait cannot support, leave empty and record in `warnings`. Filling the form with
   guesses is the surest way to make a user trust something false.

## Output

A single JSON object, nothing else.

```
{
  "niche": "the NARROW niche of the new channel",
  "niche_angle": "its own angle within that niche",
  "channel_brief": "2-4 sentences — reading it tells you what the channel makes and for whom",
  "channel_orientation": "SPECIFIC AND EXECUTABLE direction: which angles to favour, which emotions, which recurring themes, what register, and what is banned",
  "series_mode": "anthology | serial",
  "language": "language code",
  "long_target_sec": 0,
  "short_target_sec": 0,
  "signature_beat": "ONE recurring segment the audience will learn to expect every episode — say what it does and where it sits",
  "source_kind": "the kind of source this channel will run on (news article / case file / report / data + rules / fictional premise)",
  "engine_match": {"id": "an id from the catalogue, or null", "confidence": 0.0, "reason": "why"},
  "confidence": 0.0,
  "warnings": ["what the evidence does not support; the user should decide"]
}
```
