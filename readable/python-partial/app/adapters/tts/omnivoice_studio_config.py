# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/omnivoice_studio_config.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: OmniStudioConfig.as_dict
def as_dict(self):
    return asdict(self)



# Original qualified name: _path
def _path():
    app = __import__('app.config', fromlist=('get_settings',), level=0)
    get_settings = app.get_settings
    return get_settings().data_dir / _FILE



# NOT DECOMPILED: load


# NOT DECOMPILED: save
