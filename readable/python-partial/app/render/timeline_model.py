# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/timeline_model.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _f


# NOT DECOMPILED: _i


# Original qualified name: is_v2
def is_v2(config):
    if not config:
        tl = {}.get('timeline')
    else:
        tl = config.get('timeline')
    __temp_264663 = isinstance(tl, dict)
    if __temp_264663:
        __temp_264665 = _i(tl.get('version'))
        if __temp_264665 >= 2:
            return isinstance(tl.get('tracks'), list)
        else:
            return __temp_264665 >= 2
    else:
        return __temp_264663



# Original qualified name: _media_index
def _media_index(config):
    out = {}
    if not config.get('media_pool'):
        __temp_264670 = []
    for __temp_264671 in iter(__temp_264670):
        it = __temp_264671
        if not isinstance(it, dict):
            continue
            __temp_264673 = it.get('id')
        else:
            it.get('id')
        if not __temp_264673:
            continue
            out[str(it['id'])] = it
        else:
            out[str(it['id'])] = it
        continue
    return out



# NOT DECOMPILED: _scene_index


# Original qualified name: _clip_transform
def _clip_transform(raw):
    if not isinstance(raw, dict):
        return None
    return TlTransform(x_pct=_f(raw.get('x_pct'), 50.0), y_pct=_f(raw.get(
        'y_pct'), 50.0), scale_pct=max(1.0, min(400.0, _f(raw.get('scale_pct'),
        100.0))), rotate_deg=_f(raw.get('rotate_deg'), 0.0), opacity=max(0.0,
        min(1.0, _f(raw.get('opacity'), 1.0))), flip_h=bool(raw.get('flip_h')),
        flip_v=bool(raw.get('flip_v')))



# Original qualified name: _norm_transition
def _norm_transition(raw):
    app = __import__('app.render.visual_bake', fromlist=('normalize_transition'
        ,), level=0)
    normalize_transition = app.normalize_transition
    return normalize_transition(raw)



# Original qualified name: _norm_chroma
def _norm_chroma(raw):
    if isinstance(raw, dict):
        if not raw.get('enabled'):
            return None
    else:
        return None
    __temp_264707 = raw.get('color')
    if not __temp_264707:
        col = str('#00FF00').lstrip('#')
    else:
        col = str(__temp_264707).lstrip('#')
    if not re.fullmatch('[0-9a-fA-F]{6}', col):
        col = '00FF00'
    return {color: col.upper(), similarity: max(0.01, min(1.0, _f(raw.get(
        'similarity'), 0.35))), blend: max(0.0, min(0.5, _f(raw.get('blend'), 
        0.1)))}



# Original qualified name: _norm_mask
def _norm_mask(raw):
    if isinstance(raw, dict):
        if raw.get('type') not in ('rect', 'circle'):
            return None
    else:
        return None
    return {type: raw['type'], x_pct: max(0.0, min(100.0, _f(raw.get('x_pct'), 
        50))), y_pct: max(0.0, min(100.0, _f(raw.get('y_pct'), 50))), w_pct:
        max(1.0, min(100.0, _f(raw.get('w_pct'), 60))), h_pct: max(1.0, min(
        100.0, _f(raw.get('h_pct'), 60))), feather: max(0.0, min(20.0, _f(raw.
        get('feather'), 4))), radius: max(0.0, min(50.0, _f(raw.get('radius'), 
        0))), invert: bool(raw.get('invert'))}



# NOT DECOMPILED: _norm_keyframes


# NOT DECOMPILED: resolve


# Original qualified name: resolve.<locals>._drop
def _drop(why, _lbl, _tr):
    nonlocal out
    out.dropped.append(str(_tr.name) + ' · ' + str(_lbl) + ': ' + str(why))
    return None

