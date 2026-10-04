# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/transcribe.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: TranscribeStep.run


# Original qualified name: TranscribeStep.run.<locals>.on_prog
def on_prog(progress, text):
    nonlocal ctx
    ctx.emit_progress(progress, text)
    return None

