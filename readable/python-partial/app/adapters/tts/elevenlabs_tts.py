# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/elevenlabs_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: clear_voices_cache
def clear_voices_cache():
    global _VOICES_CACHE
    _VOICES_CACHE = None
    return None



# Original qualified name: _get_api_key
def _get_api_key():
    __temp_29426 = get_setting_value('elevenlabs_api_key')
    if not __temp_29426:
        key = ''.strip()
    else:
        key = __temp_29426.strip()
    if not key:
        raise make_error(E.TTS_AUTH,
            'Chưa cấu hình ElevenLabs API key. Mở Settings để nhập.')
    return key



# Original qualified name: _get_model
def _get_model():
    __temp_29430 = get_setting_value('elevenlabs_model')
    if not __temp_29430:
        return DEFAULT_MODEL
    else:
        return __temp_29430



# Original qualified name: _http_client
def _http_client():
    __temp_29431 = os.environ.get('HTTPS_PROXY')
    if not __temp_29431:
        __temp_29432 = os.environ.get('HTTP_PROXY')
        if not __temp_29432:
            proxy = None
        else:
            proxy = __temp_29432
    else:
        proxy = __temp_29431
    if proxy:
        return httpx.AsyncClient(timeout=TIMEOUT, proxy=proxy)
    return httpx.AsyncClient(timeout=TIMEOUT)



# Original qualified name: _raise_for_status
def _raise_for_status(status, body):
    if status in (401, 403):
        raise make_error(E.TTS_AUTH,
            "ElevenLabs từ chối API key (401/403). Kiểm tra: (1) key đã copy ĐÚNG và ĐỦ (không thừa/thiếu ký tự); (2) key có quyền 'Voices → Read' (key mới của ElevenLabs cho phép giới hạn quyền — hãy tạo key với full access hoặc bật quyền đọc giọng); (3) key đúng workspace/tài khoản còn hiệu lực."
            , hint=
            'Tạo lại API key tại elevenlabs.io → Profile → API Keys, chọn quyền đầy đủ (Has access to all).'
            )
    if status == 429:
        raise make_error(E.TTS_RATE_LIMIT, 'ElevenLabs rate limit.')
    if status != 200:
        raise make_error(E.TTS_NETWORK, 'ElevenLabs HTTP ' + str(status) + ': ' +
            str(body[None:200]))
    return None



# NOT DECOMPILED: _load_lib_map


# Original qualified name: _save_lib_map
def _save_lib_map(m):
    app = __import__('app.db.session', fromlist=('SessionLocal',), level=0)
    SessionLocal = app.SessionLocal
    app = __import__('app.db.models', fromlist=('Setting',), level=0)
    Setting = app.Setting
    with SessionLocal() as __temp_29444:
        db = __temp_29444
        row = db.get(Setting, _LIB_MAP_SETTING)
        val = json.dumps(m, ensure_ascii=False)
        if row:
            row.value = val
            db.commit()
            return None
        else:
            db.add(Setting(key=_LIB_MAP_SETTING, value=val))
            db.commit()
            return None



# NOT DECOMPILED: _fetch_voices_v2


# NOT DECOMPILED: _get_account_voices_raw


# NOT DECOMPILED: _fetch_account_voices


# NOT DECOMPILED: _fetch_trending_voices


# NOT DECOMPILED: list_voices


# NOT DECOMPILED: _find_account_voice_id_by_name


# NOT DECOMPILED: _resolve_voice_id


# NOT DECOMPILED: _synthesize_bytes


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: ElevenLabsProvider.synthesize
