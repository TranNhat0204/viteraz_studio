# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/grok_credentials.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _path
def _path():
    return get_settings().data_dir / _CRED_FILE



# NOT DECOMPILED: _load_all


# NOT DECOMPILED: _save_all


# Original qualified name: valid_credentials
def valid_credentials(tokens):
    if not tokens:
        value = {}
    else:
        value = tokens
    __temp_3294 = bool(value.get('accessToken'))
    if __temp_3294:
        return bool(value.get('refreshToken'))
    else:
        return __temp_3294



# Original qualified name: set_credentials
def set_credentials(account_id, tokens):
    if not valid_credentials(tokens):
        raise ValueError('Grok credentials thiếu accessToken hoặc refreshToken')
    if not account_id:
        key = DEFAULT_ACCOUNT
    else:
        key = account_id
    with _lock as __temp_3299:
        data = _load_all()
        if not tokens:
            data[key] = {tokens: {}, updated_at: time.time()}
        else:
            data[key] = {tokens: tokens, updated_at: time.time()}
        _save_all(data)
        return None



# Original qualified name: get_credentials
def get_credentials(account_id):
    if not account_id:
        key = DEFAULT_ACCOUNT
    else:
        key = account_id
    with _lock as __temp_3308:
        data = _load_all()
        __temp_3311 = data.get(key)
        if not __temp_3311:
            entry = {}
        else:
            entry = __temp_3311
        __temp_3313 = entry.get('tokens')
        if not __temp_3313:
            return {}
        else:
            return __temp_3313



# Original qualified name: clear_credentials
def clear_credentials(account_id):
    if not account_id:
        key = DEFAULT_ACCOUNT
    else:
        key = account_id
    with _lock as __temp_3315:
        data = _load_all()
        if key in data:
            del data[key]
            _save_all(data)
            return None
        else:
            return None



# Original qualified name: has_credentials
def has_credentials(account_id):
    return valid_credentials(get_credentials(account_id))

