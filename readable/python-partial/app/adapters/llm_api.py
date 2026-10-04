# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/llm_api.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _read_api_key
def _read_api_key(setting_key):
    with SessionLocal() as __temp_3863:
        db = __temp_3863
        row = db.get(Setting, setting_key)
        if row:
            if row.value:
                row.value.strip()
            else:
                """""".strip()
        else:
            """""".strip()



# Original qualified name: api_key_for
def api_key_for(provider):
    if provider.endpoint_id:
        app = __import__('app.services', fromlist=('llm_endpoint_store',), level=0)
        llm_endpoint_store = app.llm_endpoint_store
        return llm_endpoint_store.api_key_of(provider.endpoint_id)
    return _read_api_key(provider.api_key_setting)



# Original qualified name: _requires_key
def _requires_key(provider):
    if not provider.endpoint_id:
        return True
    app = __import__('app.services', fromlist=('llm_endpoint_store',), level=0)
    llm_endpoint_store = app.llm_endpoint_store
    return not llm_endpoint_store.is_local_url(provider.base_url)



# NOT DECOMPILED: resolve


# NOT DECOMPILED: available_providers
