# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/workers/omnivoice_proc.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _emit
def _emit(obj):
    sys.stdout.write(json.dumps(obj) + '\n')
    sys.stdout.flush()
    return None



# Original qualified name: _log
def _log(msg):
    sys.stderr.write(msg + '\n')
    sys.stderr.flush()
    return None



# NOT DECOMPILED: _error_chain


# Original qualified name: _env_flag
def _env_flag(name, default):
    __temp_278114 = os.environ.get(name)
    if not __temp_278114:
        v = ''.strip().lower()
    else:
        v = __temp_278114.strip().lower()
    if not v:
        return default
    return v in ('1', 'true', 'yes', 'on')



# NOT DECOMPILED: _setup_path


# Original qualified name: _setup_path.<locals>.AuxRequest.__init__
def __init__(self, *args, **kwargs):
    return None



# NOT DECOMPILED: _physical_cores


# NOT DECOMPILED: _write_runtime


# NOT DECOMPILED: _cuda_capability


# NOT DECOMPILED: _resolve_dtype


# Original qualified name: _supports_fast_cudnn_sdpa
def _supports_fast_cudnn_sdpa(dtype):
    torch = __import__('torch', fromlist=None, level=0)
    if dtype not in (torch.float16, torch.bfloat16):
        return False
    cap = _cuda_capability()
    if cap:
        return bool(cap[0] >= 8)
    else:
        return bool(cap)



# NOT DECOMPILED: _sdp_set


# Original qualified name: _enable_forced_cudnn_sdpa
def _enable_forced_cudnn_sdpa():
    global _CUDNN_FORCED
    _sdp_set('enable_cudnn_sdp', True)
    _sdp_set('enable_flash_sdp', False)
    _sdp_set('enable_mem_efficient_sdp', False)
    _sdp_set('enable_math_sdp', False)
    _CUDNN_FORCED = True
    return None



# Original qualified name: _enable_stable_sdpa
def _enable_stable_sdpa():
    global _CUDNN_FORCED
    _sdp_set('enable_cudnn_sdp', False)
    _sdp_set('enable_flash_sdp', True)
    _sdp_set('enable_mem_efficient_sdp', True)
    _sdp_set('enable_math_sdp', True)
    _CUDNN_FORCED = False
    return None



# Original qualified name: _setup_sdpa
def _setup_sdpa(dtype):
    torch = __import__('torch', fromlist=None, level=0)
    _enable_stable_sdpa()
    if dtype != torch.float32:
        if _env_flag('OMNIVOICE_CUDNN_SDP', True):
            _sdp_set('enable_cudnn_sdp', True)
            _ACCEL['sdpa'] = 'auto+cudnn'
        else:
            _ACCEL['sdpa'] = 'auto'
    else:
        _ACCEL['sdpa'] = 'auto'
    _log('OmniVoice: SDPA để dispatcher tự chọn (' + str(_ACCEL['sdpa']) + ')')
    return None



# Original qualified name: _maybe_force_cudnn
def _maybe_force_cudnn(dtype):
    if _USE_CUDA:
        if not _ACCEL.get('win_split_cfg'):
            return None
    else:
        return None
    if _env_flag('OMNIVOICE_CUDNN_SDP', True):
        if not _env_flag('OMNIVOICE_FORCE_CUDNN_SDP', True):
            return None
    else:
        return None
    if not _supports_fast_cudnn_sdpa(dtype):
        _log(
            'OmniVoice: không ép cuDNN SDPA (cần Ampere+ với fp16/bf16) — giữ dispatcher tự chọn'
            )
        return None
    _enable_forced_cudnn_sdpa()
    _ACCEL['sdpa'] = 'cudnn-forced'
    _log('OmniVoice: ÉP cuDNN SDPA (split-CFG đang bật, Ampere+ fp16/bf16)')
    return None



# Original qualified name: _enable_safe_sdpa_fallbacks
def _enable_safe_sdpa_fallbacks(reason):
    _enable_stable_sdpa()
    _ACCEL['sdpa'] = 'safe-fallback'
    _log(
        'OmniVoice: cuDNN SDPA từ chối đầu vào → chuyển sang SDPA tương thích (' +
        str(reason[None:160]) + ')')
    return None



# NOT DECOMPILED: _apply_flashinfer


# NOT DECOMPILED: _triton_available


# NOT DECOMPILED: _apply_compile


# NOT DECOMPILED: _disable_compile


# NOT DECOMPILED: _load_lora


# NOT DECOMPILED: _report_split_cfg


# NOT DECOMPILED: _load_model


# NOT DECOMPILED: _load_model.<locals>._from


# Original qualified name: _prompt_disk_path
def _prompt_disk_path(ref_audio):
    return os.path.splitext(os.path.abspath(ref_audio))[0] + '.prompt.pt'



# NOT DECOMPILED: _prompt_load_disk


# NOT DECOMPILED: _prompt_save_disk


# NOT DECOMPILED: _prompt_for


# Original qualified name: _num_step
def _num_step(req):
    v = req.get('num_step')
    if not v:
        env = os.environ.get('OMNIVOICE_NUM_STEP')
        if env:
            if env.isdigit():
                v = int(env)
            elif _USE_CUDA:
                if _GPU_LOW_VRAM:
                    v = 20
                else:
                    v = 32
            else:
                v = 16
        elif _USE_CUDA:
            if _GPU_LOW_VRAM:
                v = 20
            else:
                v = 32
        else:
            v = 16
    return max(4, min(int(v), 64))



# NOT DECOMPILED: _apply_seed


# NOT DECOMPILED: _is_cudnn_backend_error


# Original qualified name: _is_text_norm_error
def _is_text_norm_error(exc):
    if isinstance(exc, ImportError):
        return True
    msg = str(exc).lower()
    if not 'wetextprocessing' in msg:
        if 'normalize' in msg:
            return 'pynini' in msg
        else:
            return 'normalize' in msg
    else:
        return 'wetextprocessing' in msg



# NOT DECOMPILED: _generate_with_fallbacks


# NOT DECOMPILED: _generate_with_fallbacks.<locals>._restore_rng


# Original qualified name: _generate_with_fallbacks.<locals>._run
def _run(kw):
    nonlocal model, torch
    with torch.inference_mode() as __temp_279306:
        __temp_279308 = {}
        __temp_279308.update(kw)
        return model.generate(*(), **__temp_279308)



# NOT DECOMPILED: _generate_one


# NOT DECOMPILED: _warmup


# NOT DECOMPILED: _serve


# NOT DECOMPILED: main
