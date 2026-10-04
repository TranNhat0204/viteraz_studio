# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_settings.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: get_fb_settings
def get_fb_settings(db):
    out = {}
    for __temp_272328 in iter(DEFAULTS.items()):
        __temp_272329, __temp_272330 = __temp_272328
        key = __temp_272329
        default = __temp_272330
        row = db.get(Setting, key)
        if row:
            if row.value is not None:
                out[key] = row.value
            else:
                out[key] = default
        else:
            out[key] = default
        continue
    return out



# Original qualified name: get_str
def get_str(db, key, default):
    row = db.get(Setting, key)
    if row:
        if row.value is not None:
            return row.value
    return default



# NOT DECOMPILED: update_fb_settings


# NOT DECOMPILED: _parse_bounded


# NOT DECOMPILED: validate_proxy
