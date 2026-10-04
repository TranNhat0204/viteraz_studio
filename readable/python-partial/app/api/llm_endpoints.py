# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/llm_endpoints.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: ModelIn.as_dict


# NOT DECOMPILED: list_presets


# Original qualified name: list_endpoints
def list_endpoints():
    return {'endpoints': store.list_public()}



# Original qualified name: list_choices
def list_choices():
    app = __import__('app.db.models', fromlist=('Setting',), level=0)
    Setting = app.Setting
    app = __import__('app.db.session', fromlist=('SessionLocal',), level=0)
    SessionLocal = app.SessionLocal
    with SessionLocal() as __temp_209517:
        db = __temp_209517
        row = db.get(Setting, 'deepseek_api_key')
        if row:
            if not row.value:
                deepseek_ready = bool(''.strip())
            else:
                deepseek_ready = bool(row.value.strip())
        else:
            deepseek_ready = bool(row)
        builtin = [{value: 'deepseek', label: 'DeepSeek', group: 'builtin',
            kind: 'api', has_key: deepseek_ready}, {value: 'chatgpt', label:
            'ChatGPT (web)', group: 'builtin', kind: 'session'}, {value:
            'gemini', label: 'Gemini (web)', group: 'builtin', kind: 'session'}]
        custom = []
        for __temp_209531 in iter(store.list_public(enabled_only=True)):
            ep = __temp_209531
            for __temp_209532 in iter(ep['models']):
                model = __temp_209532
                if not model.get('label'):
                    __temp_209534 = model.get('max_input_tokens')
                else:
                    model.get('max_input_tokens')
                if not ep['has_key']:
                    __temp_209536 = model.get('price_in')
                else:
                    model.get('price_in')
                if not __temp_209536:
                    __temp_209538 = model.get('price_out')
                else:
                    model.get('price_out')
                if not __temp_209538:
                    __temp_209540 = model.get('price_cache_in')
                else:
                    model.get('price_cache_in')
                if not __temp_209540:
                    custom.append({value: 'api:' + str(ep['id']) + '/' + str(
                        model['id']), label: str(ep['name']) + ' · ' + str(
                        model['id']), group: ep['name'], endpoint_id: ep['id'],
                        model_id: model['id'], kind: 'api', is_default_model: 
                        model['id'] == ep['default_model'], max_input_tokens:
                        __temp_209534, has_key: ep['is_local'], price_in: 0,
                        price_out: 0, price_cache_in: 0})
                else:
                    custom.append({value: 'api:' + str(ep['id']) + '/' + str(
                        model['id']), label: str(ep['name']) + ' · ' + str(
                        model['id']), group: ep['name'], endpoint_id: ep['id'],
                        model_id: model['id'], kind: 'api', is_default_model: 
                        model['id'] == ep['default_model'], max_input_tokens:
                        __temp_209534, has_key: ep['is_local'], price_in: 0,
                        price_out: 0, price_cache_in: __temp_209540})
                continue
            continue
        return {'choices': builtin + custom}



# NOT DECOMPILED: _models_payload


# NOT DECOMPILED: create_endpoint


# Original qualified name: update_endpoint
def update_endpoint(endpoint_id, body):
    fields = body.model_dump(exclude_unset=True)
    if 'models' in fields:
        fields['models'] = _models_payload(body)
    __temp_209556 = {}
    __temp_209556.update(fields)
    return store.update(*(endpoint_id,), **__temp_209556)



# Original qualified name: endpoint_usages
def endpoint_usages(endpoint_id):
    return {'usages': store.usages_of(endpoint_id)}



# Original qualified name: delete_endpoint
def delete_endpoint(endpoint_id):
    usages = store.usages_of(endpoint_id)
    if not store.delete(endpoint_id):
        raise make_error(E.LLM_API_ENDPOINT_MISSING, 'Endpoint AI ' + repr(
            endpoint_id) + ' không tồn tại.', status_code=404)
    return {ok: True, affected: usages}



# Original qualified name: _draft_secrets
def _draft_secrets(api_key, headers, endpoint_id):
    if not api_key:
        key = ''.strip()
    else:
        key = api_key.strip()
    if key.startswith('•'):
        key = ''
    if not headers:
        extra = dict({})
    else:
        extra = dict(headers)
    if endpoint_id:
        if not key:
            key = store.api_key_of(endpoint_id)
        if headers is None:
            extra = store.headers_of(endpoint_id)
    return key, extra



# Original qualified name: _draft_dialect
def _draft_dialect(key):
    module = dialects.get(key)
    if module is None:
        raise make_error(E.PRECONDITION_MISSING, 'Định dạng API ' + repr(key) +
            ' chưa hỗ trợ.', status_code=422)
    return module



# Original qualified name: _hint_for
def _hint_for(exc):
    if not exc.message:
        low = ''.lower()
    else:
        low = exc.message.lower()
    if exc.code == E.LLM_API_BAD_RESPONSE:
        if 'model' in low:
            if not 'not supported' in low:
                if not 'not found' in low:
                    if not 'does not exist' in low:
                        if not 'not available' in low:
                            if 'no access' in low:
                                return _MODEL_REJECTED_HINT
                        else:
                            return _MODEL_REJECTED_HINT
                    else:
                        return _MODEL_REJECTED_HINT
                else:
                    return _MODEL_REJECTED_HINT
            else:
                return _MODEL_REJECTED_HINT
    __temp_209576 = _TEST_HINTS.get(exc.code)
    if not __temp_209576:
        return exc.hint
    else:
        return __temp_209576



# Original qualified name: _result_from_error
def _result_from_error(exc, started):
    return {ok: False, error_code: exc.code, message: exc.message, hint:
        _hint_for(exc), latency_ms: int((time.monotonic() - started) * 1000)}



# NOT DECOMPILED: test_endpoint


# NOT DECOMPILED: _http_get


# NOT DECOMPILED: fetch_models
