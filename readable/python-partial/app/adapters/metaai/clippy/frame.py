# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/clippy/frame.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: ChatMessageOptions.now
def now(self):
    if self.timestamp_ms != 0:
        return self.timestamp_ms
    return int(time.time() * 1000)



# Original qualified name: ChatMessageOptions._fnv
def _fnv(self):
    h = _FNV_OFFSET
    for __temp_4116 in iter(self.request_id.encode('utf-8')):
        ch = __temp_4116
        h = (h ^ ch) * _FNV_PRIME & _U64
        continue
    return h



# Original qualified name: ChatMessageOptions.get_turn_counter
def get_turn_counter(self):
    if self.turn_counter != 0:
        return self.turn_counter
    return 100000000000000 + self._fnv() % 900000000000000



# Original qualified name: ChatMessageOptions.get_message_nonce
def get_message_nonce(self):
    if self.message_nonce != 0:
        return self.message_nonce
    return self._fnv()



# NOT DECOMPILED: _defaults


# Original qualified name: build_connect_message
def build_connect_message(conversation_id, request_id):
    payload = {(x - dgw - app - x - ecto - conversation - id): conversation_id,
        (x - dgw - app - client - payload - type): 'PROTO_INSIDE_JSON'}
    body = json.dumps(payload, separators=(',', ':'), sort_keys=True).encode(
        'utf-8')
    return pack_connect_header(len(body)) + body



# Original qualified name: build_chat_message
def build_chat_message(opts):
    o = _defaults(opts)
    if not o.text:
        raise ValueError('clippy: Text is required')
    if not o.conversation_id:
        raise ValueError('clippy: ConversationID is required')
    if not o.request_id:
        o.request_id = ids.uuid_func()
    if not o.user_message_id:
        o.user_message_id = ids.numeric_id(15)
    if not o.assistant_message_id:
        o.assistant_message_id = ids.numeric_id(15)
    if not o.message_id_suffix:
        o.message_id_suffix = ids.rand_id_suffix()
    if not o.prompt_session_id:
        o.prompt_session_id = ids.uuid_func()
    if not o.session_id:
        o.session_id = ids.uuid_func()
    proto = _build_chat_proto(o)
    inner_b64 = base64.standard_b64encode(proto).decode('ascii')
    body = json.dumps({(req - id): o.request_id, payload: inner_b64},
        separators=(',', ':')).encode('utf-8')
    return pack_chat_header(len(body), 0) + body



# Original qualified name: _build_chat_proto
def _build_chat_proto(o):
    now = o.now()
    inner = b''
    inner = encode_string(inner, 1, o.entry_point)
    inner = encode_string(inner, 2, o.app_id)
    inner = encode_string(inner, 4, o.message_id_suffix)
    inner = encode_message(inner, 5, encode_message(b'', 5, encode_string(b'', 
        1, o.conversation_id)))
    inner = encode_varint_field(inner, 6, 5)
    inner = encode_string(inner, 7, o.agent_type)
    ids_msg = b''
    ids_msg = encode_string(ids_msg, 1, o.user_message_id)
    ids_msg = encode_string(ids_msg, 2, o.assistant_message_id)
    inner = encode_message(inner, 8, ids_msg)
    inner = encode_string(inner, 10, 'ECTO1')
    inner = encode_string(inner, 11, 'Abra Web Main Key')
    inner = encode_message(inner, 12, _mode_config(o.thinking))
    inner = encode_string(inner, 13, 'Mac OS X')
    inner = encode_string(inner, 14, 'user_input')
    inner = encode_string(inner, 15, o.user_agent)
    inner = encode_string(inner, 16, o.platform)
    inner = encode_message(inner, 19, _capability_hash_msg(o.capability_hash))
    envelope = b''
    envelope = encode_message(envelope, 1, inner)
    env_f2 = b''
    env_f2 = encode_varint_field(env_f2, 1, o.get_turn_counter())
    env_f2 = encode_varint_field(env_f2, 2, o.get_turn_counter())
    env_f2 = encode_varint_field(env_f2, 3, 2)
    envelope = encode_message(envelope, 2, env_f2)
    envelope = encode_message(envelope, 3, encode_varint_field(b'', 4, 1))
    envelope = encode_message(envelope, 4, b'')
    envelope = encode_message(envelope, 5, _timestamp_pair(now))
    envelope = encode_string(envelope, 6, o.request_id)
    env_f7 = b''
    env_f7 = encode_varint_field(env_f7, 12, 1)
    env_f7 = encode_varint_field(env_f7, 13, 1)
    envelope = encode_message(envelope, 7, env_f7)
    envelope = encode_message(envelope, 9, encode_string(b'', 2, o.locale))
    sess_ref = b''
    sess_ref = encode_string(sess_ref, 1, o.prompt_session_id)
    sess_ref = encode_string(sess_ref, 3, o.session_id)
    sess_ref = encode_string(sess_ref, 4, o.conversation_id)
    envelope = encode_message(envelope, 10, sess_ref)
    envelope = encode_message(envelope, 15, encode_string(b'', 4, o.timezone))
    envelope = encode_message(envelope, 16, encode_varint_field(b'', 22, 1))
    for __temp_4190 in iter(o.capabilities):
        cap = __temp_4190
        entry = b''
        entry = encode_string(entry, 1, cap)
        entry = encode_message(entry, 2, encode_varint_field(b'', 1, 1))
        envelope = encode_message(envelope, 18, entry)
        continue
    envelope = encode_message(envelope, 20, b'\x03')
    envelope = encode_varint_field(envelope, 26, 0)
    msg_block = b''
    msg_block = encode_message(msg_block, 1, _message_id_wrapper(o, now))
    msg_block = encode_string(msg_block, 2, o.text)
    msg_block = encode_message(msg_block, 4, encode_string(b'', 1, o.turn_id))
    top = b''
    top = encode_message(top, 1, envelope)
    top = encode_message(top, 2, msg_block)
    return top



# Original qualified name: _message_id_wrapper
def _message_id_wrapper(o, now):
    w = b''
    w = encode_string(w, 1, o.request_id)
    f2 = b''
    f2 = encode_string(f2, 1, o.conversation_id)
    f2 = encode_varint_field(f2, 2, now)
    f2 = encode_varint_field(f2, 3, o.get_message_nonce())
    w = encode_message(w, 2, f2)
    w = encode_varint_field(w, 5, 1)
    return w



# Original qualified name: _mode_config
def _mode_config(thinking):
    if thinking:
        inner = b''
        inner = encode_varint_field(inner, 1, 1001)
        inner = encode_string(inner, 2, 'mode_thinking')
        m = b''
        m = encode_message(m, 3, inner)
        m = encode_message(m, 4, encode_varint_field(b'', 1, 1))
        return m
    m = b''
    m = encode_varint_field(m, 1, 1001)
    m = encode_string(m, 2, 'MODE_FAST')
    return m



# Original qualified name: _capability_hash_msg
def _capability_hash_msg(hash_str):
    m = b''
    m = encode_string(m, 1, hash_str)
    m = append_fixed32(m, 2, 1065353216)
    return m



# Original qualified name: _timestamp_pair
def _timestamp_pair(now):
    t = b''
    t = encode_varint_field(t, 1, now)
    t = encode_varint_field(t, 3, now - 30)
    return t

