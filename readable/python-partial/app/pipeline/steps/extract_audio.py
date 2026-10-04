# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/extract_audio.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _need_source_audio
def _need_source_audio(config):
    explicit = config.get('keep_source_audio')
    if isinstance(explicit, bool):
        return explicit
    __temp_255843 = config.get('separate_audio')
    if not __temp_255843:
        __temp_255844 = config.get('keep_original_audio')
        if not __temp_255844:
            return bool(config.get('voice_clone_from_source'))
        else:
            return bool(__temp_255844)
    else:
        return bool(__temp_255843)



# NOT DECOMPILED: ExtractAudioStep.run


# Original qualified name: ExtractAudioStep.run.<locals>.on_prog
def on_prog(progress):
    nonlocal ctx
    ctx.emit_progress(progress, 'Đang tách âm thanh: ' + str(int(progress * 100
        )) + '%')
    return None

