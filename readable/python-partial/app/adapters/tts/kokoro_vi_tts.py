# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/kokoro_vi_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _ensure_local_kokoro_vi


# NOT DECOMPILED: _load_kokoro_vi_cls


# Original qualified name: _load_soundfile
def _load_soundfile():
    _ensure_local_kokoro_vi()
    soundfile = __import__('soundfile', fromlist=None, level=0)
    sf = soundfile
    return sf



# Original qualified name: _load_numpy
def _load_numpy():
    _ensure_local_kokoro_vi()
    numpy = __import__('numpy', fromlist=None, level=0)
    np = numpy
    return np



# Original qualified name: _is_vi_voice
def _is_vi_voice(voice):
    return voice in KOKORO_VI_VOICES



# Original qualified name: _is_kokoro_vi_installed
def _is_kokoro_vi_installed():
    return _load_kokoro_vi_cls() is not None



# Original qualified name: reset_voices_cache
def reset_voices_cache():
    global _VOICES_CACHE
    _VOICES_CACHE = None
    return None



# NOT DECOMPILED: _build_kokoro_vi


# Original qualified name: _apply_vi_voice
def _apply_vi_voice(engine, voice):
    if voice in _VI_VOICEPACK_CACHE:
        engine.voicepack = _VI_VOICEPACK_CACHE[voice]
        return None
    torch = __import__('torch', fromlist=None, level=0)
    kokoro_vietnamese = __import__('kokoro_vietnamese.core', fromlist=(
        'DEFAULT_HF_REPO_ID', 'DEFAULT_VOICEPACK_FILE',
        'resolve_voicepack_filename', '_download_or_resolve'), level=0)
    DEFAULT_HF_REPO_ID = kokoro_vietnamese.DEFAULT_HF_REPO_ID
    DEFAULT_VOICEPACK_FILE = kokoro_vietnamese.DEFAULT_VOICEPACK_FILE
    resolve_voicepack_filename = kokoro_vietnamese.resolve_voicepack_filename
    _download_or_resolve = kokoro_vietnamese._download_or_resolve
    vp_filename = resolve_voicepack_filename(voice, None)
    vp_path = _download_or_resolve(DEFAULT_HF_REPO_ID, DEFAULT_VOICEPACK_FILE,
        vp_filename)
    pack = torch.load(vp_path, map_location='cpu', weights_only=True)
    _VI_VOICEPACK_CACHE[voice] = pack
    engine.voicepack = pack
    return None



# NOT DECOMPILED: _synthesize_vi


# Original qualified name: _synthesize_vi.<locals>._generate
def _generate():
    nonlocal speed, text, voice
    engine = _build_kokoro_vi()
    _apply_vi_voice(engine, voice)
    __temp_29807, __temp_29808 = engine.synthesize(text, speed=float(speed))
    audio = __temp_29807
    _phonemes = __temp_29808
    return audio



# NOT DECOMPILED: _rate_to_speed


# NOT DECOMPILED: list_voices


# NOT DECOMPILED: _synthesize_bytes


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: KokoroViTTSProvider.synthesize
