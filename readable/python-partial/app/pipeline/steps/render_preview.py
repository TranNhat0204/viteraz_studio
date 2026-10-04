# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/render_preview.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: RenderPreviewStep._extra_hash
def _extra_hash(self, ctx):
    app = __import__('app.services.style_service', fromlist=(
        'resolve_style_for_config',), level=0)
    resolve_style_for_config = app.resolve_style_for_config
    return {'_resolved_style': resolve_style_for_config(ctx.config)}



# NOT DECOMPILED: RenderPreviewStep.run
