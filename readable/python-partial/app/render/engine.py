# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/engine.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _frame_cache_key
def _frame_cache_key(video_id, t_ms, style, removal, bare, width, background, manual_texts, overlay_images):
    blob = json.dumps([video_id, int(t_ms) // 200, style, removal, bare, width,
        background, manual_texts, overlay_images], sort_keys=True, ensure_ascii
        =False, default=str)
    return hashlib.sha256(blob.encode('utf-8')).hexdigest()



# NOT DECOMPILED: attach_karaoke_words


# Original qualified name: should_burn_subtitles
def should_burn_subtitles(config):
    return config.get('burn_subtitles', True) is not False



# NOT DECOMPILED: load_segments


# NOT DECOMPILED: _read_conform_video_slow


# Original qualified name: format_manual_texts
def format_manual_texts(manual_texts, default_end_ms):
    out = []
    if not manual_texts:
        __temp_263770 = []
    for __temp_263771 in iter(__temp_263770):
        mt = __temp_263771
        __temp_263772 = mt.get('text')
        if not __temp_263772:
            __temp_263773 = ''.strip()
        else:
            __temp_263772.strip()
        if not __temp_263773:
            continue
            __temp_263775 = mt.get('box')
        else:
            mt.get('box')
        if not __temp_263775:
            box = {}
        else:
            box = __temp_263775
        __temp_263778 = {}
        """is_manual_text""".__setitem__('is_manual_text', True)
        """text""".__setitem__('text', mt['text'].strip())
        __temp_263780 = mt.get('start_ms')
        if not __temp_263780:
            """start_ms""".__setitem__('start_ms', int(0))
            __temp_263782 = mt.get('end_ms')
        else:
            """start_ms""".__setitem__('start_ms', int(__temp_263780))
            mt.get('end_ms')
        if __temp_263782 is not None:
            """end_ms""".__setitem__('end_ms', int(mt['end_ms']))
            __temp_263786 = mt.get('anchor')
        else:
            """end_ms""".__setitem__('end_ms', default_end_ms)
            mt.get('anchor')
        if not __temp_263786:
            """anchor""".__setitem__('anchor', int(8))
            __temp_263789 = mt.get('x_pct')
        else:
            """anchor""".__setitem__('anchor', int(__temp_263786))
            mt.get('x_pct')
        if not __temp_263789:
            """x_pct""".__setitem__('x_pct', float(50))
            __temp_263793 = mt.get('y_pct')
        else:
            """x_pct""".__setitem__('x_pct', float(__temp_263789))
            mt.get('y_pct')
        if not __temp_263793:
            """y_pct""".__setitem__('y_pct', float(50))
            """font_family""".__setitem__('font_family', mt.get('font_family'))
            __temp_263798 = mt.get('font_size')
        else:
            """y_pct""".__setitem__('y_pct', float(__temp_263793))
            """font_family""".__setitem__('font_family', mt.get('font_family'))
            mt.get('font_size')
        if not __temp_263798:
            """font_size""".__setitem__('font_size', int(48))
            """color""".__setitem__('color', mt.get('color'))
            """bold""".__setitem__('bold', bool(mt.get('bold', False)))
            """italic""".__setitem__('italic', bool(mt.get('italic', False)))
            """uppercase""".__setitem__('uppercase', bool(mt.get('uppercase', 
                False)))
            __temp_263810 = box.get('enabled')
        else:
            """font_size""".__setitem__('font_size', int(__temp_263798))
            """color""".__setitem__('color', mt.get('color'))
            """bold""".__setitem__('bold', bool(mt.get('bold', False)))
            """italic""".__setitem__('italic', bool(mt.get('italic', False)))
            """uppercase""".__setitem__('uppercase', bool(mt.get('uppercase', 
                False)))
            box.get('enabled')
        if __temp_263810:
            """box""".__setitem__('box', {enabled: bool(box.get('enabled')),
                color: box.get('color', '#000000'), opacity: float(box.get(
                'opacity', 0.6))})
            """fade""".__setitem__('fade', bool(mt.get('fade', False)))
            __temp_263828 = mt.get('anim_in')
        else:
            """box""".__setitem__('box', None)
            """fade""".__setitem__('fade', bool(mt.get('fade', False)))
            mt.get('anim_in')
        if not __temp_263828:
            """anim_in""".__setitem__('anim_in', str(''))
            __temp_263833 = mt.get('anim_out')
        else:
            """anim_in""".__setitem__('anim_in', str(__temp_263828))
            mt.get('anim_out')
        if not __temp_263833:
            """anim_out""".__setitem__('anim_out', str(''))
            __temp_263837 = mt.get('z')
        else:
            """anim_out""".__setitem__('anim_out', str(__temp_263833))
            mt.get('z')
        if not __temp_263837:
            __temp_263842 = __temp_263778
            __temp_263842.update({'z': int(0)})
            out.append(__temp_263842)
        else:
            __temp_263846 = __temp_263778
            __temp_263846.update({'z': int(__temp_263837)})
            out.append(__temp_263846)
        continue
    return out



# NOT DECOMPILED: build_encoder_ladder


# NOT DECOMPILED: run_encoder_ladder


# NOT DECOMPILED: render_video


# Original qualified name: render_video.<locals>._assemble
def _assemble(codec_args, hwaccel):
    nonlocal audio_mode, eff_duration, fc_name, hw_decode, inputs, maps, music, originality, out_path, prof, quality
    __temp_263877 = []
    if hwaccel:
        __temp_263878 = __temp_263877
        __temp_263878.extend(hw_decode)
        __temp_263879 = __temp_263878
        __temp_263879.extend(inputs)
        __temp_263879.append('-filter_complex_script')
        __temp_263879.append(fc_name)
        __temp_263880 = __temp_263879
        __temp_263880.extend(maps)
        a = __temp_263880
    else:
        __temp_263882 = __temp_263877
        __temp_263882.extend([])
        __temp_263883 = __temp_263882
        __temp_263883.extend(inputs)
        __temp_263883.append('-filter_complex_script')
        __temp_263883.append(fc_name)
        __temp_263884 = __temp_263883
        __temp_263884.extend(maps)
        a = __temp_263884
    a += codec_args
    if prof:
        if prof['fps']:
            a += ['-r', str(prof['fps'])]
    if not audio_mode != 'none':
        if music:
            if prof:
                audio_k = str(prof['audio_kbps']) + 'k'
            elif quality == 'export':
                audio_k = '192k'
            else:
                audio_k = '128k'
            a += ['-c:a', 'aac', '-b:a', audio_k]
    else:
        if prof:
            audio_k = str(prof['audio_kbps']) + 'k'
        elif quality == 'export':
            audio_k = '192k'
        else:
            audio_k = '128k'
        a += ['-c:a', 'aac', '-b:a', audio_k]
    if eff_duration > 0:
        a += ['-t', format(eff_duration, '.3f')]
    if originality:
        if originality.get('strip_metadata'):
            a += ['-map_metadata', '-1']
    a += ['-movflags', '+faststart', str(out_path.resolve())]
    return a



# NOT DECOMPILED: _export_profile


# NOT DECOMPILED: _global_speedup_pct


# Original qualified name: _normalize_music
def _normalize_music(config):
    bm = config.get('background_music')
    if isinstance(bm, dict):
        if not bm.get('path'):
            return None
    else:
        return None
    raw = str(bm['path'])
    if '://' in raw:
        return None
    if not raw.startswith('\\\\'):
        if raw.startswith('//'):
            return None
    else:
        return None
    p = Path(raw)
    if p.exists():
        if not p.is_file():
            return None
    else:
        return None
    return {path: str(p.resolve()), volume: float(bm.get('volume', 0.15)), loop:
        bool(bm.get('loop', True)), fade_in_ms: int(bm.get('fade_in_ms', 800)),
        fade_out_ms: int(bm.get('fade_out_ms', 1200))}



# NOT DECOMPILED: _active_or_sample_segment


# NOT DECOMPILED: render_frame
