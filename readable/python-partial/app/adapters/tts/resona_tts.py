# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/resona_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: clear_voices_cache
def clear_voices_cache():
    global _VOICES_CACHE
    _VOICES_CACHE = None
    return None



# Original qualified name: _get_token
def _get_token():
    __temp_136771 = get_setting_value('resona_token')
    if not __temp_136771:
        token = ''.strip()
    else:
        token = __temp_136771.strip()
    if not token:
        raise make_error(E.TTS_AUTH,
            'Chưa cấu hình Resona Token. Mở Settings (tab TTS → Resona) để nhập. Tạo API Access Token tại resona.live/settings.'
            )
    return token



# Original qualified name: _auth_headers
def _auth_headers():
    token = _get_token()
    return {'Authorization': 'Bearer ' + str(token)}



# Original qualified name: _http_client
def _http_client():
    __temp_136777 = os.environ.get('HTTPS_PROXY')
    if not __temp_136777:
        __temp_136778 = os.environ.get('HTTP_PROXY')
        if not __temp_136778:
            proxy = None
        else:
            proxy = __temp_136778
    else:
        proxy = __temp_136777
    if proxy:
        return httpx.AsyncClient(timeout=TIMEOUT, proxy=proxy)
    return httpx.AsyncClient(timeout=TIMEOUT)



# NOT DECOMPILED: _resona_error


# NOT DECOMPILED: _raise_for_status


# Original qualified name: _norm_lang
def _norm_lang(code):
    if not code:
        c = ''.strip().lower()
    else:
        c = code.strip().lower()
    if not c:
        return vi
    return c.split('-')[0]



# Original qualified name: _map_voice
def _map_voice(v):
    voice_id = v.get('voice_id')
    if not voice_id:
        return None
    __temp_136815 = v.get('name')
    if not __temp_136815:
        name = voice_id
    else:
        name = __temp_136815
    __temp_136816 = v.get('gender')
    if not __temp_136816:
        gender = ''.strip().lower()
    else:
        gender = __temp_136816.strip().lower()
    if gender.startswith('f'):
        gender_vi = 'Nữ'
    elif gender.startswith('m'):
        gender_vi = 'Nam'
    else:
        gender_vi = ''
    if gender_vi:
        friendly = str(name) + ' (' + str(gender_vi) + ')'
    else:
        friendly = name
    if v.get('category') == 'cloned':
        friendly += ' [Cloned]'
    __temp_136824 = LANGUAGE_MAP.get('vi', 'Tiếng Việt')
    __temp_136826 = bool(v.get('is_featured'))
    __temp_136827 = v.get('preview_url')
    if not __temp_136827:
        return {name: voice_id, locale: 'vi', language_code: 'vi',
            language_name: __temp_136824, friendly_name: friendly, gender:
            gender, provider: PROVIDER_ID, hot: __temp_136826, demo: ''}
    else:
        return {name: voice_id, locale: 'vi', language_code: 'vi',
            language_name: __temp_136824, friendly_name: friendly, gender:
            gender, provider: PROVIDER_ID, hot: __temp_136826, demo: __temp_136827}



# NOT DECOMPILED: _fetch_all_voices


# NOT DECOMPILED: list_voices


# NOT DECOMPILED: _split_chunks


# NOT DECOMPILED: _synthesize_chunk


# NOT DECOMPILED: _synthesize_bytes


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: ResonaTTSProvider.synthesize
