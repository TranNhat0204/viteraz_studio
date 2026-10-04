# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/llm_api/registry.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: ProviderSpec.get_model


# Original qualified name: ProviderSpec.resolve_model
def resolve_model(self, model_id):
    __temp_3764 = self.get_model(model_id)
    if not __temp_3764:
        __temp_3765 = self.get_model(self.default_model)
        if not __temp_3765:
            return self.models[0]
        else:
            return __temp_3765
    else:
        return __temp_3764



# Original qualified name: ProviderSpec.chat_url
def chat_url(self):
    module = dialects.get(self.dialect)
    if module is None:
        return self.base_url.rstrip('/') + '/chat/completions'
    return module.url(self.base_url)



# NOT DECOMPILED: _parse_model


# NOT DECOMPILED: _parse_provider


# Original qualified name: clear_cache
def clear_cache():
    global _cache
    _cache = None
    return None



# NOT DECOMPILED: load_catalog


# NOT DECOMPILED: endpoint_to_provider


# NOT DECOMPILED: list_endpoint_providers


# Original qualified name: list_providers
def list_providers(include_endpoints):
    out = list(load_catalog())
    if include_endpoints:
        out.extend(list_endpoint_providers())
        return out
    else:
        return out



# NOT DECOMPILED: get_provider
