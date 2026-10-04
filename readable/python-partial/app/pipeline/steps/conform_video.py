# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/conform_video.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _voice_speed_max


# Original qualified name: _plan_stretch
def _plan_stretch(v_dur, a_dur, voice_speed_max):
    f = math.sqrt(a_dur / v_dur)
    kv = f
    ka = f
    T = v_dur * kv
    if ka > voice_speed_max:
        ka = voice_speed_max
        T = a_dur / ka
        kv = T / v_dur
    if kv > _VIDEO_SLOW_MAX:
        kv = _VIDEO_SLOW_MAX
        T = v_dur * kv
        ka = a_dur / T
    return kv, ka, T



# NOT DECOMPILED: _atempo_filter


# NOT DECOMPILED: _stretch_voice


# NOT DECOMPILED: _rescale_subtitles


# NOT DECOMPILED: _write_conform_factors


# NOT DECOMPILED: _rescale_words


# NOT DECOMPILED: ConformVideoStep.run


# NOT DECOMPILED: ConformVideoStep._run_scene_conform
