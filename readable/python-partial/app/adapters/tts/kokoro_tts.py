# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/kokoro_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _ensure_local_kokoro


# NOT DECOMPILED: _kokoro_installed_on_disk


# NOT DECOMPILED: _load_kpipeline_cls


# NOT DECOMPILED: _load_kmodel


# Original qualified name: _load_soundfile
def _load_soundfile():
    _ensure_local_kokoro()
    soundfile = __import__('soundfile', fromlist=None, level=0)
    sf = soundfile
    return sf



# Original qualified name: _load_numpy
def _load_numpy():
    _ensure_local_kokoro()
    numpy = __import__('numpy', fromlist=None, level=0)
    np = numpy
    return np



# Original qualified name: reset_voices_cache
def reset_voices_cache():
    global _VOICES_CACHE
    _VOICES_CACHE = None
    return None



# Original qualified name: _voice_to_lang
def _voice_to_lang(voice):
    info = KOKORO_VOICES.get(voice)
    if info:
        return info['lang']
    parts = voice.split('_', 1)
    if len(parts) > 1:
        if len(parts[0]) >= 2:
            return parts[0][1]
    return 'a'



# NOT DECOMPILED: _rate_to_speed


# NOT DECOMPILED: _get_pipeline


# Original qualified name: _get_pipeline.<locals>._build
def _build():
    nonlocal kpipeline_cls, lang_code
    model = _load_kmodel()
    return kpipeline_cls(lang_code=lang_code, model=model)



# NOT DECOMPILED: list_voices


# NOT DECOMPILED: _clean_text_for_kokoro


# NOT DECOMPILED: _clean_text_for_kokoro.<locals>._replace_dollar


# NOT DECOMPILED: _synthesize_bytes


# Original qualified name: _synthesize_bytes.<locals>._generate
def _generate():
    nonlocal clean_text, pipeline, speed, voice
    parts = []
    for __temp_29752 in iter(pipeline(clean_text, voice=voice, speed=speed,
        split_pattern='[.?!]+[\\s\\n]+|\\n+')):
        __temp_29753, __temp_29754, __temp_29755 = __temp_29752
        _gs = __temp_29753
        _ps = __temp_29754
        audio = __temp_29755
        if audio is None:
            continue
            __temp_29756 = len(audio)
        else:
            len(audio)
        if not __temp_29756 > 0:
            continue
            parts.append(audio)
        else:
            parts.append(audio)
        continue
    return parts



# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: KokoroTTSProvider.synthesize


# Original qualified name: KokoroTTSProvider.synthesize.<locals>._generate
def _generate():
    nonlocal cancel_check, clean_text, pipeline, speed, voice
    parts = []
    for __temp_29768 in iter(pipeline(clean_text, voice=voice, speed=speed,
        split_pattern='[.?!]+[\\s\\n]+|\\n+')):
        __temp_29769, __temp_29770, __temp_29771 = __temp_29768
        _gs = __temp_29769
        _ps = __temp_29770
        audio = __temp_29771
        if cancel_check:
            if cancel_check():
                raise make_error(E.CANCELLED, 'Đã huỷ khi tạo giọng.')
        if audio is None:
            continue
            __temp_29774 = len(audio)
        else:
            len(audio)
        if not __temp_29774 > 0:
            continue
            parts.append(audio)
        else:
            parts.append(audio)
        continue
    return parts

