# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/revo_voice_store.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: manifest_path
def manifest_path():
    sys = __import__('sys', fromlist=None, level=0)
    meipass = getattr(sys, '_MEIPASS', None)
    if meipass:
        p = Path(meipass) / 'app' / 'resources' / 'revo_voices.json'
        if p.is_file():
            return p
    return Path(__file__).resolve().parent / 'presets' / 'revo_voices.json'



# NOT DECOMPILED: load_manifest


# Original qualified name: reset_cache
def reset_cache():
    global _MANIFEST
    _MANIFEST = None
    return None



# NOT DECOMPILED: manifest_voices


# NOT DECOMPILED: base_url


# NOT DECOMPILED: default_voice_ids


# Original qualified name: download_dir
def download_dir():
    app = __import__('app.config', fromlist=('get_settings',), level=0)
    get_settings = app.get_settings
    d = get_settings().data_dir / 'resources' / 'revo_voice' / 'models'
    d.mkdir(parents=True, exist_ok=True)
    return d



# NOT DECOMPILED: _installed_path


# Original qualified name: is_installed
def is_installed(entry):
    model = _installed_path(entry.get('model', ''))
    config = _installed_path(entry.get('config', ''))
    if model is not None:
        if config is None:
            return False
    else:
        return False
    __temp_139375 = entry.get('size')
    if not __temp_139375:
        size = int(0)
    else:
        size = int(__temp_139375)
    if not not size:
        return model.stat().st_size == size
    else:
        return not size



# NOT DECOMPILED: installed_ids


# NOT DECOMPILED: _sha256


# NOT DECOMPILED: _download_file


# Original qualified name: download_voice
def download_voice(voice_id, on_progress, cancel_check):
    entry = manifest_voices().get(voice_id)
    if entry is None:
        raise make_error(E.TTS_VOICE_INVALID, "Giọng '" + str(voice_id) +
            "' không có trong danh mục Revo Voice.")
    root = base_url()
    if not root:
        raise make_error(E.TTS_NETWORK,
            'Chưa cấu hình kho giọng Revo Voice (base_url rỗng).', hint=
            "Đặt Setting 'revo_voice_base_url' hoặc build lại manifest với --base-url."
            )
    dest_dir = download_dir()
    __temp_141412 = entry.get('name')
    if not __temp_141412:
        name = voice_id
    else:
        name = __temp_141412
    with _LOCK as __temp_141413:
        if on_progress:
            on_progress(1.0, 'Đang tải cấu hình giọng ' + str(name) + '…')
            __temp_141415 = entry.get('config_size')
        else:
            entry.get('config_size')
        if not __temp_141415:
            __temp_141417 = int(0)
            __temp_141418 = entry.get('config_sha256')
        else:
            int(__temp_141415)
            entry.get('config_sha256')
        if not __temp_141418:
            _download_file(str(root) + '/' + str(entry['config']), dest_dir /
                entry['config'], __temp_141417, str(''), cancel_check=cancel_check)
            __temp_141423 = entry.get('size')
        else:
            _download_file(str(root) + '/' + str(entry['config']), dest_dir /
                entry['config'], __temp_141417, str(__temp_141418),
                cancel_check=cancel_check)
            entry.get('size')
        if not __temp_141423:
            mb = int(0) / 1000000.0
        else:
            mb = int(__temp_141423) / 1000000.0
        __temp_141429 = entry.get('size')
        if not __temp_141429:
            __temp_141430 = int(0)
            __temp_141431 = entry.get('sha256')
        else:
            int(__temp_141429)
            entry.get('sha256')
        if not __temp_141431:
            __temp_141434 = str('')
        else:
            str(__temp_141431)
        if on_progress:
    
            def __temp_141436(p):
                nonlocal mb, name, on_progress
                return on_progress(2.0 + p * 0.98, 'Đang tải giọng ' + str(name
                    ) + ' (' + format(mb, '.0f') + 'MB)… ' + format(p, '.0f') + '%'
                    )
            _download_file(str(root) + '/' + str(entry['model']), dest_dir /
                entry['model'], __temp_141430, __temp_141434, on_progress=
                __temp_141436, cancel_check=cancel_check)
            app = __import__('app.adapters.tts', fromlist=('revo_voice',), level=0)
            revo_voice = app.revo_voice
        else:
            _download_file(str(root) + '/' + str(entry['model']), dest_dir /
                entry['model'], __temp_141430, __temp_141434, on_progress=None,
                cancel_check=cancel_check)
            app = __import__('app.adapters.tts', fromlist=('revo_voice',), level=0)
            revo_voice = app.revo_voice
        revo_voice.reset_cache()
        log.info('[revo-voice] Đã tải giọng ' + str(name) + ' (' + str(voice_id
            ) + ').')
        return dest_dir / entry['model']



# NOT DECOMPILED: delete_voice
