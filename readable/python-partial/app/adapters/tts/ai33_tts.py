# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/ai33_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _cache_path
def _cache_path():
    app = __import__('app.config', fromlist=('settings',), level=0)
    settings = app.settings
    return Path(settings.data_dir) / CACHE_FILENAME



# Original qualified name: _key_fingerprint
def _key_fingerprint():
    __temp_23169 = get_setting_value('ai33_api_key')
    if not __temp_23169:
        return hashlib.sha256(''.strip().encode()).hexdigest()[None:16]
    else:
        return hashlib.sha256(__temp_23169.strip().encode()).hexdigest()[None:16]



# NOT DECOMPILED: _load_disk_cache


# NOT DECOMPILED: _save_disk_cache


# NOT DECOMPILED: clear_voices_cache


# Original qualified name: _api_key
def _api_key():
    __temp_23208 = get_setting_value('ai33_api_key')
    if not __temp_23208:
        key = ''.strip()
    else:
        key = __temp_23208.strip()
    if not key:
        raise make_error(E.TTS_AUTH,
            'Chưa cấu hình AI33 API Key. Mở trang TTS → AI33 để nhập key từ ai33.pro.'
            )
    return key



# Original qualified name: _headers
def _headers():
    return {(xi - api - key): _api_key(), Accept: 'application/json'}



# Original qualified name: _client
def _client(timeout):
    __temp_23214 = os.environ.get('HTTPS_PROXY')
    if not __temp_23214:
        __temp_23215 = os.environ.get('HTTP_PROXY')
        if not __temp_23215:
            proxy = None
        else:
            proxy = __temp_23215
    else:
        proxy = __temp_23214
    kwargs = {timeout: timeout, follow_redirects: True}
    if proxy:
        kwargs['proxy'] = proxy
    __temp_23218 = {}
    __temp_23218.update(kwargs)
    return httpx.AsyncClient(*(), **__temp_23218)



# Original qualified name: _raise_http
def _raise_http(status, detail):
    if status in (401, 403):
        raise make_error(E.TTS_AUTH,
            'AI33 từ chối API Key (401/403). Kiểm tra key và quyền sử dụng TTS.')
    if status == 429:
        raise make_error(E.TTS_RATE_LIMIT,
            'AI33 đang giới hạn tần suất (429). Vui lòng thử lại sau.')
    if status >= 400:
        raise make_error(E.TTS_NETWORK, 'AI33 HTTP ' + str(status) + ': ' + str
            (detail[None:300]))
    return None



# Original qualified name: _lang
def _lang(code):
    if not code:
        value = ''.strip().lower().replace('_', '-')
    else:
        value = code.strip().lower().replace('_', '-')
    if value:
        return value.split('-')[0]
    return 'vi'



# Original qualified name: _map_voice
def _map_voice(raw, provider_code):
    __temp_23230 = raw.get('voice_id')
    if not __temp_23230:
        __temp_23231 = raw.get('id')
        if not __temp_23231:
            voice_id = str('').strip()
        else:
            voice_id = str(__temp_23231).strip()
    else:
        voice_id = str(__temp_23230).strip()
    if not voice_id:
        return None
    __temp_23238 = raw.get('language')
    if not __temp_23238:
        language = _lang(raw.get('language_code'))
    else:
        language = _lang(__temp_23238)
    if '_' in voice_id:
        prefix = voice_id.split('_')[0].lower()
    else:
        prefix = ''
    if not provider_code:
        if prefix in VOICE_PROVIDERS:
            v_provider = prefix
        else:
            v_provider = DEFAULT_VOICE_PROVIDER
    else:
        v_provider = provider_code
    __temp_23244 = raw.get('category')
    if not __temp_23244:
        category = str('').lower()
    else:
        category = str(__temp_23244).lower()
    __temp_23249 = raw.get('language')
    if not __temp_23249:
        __temp_23250 = str(language)
        __temp_23251 = LANGUAGE_MAP.get(language, language)
        __temp_23252 = raw.get('name')
    else:
        str(__temp_23249)
        LANGUAGE_MAP.get(language, language)
        raw.get('name')
    if not __temp_23252:
        __temp_23256 = str(voice_id)
        __temp_23257 = raw.get('gender')
    else:
        str(__temp_23252)
        raw.get('gender')
    if not __temp_23257:
        __temp_23261 = str('').lower()
        __temp_23262 = raw.get('preview_url')
    else:
        str(__temp_23257).lower()
        raw.get('preview_url')
    if not __temp_23262:
        __temp_23266 = str('')
        __temp_23267 = raw.get('description')
    else:
        str(__temp_23262)
        raw.get('description')
    if not __temp_23267:
        __temp_23270 = str('')
        __temp_23271 = raw.get('accent')
    else:
        str(__temp_23267)
        raw.get('accent')
    if not __temp_23271:
        __temp_23274 = str('')
        __temp_23275 = raw.get('age')
    else:
        str(__temp_23271)
        raw.get('age')
    if not __temp_23275:
        return {name: voice_id, locale: __temp_23250, language_code: language,
            language_name: __temp_23251, friendly_name: __temp_23256, gender:
            __temp_23261, provider: PROVIDER_ID, voice_provider: v_provider,
            hot: category == 'premade', demo: __temp_23266, description:
            __temp_23270[None:DESCRIPTION_LIMIT], accent: __temp_23274, age:
            str(''), category: category}
    else:
        return {name: voice_id, locale: __temp_23250, language_code: language,
            language_name: __temp_23251, friendly_name: __temp_23256, gender:
            __temp_23261, provider: PROVIDER_ID, voice_provider: v_provider,
            hot: category == 'premade', demo: __temp_23266, description:
            __temp_23270[None:DESCRIPTION_LIMIT], accent: __temp_23274, age:
            str(__temp_23275), category: category}



# NOT DECOMPILED: _fetch_page


# NOT DECOMPILED: _fetch_voices


# Original qualified name: _fetch_voices.<locals>._absorb
def _absorb(payload):
    nonlocal provider, seen_ids, voices
    added = 0
    if not payload.get('data'):
        __temp_23303 = []
    for __temp_23304 in iter(__temp_23303):
        raw = __temp_23304
        mapped = _map_voice(raw, provider)
        if not mapped:
            continue
        if not mapped['name'] not in seen_ids:
            continue
            seen_ids.add(mapped['name'])
            voices.append(mapped)
            added += 1
        else:
            seen_ids.add(mapped['name'])
            voices.append(mapped)
            added += 1
        continue
    return added



# NOT DECOMPILED: _fetch_voices.<locals>._one


# Original qualified name: _merge_sorted
def _merge_sorted(chunks):
    merged = []
    seen = set()
    for __temp_23312 in iter(chunks):
        chunk = __temp_23312
        if isinstance(chunk, BaseException):
            log.warning('Một nguồn giọng AI33 nạp lỗi: ' + str(chunk))
            continue
        if not chunk:
            __temp_23315 = []
        for __temp_23316 in iter(__temp_23315):
            item = __temp_23316
            if not item['name'] not in seen:
                continue
                seen.add(item['name'])
                merged.append(item)
            else:
                seen.add(item['name'])
                merged.append(item)
            continue
        continue
    
    
    def __temp_23321(item):
        return not item.get('hot'), item['language_code'] != 'vi', item[
            'voice_provider'], item['friendly_name']
    
    
    merged.sort(key=__temp_23321)
    return merged



# NOT DECOMPILED: _fetch_all


# NOT DECOMPILED: _warm_full_catalog


# NOT DECOMPILED: _schedule_warm


# NOT DECOMPILED: list_voices


# NOT DECOMPILED: _speed


# NOT DECOMPILED: _create_task


# NOT DECOMPILED: _wait_for_audio


# NOT DECOMPILED: _download_audio


# NOT DECOMPILED: _synthesize_bytes


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: AI33TTSProvider.synthesize
