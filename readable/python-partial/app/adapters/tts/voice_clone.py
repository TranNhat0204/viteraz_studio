# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/voice_clone.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: voice_clones_dir
def voice_clones_dir():
    app = __import__('app.config', fromlist=('get_settings',), level=0)
    get_settings = app.get_settings
    d = get_settings().data_dir / 'resources' / 'voice_clones'
    d.mkdir(parents=True, exist_ok=True)
    return d



# Original qualified name: target_se_path
def target_se_path(clone_id):
    return voice_clones_dir() / str(clone_id) + '.pth'

