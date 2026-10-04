# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/gcloud_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _http_client
def _http_client():
    __temp_29474 = os.environ.get('HTTPS_PROXY')
    if not __temp_29474:
        __temp_29475 = os.environ.get('HTTP_PROXY')
        if not __temp_29475:
            proxy = None
        else:
            proxy = __temp_29475
    else:
        proxy = __temp_29474
    if proxy:
        return httpx.AsyncClient(timeout=TIMEOUT, proxy=proxy)
    return httpx.AsyncClient(timeout=TIMEOUT)



# NOT DECOMPILED: _get_auth_headers


# NOT DECOMPILED: _get_sa_access_token


# Original qualified name: convert_emotion_tags_to_ssml
def convert_emotion_tags_to_ssml(text):
    if not text:
        return
    processed = text
    processed = re.sub('\\[excited\\]\\s*(.*?)(?=\\[|\\<|$)',
        '<emphasis level="strong"><prosody pitch="+2st" rate="1.05">\\1</prosody></emphasis>'
        , processed, flags=re.DOTALL)
    processed = re.sub('\\[whispers\\]\\s*(.*?)(?=\\[|\\<|$)',
        '<prosody volume="soft" pitch="-1st" rate="0.95">\\1</prosody>',
        processed, flags=re.DOTALL)
    processed = re.sub('\\[cheerful\\]\\s*(.*?)(?=\\[|\\<|$)',
        '<prosody pitch="+2st">\\1</prosody>', processed, flags=re.DOTALL)
    processed = re.sub('\\[soft\\]\\s*(.*?)(?=\\[|\\<|$)',
        '<prosody volume="soft">\\1</prosody>', processed, flags=re.DOTALL)
    processed = re.sub('\\[sad\\]\\s*(.*?)(?=\\[|\\<|$)',
        '<prosody pitch="-2st" rate="0.9">\\1</prosody>', processed, flags=re.
        DOTALL)
    return processed



# Original qualified name: _build_input_payload
def _build_input_payload(text):
    has_ssml = bool(re.search(
        '<(speak|break|prosody|emphasis|say-as|phoneme|sub)', text, re.IGNORECASE))
    has_emotion_tags = bool(re.search(
        '\\[(excited|whispers|cheerful|soft|sad)\\]', text, re.IGNORECASE))
    if not has_ssml:
        if has_emotion_tags:
            ssml_content = convert_emotion_tags_to_ssml(text)
            if not ssml_content.strip().startswith('<speak>'):
                ssml_content = '<speak>' + str(ssml_content) + '</speak>'
            return {'ssml': ssml_content}
    else:
        ssml_content = convert_emotion_tags_to_ssml(text)
        if not ssml_content.strip().startswith('<speak>'):
            ssml_content = '<speak>' + str(ssml_content) + '</speak>'
        return {'ssml': ssml_content}
    return {'text': text}



# Original qualified name: _infer_language_code
def _infer_language_code(voice):
    parts = voice.split('-')
    if len(parts) >= 2:
        return str(parts[0]) + '-' + str(parts[1])
    return vi - VN



# NOT DECOMPILED: _synthesize_bytes


# Original qualified name: list_voices
def list_voices():
    voices = []
    for __temp_29553 in iter(DEFAULT_GCLOUD_VOICES):
        item = __temp_29553
        lang_code = item['locale']
        voices.append({name: item['name'], locale: item['locale'],
            language_code: lang_code, language_name: LANGUAGE_MAP.get(lang_code,
            lang_code), friendly_name: item['friendly'], gender: item['gender'],
            quality: item['quality'], provider: PROVIDER_ID})
        continue
    return voices



# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: GoogleCloudTTSProvider.synthesize
