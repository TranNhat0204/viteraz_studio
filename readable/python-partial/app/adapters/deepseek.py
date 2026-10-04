# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/deepseek.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _as_deepseek_error
def _as_deepseek_error(exc):
    code = _ERROR_MAP.get(exc.code)
    if code:
        return make_error(code, exc.message)
    return exc



# NOT DECOMPILED: _load_api_key


# Original qualified name: _format_srt_time
def _format_srt_time(ms):
    h = ms // 3600000
    m = ms % 3600000 // 60000
    s = ms % 60000 // 1000
    mill = ms % 1000
    return format(h, '02d') + ':' + format(m, '02d') + ':' + format(s, '02d'
        ) + ',' + format(mill, '03d')



# Original qualified name: _format_vtt_time
def _format_vtt_time(ms):
    h = ms // 3600000
    m = ms % 3600000 // 60000
    s = ms % 60000 // 1000
    mill = ms % 1000
    return format(h, '02d') + ':' + format(m, '02d') + ':' + format(s, '02d'
        ) + '.' + format(mill, '03d')



# Original qualified name: _segments_to_srt
def _segments_to_srt(segments):
    lines = []
    for __temp_341 in iter(enumerate(segments, 1)):
        __temp_342, __temp_343 = __temp_341
        idx = __temp_342
        seg = __temp_343
        seq = seg.get('seq')
        if seq is None:
            seq = idx
        start = _format_srt_time(seg['start_ms'])
        end = _format_srt_time(seg['end_ms'])
        text = seg.get('text', '').strip().replace('\n', ' ')
        lines.append(str(seq))
        lines.append(str(start) + ' --> ' + str(end))
        lines.append(text)
        lines.append('')
        continue
    return '\n'.join(lines)



# Original qualified name: _segments_to_vtt
def _segments_to_vtt(segments):
    lines = ['WEBVTT', '']
    for __temp_358 in iter(enumerate(segments, 1)):
        __temp_359, __temp_360 = __temp_358
        idx = __temp_359
        seg = __temp_360
        seq = seg.get('seq')
        if seq is None:
            seq = idx
        start = _format_vtt_time(seg['start_ms'])
        end = _format_vtt_time(seg['end_ms'])
        text = seg.get('text', '').strip().replace('\n', ' ')
        lines.append(str(seq))
        lines.append(str(start) + ' --> ' + str(end))
        lines.append(text)
        lines.append('')
        continue
    return '\n'.join(lines)



# Original qualified name: _lang_name
def _lang_name(code):
    if not code:
        __temp_374 = ''.strip().lower()
    else:
        code.strip().lower()
    if not code:
        return _LANG_NAMES.get(__temp_374, 'the target language')
    else:
        return _LANG_NAMES.get(__temp_374, code)



# Original qualified name: _render_glossary
def _render_glossary(glossary):
    if not glossary:
        return
    pairs = []
    if isinstance(glossary, dict):
        for __temp_382 in iter(glossary.items()):
            __temp_383, __temp_384 = __temp_382
            k = __temp_383
            v = __temp_384
            k = str(k).strip()
            v = str(v).strip()
            if not k:
                continue
            if not v:
                continue
                pairs.append('"' + str(k) + '" → "' + str(v) + '"')
            else:
                pairs.append('"' + str(k) + '" → "' + str(v) + '"')
            continue
    elif isinstance(glossary, (list, tuple, set)):
        for __temp_392 in iter(glossary):
            term = __temp_392
            t = str(term).strip()
            if not t:
                continue
                pairs.append('"' + str(t) + '"')
            else:
                pairs.append('"' + str(t) + '"')
            continue
    if not pairs:
        return
    body = '; '.join(pairs[None:200])
    return '10. GLOSSARY — render these exact terms the SAME way EVERY time across the whole video (character names, brands, places, recurring jargon). Never let a name drift between lines: ' + body + '\n'



# Original qualified name: _render_context_pairs
def _render_context_pairs(pairs, src_name, dst_name):
    if not pairs:
        return
    lines = []
    for __temp_399 in iter(pairs[-CARRYOVER_PAIRS:None]):
        __temp_400, __temp_401 = __temp_399
        s = __temp_400
        d = __temp_401
        if not s:
            s = ''.strip().replace('\n', ' ')
        else:
            s = s.strip().replace('\n', ' ')
        if not d:
            d = ''.strip().replace('\n', ' ')
        else:
            d = d.strip().replace('\n', ' ')
        if not d:
            continue
            lines.append('  - ' + str(src_name) + ': ' + str(s) + '\n    ' +
                str(dst_name) + ': ' + str(d))
        else:
            lines.append('  - ' + str(src_name) + ': ' + str(s) + '\n    ' +
                str(dst_name) + ': ' + str(d))
        continue
    if not lines:
        return
    return """CONTEXT — the lines immediately BEFORE this batch were already translated as below. Keep names, terminology, tone and register CONSISTENT with them so the dialogue flows across batches. These are reference ONLY — do not re-translate or include them in your output:
    """ + '\n'.join(
        lines) + '\n\n'



# NOT DECOMPILED: _pace_info


# Original qualified name: _retime_rule
def _retime_rule(lo, hi, cps, drift_ms):
    sec = drift_ms / 1000.0
    return "9. RE-TIME FOR EVEN, NATURAL NARRATION SPEED (this translation is read aloud as a single film-recap voice-over — THIS IS THE MOST IMPORTANT RULE). The lines are spoken back-to-back by one narrator. Each input line gives its ORIGINAL on-screen window 'start_ms'/'end_ms' and 'dur_ms'. Your job is to OUTPUT a NEW 'start_ms'/'end_ms' for every line so that EVERY line can be spoken at the SAME comfortable, natural pace (about " + format(cps, '.0f') + """ characters per second). Give a line that has MORE text MORE time, and a line with little text LESS time — BORROW time between neighbouring lines instead of cutting words, so the high-quality standard translation is preserved. HARD CONSTRAINTS:
       (a) Same order, same 'seq', same number of lines — never merge, split, add or drop a line.
       (b) Contiguous & non-overlapping: each line's new 'start_ms' = the previous line's new 'end_ms'; the times strictly increase.
       (c) STAY IN SYNC WITH THE VIDEO — do NOT drift far from the original: keep each line's new 'start_ms'/'end_ms' within about """ + format(sec, '.1f') + ' second of its original value, and keep the whole block inside its original window (first line starts at >= ' + str(lo) + ' ms, last line ends at <= ' + str(hi) + """ ms). You are only gently RE-DISTRIBUTING time inside this window so the subtitle still lines up with the scenes of the film.
       (d) Re-timing is the PRIMARY tool; only if the text genuinely cannot fit even after re-timing should you lightly tighten the longest lines (cut filler/redundancy) — and even then NEVER drop plot facts, names, numbers or meaning.
    """



# NOT DECOMPILED: _build_translate_prompt


# Original qualified name: _build_translate_prompt.<locals>._item
def _item(s):
    nonlocal pace
    if pace:
        en = int(s['end_ms'])
        st = int(s['start_ms'])
        return {seq: s['seq'], text: s['text'], start_ms: st, end_ms: en,
            dur_ms: en - st}
    return {seq: s['seq'], text: s['text']}



# NOT DECOMPILED: _input_output_desc


# NOT DECOMPILED: _example_line


# NOT DECOMPILED: _balanced_at


# NOT DECOMPILED: _find_balanced_array


# Original qualified name: _strip_md_fences
def _strip_md_fences(s):
    re = __import__('re', fromlist=None, level=0)
    app = __import__('app.core.text', fromlist=('strip_thinking_blocks',), level=0)
    strip_thinking_blocks = app.strip_thinking_blocks
    if not s:
        s = strip_thinking_blocks('')
    else:
        s = strip_thinking_blocks(s)
    m = re.search('```(?:json)?\\s*(.*?)```', s, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return s



# Original qualified name: _strip_trailing_commas
def _strip_trailing_commas(s):
    re = __import__('re', fromlist=None, level=0)
    return re.sub(',(\\s*[}\\]])', '\\1', s)



# NOT DECOMPILED: _regex_extract_texts


# NOT DECOMPILED: _parse_response_texts


# NOT DECOMPILED: _parse_response_texts.<locals>._coerce


# NOT DECOMPILED: _coerce_int


# NOT DECOMPILED: _parse_response_objects


# NOT DECOMPILED: apply_retimed


# Original qualified name: DeepSeekClient.__init__
def __init__(self, api_key):
    if not api_key:
        self.api_key = _load_api_key()
    else:
        self.api_key = api_key
    return None



# Original qualified name: DeepSeekClient._ensure_ready
def _ensure_ready(self):
    if not self.api_key:
        raise make_error(E.DEEPSEEK_AUTH,
            'API key DeepSeek trống. Mở Settings để nhập.')
    return None



# Original qualified name: DeepSeekClient._api_client
def _api_client(self, timeout):
    app = __import__('app.adapters.llm_api', fromlist=('registry',), level=0)
    registry = app.registry
    app = __import__('app.adapters.llm_api.client', fromlist=('ApiClient',),
        level=0)
    ApiClient = app.ApiClient
    provider = registry.get_provider(CATALOG_PROVIDER_KEY)
    if provider is None:
        raise make_error(E.DEEPSEEK_BAD_RESPONSE,
            "Danh mục AI thiếu khối 'deepseek' (app/resources/llm_providers.json)."
            )
    return ApiClient(provider, provider.resolve_model(None), api_key=self.
        api_key, timeout=timeout)



# NOT DECOMPILED: DeepSeekClient.test_connection


# NOT DECOMPILED: DeepSeekClient.translate_batch


# NOT DECOMPILED: DeepSeekClient._translate_single_batch


# Original qualified name: DeepSeekClient._merge_translated
def _merge_translated(self, batch, texts):
    merged = []
    for __temp_3015 in iter(enumerate(batch)):
        __temp_3016, __temp_3017 = __temp_3015
        i = __temp_3016
        seg = __temp_3017
        if i < len(texts):
            if texts[i]:
                text = texts[i]
            elif i >= len(texts):
                log.warning('DeepSeek thiếu segment seq=' + str(seg['seq']) +
                    ', giữ text gốc')
                text = seg.get('text', '')
            else:
                text = seg.get('text', '')
        elif i >= len(texts):
            log.warning('DeepSeek thiếu segment seq=' + str(seg['seq']) +
                ', giữ text gốc')
            text = seg.get('text', '')
        else:
            text = seg.get('text', '')
        merged.append({seq: seg['seq'], start_ms: seg['start_ms'], end_ms: seg[
            'end_ms'], text: text})
        continue
    return merged



# NOT DECOMPILED: DeepSeekClient.rewrite_batch


# NOT DECOMPILED: DeepSeekClient._rewrite_single_batch


# NOT DECOMPILED: DeepSeekClient._call_api
