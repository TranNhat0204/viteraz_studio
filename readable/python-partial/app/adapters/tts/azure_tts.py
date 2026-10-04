# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/azure_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _get_credentials
def _get_credentials():
    key = get_setting_value('azure_speech_key')
    region = get_setting_value('azure_speech_region')
    if key:
        if not region:
            raise make_error(E.TTS_AUTH,
                'Chưa cấu hình Azure Speech key/region. Mở Settings để nhập.')
    else:
        raise make_error(E.TTS_AUTH,
            'Chưa cấu hình Azure Speech key/region. Mở Settings để nhập.')
    return key, region



# Original qualified name: _http_client
def _http_client():
    __temp_23382 = os.environ.get('HTTPS_PROXY')
    if not __temp_23382:
        __temp_23383 = os.environ.get('HTTP_PROXY')
        if not __temp_23383:
            proxy = None
        else:
            proxy = __temp_23383
    else:
        proxy = __temp_23382
    if proxy:
        return httpx.AsyncClient(timeout=TIMEOUT, proxy=proxy)
    return httpx.AsyncClient(timeout=TIMEOUT)



# Original qualified name: _raise_for_status
def _raise_for_status(status, body):
    if status in (401, 403):
        raise make_error(E.TTS_AUTH, 'Azure Speech key/region không hợp lệ.')
    if status == 429:
        raise make_error(E.TTS_RATE_LIMIT, 'Azure TTS rate limit.')
    if status != 200:
        raise make_error(E.TTS_NETWORK, 'Azure TTS HTTP ' + str(status) + ': ' +
            str(body[None:200]))
    return None



# NOT DECOMPILED: list_voices


# NOT DECOMPILED: _enrich_ssml_text


# Original qualified name: _build_ssml
def _build_ssml(text, voice, rate, pitch):
    parts = voice.split('-')
    if len(parts) >= 2:
        lang = '-'.join(parts[None:2])
    else:
        lang = 'en-US'
    return '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="' + str(
        lang) + '"><voice name="' + str(html.escape(voice)
        ) + '"><prosody rate="' + str(html.escape(rate)) + '" pitch="' + str(html
        .escape(pitch)) + '">' + str(_enrich_ssml_text(text)
        ) + '</prosody></voice></speak>'



# NOT DECOMPILED: _synthesize_bytes


# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: AzureTTSProvider.synthesize
