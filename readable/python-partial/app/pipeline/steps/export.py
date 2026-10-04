# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/export.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _export_aspects
def _export_aspects(config):
    if not config:
        __temp_255784 = {}.get('export_profile')
    else:
        config.get('export_profile')
    if not __temp_255784:
        prof = {}
    else:
        prof = __temp_255784
    raw = prof.get('aspects')
    out = []
    if isinstance(raw, list):
        for __temp_255790 in iter(raw):
            a = __temp_255790
            if not isinstance(a, str):
                continue
            if not a in _ASPECT_DIMS:
                continue
            if not a not in out:
                continue
                out.append(a)
            else:
                out.append(a)
            continue
        return out
    else:
        return out



# Original qualified name: _override_canvas
def _override_canvas(config, aspect):
    __temp_255794, __temp_255795 = _ASPECT_DIMS[aspect]
    w = __temp_255794
    h = __temp_255795
    cfg = deepcopy(config)
    __temp_255797 = cfg.get('timeline')
    if not __temp_255797:
        tl_cfg = dict({})
    else:
        tl_cfg = dict(__temp_255797)
    __temp_255801 = tl_cfg.get('canvas')
    if not __temp_255801:
        cv = dict({})
    else:
        cv = dict(__temp_255801)
    cv.update({w: w, h: h, aspect: aspect, auto: False})
    tl_cfg['canvas'] = cv
    cfg['timeline'] = tl_cfg
    return cfg



# NOT DECOMPILED: _primary_aspect


# Original qualified name: ExportStep._extra_hash
def _extra_hash(self, ctx):
    app = __import__('app.services.style_service', fromlist=(
        'resolve_style_for_config',), level=0)
    resolve_style_for_config = app.resolve_style_for_config
    return {'_resolved_style': resolve_style_for_config(ctx.config)}



# NOT DECOMPILED: ExportStep.run
