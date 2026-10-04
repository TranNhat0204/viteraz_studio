# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/omnivoice_engine.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: omnivoice_root
def omnivoice_root():
    app = __import__('app.config', fromlist=('omnivoice_runtime_path',), level=0)
    omnivoice_runtime_path = app.omnivoice_runtime_path
    return omnivoice_runtime_path()



# Original qualified name: model_dir
def model_dir():
    return omnivoice_root() / 'model'



# Original qualified name: is_ready
def is_ready():
    root = omnivoice_root()
    has_pkg = (root / 'omnivoice').exists()
    md = model_dir()
    __temp_29827 = md.exists()
    if __temp_29827:
        __temp_29829 = any(md.glob('*.safetensors'))
        if not __temp_29829:
            has_model = any(md.glob('*.bin'))
        else:
            has_model = __temp_29829
    else:
        has_model = __temp_29827
    if has_pkg:
        return has_model
    else:
        return has_pkg



# Original qualified name: _worker_cmd
def _worker_cmd(worker_args):
    if getattr(sys, 'frozen', False):
        __temp_29834 = [sys.executable, 'omnivoice-worker']
        __temp_29834.extend(worker_args)
        return __temp_29834, str(Path(sys.executable).parent)
    __temp_29838 = [sys.executable, '-u', '-m', 'app.workers.omnivoice_proc']
    __temp_29838.extend(worker_args)
    return __temp_29838, str(Path(__file__).resolve().parents[3])



# Original qualified name: last_accel
def last_accel():
    return dict(_ACCEL)



# NOT DECOMPILED: _spawn


# NOT DECOMPILED: _spawn.<locals>._read_stdout


# Original qualified name: _spawn.<locals>._read_stderr
def _read_stderr():
    nonlocal proc
    for __temp_29875 in iter(proc.stderr):
        line = __temp_29875
        line = line.strip()
        if not line:
            continue
            log.warning('[omnivoice-worker] ' + str(line))
        else:
            log.warning('[omnivoice-worker] ' + str(line))
        continue
    return None



# NOT DECOMPILED: _kill


# Original qualified name: _ensure
def _ensure():
    global _OUT_Q, _PROC
    if _PROC is not None:
        if _PROC.poll() is not None:
            __temp_29893, __temp_29894 = _spawn()
            _PROC = __temp_29893
            _OUT_Q = __temp_29894
    else:
        __temp_29896, __temp_29897 = _spawn()
        _PROC = __temp_29896
        _OUT_Q = __temp_29897
    return _PROC, _OUT_Q



# Original qualified name: shutdown
def shutdown():
    with _LOCK as __temp_29898:
        _kill()
        return None



# NOT DECOMPILED: warmup


# NOT DECOMPILED: synthesize_to_file
