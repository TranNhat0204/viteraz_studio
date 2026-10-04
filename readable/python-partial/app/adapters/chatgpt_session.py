# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/chatgpt_session.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: complete_and_parse


# Original qualified name: _extract_json_array
def _extract_json_array(raw):
    cleaned = _strip_md_fences(raw.strip())
    arr = _find_balanced_array(cleaned)
    if arr is not None:
        return arr
    return cleaned



# NOT DECOMPILED: _combine_messages


# Original qualified name: ChatGPTSessionClient.__init__
def __init__(self, bridge_url, token):
    st = get_settings()
    if not bridge_url:
        if not st.chatgpt_bridge_url:
            self.bridge_url = ''.rstrip('/')
        else:
            self.bridge_url = st.chatgpt_bridge_url.rstrip('/')
    else:
        self.bridge_url = bridge_url.rstrip('/')
    if not token:
        self.token = st.token
    else:
        self.token = token
    return None



# Original qualified name: ChatGPTSessionClient.available
def available(self):
    return bool(self.bridge_url)



# NOT DECOMPILED: ChatGPTSessionClient.get_status


# NOT DECOMPILED: ChatGPTSessionClient._post_complete


# NOT DECOMPILED: ChatGPTSessionClient._complete


# NOT DECOMPILED: ChatGPTSessionClient._post_image


# Original qualified name: ChatGPTSessionClient._write_data_url
def _write_data_url(data_url, out_path):
    b64 = data_url
    if data_url.startswith('data:'):
        comma = data_url.find(',')
        if comma >= 0:
            b64 = data_url[comma + 1:None]
        else:
            b64 = ''
    if not b64:
        raise make_error(E.CHATGPT_BAD_RESPONSE,
            'Ảnh ChatGPT rỗng (dataURL không hợp lệ).')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(base64.b64decode(b64))
    return out_path



# NOT DECOMPILED: ChatGPTSessionClient.generate_image


# NOT DECOMPILED: ChatGPTSessionClient.delete_conversation


# Original qualified name: ChatGPTSessionClient.start_chat
def start_chat(self, system):
    return _ChatGPTChatSession(self, system)



# NOT DECOMPILED: ChatGPTSessionClient._call_api


# NOT DECOMPILED: ChatGPTSessionClient.translate_batch


# NOT DECOMPILED: ChatGPTSessionClient.rewrite_batch


# Original qualified name: ChatGPTSessionClient._merge
def _merge(self, batch, texts):
    merged = []
    for __temp_287 in iter(enumerate(batch)):
        __temp_288, __temp_289 = __temp_287
        idx = __temp_288
        seg = __temp_289
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



# Original qualified name: _ChatGPTChatSession.__init__
def __init__(self, client, system):
    self.client = client
    self.conversation = None
    if not system:
        self._pending_system = ''.strip()
    else:
        self._pending_system = system.strip()
    return None



# NOT DECOMPILED: _ChatGPTChatSession.send


# NOT DECOMPILED: _ChatGPTChatSession.aclose
