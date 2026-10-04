# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/youtube_search.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _varint


# Original qualified name: _field_varint
def _field_varint(field, value):
    return _varint(field << 3 | 0) + _varint(value)



# Original qualified name: _field_message
def _field_message(field, payload):
    return _varint(field << 3 | 2) + _varint(len(payload)) + payload



# Original qualified name: build_sp
def build_sp(sort, period, live_only, video_only):
    payload = b''
    if not sort:
        sort_code = SORTS.get('relevance', 0)
    else:
        sort_code = SORTS.get(sort, 0)
    if sort_code:
        payload += _field_varint(1, sort_code)
    inner = b''
    if period:
        if period in PERIODS:
            inner += _field_varint(1, PERIODS[period])
    if video_only:
        if not period:
            if not live_only:
                if sort_code:
                    inner += _field_varint(2, 1)
            else:
                inner += _field_varint(2, 1)
        else:
            inner += _field_varint(2, 1)
    if live_only:
        inner += _field_varint(8, 1)
    if inner:
        payload += _field_message(2, inner)
    if not payload:
        return None
    return base64.urlsafe_b64encode(payload).decode('ascii')



# NOT DECOMPILED: _flat_search


# NOT DECOMPILED: _flat_entry_to_row


# NOT DECOMPILED: search_videos


# NOT DECOMPILED: _search_via_api


# NOT DECOMPILED: _enrich_missing_dates


# NOT DECOMPILED: trending


# NOT DECOMPILED: suggest_keywords


# NOT DECOMPILED: suggest_keywords.<locals>.one
