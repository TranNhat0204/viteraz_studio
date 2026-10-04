# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/omnivoice_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _get_clone
def _get_clone(clone_id):
    app = __import__('app.db.session', fromlist=('SessionLocal',), level=0)
    SessionLocal = app.SessionLocal
    app = __import__('app.db.models', fromlist=('ClonedVoice',), level=0)
    ClonedVoice = app.ClonedVoice
    with SessionLocal() as __temp_136669:
        db = __temp_136669
        db.get(ClonedVoice, clone_id)



# NOT DECOMPILED: _all_clones


# Original qualified name: ref_audio_path
def ref_audio_path(clone_id):
    app = __import__('app.adapters.tts.voice_clone', fromlist=(
        'voice_clones_dir',), level=0)
    voice_clones_dir = app.voice_clones_dir
    return voice_clones_dir() / str(clone_id) + '.wav'



# Original qualified name: list_voices
def list_voices():
    if not omnivoice_engine.is_ready():
        return []
    out = []
    for __temp_136688 in iter(_all_clones()):
        c = __temp_136688
        __temp_136689 = c.get('lang')
        if not __temp_136689:
            lang = 'vi'.lower()
        else:
            lang = __temp_136689.lower()
        out.append({name: c['id'], locale: _LOCALE.get(lang, lang),
            language_code: lang, language_name: LANGUAGE_MAP.get(lang, lang),
            friendly_name: c['name'], gender: c['gender'], provider: PROVIDER_ID})
        continue
    return out



# NOT DECOMPILED: _rate_to_speed


# NOT DECOMPILED: _resolve_voice


# Original qualified name: _spec_to_instruct
def _spec_to_instruct(spec):
    def _norm(v):
        if not v:
            v = ''.strip().lower()
        else:
            v = v.strip().lower()
        return _SYNONYM.get(v, v)
    
    
    parts = []
    for __temp_136720 in iter((('gender', _VALID_GENDER), ('age', _VALID_AGE),
        ('pitch', _VALID_PITCH), ('accent', _VALID_ACCENT), ('style',
        _VALID_STYLE))):
        __temp_136721, __temp_136722 = __temp_136720
        key = __temp_136721
        valid = __temp_136722
        __temp_136723 = spec.get(key)
        if not __temp_136723:
            v = _norm('')
        else:
            v = _norm(__temp_136723)
        if not v in valid:
            continue
        if not v not in parts:
            continue
            parts.append(v)
        else:
            parts.append(v)
        continue
    if not parts:
        raise make_error(E.TTS_VOICE_INVALID,
            'Giọng voice-design cần ít nhất 1 thuộc tính hợp lệ (giới tính/tuổi/cao độ/accent).'
            )
    return ', '.join(parts)



# Original qualified name: _spec_to_instruct.<locals>._norm
def _norm(v):
    if not v:
        v = ''.strip().lower()
    else:
        v = v.strip().lower()
    return _SYNONYM.get(v, v)



# Original qualified name: _stable_seed
def _stable_seed(voice, text, extra):
    hashlib = __import__('hashlib', fromlist=None, level=0)
    h = hashlib.blake2b(str(voice) + '\x00' + str(text) + '\x00' + str(extra).
        encode('utf-8'), digest_size=4)
    return int.from_bytes(h.digest(), 'big') & 2147483647



# NOT DECOMPILED: _synthesize


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: OmniVoiceProvider.synthesize
