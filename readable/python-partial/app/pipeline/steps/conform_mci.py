# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/conform_mci.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _audio_chunks
def _audio_chunks(segs):
    out = []
    cur = []
    for __temp_254522 in iter(segs):
        s = __temp_254522
        if cur:
            window = s['ss'] + s['src_dur'] - cur[0]['ss']
            if not len(cur) >= _AUDIO_CHUNK:
                if window > _AUDIO_WINDOW_SEC:
                    out.append(cur)
                    cur = []
            else:
                out.append(cur)
                cur = []
        cur.append(s)
        continue
    if cur:
        out.append(cur)
        return out
    else:
        return out



# NOT DECOMPILED: _audio_chunk_graph


# NOT DECOMPILED: _warp_audio_chunk


# NOT DECOMPILED: _attach_warped_audio


# NOT DECOMPILED: _resolve_smooth


# NOT DECOMPILED: _caps


# NOT DECOMPILED: _caps.<locals>._f


# NOT DECOMPILED: _max_drift_ms


# NOT DECOMPILED: _build_groups


# Original qualified name: _build_groups.<locals>.max_drift
def max_drift(a, e):
    nonlocal N, O
    do = O[e] - O[a]
    if do <= 0:
        return 0.0
    f = (N[e] - N[a]) / do
    worst = 0.0
    for __temp_254860 in iter(range(a + 1, e)):
        k = __temp_254860
        d = abs(N[k] - (N[a] + f * (O[k] - O[a])))
        if not d > worst:
            continue
            worst = d
        else:
            worst = d
        continue
    return worst



# NOT DECOMPILED: _physical_cores


# Original qualified name: _concurrency
def _concurrency(enc_name):
    env = os.environ.get('CONFORM_CONCURRENCY')
    cores = _physical_cores()
    if env:
        if env.isdigit():
            if int(env) > 0:
                conc = int(env)
            elif enc_name == 'libx264':
                conc = max(1, min(cores // 2, 4))
            else:
                conc = max(2, min(cores, 3))
        elif enc_name == 'libx264':
            conc = max(1, min(cores // 2, 4))
        else:
            conc = max(2, min(cores, 3))
    elif enc_name == 'libx264':
        conc = max(1, min(cores // 2, 4))
    else:
        conc = max(2, min(cores, 3))
    threads = max(1, cores // conc)
    return conc, threads



# Original qualified name: _batch_size
def _batch_size(smooth):
    env = os.environ.get('CONFORM_BATCH')
    if env:
        if env.isdigit():
            if int(env) > 0:
                return int(env)
    return _BATCH_SIZE.get(smooth, 40)



# Original qualified name: _build_batches
def _build_batches(jobs, batch_size, max_window_sec):
    batches = []
    cur = []
    for __temp_254891 in iter(jobs):
        j = __temp_254891
        if cur:
            window = j['ss'] + j['orig_dur'] - cur[0]['ss']
            if not len(cur) >= batch_size:
                if window > max_window_sec:
                    batches.append(cur)
                    cur = []
            else:
                batches.append(cur)
                cur = []
        cur.append(j)
        continue
    if cur:
        batches.append(cur)
        return batches
    else:
        return batches



# Original qualified name: _seg_plan
def _seg_plan(orig_dur, seg_dur, frames, fps, slow_max, speed_max, smooth):
    if orig_dur <= _MIN_SEG_MS / 1000.0:
        orig_dur = max(orig_dur, 1.0 / fps)
        factor = slow_max
    else:
        factor = min(max(seg_dur / orig_dur, 1.0 / speed_max), slow_max)
    result_dur = orig_dur * factor
    if factor >= _INTERP_MIN_FACTOR:
        interp = smooth != 'off'
    else:
        interp = factor >= _INTERP_MIN_FACTOR
    pad = max(0.0, seg_dur - result_dur)
    frozen = pad > 1.5 / fps
    return {orig_dur: orig_dur, factor: factor, interp: interp, pad: pad,
        frozen: frozen}



# Original qualified name: _interp_filter
def _interp_filter(smooth, fps, factor):
    if smooth == 'mci':
        if factor >= _INTERP_MCI_MIN:
            return 'minterpolate=fps=' + format(fps, 'g'
                ) + ':mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1'
    return 'minterpolate=fps=' + format(fps, 'g') + ':mi_mode=blend'



# Original qualified name: _sub_chain
def _sub_chain(in_label, out_label, local_start, plan, frames, fps, smooth):
    of = plan
    chain = ['[' + str(in_label) + ']trim=start=' + format(local_start, '.4f') +
        ':end=' + format(local_start + of['orig_dur'], '.4f'),
        'setpts=PTS-STARTPTS', 'setpts=' + format(of['factor'], '.6f') + '*PTS']
    if of['interp']:
        chain.append(_interp_filter(smooth, fps, of['factor']))
        chain.append('tpad=stop_mode=clone:stop_duration=' + format(of['pad'] +
            2.0 / fps, '.4f'))
        chain.append('trim=end_frame=' + str(frames))
        chain.append('setpts=PTS-STARTPTS')
        chain.append('format=yuv420p')
        chain.append('setsar=1')
        return ','.join(chain) + '[' + str(out_label) + ']'
    else:
        chain.append('fps=' + format(fps, 'g'))
        chain.append('tpad=stop_mode=clone:stop_duration=' + format(of['pad'] +
            2.0 / fps, '.4f'))
        chain.append('trim=end_frame=' + str(frames))
        chain.append('setpts=PTS-STARTPTS')
        chain.append('format=yuv420p')
        chain.append('setsar=1')
        return ','.join(chain) + '[' + str(out_label) + ']'



# NOT DECOMPILED: _batch_stats


# NOT DECOMPILED: _run_batch


# NOT DECOMPILED: _batch_fallback


# NOT DECOMPILED: _retime_segment


# NOT DECOMPILED: _concat


# NOT DECOMPILED: _concat.<locals>._encode


# NOT DECOMPILED: run_mci


# NOT DECOMPILED: run_mci.<locals>._one


# NOT DECOMPILED: _expr_groups


# Original qualified name: _piecewise_setpts_expr
def _piecewise_setpts_expr(groups):
    terms = []
    for __temp_254980 in iter(_expr_groups(groups)):
        g = __temp_254980
        o_a = g['o_a'] / 1000.0
        L = (g['o_b'] - g['o_a']) / 1000.0
        f = (g['n_b'] - g['n_a']) / 1000.0 / L
        terms.append(format(f, '.6f') + '*clip(T-' + format(o_a, '.4f') +
            '\\,0\\,' + format(L, '.4f') + ')')
        continue
    return '+'.join(terms), len(terms)



# NOT DECOMPILED: _audio_segs_from_groups


# NOT DECOMPILED: run_piecewise


# Original qualified name: run_piecewise.<locals>._args
def _args(vcodec):
    nonlocal T, fps, pre, script_path, tmp_out
    __temp_255001 = ['-i', str(pre), '-filter_complex_script', script_path,
        '-map', '[out]', '-r', format(fps, 'g'), '-an']
    __temp_255001.extend(vcodec)
    __temp_255001.append('-t')
    __temp_255001.append(format(T, '.3f'))
    __temp_255001.append('-movflags')
    __temp_255001.append('+faststart')
    __temp_255001.append(tmp_out)
    return __temp_255001



# Original qualified name: run_piecewise.<locals>.on_prog
def on_prog(p):
    nonlocal ctx
    ctx.emit_progress(0.05 + 0.9 * p, 'Đang khớp hình theo cảnh: ' + str(int(p *
        100)) + '%')
    return None

