# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/timeline_compiler.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _poll_progress


# NOT DECOMPILED: _run


# Original qualified name: _fit_pad_vf
def _fit_pad_vf(w, h, fps):
    return 'scale=' + str(w) + ':' + str(h
        ) + ':force_original_aspect_ratio=decrease:flags=lanczos,pad=' + str(w
        ) + ':' + str(h) + ':(ow-iw)/2:(oh-ih)/2:black,fps=' + str(fps
        ) + ',format=yuv420p,setsar=1'



# Original qualified name: _cover_vf
def _cover_vf(w, h, fps):
    app = __import__('app.media.logo_zoom', fromlist=('cover_zoom_vf',), level=0)
    cover_zoom_vf = app.cover_zoom_vf
    return cover_zoom_vf(w, h, fps)



# NOT DECOMPILED: _render_base_part


# Original qualified name: _render_base_part.<locals>._blur_fc
def _blur_fc(pre_pts, tail):
    nonlocal col_chain, fps, h, w
    return '[0:v]' + str(pre_pts) + 'split=2[bg0][fg0];[bg0]scale=' + str(w
        ) + ':' + str(h) + ':force_original_aspect_ratio=increase,crop=' + str(w
        ) + ':' + str(h) + ',boxblur=20:2[bgb];[fg0]scale=' + str(w) + ':' + str(h
        ) + ':force_original_aspect_ratio=decrease:flags=lanczos[fgs];[bgb][fgs]overlay=(W-w)/2:(H-h)/2,fps=' + str(
        fps) + ',format=yuv420p,setsar=1' + str(col_chain) + str(tail) + '[v]'



# NOT DECOMPILED: _bake_base


# NOT DECOMPILED: _bake_base.<locals>._encode


# NOT DECOMPILED: _concat_parts


# Original qualified name: _ease_expr
def _ease_expr(x, ease):
    if ease == 'ease_in':
        return '(' + str(x) + ')*(' + str(x) + ')'
    if ease == 'ease_out':
        return '(1-(1-(' + str(x) + '))*(1-(' + str(x) + ')))'
    if ease == 'ease':
        return '(' + str(x) + ')*(' + str(x) + ')*(3-2*(' + str(x) + '))'
    return '(' + str(x) + ')'



# NOT DECOMPILED: kf_expr


# NOT DECOMPILED: _clip_kf


# Original qualified name: _mask_geq
def _mask_geq(mask):
    fy = mask['y_pct'] / 100.0
    fx = mask['x_pct'] / 100.0
    fh = mask['h_pct'] / 100.0
    fw = mask['w_pct'] / 100.0
    fe = mask['feather'] / 100.0
    if fe > 0:
        F = 'max(W*' + format(fe, 'g') + '\\,1)'
    else:
        F = '1'
    dx = 'abs(X-W*' + format(fx, 'g') + ')'
    dy = 'abs(Y-H*' + format(fy, 'g') + ')'
    hw = '(W*' + format(fw / 2, 'g') + ')'
    hh = '(H*' + format(fh / 2, 'g') + ')'
    if mask['type'] == 'circle':
        e = 'hypot(' + str(dx) + '/' + str(hw) + '\\,' + str(dy) + '/' + str(hh
            ) + ')'
        d = '((1-' + str(e) + ')*min(' + str(hw) + '\\,' + str(hh) + '))'
    else:
        r = mask.get('radius', 0.0) / 100.0
        if r <= 0.0001:
            d = 'min(' + str(hw) + '-' + str(dx) + '\\,' + str(hh) + '-' + str(dy
                ) + ')'
        else:
            ry = 'min(H*' + format(r, 'g') + '\\,' + str(hh) + ')'
            rx = 'min(W*' + format(r, 'g') + '\\,' + str(hw) + ')'
            qy = '(' + str(dy) + '-(' + str(hh) + '-' + str(ry) + '))'
            qx = '(' + str(dx) + '-(' + str(hw) + '-' + str(rx) + '))'
            ec = 'hypot(max(' + str(qx) + '\\,0)/' + str(rx) + '\\,max(' + str(qy
                ) + '\\,0)/' + str(ry) + ')'
            d = 'if(gt(' + str(qx) + '\\,0)*gt(' + str(qy) + '\\,0)\\,(1-' + str(ec
                ) + ')*min(' + str(rx) + '\\,' + str(ry) + ')\\,min(' + str(hw
                ) + '-' + str(dx) + '\\,' + str(hh) + '-' + str(dy) + '))'
    inside = 'clip(' + str(d) + '/' + str(F) + '\\,0\\,1)'
    if mask.get('invert'):
        a = 'alpha(X\\,Y)*(1-' + str(inside) + ')'
    else:
        a = 'alpha(X\\,Y)*' + str(inside)
    return 'geq=r=r(X\\,Y):g=g(X\\,Y):b=b(X\\,Y):a=' + str(a)



# Original qualified name: _overlay_prep_chain
def _overlay_prep_chain(idx, c, canvas_w, label):
    t = c.transform
    parts = ['[' + str(idx) + ':v]']
    if c.media_kind == 'video':
        a = c.src_in_ms / 1000.0
        need = (c.end_ms - c.start_ms) / 1000.0 * c.speed
        parts.append('trim=start=' + format(a, '.3f') + ':end=' + format(a +
            need + 0.2, '.3f') + ',')
        parts.append('setpts=PTS-STARTPTS,')
        if abs(c.speed - 1.0) > 0.001:
            parts.append('setpts=PTS/' + format(c.speed, 'g') + ',')
    if c.chroma:
        parts.append('chromakey=0x' + str(c.chroma['color']) + ':' + format(c.
            chroma['similarity'], '.3f') + ':' + format(c.chroma['blend'],
            '.3f') + ',')
        __temp_264507 = video_color_filters(c.color_grade)
    else:
        video_color_filters(c.color_grade)
    for __temp_264509 in iter(__temp_264507):
        f = __temp_264509
        parts.append(f + ',')
        continue
    parts.append('format=rgba,')
    kf_scale = _clip_kf(c, 'scale_pct')
    if t:
        base_scale = t.scale_pct
    else:
        base_scale = 100.0
    if kf_scale:
        wexpr = '(' + str(canvas_w) + '*(' + str(kf_expr(kf_scale, 0.0)) + ')/100)'
        parts.append('scale=eval=frame:w=' + str(wexpr) + ':h=-1:flags=lanczos,')
    else:
        w = max(2, round(canvas_w * base_scale / 100.0))
        parts.append('scale=' + str(w) + ':-1:flags=lanczos,')
    if t:
        if t.flip_h:
            parts.append('hflip,')
    if t:
        if t.flip_v:
            parts.append('vflip,')
    if c.mask:
        parts.append(_mask_geq(c.mask) + ',')
        kf_rot = _clip_kf(c, 'rotate_deg')
    else:
        kf_rot = _clip_kf(c, 'rotate_deg')
    if kf_rot:
        aexpr = '(' + str(kf_expr(kf_rot, 0.0)) + ')*PI/180'
        parts.append('rotate=a=' + str(aexpr) +
            ':fillcolor=none:ow=hypot(iw\\,ih):oh=hypot(iw\\,ih),')
    elif t:
        if abs(t.rotate_deg) > 0.01:
            rad = t.rotate_deg * math.pi / 180.0
            parts.append('rotate=' + format(rad, '.5f') +
                ':fillcolor=none:ow=hypot(iw\\,ih):oh=hypot(iw\\,ih),')
    if t:
        op = t.opacity
    else:
        op = 1.0
    if op < 0.999:
        parts.append('colorchannelmixer=aa=' + format(op, 'g') + ',')
        slot = (c.end_ms - c.start_ms) / 1000.0
    else:
        slot = (c.end_ms - c.start_ms) / 1000.0
    fout = c.fade_out_ms / 1000.0
    fin = c.fade_in_ms / 1000.0
    if fin > 0.001:
        parts.append('fade=t=in:st=0:d=' + format(min(fin, slot), '.3f') +
            ':alpha=1,')
    if fout > 0.001:
        if slot > fout:
            parts.append('fade=t=out:st=' + format(slot - fout, '.3f') + ':d=' +
                format(fout, '.3f') + ':alpha=1,')
            parts.append('setpts=PTS+' + format(c.start_ms / 1000.0, '.3f') + '/TB'
                )
            return ''.join(parts) + '[' + str(label) + ']'
        else:
            parts.append('setpts=PTS+' + format(c.start_ms / 1000.0, '.3f') + '/TB'
                )
            return ''.join(parts) + '[' + str(label) + ']'
    else:
        parts.append('setpts=PTS+' + format(c.start_ms / 1000.0, '.3f') + '/TB')
        return ''.join(parts) + '[' + str(label) + ']'



# Original qualified name: _audio_prep_chain
def _audio_prep_chain(idx, c, track, label):
    a = c.src_in_ms / 1000.0
    slot = (c.end_ms - c.start_ms) / 1000.0
    need = slot * c.speed
    vol = max(0.0, c.volume * track.volume)
    ch = ['[' + str(idx) + ':a]atrim=start=' + format(a, '.3f') + ':end=' +
        format(a + need, '.3f'), 'asetpts=PTS-STARTPTS']
    if abs(c.speed - 1.0) > 0.001:
        ch.append(atempo_chain(c.speed))
    if c.pitch_semitones:
        rate = 2 ** (c.pitch_semitones / 12.0)
        ch.append('aresample=48000')
        ch.append('asetrate=' + str(int(round(48000 * rate))))
        ch.append('aresample=48000')
        ch.append(atempo_chain(1.0 / rate))
    if c.denoise:
        ch.append('afftdn=nf=-28')
    if c.normalize:
        ch.append('loudnorm=I=-16:TP=-1.5:LRA=11')
        __temp_264552 = abs(vol - 1.0)
    else:
        abs(vol - 1.0)
    if __temp_264552 > 0.001:
        ch.append('volume=' + format(vol, 'g'))
    if c.fade_in_ms > 0:
        ch.append('afade=t=in:st=0:d=' + format(c.fade_in_ms / 1000.0, 'g'))
    if c.fade_out_ms > 0:
        if slot > c.fade_out_ms / 1000.0:
            ch.append('afade=t=out:st=' + format(slot - c.fade_out_ms / 1000.0,
                '.3f') + ':d=' + format(c.fade_out_ms / 1000.0, 'g'))
            ch.append('aresample=48000')
            ch.append('aformat=channel_layouts=stereo')
            ms = int(c.start_ms)
        else:
            ch.append('aresample=48000')
            ch.append('aformat=channel_layouts=stereo')
            ms = int(c.start_ms)
    else:
        ch.append('aresample=48000')
        ch.append('aformat=channel_layouts=stereo')
        ms = int(c.start_ms)
    ch.append('adelay=' + str(ms) + '|' + str(ms))
    return ','.join(ch) + '[' + str(label) + ']'



# Original qualified name: _audible
def _audible(track, c, any_solo):
    if not track.muted:
        if not c.muted:
            if not c.has_audio:
                return False
        else:
            return False
    else:
        return False
    if any_solo:
        if not track.solo:
            return False
    return c.volume * track.volume > 0.001



# NOT DECOMPILED: _probe_audio


# Original qualified name: _overlay_xy
def _overlay_xy(c):
    t = c.transform
    t0 = c.start_ms / 1000.0
    kx = _clip_kf(c, 'x_pct')
    ky = _clip_kf(c, 'y_pct')
    if kx:
        x = '(main_w*(' + str(kf_expr(kx, t0)) + ')/100-overlay_w/2)'
    elif t:
        x = '(main_w*' + format(t.x_pct / 100.0, 'g') + '-overlay_w/2)'
    else:
        x = '(main_w*' + format(50.0 / 100.0, 'g') + '-overlay_w/2)'
    if ky:
        y = '(main_h*(' + str(kf_expr(ky, t0)) + ')/100-overlay_h/2)'
        return x, y
    if t:
        y = '(main_h*' + format(t.y_pct / 100.0, 'g') + '-overlay_h/2)'
    else:
        y = '(main_h*' + format(50.0 / 100.0, 'g') + '-overlay_h/2)'
    return x, y



# NOT DECOMPILED: _bake_final


# Original qualified name: _bake_final.<locals>._args
def _args(ca):
    nonlocal alabels, dur, fc_path, inputs, maps, out
    __temp_264590 = []
    __temp_264590.extend(inputs)
    a = __temp_264590
    if fc_path is not None:
        a += ['-filter_complex_script', str(fc_path)]
    __temp_264594 = []
    __temp_264594.extend(maps)
    __temp_264595 = __temp_264594
    __temp_264595.extend(ca)
    a += __temp_264595
    if alabels:
        __temp_264597 = []
        __temp_264597.extend(('-c:a', 'aac', '-b:a', '192k'))
        a += __temp_264597
    a += ['-t', format(dur, '.3f'), '-movflags', '+faststart', str(out.resolve())]
    return a



# Original qualified name: _bake_final.<locals>._fp
def _fp(p):
    nonlocal on_progress
    if on_progress:
        on_progress(0.6 + 0.4 * max(0.0, min(1.0, p)))
        return None
    return None



# NOT DECOMPILED: _tl_hash


# NOT DECOMPILED: bake_timeline


# NOT DECOMPILED: ensure_timeline
