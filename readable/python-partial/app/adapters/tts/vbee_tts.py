# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/vbee_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: clear_voices_cache
def clear_voices_cache():
    global _VOICES_CACHE
    _VOICES_CACHE = None
    return None



# Original qualified name: _get_credentials
def _get_credentials():
    __temp_141454 = get_setting_value('vbee_app_id')
    if not __temp_141454:
        app_id = ''.strip()
    else:
        app_id = __temp_141454.strip()
    __temp_141457 = get_setting_value('vbee_token')
    if not __temp_141457:
        token = ''.strip()
    else:
        token = __temp_141457.strip()
    if app_id:
        if not token:
            raise make_error(E.TTS_AUTH,
                "Chưa cấu hình Vbee App-Id / Token. Mở Settings (tab TTS → Vbee) để nhập. Tạo tại studio.vbee.vn/apps → 'Tích hợp API'."
                )
    else:
        raise make_error(E.TTS_AUTH,
            "Chưa cấu hình Vbee App-Id / Token. Mở Settings (tab TTS → Vbee) để nhập. Tạo tại studio.vbee.vn/apps → 'Tích hợp API'."
            )
    return app_id, token



# Original qualified name: _auth_headers
def _auth_headers():
    __temp_141463, __temp_141464 = _get_credentials()
    app_id = __temp_141463
    token = __temp_141464
    return {Authorization: 'Bearer ' + str(token), (App - Id): app_id}



# Original qualified name: _http_client
def _http_client():
    __temp_141466 = os.environ.get('HTTPS_PROXY')
    if not __temp_141466:
        __temp_141467 = os.environ.get('HTTP_PROXY')
        if not __temp_141467:
            proxy = None
        else:
            proxy = __temp_141467
    else:
        proxy = __temp_141466
    if proxy:
        return httpx.AsyncClient(timeout=TIMEOUT, proxy=proxy)
    return httpx.AsyncClient(timeout=TIMEOUT)



# Original qualified name: _raise_for_status
def _raise_for_status(status, body):
    if status in (401, 403):
        raise make_error(E.TTS_AUTH,
            "Vbee từ chối TOKEN (401). App-Id đang đúng (sai App-Id thì Vbee báo 'App is not found'), nên gần như chắc chắn token đã HẾT HẠN hoặc bị thu hồi — token Vbee có thời hạn chọn lúc tạo App. Hãy tạo token mới rồi dán lại (giữ nguyên App-Id)."
            , hint=
            "studio.vbee.vn/apps → mở App đang dùng → 'Tích hợp API' → tạo Token mới."
            )
    if status == 429:
        raise make_error(E.TTS_RATE_LIMIT,
            'Vbee rate limit (429). Thử lại sau ít phút.')
    if status not in (200, 201):
        raise make_error(E.TTS_NETWORK, 'Vbee HTTP ' + str(status) + ': ' + str
            (body[None:200]))
    return None



# Original qualified name: _raise_for_body_error
def _raise_for_body_error(data):
    if not isinstance(data, dict):
        return None
    code = data.get('error_code')
    if not data.get('status') == 0:
        if code:
            __temp_141476 = data.get('error_message')
            if not __temp_141476:
                msg = str('').strip()
            else:
                msg = str(__temp_141476).strip()
            if code == 2001:
                if msg:
                    raise make_error(E.TTS_AUTH, 
                        'Vbee không tìm thấy App: App-Id không tồn tại' + str(
                        ' (' + str(msg) + ')') +
                        '. Kiểm tra lại App-Id đã copy đúng và App chưa bị xoá.',
                        hint=
                        "studio.vbee.vn/apps → mở App → 'Tích hợp API' → copy lại App-Id."
                        )
                else:
                    raise make_error(E.TTS_AUTH, 
                        'Vbee không tìm thấy App: App-Id không tồn tại' + str(
                        '') +
                        '. Kiểm tra lại App-Id đã copy đúng và App chưa bị xoá.',
                        hint=
                        "studio.vbee.vn/apps → mở App → 'Tích hợp API' → copy lại App-Id."
                        )
            if not msg:
                raise make_error(E.TTS_NETWORK, 'Vbee báo lỗi ' + str(code) +
                    ': ' + str('không rõ nguyên nhân'))
                return None
            else:
                raise make_error(E.TTS_NETWORK, 'Vbee báo lỗi ' + str(code) +
                    ': ' + str(msg))
                return None
    else:
        __temp_141485 = data.get('error_message')
        if not __temp_141485:
            msg = str('').strip()
        else:
            msg = str(__temp_141485).strip()
        if code == 2001:
            if msg:
                raise make_error(E.TTS_AUTH, 
                    'Vbee không tìm thấy App: App-Id không tồn tại' + str(' (' +
                    str(msg) + ')') +
                    '. Kiểm tra lại App-Id đã copy đúng và App chưa bị xoá.',
                    hint=
                    "studio.vbee.vn/apps → mở App → 'Tích hợp API' → copy lại App-Id."
                    )
            else:
                raise make_error(E.TTS_AUTH, 
                    'Vbee không tìm thấy App: App-Id không tồn tại' + str('') +
                    '. Kiểm tra lại App-Id đã copy đúng và App chưa bị xoá.',
                    hint=
                    "studio.vbee.vn/apps → mở App → 'Tích hợp API' → copy lại App-Id."
                    )
        if not msg:
            raise make_error(E.TTS_NETWORK, 'Vbee báo lỗi ' + str(code) + ': ' +
                str('không rõ nguyên nhân'))
            return None
        else:
            raise make_error(E.TTS_NETWORK, 'Vbee báo lỗi ' + str(code) + ': ' +
                str(msg))
            return None
    return None



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
    code = v.get('code')
    if not code:
        return None
    lang = _norm_lang(v.get('language_code'))
    __temp_141502 = v.get('gender')
    if not __temp_141502:
        gender = ''.strip().lower()
    else:
        gender = __temp_141502.strip().lower()
    __temp_141507 = v.get('name')
    if not __temp_141507:
        name = code
    else:
        name = __temp_141507
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
    __temp_141510 = LANGUAGE_MAP.get(lang, lang)
    __temp_141511 = v.get('demo')
    if not __temp_141511:
        return {name: code, locale: lang, language_code: lang, language_name:
            __temp_141510, friendly_name: friendly, gender: gender, provider:
            PROVIDER_ID, hot: False, demo: ''}
    else:
        return {name: code, locale: lang, language_code: lang, language_name:
            __temp_141510, friendly_name: friendly, gender: gender, provider:
            PROVIDER_ID, hot: False, demo: __temp_141511}



# NOT DECOMPILED: _fetch_voices_of


# NOT DECOMPILED: _fetch_all_voices


# NOT DECOMPILED: list_voices


# NOT DECOMPILED: _rate_to_speed


# NOT DECOMPILED: _split_chunks


# NOT DECOMPILED: _synthesize_chunk


# Original qualified name: _is_sync_unsupported
def _is_sync_unsupported(e):
    if not e.message:
        return 'not supported in user package' in ''.lower()
    else:
        return 'not supported in user package' in e.message.lower()



# Original qualified name: _check_cancelled
def _check_cancelled(cancel_check):
    if cancel_check:
        if cancel_check():
            raise make_error(E.CANCELLED, 'Đã huỷ khi tạo giọng.')
        return None
    return None



# NOT DECOMPILED: _request_with_retry


# NOT DECOMPILED: _submit_async


# NOT DECOMPILED: _await_async_result


# NOT DECOMPILED: _await_async_result.<locals>._poll_once


# NOT DECOMPILED: _await_async_result.<locals>._download


# NOT DECOMPILED: _synthesize_async


# NOT DECOMPILED: _synthesize_bytes


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: VbeeTTSProvider.synthesize
