# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/chatgpt_credentials.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _path
def _path():
    return get_settings().data_dir / _CRED_FILE



# NOT DECOMPILED: _load_all


# NOT DECOMPILED: _save_all


# Original qualified name: valid_credentials
def valid_credentials(tokens):
    if not tokens:
        nested = {}.get('tokens')
    else:
        nested = tokens.get('tokens')
    __temp_181 = isinstance(nested, dict)
    if __temp_181:
        __temp_183 = bool(nested.get('access_token'))
        if __temp_183:
            return bool(nested.get('refresh_token'))
        else:
            return __temp_183
    else:
        return __temp_181



# Original qualified name: set_credentials
def set_credentials(account_id, tokens):
    if not valid_credentials(tokens):
        raise ValueError(
            'ChatGPT credentials thiếu access_token hoặc refresh_token')
    if not account_id:
        key = DEFAULT_ACCOUNT
    else:
        key = account_id
    with _lock as __temp_188:
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
    with _lock as __temp_197:
        data = _load_all()
        __temp_200 = data.get(key)
        if not __temp_200:
            entry = {}
        else:
            entry = __temp_200
        __temp_202 = entry.get('tokens')
        if not __temp_202:
            return {}
        else:
            return __temp_202



# Original qualified name: clear_credentials
def clear_credentials(account_id):
    if not account_id:
        key = DEFAULT_ACCOUNT
    else:
        key = account_id
    with _lock as __temp_204:
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

