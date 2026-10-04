# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/branding.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: safe_local_path
def safe_local_path(raw):
    if not raw:
        return None
    raw = str(raw)
    if not '://' in raw:
        if not raw.startswith('\\\\'):
            if raw.startswith('//'):
                return None
        else:
            return None
    else:
        return None
    p = Path(raw)
    if p.exists():
        if p.is_file():
            return str(p.resolve())
    return None



# Original qualified name: resolve_watermark
def resolve_watermark(config):
    if not config:
        __temp_263494 = {}.get('branding')
    else:
        config.get('branding')
    if not __temp_263494:
        b = {}
    else:
        b = __temp_263494
    __temp_263497 = b.get('watermark')
    if not __temp_263497:
        wm = {}
    else:
        wm = __temp_263497
    if not wm.get('enabled'):
        return None
    path = safe_local_path(wm.get('path'))
    if not path:
        return None
    return {path: path, position: wm.get('position', 'top_right'), x_pct: wm.
        get('x_pct'), y_pct: wm.get('y_pct'), scale_pct: float(wm.get(
        'scale_pct', 12)), opacity: max(0.0, min(1.0, float(wm.get('opacity', 
        0.85)))), margin_pct: float(wm.get('margin_pct', 3))}



# Original qualified name: resolve_cta
def resolve_cta(config, duration_sec):
    if not config:
        __temp_263515 = {}.get('branding')
    else:
        config.get('branding')
    if not __temp_263515:
        b = {}
    else:
        b = __temp_263515
    __temp_263518 = b.get('cta')
    if not __temp_263518:
        cta = {}
    else:
        cta = __temp_263518
    if cta.get('enabled'):
        __temp_263521 = cta.get('text')
        if not __temp_263521:
            __temp_263522 = ''.strip()
        else:
            __temp_263521.strip()
        if __temp_263522:
            if duration_sec <= 0:
                return None
        else:
            return None
    else:
        return None
    before = float(cta.get('before_end_s', 4))
    dur = float(cta.get('duration_s', before))
    start_ms = int(max(0.0, duration_sec - before) * 1000)
    end_ms = int(min(duration_sec, max(0.0, duration_sec - before) + dur) * 1000)
    return {start_ms: start_ms, end_ms: end_ms, text: cta['text'].strip(),
        anchor: int(cta.get('anchor', 8))}



# Original qualified name: watermark_chain
def watermark_chain(logo_index, wm, frame_w, vlabel_in, vlabel_out):
    w = max(2, int(frame_w * wm['scale_pct'] / 100))
    m = max(0, int(frame_w * wm['margin_pct'] / 100))
    pos = wm['position']
    if pos == 'top_left':
        xy = str(m) + ':' + str(m)
    elif pos == 'top_right':
        xy = 'main_w-overlay_w-' + str(m) + ':' + str(m)
    elif pos == 'bottom_left':
        xy = str(m) + ':main_h-overlay_h-' + str(m)
    elif pos == 'bottom_right':
        xy = 'main_w-overlay_w-' + str(m) + ':main_h-overlay_h-' + str(m)
    elif pos == 'center':
        xy = '(main_w-overlay_w)/2:(main_h-overlay_h)/2'
    elif pos == 'custom':
        if wm.get('x_pct') is not None:
            if wm.get('y_pct') is not None:
                xy = format(float(wm['x_pct']) / 100, '.4f') + '*main_w:' + format(
                    float(wm['y_pct']) / 100, '.4f') + '*main_h'
            else:
                xy = 'main_w-overlay_w-' + str(m) + ':' + str(m)
        else:
            xy = 'main_w-overlay_w-' + str(m) + ':' + str(m)
    else:
        xy = 'main_w-overlay_w-' + str(m) + ':' + str(m)
    return ['[' + str(logo_index) + ':v]format=rgba,scale=' + str(w) +
        ':-1,colorchannelmixer=aa=' + format(wm['opacity'], 'g') + '[wm]', '[' +
        str(vlabel_in) + '][wm]overlay=' + str(xy) + '[' + str(vlabel_out) + ']']



# Original qualified name: resolve_overlays
def resolve_overlays(config):
    if not config:
        __temp_263547 = {}.get('overlay_images')
    else:
        config.get('overlay_images')
    if not __temp_263547:
        raw = []
    else:
        raw = __temp_263547
    out = []
    for __temp_263551 in iter(raw):
        ov = __temp_263551
        if isinstance(ov, dict):
            if ov.get('enabled') is False:
                continue
                path = safe_local_path(ov.get('path'))
            else:
                path = safe_local_path(ov.get('path'))
        else:
            continue
            path = safe_local_path(ov.get('path'))
        if not path:
            continue
            e = ov.get('end_ms')
        else:
            ov.get('start_ms')
            e = ov.get('end_ms')
        s = ov.get('start_ms')
        __temp_263565 = float(ov.get('x_pct', 50))
        __temp_263567 = float(ov.get('y_pct', 50))
        __temp_263571 = max(1.0, min(300.0, float(ov.get('scale_pct', 30))))
        __temp_263575 = max(0.0, min(1.0, float(ov.get('opacity', 1.0))))
        __temp_263576 = ov.get('rotate_deg', 0)
        if not __temp_263576:
            __temp_263577 = float(0)
        else:
            float(__temp_263576)
        if s is not None:
            __temp_263579 = int(s)
        if e is not None:
            out.append({path: path, x_pct: __temp_263565, y_pct: __temp_263567,
                scale_pct: __temp_263571, opacity: __temp_263575, rotate_deg:
                __temp_263577, start_ms: __temp_263579, end_ms: int(e), z: int(
                ov.get('z', 0))})
        else:
            out.append({path: path, x_pct: __temp_263565, y_pct: __temp_263567,
                scale_pct: __temp_263571, opacity: __temp_263575, rotate_deg:
                __temp_263577, start_ms: __temp_263579, end_ms: None, z: int(ov
                .get('z', 0))})
        continue
    
    
    def __temp_263589(o):
        return o['z']
    
    
    out.sort(key=__temp_263589)
    return out



# Original qualified name: _overlay_enable
def _overlay_enable(ov):
    e = ov.get('end_ms')
    s = ov.get('start_ms')
    if s is None:
        if e is None:
            return
    if s is not None:
        a = float(s) / 1000.0
    else:
        a = 0.0 / 1000.0
    if e is not None:
        b = float(e) / 1000.0
    else:
        b = 1000000000.0 / 1000.0
    return 'enable=between(t\\,' + format(a, 'g') + '\\,' + format(b, 'g') + ')'



# Original qualified name: overlay_chain
def overlay_chain(idx, ov, frame_w, vlabel_in, vlabel_out):
    w = max(2, round(frame_w * ov['scale_pct'] / 100.0))
    prep = '[' + str(idx) + ':v]format=rgba,scale=' + str(w) + ':-1'
    __temp_263597 = ov.get('rotate_deg', 0)
    if not __temp_263597:
        deg = float(0)
    else:
        deg = float(__temp_263597)
    if abs(deg) > 0.01:
        rad = deg * math.pi / 180.0
        prep += ',rotate=' + format(rad, '.5f'
            ) + ':fillcolor=none:ow=hypot(iw\\,ih):oh=hypot(iw\\,ih)'
    op = float(ov['opacity'])
    if op < 0.999:
        prep += ',colorchannelmixer=aa=' + format(op, 'g')
    prep += '[ov' + str(idx) + ']'
    xf = float(ov['x_pct']) / 100.0
    yf = float(ov['y_pct']) / 100.0
    expr = 'overlay=x=(main_w*' + format(xf, 'g'
        ) + '-overlay_w/2):y=(main_h*' + format(yf, 'g') + '-overlay_h/2)'
    en = _overlay_enable(ov)
    if en:
        expr += ':' + str(en)
    return [prep, '[' + str(vlabel_in) + '][ov' + str(idx) + ']' + str(expr) +
        '[' + str(vlabel_out) + ']']

