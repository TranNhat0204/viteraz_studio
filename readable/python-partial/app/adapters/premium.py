# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/premium.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: emotion_palette_text


# Original qualified name: estimate_chars
def estimate_chars(groups):
    total = 0
    for __temp_22824 in iter(groups):
        g = __temp_22824
        __temp_22825 = g.get('meta')
        if not __temp_22825:
            meta = {}
        else:
            meta = __temp_22825
        __temp_22827 = meta.get('prefix_tag')
        if not __temp_22827:
            __temp_22828 = len('')
            __temp_22829 = g.get('text')
        else:
            len(__temp_22827)
            g.get('text')
        if not __temp_22829:
            total += __temp_22828 + len('')
        else:
            total += __temp_22828 + len(__temp_22829)
        continue
    return total



# Original qualified name: char_budget
def char_budget(slot_ms, dst_lang, speech_rate):
    if not dst_lang:
        cps = CHARS_PER_SEC.get(''.lower(), DEFAULT_CPS)
    else:
        cps = CHARS_PER_SEC.get(dst_lang.lower(), DEFAULT_CPS)
    budget = max(slot_ms, 0) / 1000.0 * cps * max(speech_rate, 0.5
        ) * _BUDGET_HEADROOM
    return max(int(round(budget)), 8)



# NOT DECOMPILED: style_for_emotion


# NOT DECOMPILED: audio_tag_palette_text


# NOT DECOMPILED: medium_vn_style_for


# Original qualified name: to_blocks
def to_blocks(batch, dst_lang):
    blocks = []
    for __temp_22866 in iter(batch):
        s = __temp_22866
        slot_ms = max(int(s['end_ms']) - int(s['start_ms']), 0)
        __temp_22870 = char_budget(slot_ms, dst_lang)
        if not s.get('text', ''):
            __temp_22872 = s.get('text_src', '')
        else:
            s.get('text_src', '')
        if not __temp_22872:
            blocks.append({seq: s['seq'], start_ms: s['start_ms'], end_ms: s[
                'end_ms'], slot_ms: slot_ms, max_chars: __temp_22870, text: '',
                text_src: ''})
        else:
            blocks.append({seq: s['seq'], start_ms: s['start_ms'], end_ms: s[
                'end_ms'], slot_ms: slot_ms, max_chars: __temp_22870, text: '',
                text_src: __temp_22872})
        continue
    return blocks



# Original qualified name: build_rewrite_messages
def build_rewrite_messages(blocks, src_lang, dst_lang, mode):
    if mode in STANDARD_PROMPTS:
        mode_instr = STANDARD_PROMPTS[mode]
        allowed = STANDARD_EMOTIONS
        engine_note = (
            "VOICE ENGINE — plain TTS (no acting, no audio tags). The voice reads flat, so emotion is NOT rendered: do not try to perform feeling. Write purely for clarity and natural spoken rhythm; keep 'emotion' at 'neutral' (or 'calm') and 'speech_rate' near 1.0."
            )
        want_prefix_tag = False
    elif mode in MEDIUM_VN_PROMPTS:
        mode_instr = MEDIUM_VN_PROMPTS[mode]
        allowed = MELO_EMOTIONS
        engine_note = (
            "VOICE ENGINE — Edge-TTS Vietnamese base + OpenVoice tone-color (optional clone). Emotions are rendered by post-processing (speed / pitch / audio filters), not by an acting model, so each label is a tonal color. Pick the SINGLE closest label from the palette below and NEVER use a label outside it. Because the engine cannot truly 'act', also carry the feeling through word choice and sentence rhythm."
            )
        want_prefix_tag = False
    else:
        mode_instr = MODE_PROMPTS.get(mode, MODE_PROMPTS['review'])
        allowed = EMOTIONS
        engine_note = (
            "VOICE ENGINE — ElevenLabs v3 (premium). Each emotion label maps to expressive voice_settings AND the model genuinely ACTS the emotion. It also obeys delivery cues you write into the text: audio tags in [brackets] (e.g. [whispers], [excited], [sighs], [laughs], [sarcastic], [crying]); ellipses '…' for a pause or hesitation; ALL-CAPS for emphasis/volume; an em-dash '—' for an abrupt break; and '?' / '!' for intonation. Tags work best on this engine — use ONLY tags that suit the voice's range, place them right before the phrase they color, and never spam them. Punctuation and word choice should carry most of the feeling; tags are accents, not decoration."
            )
        want_prefix_tag = True
    emotions = ', '.join(allowed)
    palette = emotion_palette_text(allowed)
    if want_prefix_tag:
        delivery_rule = """  5. DELIVERY: optionally set "prefix_tag" to an ElevenLabs audio tag (e.g. "[dramatic pause] ", "[whispers] ") — use rarely, only when it elevates the moment; otherwise an empty string.
    """
        example_prefix = '[dramatic pause] '
    else:
        delivery_rule = """  5. DELIVERY: this engine does NOT support inline audio tags — always set "prefix_tag" to an empty string "".
    """
        example_prefix = ''
    system_msg = (
        'You are an award-winning film-recap screenwriter and dubbing director. Your craft is turning raw, machine-translated subtitles into a natural, emotionally compelling voice-over script written in '
         + str(dst_lang) + ' (source language: ' + str(src_lang) +
        """) that sounds like a professional movie-recap narrator — never robotic, never word-for-word.
    
    """
         + str(mode_instr) + '\n\n' + str(engine_note) +
        """
    
    EMOTION PALETTE — the ONLY emotion labels you may use, with their meaning. Read each group's mood and pick the one that fits best:
    """
         + str(palette) +
        """
    
    INPUT: a JSON array of subtitle blocks. Each block has:
      - "seq": id; "start_ms"/"end_ms": timing; "slot_ms": duration in ms;
      - "text": the baseline """
         + str(dst_lang) + ' translation; "text_src": the original ' + str(
        src_lang) +
        """ line (use it to stay faithful).
    
    TASK — re-author the script as an ordered list of "groups" optimized for voice-over:
      1. RE-SEGMENT: merge choppy fragments into complete, flowing sentences (list the merged ids in "src_seqs"); split any over-long block into several groups. Aim for thought-complete lines, not word fragments.
      2. TIMING: set each group's "start_ms"/"end_ms" to span exactly its source blocks — contiguous, no overlaps, no large gaps.
      3. LENGTH & PACING — HARD LIMIT (most important rule): the voice-over MUST fit the time slot or the video desyncs. Every input block carries a "max_chars" already computed from its duration. For each output group, the length of "new_text" (including any prefix_tag / inline tags) MUST NOT exceed the SUM of "max_chars" of the blocks you merged into it (the ones listed in "src_seqs"). Treat this as a STRICT CEILING, not a target — when in doubt, write SHORTER and tighter, cut filler words. Slow emotions ('sad','calm') should land well under the limit; fast emotions ('excited','angry') may approach it but NEVER exceed it. Count characters before finalizing each line.
      4. EMOTION: tag each group with "emotion" (EXACTLY one of: """
         + str(emotions) +
        """), "intensity" (0..1 — how strongly to apply it) and "speech_rate" (0.8..1.2), all chosen to match the scene's mood. Vary the emotion across groups to follow the story's arc — do NOT leave everything 'neutral'.
    """
         + str(delivery_rule) +
        """  6. FIDELITY: never invent plot facts, names, or outcomes not present in the source.
    
    OUTPUT: ONLY a JSON array of group objects — no markdown, no commentary. Each object:
      {"src_seqs":[int], "start_ms":int, "end_ms":int, "new_text":string, "emotion":string, "intensity":number, "speech_rate":number, "prefix_tag":string}
    
    Example (format only — write new_text in """
         + str(dst_lang) +
        """):
      [{"src_seqs":[12,13,14],"start_ms":12000,"end_ms":17000,"new_text":"...","emotion":"tense","intensity":0.9,"speech_rate":0.95,"prefix_tag":\""""
         + str(example_prefix) + '"}]')
    if mode == 'adam_hot_trend':
        system_msg += """
    
    AUDIO TAG PALETTE — embed these inline inside new_text (place "[tag] " right before the phrase). Examples include target-language interjections:
    """ + audio_tag_palette_text() + """
    Example new_text: "[amazed] WAOOOO... [whispering] nhưng điều hắn không ngờ tới là... [shouting] tất cả chỉ là một cái bẫy!\""""
    payload = json.dumps(blocks, ensure_ascii=False)
    return [{role: 'system', content: system_msg}, {role: 'user', content: payload}
        ]



# Original qualified name: _clean_json_array
def _clean_json_array(raw):
    cleaned = raw.strip()
    if cleaned.startswith('```'):
        cleaned = cleaned.strip('`').strip()
        if cleaned.lower().startswith('json'):
            cleaned = cleaned[4:None].strip()
    b = cleaned.rfind(']')
    a = cleaned.find('[')
    if a != -1:
        if b != -1:
            if b > a:
                return cleaned[a:b + 1]
    return cleaned



# NOT DECOMPILED: _coerce_int


# NOT DECOMPILED: _salvage_objects


# NOT DECOMPILED: parse_rewrite_response


# Original qualified name: spoken_len
def spoken_len(text):
    if not text:
        return len(_TAG_RE.sub('', '').strip())
    else:
        return len(_TAG_RE.sub('', text).strip())



# NOT DECOMPILED: _trim_to_spoken


# NOT DECOMPILED: effective_speech_rate


# Original qualified name: audit_and_fit
def audit_and_fit(groups, dst_lang, tier, trim_ratio):
    over = 0
    trimmed = 0
    covered = 0
    worst_ratio = 1.0
    for __temp_22934 in iter(groups):
        g = __temp_22934
        slot = max(int(g['end_ms']) - int(g['start_ms']), 0)
        covered += slot
        __temp_22938 = g.get('meta')
        if not __temp_22938:
            eff = effective_speech_rate({}, tier)
        else:
            eff = effective_speech_rate(__temp_22938, tier)
        budget = char_budget(slot, dst_lang, eff)
        sp = spoken_len(g.get('text', ''))
        if budget <= 0:
            continue
            ratio = sp / budget
        else:
            ratio = sp / budget
        if ratio > 1.0:
            over += 1
            worst_ratio = max(worst_ratio, ratio)
        if not ratio > trim_ratio:
            continue
            trimmed += 1
        else:
            trimmed += 1
        continue
    return {groups: len(groups), over_budget: over, worst_ratio: round(
        worst_ratio, 2), trimmed: trimmed, covered_ms: covered}



# Original qualified name: _normalize_timeline
def _normalize_timeline(groups, lo, hi):
    if not groups:
        return groups
    
    
    def __temp_22949(g):
        return g['start_ms'], g['end_ms']
    
    
    groups.sort(key=__temp_22949)
    prev_end = lo
    for __temp_22951 in iter(groups):
        g = __temp_22951
        g['start_ms'] = max(lo, min(int(g['start_ms']), hi))
        g['end_ms'] = max(g['start_ms'] + 1, min(int(g['end_ms']), hi))
        if g['start_ms'] < prev_end:
            g['start_ms'] = min(prev_end, hi)
            if g['end_ms'] <= g['start_ms']:
                g['end_ms'] = min(g['start_ms'] + 200, hi)
        prev_end = g['end_ms']
        continue
    return groups

