# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/filtergraph.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: escape_filter_path
def escape_filter_path(p):
    s = str(Path(p).resolve()).replace('\\', '/')
    return s.replace(':', '\\:')



# Original qualified name: _clamp
def _clamp(v, lo, hi):
    return max(lo, min(hi, v))



# Original qualified name: _region_size_ok
def _region_size_ok(r):
    __temp_263999 = float(r.get('w_pct', 0))
    if __temp_263999 > 0.5:
        return float(r.get('h_pct', 0)) > 0.5
    else:
        return __temp_263999 > 0.5



# Original qualified name: _region_px
def _region_px(r, W, H):
    x = _clamp(round(float(r.get('x_pct', 0)) / 100 * W), 0, W - 2)
    y = _clamp(round(float(r.get('y_pct', 0)) / 100 * H), 0, H - 2)
    w = _clamp(round(float(r.get('w_pct', 0)) / 100 * W), 2, W - x)
    h = _clamp(round(float(r.get('h_pct', 0)) / 100 * H), 2, H - y)
    return x, y, w, h



# Original qualified name: _region_px_delogo
def _region_px_delogo(r, W, H):
    __temp_264019, __temp_264020, __temp_264021, __temp_264022 = _region_px(r, W, H
        )
    x = __temp_264019
    y = __temp_264020
    w = __temp_264021
    h = __temp_264022
    x = _clamp(x, 1, W - 3)
    y = _clamp(y, 1, H - 3)
    w = _clamp(w, 1, W - x - 1)
    h = _clamp(h, 1, H - y - 1)
    return x, y, w, h



# Original qualified name: _enable_expr
def _enable_expr(r, ignore_time, time_scale):
    t0 = r.get('t_start_ms')
    t1 = r.get('t_end_ms')
    if not ignore_time:
        if t0 is None:
            if t1 is None:
                return
    else:
        return
    if t0 is not None:
        a = float(t0) / 1000.0 * time_scale
    else:
        a = 0 / 1000.0 * time_scale
    if t1 is not None:
        b = float(t1) / 1000.0 * time_scale
    else:
        b = 1000000000.0 / 1000.0 * time_scale
    return 'enable=between(t\\,' + format(a, 'g') + '\\,' + format(b, 'g') + ')'



# NOT DECOMPILED: _video_chains


# NOT DECOMPILED: _region_in_expr


# Original qualified name: _gate_vol
def _gate_vol(in_expr, in_val, out_val):
    return 'if(gt(' + str(in_expr) + '\\,0)\\,' + format(in_val, 'g'
        ) + '\\,' + format(out_val, 'g') + ')'



# Original qualified name: _audio_chains
def _audio_chains(audio_mode, orig_volume, vo, music_index, music, duration_sec, speed, vo_volume, ducking, orig_regions, region_orig_volume, has_original_audio, conform_video_slow, vo_keep_ranges):
    chains = []
    base = None
    if not orig_regions:
        regions = []
    else:
        regions = orig_regions
    __temp_264077 = bool(regions)
    if __temp_264077:
        use_regions = has_original_audio
    else:
        use_regions = __temp_264077
    if use_regions:
        in_expr = _region_in_expr(regions)
    else:
        in_expr = '0'
    vo_src = str(vo) + ':a'
    if vo_keep_ranges is not None:
        if audio_mode in ('amix', 'voiceover'):
            if vo_keep_ranges:
                keep = _region_in_expr(vo_keep_ranges)
                chains.append('[' + str(vo) + ':a]volume=if(gt(' + str(keep) +
                    '\\,0)\\,1\\,0):eval=frame[vok]')
                vo_src = 'vok'
            else:
                chains.append('[' + str(vo) + ':a]volume=0[vok]')
                vo_src = 'vok'
    if not conform_video_slow:
        cf_slow = float(1.0)
    else:
        cf_slow = float(conform_video_slow)
    oa_src = '0:a'
    if cf_slow > 1.0001:
        if not use_regions:
            if audio_mode in ('amix', 'original'):
                chains.append('[0:a]' + str(atempo_chain(1.0 / cf_slow)) + '[oacf]'
                    )
                oa_src = 'oacf'
        else:
            chains.append('[0:a]' + str(atempo_chain(1.0 / cf_slow)) + '[oacf]')
            oa_src = 'oacf'
    if use_regions:
        if audio_mode in ('amix', 'original'):
            base_out = orig_volume
        else:
            base_out = 0.0
        o_expr = _gate_vol(in_expr, region_orig_volume, base_out)
        chains.append('[' + str(oa_src) + ']volume=' + str(o_expr) +
            ':eval=frame[oa]')
        mix = ['oa']
        if audio_mode in ('amix', 'voiceover'):
            v_expr = _gate_vol(in_expr, 0.0, vo_volume)
            chains.append('[' + str(vo_src) + ']volume=' + str(v_expr) +
                ':eval=frame[va]')
            mix.append('va')
            __temp_264094 = len(mix)
        else:
            len(mix)
        if __temp_264094 >= 2:
            chains.append('[' + str(']['.join(mix)) + ']amix=inputs=' + str(len
                (mix)) + ':duration=longest:normalize=0[abase]')
            base = 'abase'
        else:
            chains.append('[' + str(mix[0]) + ']anull[abase]')
            base = 'abase'
    elif audio_mode == 'amix':
        if ducking:
            if ducking > 0.001:
                ratio = max(2.0, min(20.0, 1.0 + ducking * 19.0))
                chains.append('[' + str(oa_src) + ']volume=' + format(
                    orig_volume, 'g') + '[oa];[' + str(vo_src) + ']volume=' +
                    format(vo_volume, 'g') +
                    '[va];[va]asplit=2[va1][vsc];[oa][vsc]sidechaincompress=threshold=0.06:ratio='
                     + format(ratio, 'g') +
                    ':attack=5:release=250[oad];[oad][va1]amix=inputs=2:duration=longest:normalize=0[abase]'
                    )
                base = 'abase'
            else:
                chains.append('[' + str(oa_src) + ']volume=' + format(
                    orig_volume, 'g') + '[oa];[' + str(vo_src) + ']volume=' +
                    format(vo_volume, 'g') +
                    '[va];[oa][va]amix=inputs=2:duration=longest:normalize=0[abase]'
                    )
                base = 'abase'
        else:
            chains.append('[' + str(oa_src) + ']volume=' + format(orig_volume,
                'g') + '[oa];[' + str(vo_src) + ']volume=' + format(vo_volume,
                'g') +
                '[va];[oa][va]amix=inputs=2:duration=longest:normalize=0[abase]')
            base = 'abase'
    elif audio_mode == 'voiceover':
        chains.append('[' + str(vo_src) + ']volume=' + format(vo_volume, 'g') +
            '[abase]')
        base = 'abase'
    elif audio_mode == 'original':
        chains.append('[' + str(oa_src) + ']anull[abase]')
        base = 'abase'
    amus = None
    if music_index is not None:
        if music:
            mv = float(music.get('volume', 0.15))
            fin = max(0.0, float(music.get('fade_in_ms', 0)) / 1000.0)
            fout = max(0.0, float(music.get('fade_out_ms', 0)) / 1000.0)
            if not duration_sec:
                d = float(0)
            else:
                d = float(duration_sec)
            if use_regions:
                mparts = ['[' + str(music_index) + ':a]volume=' + str(_gate_vol
                    (in_expr, 0.0, mv)) + ':eval=frame']
            else:
                mparts = ['[' + str(music_index) + ':a]volume=' + format(mv, 'g')]
            if d > 0:
                mparts += ['atrim=0:' + format(d, 'g'), 'asetpts=PTS-STARTPTS']
            if fin > 0:
                mparts.append('afade=t=in:st=0:d=' + format(fin, 'g'))
            if d > 0:
                if fout > 0:
                    if d > fout:
                        mparts.append('afade=t=out:st=' + format(d - fout, 'g') +
                            ':d=' + format(fout, 'g'))
                        chains.append(','.join(mparts) + '[amus]')
                        amus = 'amus'
                    else:
                        chains.append(','.join(mparts) + '[amus]')
                        amus = 'amus'
                else:
                    chains.append(','.join(mparts) + '[amus]')
                    amus = 'amus'
            else:
                chains.append(','.join(mparts) + '[amus]')
                amus = 'amus'
    final = None
    if base:
        if amus:
            chains.append('[' + str(base) + '][' + str(amus) +
                ']amix=inputs=2:duration=longest:normalize=0[amixed]')
            final = 'amixed'
        elif base:
            final = base
        elif amus:
            final = amus
    elif base:
        final = base
    elif amus:
        final = amus
    if final is None:
        return chains, ['-an']
    if speed:
        if abs(speed - 1.0) > 0.001:
            chains.append('[' + str(final) + ']atempo=' + format(speed, 'g') +
                '[aout]')
            final = 'aout'
    return chains, ['-map', '[' + str(final) + ']']



# Original qualified name: build_filtergraph
def build_filtergraph(src_w, src_h, scale_height, has_subs, ass_name, fontsdir, audio_mode, orig_volume, vo_volume, ducking, orig_regions, region_orig_volume, has_original_audio, removal, ignore_time, voiceover_index, music_index, music, duration_sec, originality, frame_w, frame_h, watermark, watermark_index, overlay_layers, extra_speed, conform_video_slow, color_grade, effects, background_index, canvas_w, canvas_h, vo_keep_ranges):
    if not originality:
        __temp_264138 = float({}.get('speed', 1.0))
    else:
        float(originality.get('speed', 1.0))
    if not extra_speed:
        speed = __temp_264138 * float(1.0)
    else:
        speed = __temp_264138 * float(extra_speed)
    """removal""".__setitem__('removal', removal)
    """src_w""".__setitem__('src_w', src_w)
    """src_h""".__setitem__('src_h', src_h)
    """scale_height""".__setitem__('scale_height', scale_height)
    """has_subs""".__setitem__('has_subs', has_subs)
    """ass_name""".__setitem__('ass_name', ass_name)
    """fontsdir""".__setitem__('fontsdir', fontsdir)
    """ignore_time""".__setitem__('ignore_time', ignore_time)
    """originality""".__setitem__('originality', originality)
    """frame_w""".__setitem__('frame_w', frame_w)
    """frame_h""".__setitem__('frame_h', frame_h)
    """speed""".__setitem__('speed', speed)
    """color_grade""".__setitem__('color_grade', color_grade)
    """effects""".__setitem__('effects', effects)
    """duration_sec""".__setitem__('duration_sec', duration_sec)
    """conform_video_slow""".__setitem__('conform_video_slow', conform_video_slow)
    """background_index""".__setitem__('background_index', background_index)
    """canvas_w""".__setitem__('canvas_w', canvas_w)
    """canvas_h""".__setitem__('canvas_h', canvas_h)
    chains = _video_chains(*(), **{})
    vlabel = 'v'
    if background_index is not None:
        fw = canvas_w
    else:
        if scale_height:
            fh = int(scale_height)
        elif not frame_h:
            fh = src_h
        else:
            fh = frame_h
        if not frame_w:
            if src_h:
                fw = round(src_w * fh / src_h / 2) * 2
            else:
                fw = src_w
        else:
            fw = frame_w
    if watermark:
        if watermark_index is not None:
            app = __import__('app.render.branding', fromlist=('watermark_chain'
                ,), level=0)
            watermark_chain = app.watermark_chain
            chains += watermark_chain(watermark_index, watermark, fw, 'v', 'vwm')
            vlabel = 'vwm'
    if overlay_layers:
        app = __import__('app.render.branding', fromlist=('overlay_chain',),
            level=0)
        overlay_chain = app.overlay_chain
        for __temp_264149 in iter(enumerate(overlay_layers)):
            __temp_264150, __temp_264151 = __temp_264149
            k = __temp_264150
            layer = __temp_264151
            nxt = 'vov' + str(k)
            if layer.get('kind') == 'image':
                chains += overlay_chain(layer['index'], layer['ov'], fw, vlabel,
                    nxt)
                vlabel = nxt
            else:
                s = '[' + str(vlabel) + ']ass=' + str(layer['ass_name'])
                if fontsdir:
                    s += ':fontsdir=' + str(escape_filter_path(fontsdir))
                chains.append(s + '[' + str(nxt) + ']')
                vlabel = nxt
            continue
        maps = ['-map', '[' + str(vlabel) + ']']
    else:
        maps = ['-map', '[' + str(vlabel) + ']']
    __temp_264159, __temp_264160 = _audio_chains(audio_mode, orig_volume,
        voiceover_index, music_index, music, duration_sec, speed, vo_volume=
        vo_volume, ducking=ducking, orig_regions=orig_regions,
        region_orig_volume=region_orig_volume, has_original_audio=
        has_original_audio, conform_video_slow=conform_video_slow,
        vo_keep_ranges=vo_keep_ranges)
    achains = __temp_264159
    amaps = __temp_264160
    chains += achains
    maps += amaps
    return ';'.join(chains), maps



# Original qualified name: decide_audio_mode
def decide_audio_mode(voiceover_exists, has_original_audio, keep_original):
    if voiceover_exists:
        if has_original_audio:
            if keep_original:
                return amix
    if voiceover_exists:
        return voiceover
    if has_original_audio:
        return original
    return none



# NOT DECOMPILED: _active_cpu_jobs


# Original qualified name: _encode_threads
def _encode_threads():
    __temp_264164 = os.cpu_count()
    if not __temp_264164:
        n = 4
    else:
        n = __temp_264164
    return max(2, min(n // _active_cpu_jobs(), 8))



# Original qualified name: _intermediate_q
def _intermediate_q(config):
    return 16



# Original qualified name: video_codec_args
def video_codec_args(quality, config):
    thr = ['-threads', str(_encode_threads())]
    if quality == 'export':
        __temp_264173 = ['-c:v', 'libx264', '-preset', 'medium', '-crf', str(
            _EXPORT_CPU_CRF), '-pix_fmt', 'yuv420p']
        __temp_264173.extend(thr)
        return __temp_264173
    if quality == 'intermediate':
        __temp_264176 = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf',
            _intermediate_q(config), '-pix_fmt', 'yuv420p']
        __temp_264176.extend(thr)
        return __temp_264176
    __temp_264178 = ['-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '28',
        '-pix_fmt', 'yuv420p']
    __temp_264178.extend(thr)
    return __temp_264178



# Original qualified name: profile_codec_args
def profile_codec_args(prof):
    if prof.get('codec') == 'h265':
        codec = 'libx265'
    else:
        codec = 'libx264'
    args = ['-c:v', codec, '-preset', 'medium', '-pix_fmt', 'yuv420p',
        '-threads', str(_encode_threads())]
    if prof.get('mode') == 'bitrate':
        if prof.get('bitrate_kbps'):
            br = int(prof['bitrate_kbps'])
            args += ['-b:v', str(br) + 'k', '-maxrate', str(int(br * 1.5)) +
                'k', '-bufsize', str(br * 2) + 'k']
        else:
            args += ['-crf', str(int(prof.get('crf', 18)))]
    else:
        args += ['-crf', str(int(prof.get('crf', 18)))]
    if codec == 'libx265':
        args += ['-tag:v', 'hvc1']
    return args



# Original qualified name: profile_hw_codec_variants
def profile_hw_codec_variants(prof, encoder):
    hevc = prof.get('codec') == 'h265'
    __temp_264198 = prof.get('mode')
    if __temp_264198 == 'bitrate':
        bitrate_mode = bool(prof.get('bitrate_kbps'))
    else:
        bitrate_mode = __temp_264198 == 'bitrate'
    if bitrate_mode:
        br = int(prof['bitrate_kbps'])
        rc_qsv = ['-b:v', str(br) + 'k', '-maxrate', str(int(br * 1.5)) + 'k',
            '-bufsize', str(br * 2) + 'k']
        rc_nv = rc_qsv
        __temp_264205 = ['-rc', 'vbr_peak']
        __temp_264205.extend(rc_qsv)
        rc_amf = __temp_264205
        rc_vt = rc_qsv
    else:
        crf = int(prof.get('crf', 18))
    
        def q(enc):
            nonlocal crf
            return str(max(1, min(51, crf + _CQ_OFFSET.get(enc, 0))))
        if hevc:
            rc_qsv = ['-global_quality', q('hevc_qsv')]
        else:
            rc_qsv = ['-global_quality', q('h264_qsv')]
        if hevc:
            rc_nv = ['-rc', 'vbr', '-cq', q('hevc_nvenc'), '-b:v', '0']
        else:
            rc_nv = ['-rc', 'vbr', '-cq', q('h264_nvenc'), '-b:v', '0']
        if hevc:
            __temp_264221 = q('hevc_amf')
        else:
            q('h264_amf')
        if hevc:
            rc_amf = ['-rc', 'cqp', '-qp_i', __temp_264221, '-qp_p', q('hevc_amf')]
        else:
            rc_amf = ['-rc', 'cqp', '-qp_i', __temp_264221, '-qp_p', q('h264_amf')]
        rc_vt = None
    if hevc:
        tag = ['-tag:v', 'hvc1']
    else:
        tag = []
    if encoder in ('h264_nvenc', 'hevc_nvenc'):
        pix = ['-pix_fmt', 'yuv420p']
        __temp_264231 = ['-c:v', encoder]
        __temp_264231.extend(rc_nv)
        __temp_264232 = __temp_264231
        __temp_264232.extend(pix)
        __temp_264233 = __temp_264232
        __temp_264233.extend(tag)
        bare = __temp_264233
        __temp_264235 = ['-c:v', encoder, '-preset', 'p5']
        __temp_264235.extend(rc_nv)
        __temp_264236 = __temp_264235
        __temp_264236.extend(pix)
        __temp_264237 = __temp_264236
        __temp_264237.extend(tag)
        base = __temp_264237
        __temp_264239 = []
        __temp_264239.extend(base)
        __temp_264239.append('-rc-lookahead')
        __temp_264239.append('32')
        __temp_264239.append('-spatial-aq')
        __temp_264239.append('1')
        __temp_264239.append('-temporal-aq')
        __temp_264239.append('1')
        __temp_264239.append('-bf')
        __temp_264239.append('3')
        return [__temp_264239, base, bare]
    if encoder in ('h264_qsv', 'hevc_qsv'):
        if encoder == 'h264_qsv':
            qsv_preset = 'veryslow'
        else:
            qsv_preset = 'slow'
        pix = ['-pix_fmt', 'nv12']
        __temp_264243 = ['-c:v', encoder]
        __temp_264243.extend(rc_qsv)
        __temp_264244 = __temp_264243
        __temp_264244.extend(pix)
        __temp_264245 = __temp_264244
        __temp_264245.extend(tag)
        bare = __temp_264245
        __temp_264247 = ['-c:v', encoder, '-preset', qsv_preset]
        __temp_264247.extend(rc_qsv)
        __temp_264247.append('-extbrc')
        __temp_264247.append('1')
        __temp_264247.append('-bf')
        __temp_264247.append('3')
        __temp_264248 = __temp_264247
        __temp_264248.extend(pix)
        __temp_264249 = __temp_264248
        __temp_264249.extend(tag)
        base = __temp_264249
        if encoder == 'h264_qsv':
            __temp_264251 = []
            __temp_264251.extend(base)
            __temp_264251.append('-adaptive_i')
            __temp_264251.append('1')
            __temp_264251.append('-adaptive_b')
            __temp_264251.append('1')
            base = __temp_264251
        if bitrate_mode:
            __temp_264253 = []
            __temp_264253.extend(base)
            __temp_264253.append('-look_ahead')
            __temp_264253.append('1')
            __temp_264253.append('-look_ahead_depth')
            __temp_264253.append('40')
            return [__temp_264253, base, bare]
        return [base, bare]
    if encoder in ('h264_amf', 'hevc_amf'):
        pix = ['-pix_fmt', 'yuv420p']
        __temp_264258 = ['-c:v', encoder, '-quality', 'quality']
        __temp_264258.extend(rc_amf)
        __temp_264259 = __temp_264258
        __temp_264259.extend(pix)
        __temp_264260 = __temp_264259
        __temp_264260.extend(tag)
        __temp_264262 = ['-c:v', encoder]
        __temp_264262.extend(rc_amf)
        __temp_264263 = __temp_264262
        __temp_264263.extend(pix)
        __temp_264264 = __temp_264263
        __temp_264264.extend(tag)
        return [__temp_264260, __temp_264264]
    if encoder in ('h264_videotoolbox', 'hevc_videotoolbox'):
        if rc_vt:
            __temp_264267 = ['-c:v', encoder]
            __temp_264267.extend(rc_vt)
            __temp_264267.append('-pix_fmt')
            __temp_264267.append('yuv420p')
            __temp_264268 = __temp_264267
            __temp_264268.extend(tag)
            return [__temp_264268]
        return []
    return []



# Original qualified name: hwaccel_decode_args
def hwaccel_decode_args(config):
    app = __import__('app.core.gpu', fromlist=('effective_hw_encoder',), level=0)
    effective_hw_encoder = app.effective_hw_encoder
    pref = effective_hw_encoder(config)
    if pref in _CPU_PREFS:
        return []
    return ['-hwaccel', 'auto']



# NOT DECOMPILED: _nvidia_driver_ok


# Original qualified name: _hw_codec_args
def _hw_codec_args(encoder, quality, config):
    (__temp_264277, __temp_264278, __temp_264279, __temp_264280, __temp_264281
        ) = _QUALITY_TIERS.get(quality, _QUALITY_TIERS['preview'])
    nv_preset = __temp_264277
    qsv_preset = __temp_264278
    amf_quality = __temp_264279
    q = __temp_264280
    vt_bitrate = __temp_264281
    if quality == 'intermediate':
        q = _intermediate_q(config)
    if encoder == 'h264_nvenc':
        return ['-c:v', 'h264_nvenc', '-preset', nv_preset, '-rc', 'vbr', '-cq',
            q, '-b:v', '0', '-pix_fmt', 'yuv420p']
    if encoder == 'h264_qsv':
        return ['-c:v', 'h264_qsv', '-preset', qsv_preset, '-global_quality', q,
            '-pix_fmt', 'nv12']
    if encoder == 'h264_amf':
        return ['-c:v', 'h264_amf', '-quality', amf_quality, '-rc', 'cqp',
            '-qp_i', q, '-qp_p', q, '-pix_fmt', 'yuv420p']
    if encoder == 'h264_videotoolbox':
        return ['-c:v', 'h264_videotoolbox', '-b:v', vt_bitrate, '-pix_fmt',
            'yuv420p']
    return None



# NOT DECOMPILED: resolve_video_codec_chain


# NOT DECOMPILED: resolve_video_codec_args


# NOT DECOMPILED: resolve_profile_codec_chain


# Original qualified name: audio_codec_args
def audio_codec_args(audio_mode, quality):
    if audio_mode == 'none':
        return []
    if quality == 'export':
        bitrate = '192k'
    else:
        bitrate = '128k'
    return ['-c:a', 'aac', '-b:a', bitrate]

