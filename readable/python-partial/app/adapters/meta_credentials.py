# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/meta_credentials.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _path
def _path():
    return get_settings().data_dir / _CRED_FILE



# NOT DECOMPILED: _load_all


# Original qualified name: _save_all
def _save_all(data):
    p = _path()
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8'
        )
    tmp.replace(p)
    return None



# NOT DECOMPILED: set_credentials


# Original qualified name: get_credentials
def get_credentials(account_id):
    if not account_id:
        key = DEFAULT_ACCOUNT
    else:
        key = account_id
    with _lock as __temp_3927:
        data = _load_all()
        __temp_3930 = data.get(key)
        if not __temp_3930:
            entry = {}
        else:
            entry = __temp_3930
        if not entry.get('cookies'):
            __temp_3933 = {}
            __temp_3934 = entry.get('access_token')
        else:
            entry.get('access_token')
        if not __temp_3934:
            __temp_3936 = entry.get('user_agent')
        else:
            entry.get('user_agent')
        if not __temp_3936:
            return {cookies: __temp_3933, access_token: '', user_agent: ''}
        else:
            return {cookies: __temp_3933, access_token: '', user_agent: __temp_3936
                }



# Original qualified name: clear_credentials
def clear_credentials(account_id):
    if not account_id:
        key = DEFAULT_ACCOUNT
    else:
        key = account_id
    with _lock as __temp_3940:
        data = _load_all()
        if key in data:
            del data[key]
            _save_all(data)
            return None
        else:
            return None



# Original qualified name: has_credentials
def has_credentials(account_id):
    creds = get_credentials(account_id)
    __temp_3946 = bool(creds['cookies'])
    if not __temp_3946:
        return bool(creds['access_token'])
    else:
        return __temp_3946

