# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/clippy/parse.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _type_proto_payload
def _type_proto_payload(data):
    if data:
        if not data[0] != TYPE_PROTO:
            if len(data) < 8:
                return None, False
        else:
            return None, False
    else:
        return None, False
    payload_len = data[3] | data[4] << 8
    if 8 + payload_len > len(data):
        payload_len = len(data) - 8
        if payload_len < 0:
            payload_len = 0
    return data[8:8 + payload_len], True



# Original qualified name: Frame.__init__
def __init__(self):
    self.type = 0
    self.seq = 0
    self.sub_type = 0
    self.payload = None
    self.inner_proto = None
    self.raw = b''
    return None



# NOT DECOMPILED: parse_frame


# NOT DECOMPILED: _extract_field5_json


# Original qualified name: is_full_response
def is_full_response(data):
    __temp_9223, __temp_9224, __temp_9225 = response_text_info(data)
    _ = __temp_9223
    _ = __temp_9224
    is_full = __temp_9225
    return is_full



# NOT DECOMPILED: response_seq


# Original qualified name: response_text
def response_text(data):
    __temp_9237, __temp_9238, __temp_9239 = response_text_info(data)
    txt = __temp_9237
    ok = __temp_9238
    _ = __temp_9239
    return txt, ok



# NOT DECOMPILED: response_text_info


# Original qualified name: _extract_proto_delta_text
def _extract_proto_delta_text(proto):
    __temp_9276, __temp_9277 = _read_field(proto, 1)
    f1 = __temp_9276
    ok = __temp_9277
    if not ok:
        return '', False, False
    __temp_9279, __temp_9280 = _read_field(f1, 4)
    f4 = __temp_9279
    ok = __temp_9280
    if not ok:
        return '', False, False
    __temp_9282, __temp_9283 = _read_field_string(f4, 1)
    delta = __temp_9282
    ok = __temp_9283
    if ok:
        if delta:
            return delta, True, False
    __temp_9285, __temp_9286 = _read_field_string(f4, 2)
    full = __temp_9285
    ok = __temp_9286
    if ok:
        if full:
            return full, True, True
    return '', False, False



# NOT DECOMPILED: _read_field


# Original qualified name: _read_field_string
def _read_field_string(proto, field_num):
    __temp_11022, __temp_11023 = _read_field(proto, field_num)
    payload = __temp_11022
    ok = __temp_11023
    if not ok:
        return '', False
    return payload.decode('utf-8', 'ignore'), True



# Original qualified name: _skip_field
def _skip_field(proto, off, wt):
    if wt == 0:
        __temp_11026, __temp_11027, __temp_11028 = read_varint(proto, off)
        _ = __temp_11026
        n = __temp_11027
        ok = __temp_11028
        if not ok:
            return off, False
        return off + n, True
    if wt == 1:
        if off + 8 > len(proto):
            return off, False
        return off + 8, True
    if wt == 5:
        if off + 4 > len(proto):
            return off, False
        return off + 4, True
    return off, False



# NOT DECOMPILED: _extract_embedded_json


# NOT DECOMPILED: _first_delta


# Original qualified name: _join_section_text
def _join_section_text(sections):
    if not isinstance(sections, list):
        return
    parts = []
    for __temp_11044 in iter(sections):
        sec = __temp_11044
        if not isinstance(sec, dict):
            continue
            vm = sec.get('view_model')
        else:
            vm = sec.get('view_model')
        if not isinstance(vm, dict):
            continue
            prim = vm.get('primitive')
        else:
            prim = vm.get('primitive')
        if not isinstance(prim, dict):
            continue
            t = prim.get('text')
        else:
            t = prim.get('text')
        if not isinstance(t, str):
            continue
        if not t:
            continue
            parts.append(t)
        else:
            parts.append(t)
        continue
    if not parts:
        return
    return '\n'.join(parts)

