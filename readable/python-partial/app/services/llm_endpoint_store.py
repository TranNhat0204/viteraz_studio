# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/llm_endpoint_store.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _clean_base_url
def _clean_base_url(raw):
    if not raw:
        url = ''.strip().rstrip('/')
    else:
        url = raw.strip().rstrip('/')
    if not url:
        raise make_error(E.PRECONDITION_MISSING,
            'Thiếu Base URL của endpoint AI.', status_code=422)
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        raise make_error(E.PRECONDITION_MISSING, 
            'Base URL phải bắt đầu bằng http:// hoặc https:// (nhận: ' + repr(
            raw) + ').', status_code=422)
    if not parsed.netloc:
        raise make_error(E.PRECONDITION_MISSING, 'Base URL thiếu tên miền: ' +
            repr(raw), status_code=422)
    return url



# Original qualified name: clean_base_url
def clean_base_url(raw):
    return _clean_base_url(raw)



# NOT DECOMPILED: is_local_url


# Original qualified name: _clean_dialect
def _clean_dialect(raw):
    if not raw:
        __temp_274480 = ''.strip()
    else:
        raw.strip()
    if not __temp_274480:
        value = DEFAULT_DIALECT
    else:
        value = __temp_274480
    if value not in DIALECTS:
        raise make_error(E.PRECONDITION_MISSING, 'Định dạng API ' + repr(value) +
            ' chưa hỗ trợ. Đang có: ' + str(', '.join(DIALECTS)) + '.',
            status_code=422)
    return value



# NOT DECOMPILED: _pos_int


# NOT DECOMPILED: _non_neg_float


# Original qualified name: _clean_models
def _clean_models(raw):
    out = []
    seen = set()
    if not raw:
        __temp_274488 = []
    for __temp_274489 in iter(__temp_274488):
        item = __temp_274489
        if isinstance(item, str):
            item = {'id': item}
        if not isinstance(item, dict):
            continue
            __temp_274493 = item.get('id')
        else:
            item.get('id')
        if not __temp_274493:
            model_id = str('').strip()
        else:
            model_id = str(__temp_274493).strip()
        if model_id:
            if model_id in seen:
                continue
                seen.add(model_id)
                __temp_274500 = item.get('label')
            else:
                seen.add(model_id)
                item.get('label')
        else:
            continue
            seen.add(model_id)
            item.get('label')
        if not __temp_274500:
            out.append({id: model_id, label: str(model_id).strip(),
                max_input_tokens: _pos_int(item.get('max_input_tokens'), 128000
                ), max_output_tokens: _pos_int(item.get('max_output_tokens'), 
                8192), price_in: _non_neg_float(item.get('price_in'), 0.0),
                price_out: _non_neg_float(item.get('price_out'), 0.0),
                price_cache_in: _non_neg_float(item.get('price_cache_in'), 0.0),
                supports_reasoning_effort: bool(item.get(
                'supports_reasoning_effort', False)), honors_temperature: bool(
                item.get('honors_temperature', True))})
        else:
            out.append({id: model_id, label: str(__temp_274500).strip(),
                max_input_tokens: _pos_int(item.get('max_input_tokens'), 128000
                ), max_output_tokens: _pos_int(item.get('max_output_tokens'), 
                8192), price_in: _non_neg_float(item.get('price_in'), 0.0),
                price_out: _non_neg_float(item.get('price_out'), 0.0),
                price_cache_in: _non_neg_float(item.get('price_cache_in'), 0.0),
                supports_reasoning_effort: bool(item.get(
                'supports_reasoning_effort', False)), honors_temperature: bool(
                item.get('honors_temperature', True))})
        continue
    if not out:
        raise make_error(E.PRECONDITION_MISSING,
            "Endpoint phải có ít nhất một model. Bấm 'Lấy danh sách' hoặc thêm tay."
            , status_code=422)
    return out



# Original qualified name: _clean_headers
def _clean_headers(raw):
    if not raw:
        return {}
    if not isinstance(raw, dict):
        raise make_error(E.PRECONDITION_MISSING,
            'Header thêm phải là cặp tên và giá trị.', status_code=422)
    __temp_274546 = set()
    __temp_274546.update(frozenset({'x-api-key', 'content-type', 'authorization'}))
    reserved = __temp_274546
    out = {}
    for __temp_274549 in iter(raw.items()):
        __temp_274550, __temp_274551 = __temp_274549
        key = __temp_274550
        value = __temp_274551
        name = str(key).strip()
        if not name:
            continue
            __temp_274554 = name.lower()
        else:
            name.lower()
        if __temp_274554 in reserved:
            raise make_error(E.PRECONDITION_MISSING, 'Header ' + repr(name) +
                " do hệ thống tự đặt từ API key — bỏ nó khỏi 'Header thêm'.",
                status_code=422)
        out[name] = str(value)
        continue
    return out



# NOT DECOMPILED: _models_of


# NOT DECOMPILED: _key_tail


# Original qualified name: to_public
def to_public(row):
    return {id: row.id, name: row.name, preset_key: row.preset_key, dialect:
        row.dialect, base_url: row.base_url, has_key: bool(row.api_key_enc),
        key_tail: _key_tail(row), models: _models_of(row), default_model: row.
        default_model, timeout_s: row.timeout_s, enabled: bool(row.enabled),
        is_local: is_local_url(row.base_url)}



# NOT DECOMPILED: list_public


# NOT DECOMPILED: get


# NOT DECOMPILED: api_key_of


# NOT DECOMPILED: headers_of


# Original qualified name: _encode_headers
def _encode_headers(headers):
    clean = _clean_headers(headers)
    if not clean:
        return None
    return encrypt_secret(json.dumps(clean, ensure_ascii=False))



# NOT DECOMPILED: _pick_default


# Original qualified name: create
def create(name, base_url, dialect, api_key, models, default_model, preset_key, headers, timeout_s, enabled):
    if not name:
        name = ''.strip()
    else:
        name = name.strip()
    if not name:
        raise make_error(E.PRECONDITION_MISSING, 'Endpoint AI phải có tên.',
            status_code=422)
    clean_models = _clean_models(models)
    if not preset_key:
        __temp_274630 = ''.strip()
    else:
        preset_key.strip()
    if not __temp_274630:
        __temp_274632 = _clean_dialect(dialect)
        __temp_274633 = _clean_base_url(base_url)
    else:
        _clean_dialect(dialect)
        _clean_base_url(base_url)
    if not api_key:
        __temp_274636 = ''.strip()
    else:
        api_key.strip()
    if __temp_274636:
        __temp_274639 = encrypt_secret(api_key.strip())
        __temp_274640 = _encode_headers(headers)
        __temp_274641 = json.dumps(clean_models, ensure_ascii=False)
        __temp_274642 = _pick_default(default_model, clean_models)
        __temp_274645 = max(MIN_TIMEOUT_S, min(MAX_TIMEOUT_S, _pos_int(
            timeout_s, 300)))
    else:
        _encode_headers(headers)
        json.dumps(clean_models, ensure_ascii=False)
        _pick_default(default_model, clean_models)
        max(MIN_TIMEOUT_S, min(MAX_TIMEOUT_S, _pos_int(timeout_s, 300)))
    if enabled:
        row = LlmEndpoint(name=name, preset_key=None, dialect=__temp_274632,
            base_url=__temp_274633, api_key_enc=__temp_274639, headers_enc=
            __temp_274640, models_json=__temp_274641, default_model=
            __temp_274642, timeout_s=__temp_274645, enabled=1)
    else:
        row = LlmEndpoint(name=name, preset_key=None, dialect=__temp_274632,
            base_url=__temp_274633, api_key_enc=__temp_274639, headers_enc=
            __temp_274640, models_json=__temp_274641, default_model=
            __temp_274642, timeout_s=__temp_274645, enabled=0)
    with SessionLocal() as __temp_274655:
        db = __temp_274655
        if db.query(LlmEndpoint).count() >= MAX_ENDPOINTS:
            raise make_error(E.PRECONDITION_MISSING, 'Đã đạt trần ' + str(
                MAX_ENDPOINTS) + ' endpoint AI. Xoá bớt cái không dùng.',
                status_code=422)
        db.add(row)
        db.commit()
        db.refresh(row)
        out = to_public(row)
        log.info('[llm_endpoint] tạo ' + str(out['id']) + ' — ' + str(name) +
            ' (' + str(out['dialect']) + ')')
        return out



# Original qualified name: update
def update(endpoint_id, **fields):
    with SessionLocal() as __temp_274666:
        db = __temp_274666
        if not endpoint_id:
            row = db.get(LlmEndpoint, ''.strip())
        else:
            row = db.get(LlmEndpoint, endpoint_id.strip())
        if row is None:
            raise make_error(E.LLM_API_ENDPOINT_MISSING, 'Endpoint AI ' + repr(
                endpoint_id) + ' không còn tồn tại.', status_code=404)
        if 'name' in fields:
            if not fields['name']:
                __temp_274672 = ''.strip()
            else:
                fields['name'].strip()
            if __temp_274672:
                row.name = fields['name'].strip()
        if 'dialect' in fields:
            if fields['dialect']:
                row.dialect = _clean_dialect(fields['dialect'])
        if 'base_url' in fields:
            if fields['base_url']:
                row.base_url = _clean_base_url(fields['base_url'])
        if 'preset_key' in fields:
            if not fields['preset_key']:
                __temp_274677 = ''.strip()
            else:
                fields['preset_key'].strip()
            if not __temp_274677:
                row.preset_key = None
            else:
                row.preset_key = __temp_274677
        if fields.get('clear_key'):
            row.api_key_enc = None
        else:
            __temp_274680 = fields.get('api_key')
            if not __temp_274680:
                __temp_274681 = ''.strip()
            else:
                __temp_274680.strip()
            if __temp_274681:
                row.api_key_enc = encrypt_secret(fields['api_key'].strip())
        if 'headers' in fields:
            row.headers_enc = _encode_headers(fields['headers'])
        if fields.get('models') is not None:
            clean_models = _clean_models(fields['models'])
            row.models_json = json.dumps(clean_models, ensure_ascii=False)
            __temp_274689 = fields.get('default_model')
            if not __temp_274689:
                row.default_model = _pick_default(row.default_model, clean_models)
            else:
                row.default_model = _pick_default(__temp_274689, clean_models)
        elif fields.get('default_model'):
            row.default_model = _pick_default(fields['default_model'],
                _models_of(row))
        if fields.get('timeout_s') is not None:
            row.timeout_s = max(MIN_TIMEOUT_S, min(MAX_TIMEOUT_S, _pos_int(
                fields['timeout_s'], 300)))
        if fields.get('enabled') is not None:
            if fields['enabled']:
                row.enabled = 1
            else:
                row.enabled = 0
        db.commit()
        db.refresh(row)
        to_public(row)



# Original qualified name: delete
def delete(endpoint_id):
    with SessionLocal() as __temp_274705:
        db = __temp_274705
        if not endpoint_id:
            row = db.get(LlmEndpoint, ''.strip())
        else:
            row = db.get(LlmEndpoint, endpoint_id.strip())
        if row is None:
            return False
        db.delete(row)
        db.commit()
        log.info('[llm_endpoint] xoá ' + str(endpoint_id))
        return True



# NOT DECOMPILED: usages_of


# Original qualified name: usages_of.<locals>._hits
def _hits(value):
    nonlocal prefix
    if not value:
        text = str('').strip()
    else:
        text = str(value).strip()
    if not text == prefix:
        return text.startswith(prefix + '/')
    else:
        return text == prefix

