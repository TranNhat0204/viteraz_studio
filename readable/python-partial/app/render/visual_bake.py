# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/visual_bake.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: normalize_transition


# Original qualified name: _ken_burns_vf
def _ken_burns_vf(w, h, zoom_in, total_frames):
    app = __import__('app.media.logo_zoom', fromlist=('safe_zoom_factor',), level=0
        )
    safe_zoom_factor = app.safe_zoom_factor
    n = max(1, int(total_frames))
    floor = max(1.0, safe_zoom_factor())
    if zoom_in:
        z = format(floor, '.4f') + '+0.12*on/' + str(n)
    else:
        z = format(floor + 0.12, '.4f') + '-0.12*on/' + str(n)
    ss_h = h * 4
    ss_w = w * 4
    return 'scale=' + str(ss_w) + ':' + str(ss_h
        ) + ':force_original_aspect_ratio=increase:flags=lanczos,crop=' + str(ss_w
        ) + ':' + str(ss_h) + ",zoompan=z='" + str(z) + "':d=" + str(n
        ) + ":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=" + str(w) + 'x' + str(h
        ) + ':fps=' + str(_FPS) + ',format=yuv420p,setsar=1'



# Original qualified name: _fit_vf
def _fit_vf(w, h):
    app = __import__('app.media.logo_zoom', fromlist=('cover_zoom_vf',), level=0)
    cover_zoom_vf = app.cover_zoom_vf
    return cover_zoom_vf(w, h, _FPS)



# NOT DECOMPILED: real_file


# Original qualified name: _media_kind
def _media_kind(p, declared):
    suf = p.suffix.lower()
    if suf in _VIDEO_SUFFIXES:
        return video
    if suf in _IMAGE_SUFFIXES:
        return image
    if declared in ('video', 'image'):
        return declared
    return 'image'



# Original qualified name: buildable_asset
def buildable_asset(scene):
    if not isinstance(scene, dict):
        return None
    p = real_file(scene.get('asset_path'))
    if p is not None:
        return p, _media_kind(p, scene.get('asset_kind'))
    p = real_file(scene.get('image_path'))
    if p is not None:
        return p, 'image'
    return None



# Original qualified name: dims_for
def dims_for(config):
    app = __import__('app.pipeline.steps.flow_generate', fromlist=(
        'aspect_to_dims',), level=0)
    aspect_to_dims = app.aspect_to_dims
    engine_id = config.get('engine_id')
    if engine_id:
        engine = channel_engines.get_engine(engine_id)
    else:
        engine = None
    aspect = config.get('aspect')
    if aspect not in ('16:9', '9:16'):
        if engine:
            __temp_265004 = engine.meta.get('aspect_ratio')
        if not __temp_265004:
            aspect = '16:9'
        else:
            aspect = __temp_265004
    return aspect_to_dims(aspect)



# NOT DECOMPILED: _load_scenes


# Original qualified name: default_clips
def default_clips(scenes):
    clips = []
    for __temp_265016 in iter(scenes):
        s = __temp_265016
        if s.get('render_skip'):
            continue
            seq = s.get('seq')
        else:
            seq = s.get('seq')
        if seq is None:
            continue
            __temp_265021 = s.get('render_start_ms', s.get('start_ms', 0))
        else:
            s.get('render_start_ms', s.get('start_ms', 0))
        if not __temp_265021:
            start = int(0)
        else:
            start = int(__temp_265021)
        __temp_265027 = s.get('render_end_ms', s.get('end_ms', start + 4000))
        if not __temp_265027:
            end = int(start + 4000)
        else:
            end = int(__temp_265027)
        if end <= start:
            end = start + _MIN_SCENE_MS
        clips.append({seq: int(seq), start_ms: start, end_ms: end})
        continue
    
    
    def __temp_265033(c):
        return c['start_ms']
    
    
    clips.sort(key=__temp_265033)
    return clips



# NOT DECOMPILED: resolve_clips


# NOT DECOMPILED: _run


# NOT DECOMPILED: _render_image_clip


# NOT DECOMPILED: _render_video_clip


# NOT DECOMPILED: _render_black_clip


# NOT DECOMPILED: _concat


# Original qualified name: build_xfade_graph
def build_xfade_graph(durs, trans):
    chains = []
    prev = '0:v'
    running = durs[0]
    for __temp_265118 in iter(range(1, len(durs))):
        k = __temp_265118
        tr = trans[k - 1]
        lbl = 'vt' + str(k)
        if tr:
            tdur = float(tr['dur'])
            off = max(0.0, running - tdur)
            chains.append('[' + str(prev) + '][' + str(k) +
                ':v]xfade=transition=' + str(tr['type']) + ':duration=' +
                format(tdur, '.3f') + ':offset=' + format(off, '.3f') + '[' +
                str(lbl) + ']')
            running = running + durs[k] - tdur
        else:
            chains.append('[' + str(prev) + '][' + str(k) +
                ':v]concat=n=2:v=1:a=0[' + str(lbl) + ']')
            running = running + durs[k]
        prev = lbl
        continue
    return ';'.join(chains), prev, running



# NOT DECOMPILED: _render_transitions


# NOT DECOMPILED: bake_source


# NOT DECOMPILED: bake_source.<locals>._encode


# NOT DECOMPILED: ensure_source
