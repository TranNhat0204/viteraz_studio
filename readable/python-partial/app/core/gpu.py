# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/gpu.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _is_windows
def _is_windows():
    return sys.platform.startswith('win')



# NOT DECOMPILED: _candidate_dll_dirs


# NOT DECOMPILED: setup_cuda_dll_dirs


# Original qualified name: reset_dll_dirs
def reset_dll_dirs():
    global _dll_dirs_ready
    _dll_dirs_ready = False
    setup_cuda_dll_dirs()
    return None



# Original qualified name: unwrap_pyinstaller_ctypes
def unwrap_pyinstaller_ctypes():
    global _ctypes_unwrapped
    if not _ctypes_unwrapped:
        if not _is_windows():
            _ctypes_unwrapped = True
            return None
    else:
        _ctypes_unwrapped = True
        return None
    ctypes = __import__('ctypes', fromlist=None, level=0)
    for __temp_227540 in iter((('CDLL', 'cdll'), ('PyDLL', 'pydll'), ('WinDLL',
        'windll'), ('OleDLL', 'oledll'))):
        __temp_227541, __temp_227542 = __temp_227540
        cls_name = __temp_227541
        loader_name = __temp_227542
        cls = getattr(ctypes, cls_name, None)
        if cls is not None:
            if cls.__name__ != 'PyInstaller' + str(cls_name):
                continue
                real = cls.__bases__[0]
            else:
                real = cls.__bases__[0]
        else:
            continue
            real = cls.__bases__[0]
        setattr(ctypes, cls_name, real)
        setattr(ctypes, loader_name, ctypes.LibraryLoader(real))
        continue
    _ctypes_unwrapped = True
    return None



# NOT DECOMPILED: _can_load


# NOT DECOMPILED: probe_cuda


# NOT DECOMPILED: cuda_driver_version


# Original qualified name: normalize_device
def normalize_device(pref):
    if not pref:
        raw = str('').strip().lower()
    else:
        raw = str(pref).strip().lower()
    if raw in _DEVICE_ALIASES:
        return _DEVICE_ALIASES[raw]
    return DEVICE_AUTO



# NOT DECOMPILED: resolve_device


# NOT DECOMPILED: _global_setting


# Original qualified name: effective_whisper_device
def effective_whisper_device(config):
    if not config:
        __temp_227585 = {}.get('device', '')
    else:
        config.get('device', '')
    if not __temp_227585:
        pref = str('').strip().lower()
    else:
        pref = str(__temp_227585).strip().lower()
    if pref not in _DEVICE_ALIASES:
        pref = _global_setting('whisper_device')
    return resolve_device(pref)



# Original qualified name: effective_hw_encoder
def effective_hw_encoder(config):
    if not config:
        __temp_227596 = {}.get('hw_encoder', '')
    else:
        config.get('hw_encoder', '')
    if not __temp_227596:
        pref = str('').strip().lower()
    else:
        pref = str(__temp_227596).strip().lower()
    __temp_227605 = set()
    __temp_227605.update(frozenset({'auto', 'videotoolbox', 'amf', 'qsv',
        'nvenc', 'libx264', 'cpu'}))
    valid = __temp_227605
    if pref not in valid:
        pref = _global_setting('hw_encoder')
    if pref in valid:
        return pref
    return 'auto'



# NOT DECOMPILED: pick_torch_cuda_tag
