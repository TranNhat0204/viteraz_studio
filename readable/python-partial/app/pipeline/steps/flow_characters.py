# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/flow_characters.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _slug
def _slug(name):
    return _slugify(name, 40, default='char')



# Original qualified name: _portrait_prompt
def _portrait_prompt(engine, name, description, aspect):
    app = __import__('app.services.channel_engines', fromlist=(
        'portrait_prompt',), level=0)
    portrait_prompt = app.portrait_prompt
    return portrait_prompt(engine, name, description, aspect=aspect)



# NOT DECOMPILED: FlowCharactersStep.run
