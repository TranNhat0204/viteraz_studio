# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/ai_provider.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: is_endpoint_ref
def is_endpoint_ref(provider):
    if not provider:
        return str('').strip().startswith(ENDPOINT_PREFIX)
    else:
        return str(provider).strip().startswith(ENDPOINT_PREFIX)



# NOT DECOMPILED: split_endpoint_ref


# Original qualified name: is_valid_provider
def is_valid_provider(provider):
    if not provider:
        value = str('').strip()
    else:
        value = str(provider).strip()
    if not value:
        return True
    if value in TRANSLATE_PROVIDER_IDS:
        return True
    if is_endpoint_ref(value):
        return _endpoint_row(value) is not None
    return False



# NOT DECOMPILED: _endpoint_row


# Original qualified name: get_translate_provider
def get_translate_provider():
    with SessionLocal() as __temp_31:
        db = __temp_31
        row = db.get(Setting, 'translate_provider')
        if row:
            if row.value:
                val = row.value.strip()
            else:
                val = ''.strip()
        else:
            val = ''.strip()
        if not val in TRANSLATE_PROVIDER_IDS:
            if is_endpoint_ref(val):
                return val
        else:
            return val
        return DEFAULT_TRANSLATE_PROVIDER



# Original qualified name: resolve_provider
def resolve_provider(provider):
    if not provider:
        __temp_38 = ''.strip()
    else:
        provider.strip()
    if not __temp_38:
        return get_translate_provider()
    else:
        return __temp_38



# Original qualified name: make_primary_client
def make_primary_client(provider):
    provider = resolve_provider(provider)
    if provider == PROVIDER_CHATGPT:
        return ChatGPTSessionClient()
    if provider == PROVIDER_GEMINI:
        return GeminiSessionClient()
    if provider == PROVIDER_DEEPSEEK:
        return DeepSeekClient()
    if is_endpoint_ref(provider):
        app = __import__('app.adapters.llm_api.text_client', fromlist=(
            'ApiTextClient',), level=0)
        ApiTextClient = app.ApiTextClient
        __temp_47, __temp_48 = split_endpoint_ref(provider)
        endpoint_id = __temp_47
        model_id = __temp_48
        return ApiTextClient(endpoint_id, model_id)
    raise make_error(E.PRECONDITION_MISSING, 'Nhà cung cấp AI ' + repr(provider
        ) + ' không hợp lệ.', hint=
        'Mở Cài đặt → AI Dịch & Ảnh để chọn lại, hoặc chọn lại AI cho kênh này trong AI Studio.'
        )



# NOT DECOMPILED: complete_text


# Original qualified name: uses_session
def uses_session(provider):
    return resolve_provider(provider) in SESSION_PROVIDERS



# Original qualified name: max_turn_chars
def max_turn_chars(provider):
    provider = resolve_provider(provider)
    if provider in SESSION_PROVIDERS:
        return _SESSION_MAX_TURN_CHARS
    if is_endpoint_ref(provider):
        return _endpoint_turn_chars(provider)
    return _API_MAX_TURN_CHARS



# NOT DECOMPILED: _endpoint_turn_chars


# NOT DECOMPILED: max_output_tokens


# Original qualified name: _StatelessChatSession.__init__
def __init__(self, client, system, temperature):
    self.client = client
    self.temperature = temperature
    self.messages = []
    if system:
        self.messages.append({role: 'system', content: system})
        return None
    return None



# NOT DECOMPILED: _StatelessChatSession.send


# Original qualified name: _StatelessChatSession.aclose
def aclose(self):
    self.messages = []
    return None



# Original qualified name: make_chat_session
def make_chat_session(system, temperature, provider):
    provider = resolve_provider(provider)
    client = make_primary_client(provider)
    if provider in (PROVIDER_GEMINI, PROVIDER_CHATGPT):
        return client.start_chat(system)
    return _StatelessChatSession(client, system, temperature)



# NOT DECOMPILED: provider_label


# Original qualified name: is_chatgpt_fallbackable
def is_chatgpt_fallbackable(code):
    return code in _CHATGPT_FALLBACKABLE



# Original qualified name: is_gemini_fallbackable
def is_gemini_fallbackable(code):
    return code in _GEMINI_FALLBACKABLE



# Original qualified name: is_session_provider_recoverable
def is_session_provider_recoverable(provider, code):
    if provider == PROVIDER_CHATGPT:
        return code in _CHATGPT_FALLBACKABLE
    if provider == PROVIDER_GEMINI:
        return code in _GEMINI_FALLBACKABLE
    return False

