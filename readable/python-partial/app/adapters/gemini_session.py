# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/gemini_session.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: get_gemini_model
def get_gemini_model():
    with SessionLocal() as __temp_3206:
        db = __temp_3206
        row = db.get(Setting, 'gemini_model')
        if row:
            if row.value:
                val = row.value.strip()
            else:
                val = ''.strip()
        else:
            val = ''.strip()
        val = GEMINI_MODEL_MIGRATION.get(val, val)
        if val in GEMINI_MODEL_IDS:
            return val
        return DEFAULT_GEMINI_MODEL



# Original qualified name: GeminiSessionClient.__init__
def __init__(self, bridge_url, token, model):
    st = get_settings()
    if not bridge_url:
        if not st.gemini_bridge_url:
            self.bridge_url = ''.rstrip('/')
        else:
            self.bridge_url = st.gemini_bridge_url.rstrip('/')
    else:
        self.bridge_url = bridge_url.rstrip('/')
    if not token:
        self.token = st.token
    else:
        self.token = token
    if not model:
        self.model = get_gemini_model()
    else:
        self.model = model
    return None



# Original qualified name: GeminiSessionClient.available
def available(self):
    return bool(self.bridge_url)



# NOT DECOMPILED: GeminiSessionClient.get_status


# NOT DECOMPILED: GeminiSessionClient._post_complete


# NOT DECOMPILED: GeminiSessionClient._complete


# NOT DECOMPILED: GeminiSessionClient._delete_conversation


# Original qualified name: GeminiSessionClient.start_chat
def start_chat(self, system):
    return _GeminiChatSession(self, system)



# NOT DECOMPILED: GeminiSessionClient._call_api


# NOT DECOMPILED: GeminiSessionClient.translate_batch


# NOT DECOMPILED: GeminiSessionClient.rewrite_batch


# Original qualified name: GeminiSessionClient._merge
def _merge(self, batch, texts):
    merged = []
    for __temp_3265 in iter(enumerate(batch)):
        __temp_3266, __temp_3267 = __temp_3265
        idx = __temp_3266
        seg = __temp_3267
        if idx < len(texts):
            if texts[idx]:
                text = texts[idx]
            else:
                text = seg.get('text', '')
        else:
            text = seg.get('text', '')
        merged.append({seq: seg['seq'], start_ms: seg['start_ms'], end_ms: seg[
            'end_ms'], text: text})
        continue
    return merged



# Original qualified name: _GeminiChatSession.__init__
def __init__(self, client, system):
    self.client = client
    self.conversation = None
    if not system:
        self._pending_system = ''.strip()
    else:
        self._pending_system = system.strip()
    return None



# NOT DECOMPILED: _GeminiChatSession.send


# NOT DECOMPILED: _GeminiChatSession.aclose
