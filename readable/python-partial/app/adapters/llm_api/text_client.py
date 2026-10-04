# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/llm_api/text_client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: ApiTextClient.__init__
def __init__(self, endpoint_id, model_id):
    app = __import__('app.adapters', fromlist=('llm_api',), level=0)
    llm_api = app.llm_api
    app = __import__('app.adapters.llm_api.registry', fromlist=(
        'ENDPOINT_PREFIX',), level=0)
    ENDPOINT_PREFIX = app.ENDPOINT_PREFIX
    self._api = llm_api.resolve(str(ENDPOINT_PREFIX) + str(endpoint_id), model_id)
    self.endpoint_id = endpoint_id
    self.api_key = self._api.api_key
    return None



# Original qualified name: ApiTextClient._ensure_ready
def _ensure_ready(self):
    return None



# Original qualified name: ApiTextClient.label
def label(self):
    return str(self._api.provider.label) + ' · ' + str(self._api.model.id)



# NOT DECOMPILED: ApiTextClient.test_connection


# NOT DECOMPILED: ApiTextClient._call_api


# Original qualified name: ApiTextClient._translate_error
def _translate_error(self, exc):
    if exc.code == E.LLM_API_CONTEXT_TOO_LONG:
        log.info('[llm_api] ' + str(self.label) +
            ': vượt ngữ cảnh → để lớp cha chia đôi lô')
        return make_error(E.DEEPSEEK_CONTEXT_TOO_LONG, exc.message, hint=exc.hint)
    return exc

