# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/style_schema.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _clamp_num


# NOT DECOMPILED: _safe_hex


# Original qualified name: _safe_family
def _safe_family(v):
    if isinstance(v, str):
        if not v.strip():
            return Arial
    else:
        return Arial
    __temp_264361 = re.sub('[,{}\\r\\n]', ' ', v).strip()
    if not __temp_264361[None:64]:
        return 'Arial'
    else:
        return __temp_264361[None:64]



# Original qualified name: _deep_merge
def _deep_merge(base, override):
    if not override:
        return base
    for __temp_264363 in iter(override.items()):
        __temp_264364, __temp_264365 = __temp_264363
        k = __temp_264364
        v = __temp_264365
        if isinstance(v, dict):
            if isinstance(base.get(k), dict):
                _deep_merge(base[k], v)
                continue
                base[k] = v
            else:
                base[k] = v
        else:
            base[k] = v
        continue
    return base



# Original qualified name: resolve_style
def resolve_style(config):
    style = copy.deepcopy(DEFAULT_STYLE)
    if not config:
        __temp_264372 = {}.get('subtitle_style')
    else:
        config.get('subtitle_style')
    if not __temp_264372:
        sub = {}
    else:
        sub = __temp_264372
    preset_style = sub.get('_resolved_preset')
    if isinstance(preset_style, dict):
        _deep_merge(style, preset_style)
        _deep_merge(style, sub.get('overrides'))
        return style
    else:
        _deep_merge(style, sub.get('overrides'))
        return style



# NOT DECOMPILED: validate_style
