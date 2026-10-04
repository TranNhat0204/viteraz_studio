# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/capcut_tts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: clear_voices_cache
def clear_voices_cache():
    global _VOICES_CACHE
    _VOICES_CACHE = None
    return None



# Original qualified name: _voice_json_path
def _voice_json_path():
    return capcut_client.vendored_dir() / 'Voice.json'



# NOT DECOMPILED: _load_voice_catalog


# Original qualified name: encode_voice
def encode_voice(voice_type, resource_id):
    return str(voice_type) + str(_VOICE_SEP) + str(resource_id)



# NOT DECOMPILED: _decode_voice


# Original qualified name: _lang_code
def _lang_code(entry):
    __temp_23529 = entry.get('lan')
    if not __temp_23529:
        __temp_23530 = entry.get('lang')
        if not __temp_23530:
            __temp_23531 = ''.split('-')
        else:
            __temp_23530.split('-')
        if not __temp_23531[0]:
            code = 'vi'.lower()
        else:
            code = __temp_23531[0].lower()
    else:
        code = __temp_23529.lower()
    if code in LANGUAGE_MAP:
        return code
    return code



# NOT DECOMPILED: list_voices


# NOT DECOMPILED: _parse_rate


# Original qualified name: _build_device
def _build_device(override):
    client = capcut_client.load_client()
    device = deepcopy(client.DEFAULT_DEVICE)
    if not override:
        device.update({})
        return device
    else:
        device.update(override)
        return device



# NOT DECOMPILED: _build_new_request


# NOT DECOMPILED: _build_query_request


# Original qualified name: _extract_task
def _extract_task(resp_json):
    if not resp_json:
        __temp_23586 = {}.get('data')
    else:
        resp_json.get('data')
    if not __temp_23586:
        __temp_23589 = {}.get('tasks')
    else:
        __temp_23586.get('tasks')
    if not __temp_23589:
        tasks = []
    else:
        tasks = __temp_23589
    if not tasks:
        raise make_error(E.TTS_NETWORK, 'CapCut không trả task: ' + str(str(
            resp_json)[None:200]))
    return tasks[0]



# Original qualified name: _task_status
def _task_status(task):
    __temp_23594 = task.get('status')
    if not __temp_23594:
        return str('').lower()
    else:
        return str(__temp_23594).lower()



# NOT DECOMPILED: _find_audio_url


# NOT DECOMPILED: _deep_find_url


# NOT DECOMPILED: _looks_like_audio


# NOT DECOMPILED: _is_rejection


# Original qualified name: _post
def _post(url, headers, body_text, timeout):
    client = capcut_client.load_client()
    if client.requests is None:
        raise make_error(E.TTS_NETWORK, "Thiếu thư viện 'requests' cho CapCut TTS."
            )
    return client.requests.post(url, headers=headers, data=body_text.encode(
        'utf-8'), timeout=timeout)



# NOT DECOMPILED: _submit_and_poll_sync


# Original qualified name: _submit_and_poll_sync.<locals>._cancelled
def _cancelled():
    nonlocal cancel_check
    if cancel_check:
        return bool(cancel_check())
    else:
        return bool(cancel_check)



# NOT DECOMPILED: _split_chunks


# NOT DECOMPILED: _synthesize_bytes


# Original qualified name: _synthesize_bytes.<locals>._chunk_progress
def _chunk_progress(p, msg):
    nonlocal idx, on_progress, total_chunks
    if on_progress:
        overall_p = (idx - 1 + p) / total_chunks
        on_progress(overall_p, '[' + str(idx) + '/' + str(total_chunks) + '] ' +
            str(msg))
        return None
    return None



# NOT DECOMPILED: preview_voice


# NOT DECOMPILED: CapCutTTSProvider.synthesize
