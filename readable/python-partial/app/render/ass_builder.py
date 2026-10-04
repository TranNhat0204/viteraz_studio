# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/ass_builder.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: ass_color


# Original qualified name: _color_override
def _color_override(tag, hex_rgb):
    full = ass_color(hex_rgb, 1.0)
    return '\\' + str(tag) + '&H' + str(full[4:None])



# Original qualified name: ass_time
def ass_time(ms):
    ms = max(0, int(ms))
    cs = ms // 10
    __temp_260175, __temp_260176 = divmod(cs, 100)
    s = __temp_260175
    cs = __temp_260176
    __temp_260178, __temp_260179 = divmod(s, 60)
    m = __temp_260178
    s = __temp_260179
    __temp_260181, __temp_260182 = divmod(m, 60)
    h = __temp_260181
    m = __temp_260182
    return format(h, 'd') + ':' + format(m, '02d') + ':' + format(s, '02d'
        ) + '.' + format(cs, '02d')



# Original qualified name: escape_text
def escape_text(text, uppercase):
    if not text:
        t = ''.strip()
    else:
        t = text.strip()
    if uppercase:
        t = t.upper()
    t = t.replace('\\', '\\\\').replace('{', '(').replace('}', ')')
    t = t.replace('\r\n', '\\N').replace('\n', '\\N').replace('\r', '\\N')
    return t



# Original qualified name: _anchor_xy
def _anchor_xy(style, play_w, play_h):
    pos = style.get('position', {})
    align = int(pos.get('anchor', 2))
    margin_v = float(pos.get('margin_v', 42))
    margin_h = float(pos.get('margin_h', 60))
    if align in (1, 4, 7):
        x = margin_h
    elif align in (3, 6, 9):
        x = play_w - margin_h
    else:
        x = play_w / 2.0
    if align in (1, 2, 3):
        y = play_h - margin_v
    elif align in (7, 8, 9):
        y = margin_v
    else:
        y = play_h / 2.0
    return x, y, align



# Original qualified name: _lr_margins
def _lr_margins(style, play_w):
    layout = style.get('layout', {})
    mw = layout.get('max_width_pct')
    if isinstance(mw, (int, float)):
        if 10 <= mw:
            if mw <= 100:
                side = round((1.0 - mw / 100.0) / 2.0 * play_w)
                return side, side
    margin_h = int(style.get('position', {}).get('margin_h', 60))
    return margin_h, margin_h



# Original qualified name: _slide_from
def _slide_from(name, x, y, dh, dv):
    if name == 'slide_up':
        return x, y + dv
    if name == 'slide_down':
        return x, y - dv
    if name == 'slide_left':
        return x + dh, y
    if name == 'slide_right':
        return x - dh, y
    return x, y



# Original qualified name: _slide_to
def _slide_to(name, x, y, dh, dv):
    if name == 'slide_up':
        return x, y - dv
    if name == 'slide_down':
        return x, y + dv
    if name == 'slide_left':
        return x - dh, y
    if name == 'slide_right':
        return x + dh, y
    return x, y



# Original qualified name: _anim_tags
def _anim_tags(eff, x, y, align, play_w, play_h, dur_ms):
    etype = eff.get('type', 'fade')
    __temp_260210 = eff.get('anim_in')
    if not __temp_260210:
        anim_in = _LEGACY_IN.get(etype, 'fade')
    else:
        anim_in = __temp_260210
    __temp_260212 = eff.get('anim_out')
    if not __temp_260212:
        anim_out = _LEGACY_OUT.get(etype, 'fade')
    else:
        anim_out = __temp_260212
    fin = max(1, min(int(eff.get('in_ms', 200)), max(1, dur_ms // 2)))
    fout = max(1, min(int(eff.get('out_ms', 160)), max(1, dur_ms // 2)))
    out_start = max(0, dur_ms - fout)
    dh = play_w * 0.06
    dv = play_h * 0.06
    tags = []
    if anim_in in _SLIDES_IN:
        __temp_260227, __temp_260228 = _slide_from(anim_in, x, y, dh, dv)
        fx = __temp_260227
        fy = __temp_260228
        tags.append('\\an' + str(align) + '\\move(' + format(fx, '.0f') + ',' +
            format(fy, '.0f') + ',' + format(x, '.0f') + ',' + format(y, '.0f') +
            ',0,' + str(fin) + ')')
    elif anim_out in _SLIDES_OUT:
        __temp_260231, __temp_260232 = _slide_to(anim_out, x, y, dh, dv)
        tx = __temp_260231
        ty = __temp_260232
        tags.append('\\an' + str(align) + '\\move(' + format(x, '.0f') + ',' +
            format(y, '.0f') + ',' + format(tx, '.0f') + ',' + format(ty, '.0f'
            ) + ',' + str(out_start) + ',' + str(dur_ms) + ')')
    else:
        tags.append('\\an' + str(align) + '\\pos(' + format(x, '.0f') + ',' +
            format(y, '.0f') + ')')
    if anim_in != 'none':
        ain = fin
    else:
        ain = 0
    if anim_out != 'none':
        aout = fout
    else:
        aout = 0
    if not ain:
        if aout:
            tags.append('\\fad(' + str(ain) + ',' + str(aout) + ')')
            pre = {pop: (62, 62), zoom: (140, 140), bounce: (40, 40)}.get(anim_in)
        else:
            pre = {pop: (62, 62), zoom: (140, 140), bounce: (40, 40)}.get(anim_in)
    else:
        tags.append('\\fad(' + str(ain) + ',' + str(aout) + ')')
        pre = {pop: (62, 62), zoom: (140, 140), bounce: (40, 40)}.get(anim_in)
    if pre:
        tags.append('\\fscx' + str(pre[0]) + '\\fscy' + str(pre[1]))
        if anim_in == 'bounce':
            mid = max(1, int(fin * 0.7))
            tags.append('\\t(0,' + str(mid) + ',\\fscx112\\fscy112)\\t(' + str(
                mid) + ',' + str(fin) + ',\\fscx100\\fscy100)')
        else:
            tags.append('\\t(0,' + str(fin) + ',\\fscx100\\fscy100)')
    if anim_out == 'shrink':
        tags.append('\\t(' + str(out_start) + ',' + str(dur_ms) +
            ',\\fscx62\\fscy62)')
        return _wrap(''.join(tags))
    elif anim_out == 'zoom':
        tags.append('\\t(' + str(out_start) + ',' + str(dur_ms) +
            ',\\fscx150\\fscy150)')
        return _wrap(''.join(tags))
    else:
        return _wrap(''.join(tags))



# Original qualified name: _build_dialogue_text
def _build_dialogue_text(style, seg, play_w, play_h):
    __temp_260256 = style.get('effect')
    if not __temp_260256:
        eff = {}
    else:
        eff = __temp_260256
    etype = eff.get('type', 'none')
    uppercase = bool(style.get('font', {}).get('uppercase'))
    raw = escape_text(seg.get('text', ''), uppercase)
    dur_ms = max(1, int(seg.get('end_ms', 0)) - int(seg.get('start_ms', 0)))
    fade_in = int(eff.get('in_ms', 200))
    fade_out = int(eff.get('out_ms', 160))
    pos = style.get('position', {})
    custom = pos.get('custom')
    if isinstance(custom, dict):
        if 'x_pct' in custom:
            if 'y_pct' in custom:
                x = float(custom['x_pct']) / 100.0 * play_w
                y = float(custom['y_pct']) / 100.0 * play_h
                align = 5
            else:
                __temp_260281, __temp_260282, __temp_260283 = _anchor_xy(style,
                    play_w, play_h)
                x = __temp_260281
                y = __temp_260282
                align = __temp_260283
        else:
            __temp_260285, __temp_260286, __temp_260287 = _anchor_xy(style,
                play_w, play_h)
            x = __temp_260285
            y = __temp_260286
            align = __temp_260287
    else:
        __temp_260289, __temp_260290, __temp_260291 = _anchor_xy(style, play_w,
            play_h)
        x = __temp_260289
        y = __temp_260290
        align = __temp_260291
    pos_tag = '\\an' + str(align) + '\\pos(' + format(x, '.0f') + ',' + format(y,
        '.0f') + ')'
    if etype == 'typewriter':
        return _typewriter(raw, dur_ms, pos_tag, fade_out)
    if etype == 'karaoke':
        return _karaoke(style, seg, raw, dur_ms, pos_tag, fade_in, fade_out, eff)
    return _anim_tags(eff, x, y, align, play_w, play_h, dur_ms) + raw



# Original qualified name: _wrap
def _wrap(tags):
    if tags:
        return '{' + tags + '}'
    return ''



# NOT DECOMPILED: _typewriter


# NOT DECOMPILED: _karaoke


# NOT DECOMPILED: build_style_line


# Original qualified name: _wrap_style
def _wrap_style(style):
    __temp_263353 = style.get('layout')
    if not __temp_263353:
        w = str({}.get('wrap', 'smart')).lower()
    else:
        w = str(__temp_263353.get('wrap', 'smart')).lower()
    return {smart: 0, even: 0, line: 1, none: 2}.get(w, 0)



# Original qualified name: build_ass
def build_ass(segments, style, play_w, play_h, extra_events):
    header = ['[Script Info]', 'ScriptType: v4.00+', 'PlayResX: ' + str(int(
        play_w)), 'PlayResY: ' + str(int(play_h)), 'ScaledBorderAndShadow: yes',
        'WrapStyle: ' + str(_wrap_style(style)), 'YCbCr Matrix: TV.709', '',
        '[V4+ Styles]',
        'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding'
        , build_style_line(style, play_w),
        'Style: ManualBox,Arial,48,&H00FFFFFF,&H00FFFFFF,&H80000000,&H00000000,0,0,0,0,100,100,0,0,3,8,0,5,60,60,42,1'
        , '', '[Events]',
        'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text'
        ]
    events = []
    for __temp_263369 in iter(segments):
        seg = __temp_263369
        __temp_263370 = seg.get('text')
        if not __temp_263370:
            __temp_263371 = ''.strip()
        else:
            __temp_263370.strip()
        if not __temp_263371:
            continue
            start = ass_time(seg.get('start_ms', 0))
        else:
            start = ass_time(seg.get('start_ms', 0))
        end = ass_time(seg.get('end_ms', 0))
        text = _build_dialogue_text(style, seg, play_w, play_h)
        events.append('Dialogue: 0,' + str(start) + ',' + str(end) +
            ',Default,,0,0,0,,' + str(text))
        continue
    if not extra_events:
        __temp_263381 = []
    for __temp_263382 in iter(__temp_263381):
        ev = __temp_263382
        __temp_263383 = ev.get('text')
        if not __temp_263383:
            __temp_263384 = ''.strip()
        else:
            __temp_263383.strip()
        if not __temp_263384:
            continue
            start = ass_time(ev.get('start_ms', 0))
        else:
            start = ass_time(ev.get('start_ms', 0))
        end = ass_time(ev.get('end_ms', 0))
        if ev.get('is_manual_text'):
            anchor = int(ev.get('anchor', 8))
            x = float(ev.get('x_pct', 50)) / 100.0 * play_w
            y = float(ev.get('y_pct', 50)) / 100.0 * play_h
            fsize = int(ev.get('font_size', 48))
            dur_ms = max(1, int(ev.get('end_ms', 0)) - int(ev.get('start_ms', 0)))
            __temp_263406 = ev.get('box')
            if not __temp_263406:
                box = {}
            else:
                box = __temp_263406
            has_box = bool(box.get('enabled'))
            if has_box:
                style_name = 'ManualBox'
            else:
                style_name = 'Default'
            style_tags = []
            if ev.get('font_family'):
                style_tags.append('\\fn' + str(ev['font_family']))
                style_tags.append('\\fs' + str(fsize))
                __temp_263414 = ev.get('color')
            else:
                style_tags.append('\\fs' + str(fsize))
                ev.get('color')
            if __temp_263414:
                style_tags.append(_color_override('1c', ev['color']) + '&')
                __temp_263419 = ev.get('bold')
            else:
                ev.get('bold')
            if __temp_263419:
                style_tags.append('\\b1')
                __temp_263422 = ev.get('italic')
            else:
                ev.get('italic')
            if __temp_263422:
                style_tags.append('\\i1')
            if has_box:
                pad = box.get('padding')
                if pad is not None:
                    pad = float(pad)
                else:
                    pad = max(6.0, fsize * 0.28)
                a = max(0, min(255, round((1.0 - float(box.get('opacity', 0.6))
                    ) * 255)))
                style_tags.append(_color_override('3c', box.get('color',
                    '#000000')) + '&')
                style_tags.append('\\3a&H' + format(a, '02X') + '&\\bord' +
                    format(pad, '.0f') + '\\shad0')
                __temp_263437 = ev.get('anim_in')
            else:
                ev.get('anim_in')
            if not __temp_263437:
                if ev.get('fade'):
                    anim_in = str('fade')
                else:
                    anim_in = str('none')
            else:
                anim_in = str(__temp_263437)
            __temp_263443 = ev.get('anim_out')
            if not __temp_263443:
                if ev.get('fade'):
                    anim_out = str('fade')
                else:
                    anim_out = str('none')
            else:
                anim_out = str(__temp_263443)
            body = escape_text(ev['text'], bool(ev.get('uppercase')))
            if anim_in == 'typewriter':
                head = '\\an' + str(anchor) + '\\pos(' + format(x, '.0f'
                    ) + ',' + format(y, '.0f') + ')' + ''.join(style_tags)
                if anim_out not in ('', 'none'):
                    fout = 220
                else:
                    fout = 0
                events.append('Dialogue: 2,' + str(start) + ',' + str(end) +
                    ',' + str(style_name) + ',,0,0,0,,' + _typewriter(body,
                    dur_ms, head, fout))
                continue
            if not anim_in != 'none':
                if anim_out != 'none':
                    eff = {type: 'fade', anim_in: anim_in, anim_out: anim_out,
                        in_ms: 260, out_ms: 220}
                    anim = _anim_tags(eff, x, y, anchor, play_w, play_h, dur_ms)
                    events.append('Dialogue: 2,' + str(start) + ',' + str(end) +
                        ',' + str(style_name) + ',,0,0,0,,{' + str(anim[1:-1]) +
                        str(''.join(style_tags)) + '}' + str(body))
                    continue
                    __temp_263459 = ['\\an' + str(anchor), '\\pos(' + format(x,
                        '.0f') + ',' + format(y, '.0f') + ')']
                    __temp_263459.extend(style_tags)
                    tags_list = __temp_263459
                else:
                    __temp_263461 = ['\\an' + str(anchor), '\\pos(' + format(x,
                        '.0f') + ',' + format(y, '.0f') + ')']
                    __temp_263461.extend(style_tags)
                    tags_list = __temp_263461
            else:
                eff = {type: 'fade', anim_in: anim_in, anim_out: anim_out,
                    in_ms: 260, out_ms: 220}
                anim = _anim_tags(eff, x, y, anchor, play_w, play_h, dur_ms)
                events.append('Dialogue: 2,' + str(start) + ',' + str(end) +
                    ',' + str(style_name) + ',,0,0,0,,{' + str(anim[1:-1]) +
                    str(''.join(style_tags)) + '}' + str(body))
                continue
                __temp_263467 = ['\\an' + str(anchor), '\\pos(' + format(x,
                    '.0f') + ',' + format(y, '.0f') + ')']
                __temp_263467.extend(style_tags)
                tags_list = __temp_263467
            events.append('Dialogue: 2,' + str(start) + ',' + str(end) + ',' +
                str(style_name) + ',,0,0,0,,{' + str(''.join(tags_list)) + '}' +
                str(body))
            continue
            anchor = int(ev.get('anchor', 8))
        else:
            anchor = int(ev.get('anchor', 8))
        body = escape_text(ev['text'], bool(style.get('font', {}).get('uppercase'))
            )
        tags = '\\an' + str(anchor) + '\\fad(200,200)'
        events.append('Dialogue: 1,' + str(start) + ',' + str(end) +
            ',Default,,0,0,0,,{' + str(tags) + '}' + str(body))
        continue
    return '\n'.join(header + events) + '\n'



# Original qualified name: write_ass_file
def write_ass_file(segments, style, play_w, play_h, out_path, extra_events):
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_ass(segments, style, play_w, play_h, extra_events),
        encoding='utf-8')
    return out

