# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/color_grade.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _num


# Original qualified name: _lut_value
def _lut_value(p):
    s = str(Path(p).resolve()).replace('\\', '/').replace("'", "\\'")
    return "'" + str(s) + "'"



# Original qualified name: video_color_filters
def video_color_filters(grade):
    if isinstance(grade, dict):
        if not grade.get('enabled'):
            return []
    else:
        return []
    f = []
    b = _num(grade.get('brightness'))
    c = _num(grade.get('contrast'))
    s = _num(grade.get('saturation'))
    g = _num(grade.get('gamma'))
    eq = []
    if b:
        eq.append('brightness=' + format(b / 100 * 0.5, '.4f'))
    if c:
        eq.append('contrast=' + format(1 + c / 100 * 0.5, '.4f'))
    if s:
        eq.append('saturation=' + format(max(0.0, 1 + s / 100), '.4f'))
    if g:
        eq.append('gamma=' + format(min(10.0, max(0.1, 1 + g / 100 * 0.6)), '.4f'))
    if eq:
        f.append('eq=' + ':'.join(eq))
        t = _num(grade.get('temperature'))
    else:
        t = _num(grade.get('temperature'))
    ti = _num(grade.get('tint'))
    cb = []
    if t:
        tf = t / 100 * 0.3
        cb.append('rm=' + format(tf, '.4f'))
        cb.append('bm=' + format(-tf, '.4f'))
    if ti:
        cb.append('gm=' + format(-(ti / 100 * 0.3), '.4f'))
    if cb:
        f.append('colorbalance=' + ':'.join(cb))
        sh = _num(grade.get('shadows'))
    else:
        sh = _num(grade.get('shadows'))
    hi = _num(grade.get('highlights'))
    if not sh:
        if hi:
            if sh > 0:
                black = min(0.25, max(0.0, sh / 100 * 0.15))
            else:
                black = 0.0
            if hi:
                white = min(1.0, max(0.5, 1 + hi / 100 * 0.15))
            else:
                white = 1.0
            f.append("curves=all='0/" + format(black, '.3f') + ' 1/' + format(
                white, '.3f') + "'")
            lut = grade.get('lut_path')
        else:
            lut = grade.get('lut_path')
    else:
        if sh > 0:
            black = min(0.25, max(0.0, sh / 100 * 0.15))
        else:
            black = 0.0
        if hi:
            white = min(1.0, max(0.5, 1 + hi / 100 * 0.15))
        else:
            white = 1.0
        f.append("curves=all='0/" + format(black, '.3f') + ' 1/' + format(white,
            '.3f') + "'")
        lut = grade.get('lut_path')
    if lut:
        f.append('lut3d=' + str(_lut_value(str(lut))))
        return f
    else:
        return f



# NOT DECOMPILED: _letterbox_frac


# Original qualified name: video_fx_pre_sub
def video_fx_pre_sub(effects, frame_w, frame_h):
    if not isinstance(effects, dict):
        return []
    f = []
    blur = _num(effects.get('blur'))
    if blur > 0:
        f.append('gblur=sigma=' + format(blur / 100 * 4, '.3f'))
        sharp = _num(effects.get('sharpen'))
    else:
        sharp = _num(effects.get('sharpen'))
    if sharp > 0:
        f.append('unsharp=5:5:' + format(sharp / 100 * 1.5, '.3f') + ':5:5:0.0')
        grain = _num(effects.get('grain'))
    else:
        grain = _num(effects.get('grain'))
    if grain > 0:
        f.append('noise=alls=' + str(int(grain / 100 * 20)) + ':allf=t')
        vig = _num(effects.get('vignette'))
    else:
        vig = _num(effects.get('vignette'))
    if vig > 0:
        f.append('vignette=a=' + format(0.4 + vig / 100 * 1.1, '.4f'))
    if frame_w:
        if frame_h:
            aspect = frame_w / frame_h
        else:
            aspect = 0.0
    else:
        aspect = 0.0
    frac = _letterbox_frac(str(effects.get('letterbox', 'none')), aspect)
    if frac > 0:
        if frame_w:
            if frame_h:
                bar = max(2, int(frame_h * frac) // 2 * 2)
                f.append('drawbox=x=0:y=0:w=' + str(frame_w) + ':h=' + str(bar) +
                    ':color=black@1.0:t=fill')
                f.append('drawbox=x=0:y=' + str(frame_h - bar) + ':w=' + str(
                    frame_w) + ':h=' + str(bar) + ':color=black@1.0:t=fill')
                return f
            else:
                return f
        else:
            return f
    else:
        return f



# Original qualified name: video_fx_post_sub
def video_fx_post_sub(effects, duration_sec):
    if not isinstance(effects, dict):
        return []
    f = []
    fin = _num(effects.get('fade_in_ms')) / 1000.0
    fout = _num(effects.get('fade_out_ms')) / 1000.0
    if fin > 0:
        f.append('fade=t=in:st=0:d=' + format(fin, '.3f'))
    if fout > 0:
        if duration_sec:
            if duration_sec > fout:
                f.append('fade=t=out:st=' + format(duration_sec - fout, '.3f') +
                    ':d=' + format(fout, '.3f'))
                return f
            else:
                return f
        else:
            return f
    else:
        return f

