# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/separate_audio.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: SeparateAudioStep.run


# Original qualified name: SeparateAudioStep.run.<locals>.on_prog
def on_prog(p):
    nonlocal ctx
    ctx.emit_progress(p, 'Đang tách nguồn: ' + str(int(p * 100)) + '%')
    return None



# NOT DECOMPILED: SeparateAudioStep._ensure_source_audio


# NOT DECOMPILED: SeparateAudioStep._wire_music_into_config
