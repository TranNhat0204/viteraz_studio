# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/clippy/template.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: build_from_template
def build_from_template(opts):
    if not opts.template_b64:
        raise ValueError('clippy: TemplateB64 is required')
    if not opts.template_text:
        raise ValueError('clippy: TemplateText is required (the marker to locate)')
    if not opts.new_text:
        raise ValueError('clippy: NewText is required')
    if not opts.conversation_id:
        raise ValueError('clippy: ConversationID is required')
    tpl = base64.standard_b64decode(opts.template_b64)
    if not len(tpl) < 9:
        if tpl[0] != 13:
            raise ValueError(
                'clippy: template is not a type-0x0d frame (byte0=0x' + format(
                tpl[0], '02x') + ')')
    else:
        raise ValueError('clippy: template is not a type-0x0d frame (byte0=0x' +
            format(tpl[0], '02x') + ')')
    outer = json.loads(tpl[8:None])
    outer_req_id = outer.get('req-id', '')
    inner = base64.standard_b64decode(outer['payload'])
    if not opts.request_id:
        new_req_id = ids.uuid_func()
    else:
        new_req_id = opts.request_id
    inner = _replace_all_text_field_values(inner, opts.template_text, opts.new_text
        )
    tpl_conv = _extract_template_conversation_id(inner)
    if not tpl_conv:
        raise ValueError('clippy: could not locate template conversation id')
    if tpl_conv != opts.conversation_id:
        inner = _bytes_replace_all(inner, tpl_conv.encode(), opts.
            conversation_id.encode())
    if outer_req_id:
        if outer_req_id != new_req_id:
            inner = _bytes_replace_all(inner, outer_req_id.encode(), new_req_id
                .encode())
    if opts.media_id:
        if not opts.media_mime:
            mime = 'image/jpeg'
        else:
            mime = opts.media_mime
        if not opts.media_filename:
            filename = 'upload.png'
        else:
            filename = opts.media_filename
        inner = _replace_all_text_field_values(inner, '867051314767696', opts.
            media_id)
        inner = _replace_all_text_field_values(inner, 'student_card.png', filename)
        inner = _replace_all_text_field_values(inner, 'image/png', mime)
        inner = _inject_attachment(inner, opts.media_id, mime, filename)
    inner_b64 = base64.standard_b64encode(inner).decode('ascii')
    body = json.dumps({(req - id): new_req_id, payload: inner_b64}, separators=
        (',', ':')).encode('utf-8')
    orig_body_len = len(tpl) - 8
    orig_len_field = tpl[3] | tpl[4] << 8
    length_field_delta = orig_len_field - orig_body_len
    new_len_field = len(body) + length_field_delta
    header = bytearray(tpl[None:8])
    header[3] = new_len_field & 255
    header[4] = new_len_field >> 8 & 255
    return bytes(header) + body



# NOT DECOMPILED: _inject_attachment


# NOT DECOMPILED: _payload_has_field


# NOT DECOMPILED: _substitute_media_id_in_attachment


# Original qualified name: _replace_all_text_field_values
def _replace_all_text_field_values(proto, old_text, new_text):
    __temp_20033, __temp_20034, __temp_20035 = _replace_text_field_values(proto,
        old_text.encode('utf-8'), new_text.encode('utf-8'), 0)
    rewritten = __temp_20033
    _ = __temp_20034
    ok = __temp_20035
    if not ok:
        return proto
    return rewritten



# NOT DECOMPILED: _replace_text_field_values


# NOT DECOMPILED: _extract_template_conversation_id


# NOT DECOMPILED: _is_uuid_chars


# NOT DECOMPILED: _scan_for_uuid


# Original qualified name: _bytes_replace_all
def _bytes_replace_all(s, old, new):
    if not old:
        return s
    return s.replace(old, new)

