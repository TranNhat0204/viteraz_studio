# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _edge_fallback_voice
def _edge_fallback_voice(dst_lang):
    if not dst_lang:
        return _EDGE_FALLBACK_VOICE.get('vi'.lower(), 'vi-VN-NamMinhNeural')
    else:
        return _EDGE_FALLBACK_VOICE.get(dst_lang.lower(), 'vi-VN-NamMinhNeural')



# NOT DECOMPILED: _voice_display_name


# Original qualified name: _parse_lexicon
def _parse_lexicon(raw):
    pairs = []
    if isinstance(raw, dict):
        items = raw.items()
    elif isinstance(raw, (list, tuple)):
        items = []
        for __temp_259335 in iter(raw):
            it = __temp_259335
            if isinstance(it, (list, tuple)):
                if len(it) == 2:
                    items.append((it[0], it[1]))
                    continue
                    __temp_259339 = isinstance(it, str)
                else:
                    isinstance(it, str)
            else:
                isinstance(it, str)
            if not __temp_259339:
                continue
            if not '=' in it:
                continue
                __temp_259343, __temp_259344 = it.split('=', 1)
                k = __temp_259343
            else:
                __temp_259346, __temp_259347 = it.split('=', 1)
                k = __temp_259346
            v = __temp_259344
            items.append((k, v))
            continue
    else:
        return pairs
    for __temp_259349 in iter(items):
        __temp_259350, __temp_259351 = __temp_259349
        k = __temp_259350
        v = __temp_259351
        k = str(k).strip()
        v = str(v).strip()
        if not k:
            continue
        if not v:
            continue
            pairs.append((k, v))
        else:
            pairs.append((k, v))
        continue
    
    
    def __temp_259358(p):
        return len(p[0])
    
    
    pairs.sort(key=__temp_259358, reverse=True)
    return pairs



# NOT DECOMPILED: normalize_text_symbols_fallback


# NOT DECOMPILED: normalize_text_symbols_fallback.<locals>._replace_dollar


# Original qualified name: apply_lexicon
def apply_lexicon(text, lexicon, dst_lang):
    if not text:
        return text
    out = normalize_text_symbols_fallback(text, dst_lang)
    if not lexicon:
        return out
    re = __import__('re', fromlist=None, level=0)
    for __temp_259382 in iter(lexicon):
        __temp_259383, __temp_259384 = __temp_259382
        term = __temp_259383
        spoken = __temp_259384
        if term.isascii():
            if term.replace(' ', '').isalnum():
                out = re.sub('\\b' + str(re.escape(term)) + '\\b', spoken, out,
                    flags=re.IGNORECASE)
                continue
                out = re.sub(re.escape(term), spoken, out, flags=re.IGNORECASE)
            else:
                out = re.sub(re.escape(term), spoken, out, flags=re.IGNORECASE)
        else:
            out = re.sub(re.escape(term), spoken, out, flags=re.IGNORECASE)
        continue
    return out



# NOT DECOMPILED: _combine_rate


# NOT DECOMPILED: TTSStep.run


# Original qualified name: TTSStep.run.<locals>._q
def _q(db, kind):
    nonlocal ctx
    return db.query(SubtitleSegment).filter(SubtitleSegment.video_id == ctx.
        video_id, SubtitleSegment.kind == kind).order_by(SubtitleSegment.seq).all()



# Original qualified name: TTSStep.run.<locals>._cache_file
def _cache_file(synth_text, style, context):
    nonlocal cache_dir, ctx, pitch, provider_id, rate, voice
    key_parts = [provider_id, voice, rate, pitch, synth_text, style, context]
    bust = ctx.config.get('tts_cache_bust')
    if bust:
        key_parts.append({'bust': str(bust)})
        key = hashlib.sha256(json.dumps(key_parts, sort_keys=True, ensure_ascii
            =False).encode('utf-8')).hexdigest()
    else:
        key = hashlib.sha256(json.dumps(key_parts, sort_keys=True, ensure_ascii
            =False).encode('utf-8')).hexdigest()
    return cache_dir / str(key) + '.wav'



# NOT DECOMPILED: TTSStep.run.<locals>._render_segment


# NOT DECOMPILED: TTSStep._synth_chunk


# NOT DECOMPILED: TTSStep._synth_chunk.<locals>._render


# NOT DECOMPILED: TTSStep._transcribe_words


# Original qualified name: TTSStep._align_ladder
def _align_ladder(self, ctx):
    app = __import__('app.adapters.whisper_engine', fromlist=(
        'align_model_name',), level=0)
    align_model_name = app.align_model_name
    fast = align_model_name(ctx.config)
    __temp_259573 = ctx.config.get('whisper_model')
    if not __temp_259573:
        main = str('small')
    else:
        main = str(__temp_259573)
    rungs = [{model_override: '', force_cpu: False, label: "model '" + str(fast
        ) + "'"}]
    if main:
        if main != fast:
            rungs.append({model_override: main, force_cpu: False, label: 
                "model '" + str(main) + "' (lớn hơn)", heavier: True})
            rungs.append({model_override: fast, force_cpu: True, label: 
                "model '" + str(fast) + "' trên CPU"})
            return self._dedupe_rungs(ctx, rungs)[None:_ALIGN_ATTEMPTS]
        else:
            rungs.append({model_override: fast, force_cpu: True, label: 
                "model '" + str(fast) + "' trên CPU"})
            return self._dedupe_rungs(ctx, rungs)[None:_ALIGN_ATTEMPTS]
    else:
        rungs.append({model_override: fast, force_cpu: True, label: "model '" +
            str(fast) + "' trên CPU"})
        return self._dedupe_rungs(ctx, rungs)[None:_ALIGN_ATTEMPTS]



# NOT DECOMPILED: TTSStep._rung_identity


# Original qualified name: TTSStep._dedupe_rungs
def _dedupe_rungs(cls, ctx, rungs):
    out = []
    seen = set()
    for __temp_259596 in iter(rungs):
        r = __temp_259596
        key = cls._rung_identity(ctx, r)
        if key in seen:
            continue
            seen.add(key)
            out.append(r)
        else:
            seen.add(key)
            out.append(r)
        continue
    return out



# NOT DECOMPILED: TTSStep._whisper_align


# NOT DECOMPILED: TTSStep._chunk_limit


# NOT DECOMPILED: TTSStep._omni_speed_ctx


# NOT DECOMPILED: TTSStep._run_tts_first


# NOT DECOMPILED: TTSStep.extract_voice_timing


# NOT DECOMPILED: TTSStep._run_tts_conform


# NOT DECOMPILED: TTSStep._shorten_lines


# NOT DECOMPILED: TTSStep._run_tts_film


# NOT DECOMPILED: TTSStep._run_tts_film.<locals>._synth_line


# NOT DECOMPILED: TTSStep._run_tts_film.<locals>._too_fast


# NOT DECOMPILED: TTSStep._run_tts_continuous


# NOT DECOMPILED: _wav_duration_ms


# NOT DECOMPILED: _speech_onsets


# NOT DECOMPILED: _snap_starts


# NOT DECOMPILED: _time_fit


# NOT DECOMPILED: _loudness_normalize


# NOT DECOMPILED: _gen_silence


# NOT DECOMPILED: _fit_exact_ms


# NOT DECOMPILED: _kata_to_hira


# Original qualified name: _match_units
def _match_units(text):
    if not text:
        text = unicodedata.normalize('NFKC', '').lower()
    else:
        text = unicodedata.normalize('NFKC', text).lower()
    text = _kata_to_hira(text)
    text = re.sub('[^\\w\\s]', ' ', text, flags=re.UNICODE)
    units = []
    for __temp_259919 in iter(text.split()):
        word = __temp_259919
        buf = ''
        for __temp_259920 in iter(word):
            ch = __temp_259920
            if _UNSPACED_RE.match(ch):
                if buf:
                    units.append(buf)
                    buf = ''
                units.append(ch)
                continue
                buf += ch
            else:
                buf += ch
            continue
        if not buf:
            continue
            units.append(buf)
        else:
            units.append(buf)
        continue
    return units



# Original qualified name: _whisper_units
def _whisper_units(words):
    units = []
    times = []
    for __temp_259928 in iter(words):
        w = __temp_259928
        u = _match_units(w.get('text', ''))
        if not u:
            continue
            __temp_259931 = w.get('start_ms')
        else:
            w.get('start_ms')
        if not __temp_259931:
            st = float(0)
        else:
            st = float(__temp_259931)
        __temp_259935 = w.get('end_ms')
        if not __temp_259935:
            en = float(st)
        else:
            en = float(__temp_259935)
        span = max(0.0, en - st)
        for __temp_259940 in iter(enumerate(u)):
            __temp_259941, __temp_259942 = __temp_259940
            i = __temp_259941
            tok = __temp_259942
            units.append(tok)
            times.append(st + span * i / len(u))
            continue
        continue
    return units, times



# Original qualified name: _chunk_texts
def _chunk_texts(texts, max_chars):
    chunks = []
    cur = []
    cur_len = 0
    for __temp_259948 in iter(texts):
        t = __temp_259948
        if not t:
            t = ''.strip()
        else:
            t = t.strip()
        if not t:
            continue
            add = len(t) + 1
        else:
            add = len(t) + 1
        if cur:
            if cur_len + add > max_chars:
                chunks.append('\n'.join(cur))
                cur_len = 0
                cur = []
        cur.append(t)
        cur_len += add
        continue
    if cur:
        chunks.append('\n'.join(cur))
        return chunks
    else:
        return chunks



# Original qualified name: _chunk_context
def _chunk_context(base, chunks, index):
    if not base:
        context = dict({})
    else:
        context = dict(base)
    context['chunk_index'] = index + 1
    context['chunk_total'] = len(chunks)
    if index > 0:
        context['previous_text'] = chunks[index - 1][-300:None]
    if index < len(chunks) - 1:
        context['next_text'] = chunks[index + 1][None:300]
    return context



# Original qualified name: _clamp_marks
def _clamp_marks(marks):
    out = []
    prev_end = 0
    for __temp_259965 in iter(marks):
        __temp_259966, __temp_259967 = __temp_259965
        o_s = __temp_259966
        o_e = __temp_259967
        st = max(int(o_s), prev_end)
        en = max(int(o_e), st)
        out.append((st, en))
        prev_end = en
        continue
    return out



# Original qualified name: _film_speed_factor
def _film_speed_factor(dur_ms, slot_ms, tol_ms):
    if not slot_ms <= 0:
        if dur_ms <= slot_ms + max(int(tol_ms), 0):
            return 1.0
    else:
        return 1.0
    return dur_ms / slot_ms



# NOT DECOMPILED: _shorten_prompt


# Original qualified name: _shorten_budget
def _shorten_budget(text, factor, speed_warn, safety):
    if not text:
        n = len(''.strip())
    else:
        n = len(text.strip())
    if not n == 0:
        if factor <= speed_warn:
            return n
    else:
        return n
    return max(8, int(n * (speed_warn / factor) * safety))



# NOT DECOMPILED: _parse_shorten


# Original qualified name: _film_budgets
def _film_budgets(marks, total_ms, spill_max_ms, guard_ms):
    out = []
    n = len(marks)
    for __temp_260001 in iter(enumerate(marks)):
        __temp_260002, __temp_260003 = __temp_260001
        i = __temp_260002
        __temp_260004, __temp_260005 = __temp_260003
        s = __temp_260004
        e = __temp_260005
        slot = max(0, e - s)
        if i + 1 < n:
            room = marks[i + 1][0] - e - guard_ms
        elif total_ms:
            room = total_ms - e
        else:
            room = spill_max_ms
        out.append(slot + max(0, min(int(room), spill_max_ms)))
        continue
    return out



# Original qualified name: _build_film_timeline
def _build_film_timeline(marks, durs_ms):
    out = []
    for __temp_260013 in iter(zip(marks, durs_ms)):
        __temp_260014, __temp_260015 = __temp_260013
        __temp_260016, __temp_260017 = __temp_260014
        o_s = __temp_260016
        _o_e = __temp_260017
        d = __temp_260015
        st = max(int(o_s), 0)
        out.append((st, st + max(int(d), 0)))
        continue
    return out



# NOT DECOMPILED: _interp_times


# NOT DECOMPILED: _align_sentences


# NOT DECOMPILED: _persist_karaoke_words


# NOT DECOMPILED: _karaoke_word_spans


# NOT DECOMPILED: _concat_wavs_smooth


# NOT DECOMPILED: _concat_wavs
