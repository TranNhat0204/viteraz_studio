# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/gemini_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: clear_voices_cache
def clear_voices_cache():
    return None



# Original qualified name: _get_api_key
def _get_api_key():
    __temp_29561 = get_setting_value('gemini_api_key')
    if not __temp_29561:
        key = ''.strip()
    else:
        key = __temp_29561.strip()
    if not key:
        raise make_error(E.TTS_AUTH,
            'Chưa cấu hình Gemini API Key. Mở Settings để nhập.', hint=
            'Tạo API Key miễn phí tại aistudio.google.com/apikey')
    return key



# Original qualified name: _http_client
def _http_client():
    __temp_29565 = os.environ.get('HTTPS_PROXY')
    if not __temp_29565:
        __temp_29566 = os.environ.get('HTTP_PROXY')
        if not __temp_29566:
            proxy = None
        else:
            proxy = __temp_29566
    else:
        proxy = __temp_29565
    if proxy:
        return httpx.AsyncClient(timeout=TIMEOUT, proxy=proxy)
    return httpx.AsyncClient(timeout=TIMEOUT)



# Original qualified name: _one_line
def _one_line(value, limit):
    if not value:
        return ' '.join(str('').split())[None:limit]
    else:
        return ' '.join(str(value).split())[None:limit]



# NOT DECOMPILED: _consistency_seed


# NOT DECOMPILED: parse_rate_mult


# NOT DECOMPILED: parse_pitch_semitones


# NOT DECOMPILED: _language_code


# NOT DECOMPILED: _directed_transcript


# NOT DECOMPILED: _synthesize_bytes


# Original qualified name: list_voices
def list_voices():
    app = __import__('app.adapters.tts.base', fromlist=('LANGUAGE_MAP',), level=0)
    LANGUAGE_MAP = app.LANGUAGE_MAP
    voices = []
    for __temp_29680 in iter(DEFAULT_GEMINI_VOICES):
        item = __temp_29680
        lang_code = item['locale']
        voices.append({name: item['name'], locale: item['locale'],
            language_code: lang_code, language_name: LANGUAGE_MAP.get(lang_code,
            lang_code), friendly_name: item['friendly'], gender: item['gender'],
            provider: PROVIDER_ID})
        continue
    return voices



# NOT DECOMPILED: _apply_gemini_dsp


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: GeminiTTSProvider.synthesize
