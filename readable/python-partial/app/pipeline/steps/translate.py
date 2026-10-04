# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/translate.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: TranslateStep.run


# Original qualified name: TranslateStep.run.<locals>.on_prog
def on_prog(progress, text):
    nonlocal ctx
    base = 0.05 + progress * 0.9
    ctx.emit_progress(base, str(text))
    return None



# NOT DECOMPILED: TranslateStep.run.<locals>._do_translate
