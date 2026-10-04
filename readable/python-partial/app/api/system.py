# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/system.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _pip_install_cmd
def _pip_install_cmd(args):
    if getattr(sys, 'frozen', False):
        __temp_209980 = [sys.executable, 'pip', 'install']
        __temp_209980.extend(args)
        return __temp_209980
    __temp_209982 = [sys.executable, '-m', 'pip', 'install']
    __temp_209982.extend(args)
    return __temp_209982



# NOT DECOMPILED: _is_transient_pip_err


# NOT DECOMPILED: _run_pip_retry


# NOT DECOMPILED: _clear_readonly


# Original qualified name: _robust_rmtree
def _robust_rmtree(path):
    _clear_readonly(path)
    shutil.rmtree(path, ignore_errors=True)
    return None



# NOT DECOMPILED: _short_pip_tmp


# Original qualified name: _torch_pip_args
def _torch_pip_args(prefer_gpu):
    app = __import__('app.core', fromlist=('gpu',), level=0)
    gpu = app.gpu
    if prefer_gpu:
        tag = gpu.pick_torch_cuda_tag()
    else:
        tag = None
    if tag:
        return ['torch', 'torchaudio', '--index-url', 
            'https://download.pytorch.org/whl/' + str(tag)], tag
    __temp_210036 = []
    __temp_210036.extend(('torch', 'torchaudio', '--only-binary', ':all:'))
    return __temp_210036, None



# Original qualified name: health
def health():
    return {status: 'ok', version: VERSION, db: 'ok'}



# Original qualified name: ffmpeg_check
def ffmpeg_check(path):
    if path:
        p = Path(path)
        if p.exists():
            if p.is_file():
                return {ok: True, path: str(p.resolve()), version: 'custom version'
                    }
        resolved = (get_settings().data_dir / p).resolve()
        if resolved.exists():
            if resolved.is_file():
                return {ok: True, path: str(resolved), version: 'custom version'}
        exe = shutil.which(path)
        if exe:
            return {ok: True, path: exe, version: 'custom version'}
    local_path = get_settings().data_dir / 'resources' / 'ffmpeg' / 'ffmpeg.exe'
    if local_path.exists():
        return {ok: True, path: str(local_path), version: 'v6.1 local'}
    exe = shutil.which('ffmpeg')
    if exe:
        return {ok: True, path: exe, version: 'system version'}
    return {ok: False, error_code: 'FFMPEG_NOT_FOUND', hint:
        "Chọn ffmpeg.exe trong Settings hoặc bấm nút 'Tải & Cài đặt FFmpeg' để cài đặt tự động."
        }



# NOT DECOMPILED: get_windows_gpus


# NOT DECOMPILED: perf_snapshot


# NOT DECOMPILED: gpu_check


# NOT DECOMPILED: _toolkit_message


# Original qualified name: _set_toolkit_state
def _set_toolkit_state(status, progress, profile, phase, error_code, installed_profile, error_detail):
    state = install_states['toolkit']
    __temp_210101 = round(progress, 1)
    __temp_210102 = _toolkit_message(phase, status, error_detail)
    if profile is not None:
        state.update({status: status, progress: __temp_210101, message:
            __temp_210102, profile: profile, phase: phase, error_code:
            error_code, error_detail: error_detail})
    else:
        state.update({status: status, progress: __temp_210101, message:
            __temp_210102, profile: state.get('profile'), phase: phase,
            error_code: error_code, error_detail: error_detail})
    if installed_profile is not None:
        state['installed_profile'] = installed_profile
    bus.emit_nowait({type: 'system.progress', target: 'toolkit', profile: state
        .get('profile'), phase: phase, status: status, progress: state[
        'progress'], message: state['message'], error_code: error_code,
        error_detail: error_detail})
    return None



# Original qualified name: _local_media_engine_path
def _local_media_engine_path():
    return get_settings().data_dir / 'resources' / 'ffmpeg' / 'ffmpeg.exe'



# Original qualified name: _is_media_engine_ready
def _is_media_engine_ready():
    __temp_210113 = _local_media_engine_path().exists()
    if not __temp_210113:
        return shutil.which('ffmpeg') is not None
    else:
        return __temp_210113



# Original qualified name: _is_speech_engine_ready
def _is_speech_engine_ready(model):
    model_dir = get_settings().data_dir / 'models' / model
    __temp_210116 = (model_dir / 'model.bin').exists()
    if __temp_210116:
        return (model_dir / 'config.json').exists()
    else:
        return __temp_210116



# Original qualified name: _local_edge_tts_path
def _local_edge_tts_path():
    return get_settings().data_dir / 'resources' / 'edge-tts'



# Original qualified name: _is_edge_tts_ready
def _is_edge_tts_ready():
    pkg_dir = _local_edge_tts_path()
    __temp_210120 = (pkg_dir / 'edge_tts').exists()
    if __temp_210120:
        return any((pkg_dir / 'edge_tts').iterdir())
    else:
        return __temp_210120



# NOT DECOMPILED: _toolkit_status_response


# Original qualified name: ensure_media_engine_sync
def ensure_media_engine_sync(on_progress):
    if not _is_media_engine_ready():
        download_ffmpeg_sync(on_progress=on_progress)
        return None
    if on_progress:
        on_progress(100.0)
        return None
    return None



# Original qualified name: ensure_speech_engine_sync
def ensure_speech_engine_sync(model, on_progress):
    if not _is_speech_engine_ready(model):
        download_whisper_sync(model, on_progress=on_progress)
        return None
    if on_progress:
        on_progress(100.0)
        return None
    return None



# Original qualified name: ensure_edge_tts_sync
def ensure_edge_tts_sync(on_progress):
    if not _is_edge_tts_ready():
        download_edge_tts_sync(on_progress=on_progress)
        return None
    if on_progress:
        on_progress(100.0)
        return None
    return None



# Original qualified name: ensure_revo_voice_sync
def ensure_revo_voice_sync(on_progress):
    if not _is_revo_voice_ready():
        download_revo_voice_sync(on_progress=on_progress)
        return None
    if on_progress:
        on_progress(100.0)
        return None
    return None



# NOT DECOMPILED: install_toolkit_profile_sync


# Original qualified name: install_toolkit_profile_sync.<locals>.media_cb
def media_cb(p):
    nonlocal profile
    overall = 10.0 + p / 100.0 * 20.0
    _set_toolkit_state(status='installing', progress=overall, profile=profile,
        phase='media_engine')
    return None



# Original qualified name: install_toolkit_profile_sync.<locals>.speech_cb
def speech_cb(p):
    nonlocal profile
    overall = 25.0 + p / 100.0 * 53.0
    _set_toolkit_state(status='installing', progress=overall, profile=profile,
        phase='speech_engine')
    return None



# Original qualified name: install_toolkit_profile_sync.<locals>.floor_cb
def floor_cb(p):
    nonlocal profile
    overall = 78.0 + p / 100.0 * 7.0
    _set_toolkit_state(status='installing', progress=overall, profile=profile,
        phase='speech_engine')
    return None



# NOT DECOMPILED: download_ffmpeg_sync


# NOT DECOMPILED: download_whisper_sync


# NOT DECOMPILED: download_edge_tts_sync


# Original qualified name: _local_kokoro_path
def _local_kokoro_path():
    return get_settings().data_dir / 'resources' / 'kokoro'



# Original qualified name: _is_kokoro_ready
def _is_kokoro_ready():
    pkg_dir = _local_kokoro_path()
    __temp_225316 = (pkg_dir / 'kokoro').exists()
    if __temp_225316:
        has_kokoro = any((pkg_dir / 'kokoro').iterdir())
    else:
        has_kokoro = __temp_225316
    has_misaki = (pkg_dir / 'misaki').exists()
    has_spacy = (pkg_dir / 'spacy').exists()
    if has_kokoro:
        if has_misaki:
            return has_spacy
        else:
            return has_misaki
    else:
        return has_kokoro



# Original qualified name: _kokoro_status_response
def _kokoro_status_response():
    state = install_states.get('kokoro', {status: 'idle', progress: 0.0,
        message: ''}).copy()
    status = state.get('status', 'idle')
    if status in frozenset({'installing', 'checking', 'downloading'}):
        return state
    if status == 'failed':
        return state
    if _is_kokoro_ready():
        return {status: 'success', progress: 100.0, message:
            'Kokoro TTS đã sẵn sàng!'}
    return {status: 'idle', progress: 0.0, message: ''}



# Original qualified name: _local_kokoro_vi_path
def _local_kokoro_vi_path():
    return get_settings().data_dir / 'resources' / 'kokoro_vi'



# Original qualified name: _is_kokoro_vi_ready
def _is_kokoro_vi_ready():
    pkg_dir = _local_kokoro_vi_path()
    __temp_225330 = (pkg_dir / 'kokoro_vietnamese').exists()
    if __temp_225330:
        has_vi = any((pkg_dir / 'kokoro_vietnamese').iterdir())
    else:
        has_vi = __temp_225330
    return has_vi



# Original qualified name: _kokoro_vi_status_response
def _kokoro_vi_status_response():
    state = install_states.get('kokoro_vi', {status: 'idle', progress: 0.0,
        message: ''}).copy()
    status = state.get('status', 'idle')
    if status in frozenset({'installing', 'checking', 'downloading'}):
        return state
    if _is_kokoro_vi_ready():
        return {status: 'success', progress: 100.0, message:
            'Kokoro Việt Nam đã sẵn sàng!'}
    if status == 'failed':
        return state
    return {status: 'idle', progress: 0.0, message: ''}



# NOT DECOMPILED: _revo_voice_status_response


# NOT DECOMPILED: _is_revo_voice_ready


# NOT DECOMPILED: _is_revo_voice_engine_ready


# Original qualified name: _legacy_openvoice_path
def _legacy_openvoice_path():
    return get_settings().data_dir / 'resources' / 'openvoice'



# Original qualified name: _local_omnivoice_path
def _local_omnivoice_path():
    app = __import__('app.config', fromlist=('omnivoice_runtime_path',), level=0)
    omnivoice_runtime_path = app.omnivoice_runtime_path
    return omnivoice_runtime_path()



# NOT DECOMPILED: _omnivoice_supported


# NOT DECOMPILED: _is_omnivoice_ready


# NOT DECOMPILED: _omnivoice_runtime_info


# NOT DECOMPILED: _omnivoice_device_fields


# NOT DECOMPILED: _omnivoice_accel


# NOT DECOMPILED: _omnivoice_gpu_banner_dismissed


# Original qualified name: _omnivoice_status_response
def _omnivoice_status_response():
    global _omnivoice_failed_at
    time = __import__('time', fromlist=None, level=0)
    _time = time
    state = install_states.get('omnivoice', {status: 'idle', progress: 0.0,
        message: ''}).copy()
    status = state.get('status', 'idle')
    if status in frozenset({'installing', 'checking', 'downloading'}):
        __temp_225630 = {}
        __temp_225630.update(state)
        __temp_225632 = __temp_225630
        __temp_225632.update(_omnivoice_device_fields())
        return __temp_225632
    now = _time.monotonic()
    if status == 'failed':
        if _omnivoice_failed_at is None:
            _omnivoice_failed_at = now
    if _omnivoice_failed_at is not None:
        if now - _omnivoice_failed_at < _OMNIVOICE_FAIL_TTL:
            __temp_225635 = {}
            __temp_225635.update(state)
            __temp_225638 = __temp_225635
            __temp_225638.update({status: 'failed', last_error: state.get(
                'message', '')})
            __temp_225640 = __temp_225638
            __temp_225640.update(_omnivoice_device_fields())
            return __temp_225640
    if _omnivoice_failed_at is not None:
        if now - _omnivoice_failed_at >= _OMNIVOICE_FAIL_TTL:
            _omnivoice_failed_at = None
    if _is_omnivoice_ready():
        __temp_225644 = {status: 'success', progress: 100.0, message:
            'OmniVoice (clone đa ngữ) đã sẵn sàng!'}
        __temp_225644.update(_omnivoice_device_fields())
        return __temp_225644
    if status == 'failed':
        __temp_225646 = {}
        __temp_225646.update(state)
        __temp_225648 = __temp_225646
        __temp_225648.update(_omnivoice_device_fields())
        return __temp_225648
    __temp_225651 = {status: 'idle', progress: 0.0, message: ''}
    __temp_225651.update(_omnivoice_device_fields())
    return __temp_225651



# Original qualified name: _local_demucs_path
def _local_demucs_path():
    return get_settings().data_dir / 'resources' / 'demucs'



# NOT DECOMPILED: _is_demucs_ready


# Original qualified name: _demucs_status_response
def _demucs_status_response():
    state = install_states.get('demucs', {status: 'idle', progress: 0.0,
        message: ''}).copy()
    status = state.get('status', 'idle')
    if status in frozenset({'installing', 'checking', 'downloading'}):
        return state
    if _is_demucs_ready():
        return {status: 'success', progress: 100.0, message:
            'Demucs (tách giọng/nhạc) đã sẵn sàng!'}
    if status == 'failed':
        return state
    return {status: 'idle', progress: 0.0, message: ''}



# Original qualified name: _local_ytdlp_path
def _local_ytdlp_path():
    return get_settings().data_dir / 'resources' / 'yt-dlp'



# NOT DECOMPILED: _is_ytdlp_ready


# Original qualified name: _ytdlp_status_response
def _ytdlp_status_response():
    state = install_states.get('ytdlp', {status: 'idle', progress: 0.0, message:
        ''}).copy()
    status = state.get('status', 'idle')
    if status in frozenset({'installing', 'checking', 'downloading'}):
        return state
    if _is_ytdlp_ready():
        return {status: 'success', progress: 100.0, message:
            'yt-dlp (YouTube/Bilibili) đã sẵn sàng!'}
    if status == 'failed':
        return state
    return {status: 'idle', progress: 0.0, message: ''}



# NOT DECOMPILED: download_ytdlp_sync


# Original qualified name: download_ytdlp_sync.<locals>._emit
def _emit(status, progress, message, error):
    nonlocal on_progress
    install_states['ytdlp'] = {status: status, progress: progress, message: message
        }
    evt = {type: 'system.progress', target: 'ytdlp', status: status, progress:
        progress, message: message}
    if error:
        evt['error'] = error
    bus.emit_nowait(evt)
    if on_progress:
        on_progress(progress)
        return None
    return None



# NOT DECOMPILED: download_demucs_sync


# Original qualified name: download_demucs_sync.<locals>._emit
def _emit(status, progress, message, error):
    nonlocal on_progress
    install_states['demucs'] = {status: status, progress: progress, message:
        message}
    evt = {type: 'system.progress', target: 'demucs', status: status, progress:
        progress, message: message}
    if error:
        evt['error'] = error
    bus.emit_nowait(evt)
    if on_progress:
        on_progress(progress)
        return None
    return None



# NOT DECOMPILED: download_demucs_sync.<locals>._pip


# Original qualified name: _local_cuda_path
def _local_cuda_path():
    return get_settings().data_dir / 'resources' / 'cuda'



# NOT DECOMPILED: _is_cuda_pack_ready


# Original qualified name: _cuda_status_response
def _cuda_status_response():
    app = __import__('app.core', fromlist=('gpu',), level=0)
    gpu = app.gpu
    state = install_states.get('cuda', {status: 'idle', progress: 0.0, message: ''}
        ).copy()
    status = state.get('status', 'idle')
    ready = _is_cuda_pack_ready()
    dv = gpu.cuda_driver_version()
    has_gpu = dv is not None
    base = {has_gpu: has_gpu, pack_installed: ready, install_dir: str(
        _local_cuda_path())}
    if status in frozenset({'installing', 'checking', 'downloading'}):
        __temp_225749 = {}
        __temp_225749.update(state)
        __temp_225750 = __temp_225749
        __temp_225750.update(base)
        return __temp_225750
    if ready:
        __temp_225752 = {status: 'success', progress: 100.0, message:
            'Tăng tốc GPU (cuBLAS/cuDNN) đã sẵn sàng!'}
        __temp_225752.update(base)
        return __temp_225752
    if status == 'failed':
        __temp_225754 = {}
        __temp_225754.update(state)
        __temp_225755 = __temp_225754
        __temp_225755.update(base)
        return __temp_225755
    __temp_225757 = {status: 'idle', progress: 0.0, message: ''}
    __temp_225757.update(base)
    return __temp_225757



# NOT DECOMPILED: download_cuda_runtime_sync


# Original qualified name: download_cuda_runtime_sync.<locals>._emit
def _emit(status, progress, message, error):
    nonlocal on_progress
    install_states['cuda'] = {status: status, progress: progress, message: message}
    evt = {type: 'system.progress', target: 'cuda', status: status, progress:
        progress, message: message}
    if error:
        evt['error'] = error
    bus.emit_nowait(evt)
    if on_progress:
        on_progress(progress)
        return None
    return None



# NOT DECOMPILED: download_cuda_runtime_sync.<locals>._run


# NOT DECOMPILED: _install_kokoro_vi_source


# NOT DECOMPILED: _kokoro_warmup_vi_model_sync


# NOT DECOMPILED: _kokoro_warmup_model_sync


# NOT DECOMPILED: _kokoro_verify_en_sync


# NOT DECOMPILED: _prepare_target_clean_install


# NOT DECOMPILED: download_kokoro_sync


# Original qualified name: download_kokoro_sync.<locals>._emit
def _emit(status, progress, message, error):
    nonlocal on_progress
    install_states['kokoro'] = {status: status, progress: progress, message:
        message}
    evt = {type: 'system.progress', target: 'kokoro', status: status, progress:
        progress, message: message}
    if error:
        evt['error'] = error
    bus.emit_nowait(evt)
    if on_progress:
        on_progress(progress)
        return None
    return None



# NOT DECOMPILED: download_kokoro_sync.<locals>._pip


# NOT DECOMPILED: download_kokoro_vi_sync


# Original qualified name: download_kokoro_vi_sync.<locals>._emit
def _emit(status, progress, message, error):
    nonlocal on_progress
    install_states['kokoro_vi'] = {status: status, progress: progress, message:
        message}
    evt = {type: 'system.progress', target: 'kokoro_vi', status: status,
        progress: progress, message: message}
    if error:
        evt['error'] = error
    bus.emit_nowait(evt)
    if on_progress:
        on_progress(progress)
        return None
    return None



# NOT DECOMPILED: download_kokoro_vi_sync.<locals>._pip


# NOT DECOMPILED: download_revo_voice_sync


# Original qualified name: download_revo_voice_sync.<locals>._emit
def _emit(status, progress, message, error):
    nonlocal on_progress
    install_states['revo_voice'] = {status: status, progress: progress, message:
        message}
    evt = {type: 'system.progress', target: 'revo_voice', status: status,
        progress: progress, message: message}
    if error:
        evt['error'] = error
    bus.emit_nowait(evt)
    if on_progress:
        on_progress(progress)
        return None
    return None



# NOT DECOMPILED: _bundled_omnivoice_wheel


# NOT DECOMPILED: _purge_torch


# Original qualified name: _purge_torch.<locals>._attempt
def _attempt():
    nonlocal pkg_dirs, shutil, target
    for __temp_226011 in iter(pkg_dirs):
        name = __temp_226011
        p = target / name
        if not p.is_dir():
            continue
            shutil.rmtree(p, ignore_errors=True)
        else:
            shutil.rmtree(p, ignore_errors=True)
        continue
    for __temp_226015 in iter(('torch*.dist-info', 'torchaudio*.dist-info',
        'nvidia*.dist-info', 'torio*.dist-info')):
        pat = __temp_226015
        for __temp_226017 in iter(target.glob(pat)):
            info = __temp_226017
            shutil.rmtree(info, ignore_errors=True)
            continue
        continue
    return None



# NOT DECOMPILED: _installed_torch_version


# NOT DECOMPILED: _wipe_omnivoice_runtime


# NOT DECOMPILED: _wipe_omnivoice_runtime.<locals>._attempt


# NOT DECOMPILED: download_omnivoice_sync


# Original qualified name: download_omnivoice_sync.<locals>._emit
def _emit(status, progress, message, error):
    nonlocal on_progress
    install_states['omnivoice'] = {status: status, progress: progress, message:
        message}
    evt = {type: 'system.progress', target: 'omnivoice', status: status,
        progress: progress, message: message}
    if error:
        evt['error'] = error
    bus.emit_nowait(evt)
    if on_progress:
        on_progress(progress)
        return None
    return None



# Original qualified name: download_omnivoice_sync.<locals>._pip_cmd
def _pip_cmd(args):
    nonlocal target
    __temp_226080 = []
    __temp_226080.extend(args)
    __temp_226080.append('--target')
    __temp_226080.append(str(target))
    __temp_226080.append('--no-cache-dir')
    __temp_226080.append('--no-compile')
    __temp_226080.append('--quiet')
    __temp_226080.append('--timeout')
    __temp_226080.append('120')
    __temp_226080.append('--retries')
    __temp_226080.append('5')
    return _pip_install_cmd(__temp_226080)



# Original qualified name: download_omnivoice_sync.<locals>._purge_pip_tmp
def _purge_pip_tmp():
    nonlocal _pip_tmp
    shutil.rmtree(_pip_tmp, ignore_errors=True)
    return None



# Original qualified name: download_omnivoice_sync.<locals>._pip_env
def _pip_env():
    nonlocal _pip_tmp
    _pip_tmp.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env['TMPDIR'] = str(_pip_tmp)
    env['TEMP'] = str(_pip_tmp)
    env['TMP'] = str(_pip_tmp)
    return env



# NOT DECOMPILED: download_omnivoice_sync.<locals>._is_transient


# NOT DECOMPILED: download_omnivoice_sync.<locals>._log_pip_skip_warnings


# Original qualified name: download_omnivoice_sync.<locals>._pip
def _pip(args, timeout, label):
    nonlocal _log_pip_skip_warnings, _pip_cmd, _pip_env, subprocess
    __temp_226104 = {capture_output: True, text: True, timeout: timeout, env:
        _pip_env()}
    __temp_226104.update(no_window_kwargs())
    proc = subprocess.run(*(_pip_cmd(args),), **__temp_226104)
    if proc.returncode != 0:
        __temp_226106 = proc.stderr.strip()
        if not __temp_226106:
            __temp_226107 = proc.stdout.strip()
            if not __temp_226107:
                tail = ''[-400:None]
            else:
                tail = __temp_226107[-400:None]
        else:
            tail = __temp_226106[-400:None]
        if not tail:
            raise Exception(str(label) + ': ' + str('pip exit ' + str(proc.
                returncode)))
            _log_pip_skip_warnings(proc, label)
            return None
        else:
            raise Exception(str(label) + ': ' + str(tail))
            _log_pip_skip_warnings(proc, label)
            return None
    _log_pip_skip_warnings(proc, label)
    return None



# NOT DECOMPILED: download_omnivoice_sync.<locals>._pip_hb


# NOT DECOMPILED: download_omnivoice_sync.<locals>._pip_hb.<locals>._run


# NOT DECOMPILED: download_omnivoice_sync.<locals>._dl_model


# Original qualified name: install_ffmpeg
def install_ffmpeg(background_tasks):
    if install_states['ffmpeg']['status'] == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_ffmpeg_sync)
    return {'status': 'started'}



# Original qualified name: install_whisper
def install_whisper(body, background_tasks):
    model = body.model
    if model not in WHISPER_MODELS:
        raise HTTPException(status_code=400, detail='Model không hợp lệ')
    model_state = install_states['whisper'].get(model, {'status': 'idle'})
    if model_state['status'] == 'downloading':
        return {status: 'already_installing', model: model}
    background_tasks.add_task(download_whisper_sync, model)
    return {status: 'started', model: model}



# Original qualified name: install_edge_tts
def install_edge_tts(background_tasks):
    state = install_states.get('edge_tts', {})
    if state.get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_edge_tts_sync)
    return {'status': 'started'}



# Original qualified name: get_edge_tts_status
def get_edge_tts_status():
    return install_states.get('edge_tts', {status: 'idle', progress: 0.0,
        message: ''})



# Original qualified name: install_kokoro
def install_kokoro(background_tasks):
    state = install_states.get('kokoro', {})
    if state.get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_kokoro_sync)
    return {'status': 'started'}



# Original qualified name: get_kokoro_status
def get_kokoro_status():
    return _kokoro_status_response()



# Original qualified name: install_kokoro_vi
def install_kokoro_vi(background_tasks):
    state = install_states.get('kokoro_vi', {})
    if state.get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_kokoro_vi_sync)
    return {'status': 'started'}



# Original qualified name: get_kokoro_vi_status
def get_kokoro_vi_status():
    return _kokoro_vi_status_response()



# Original qualified name: install_revo_voice
def install_revo_voice(background_tasks):
    state = install_states.get('revo_voice', {})
    if state.get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_revo_voice_sync)
    return {'status': 'started'}



# Original qualified name: get_revo_voice_status
def get_revo_voice_status():
    return _revo_voice_status_response()



# NOT DECOMPILED: get_revo_voice_catalog


# NOT DECOMPILED: _download_revo_voice_model_sync


# Original qualified name: _download_revo_voice_model_sync.<locals>._emit
def _emit(status, progress, message, error):
    nonlocal voice_id
    revo_voice_downloads[voice_id] = {status: status, progress: progress,
        message: message}
    evt = {type: 'system.progress', target: 'revo_voice_model', voice: voice_id,
        status: status, progress: progress, message: message}
    if error:
        evt['error'] = error
    bus.emit_nowait(evt)
    return None



# Original qualified name: download_revo_voice_model
def download_revo_voice_model(voice_id, background_tasks):
    app = __import__('app.adapters.tts', fromlist=('revo_voice_store',), level=0)
    revo_voice_store = app.revo_voice_store
    if voice_id not in revo_voice_store.manifest_voices():
        raise HTTPException(status_code=404, detail="Không có giọng '" + str(
            voice_id) + "' trong danh mục.")
    if revo_voice_downloads.get(voice_id, {}).get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(_download_revo_voice_model_sync, voice_id)
    return {'status': 'started'}



# Original qualified name: delete_revo_voice_model
def delete_revo_voice_model(voice_id):
    app = __import__('app.adapters.tts', fromlist=('revo_voice_store',), level=0)
    revo_voice_store = app.revo_voice_store
    removed = revo_voice_store.delete_voice(voice_id)
    revo_voice_downloads.pop(voice_id, None)
    return {ok: True, removed: removed}



# Original qualified name: get_revo_voice_config
def get_revo_voice_config():
    app = __import__('app.adapters.tts', fromlist=('revo_voice_config',), level=0)
    revo_voice_config = app.revo_voice_config
    __temp_226214 = {}
    __temp_226214.update(revo_voice_config.load().as_dict())
    __temp_226216 = __temp_226214
    __temp_226216.update({'defaults': revo_voice_config.DEFAULTS})
    return __temp_226216



# Original qualified name: update_revo_voice_config
def update_revo_voice_config(body):
    app = __import__('app.adapters.tts', fromlist=('revo_voice_config',), level=0)
    revo_voice_config = app.revo_voice_config
    cfg = revo_voice_config.save(body.model_dump(exclude_none=True))
    __temp_226221 = {}
    __temp_226221.update(cfg.as_dict())
    __temp_226223 = __temp_226221
    __temp_226223.update({'defaults': revo_voice_config.DEFAULTS})
    return __temp_226223



# NOT DECOMPILED: revo_voice_speak


# Original qualified name: install_omnivoice
def install_omnivoice(background_tasks, force_gpu, force_cpu):
    if not _omnivoice_supported():
        return {status: 'failed', error_code: 'OMNIVOICE_NO_GPU', message:
            'OmniVoice cần GPU NVIDIA (CUDA ≥ 12.6). Máy này không hỗ trợ.'}
    state = install_states.get('omnivoice', {})
    if state.get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_omnivoice_sync, None, force_gpu, force_cpu)
    return {'status': 'started'}



# Original qualified name: get_omnivoice_status
def get_omnivoice_status():
    return _omnivoice_status_response()



# NOT DECOMPILED: set_omnivoice_gpu_banner


# NOT DECOMPILED: set_omnivoice_workspace_endpoint


# Original qualified name: get_omni_studio_config
def get_omni_studio_config():
    app = __import__('app.adapters.tts.omnivoice_studio_config', fromlist=(
        'load', 'DEFAULTS'), level=0)
    load = app.load
    DEFAULTS = app.DEFAULTS
    cfg = load()
    __temp_226504 = {}
    __temp_226504.update(cfg.as_dict())
    __temp_226507 = __temp_226504
    __temp_226507.update({'defaults': DEFAULTS.as_dict()})
    return __temp_226507



# Original qualified name: update_omni_studio_config
def update_omni_studio_config(body):
    app = __import__('app.adapters.tts.omnivoice_studio_config', fromlist=(
        'save', 'DEFAULTS'), level=0)
    save = app.save
    DEFAULTS = app.DEFAULTS
    cfg = save(body.model_dump(exclude_none=True))
    __temp_226512 = {}
    __temp_226512.update(cfg.as_dict())
    __temp_226515 = __temp_226512
    __temp_226515.update({'defaults': DEFAULTS.as_dict()})
    return __temp_226515



# NOT DECOMPILED: _studio_split


# NOT DECOMPILED: omnivoice_studio_enqueue


# Original qualified name: omnivoice_studio_jobs
def omnivoice_studio_jobs():
    app = __import__('app.services', fromlist=('voice_studio',), level=0)
    voice_studio = app.voice_studio
    return {ok: True, jobs: voice_studio.list_jobs(), output_dir: str(
        voice_studio.output_dir())}



# Original qualified name: omnivoice_studio_cancel
def omnivoice_studio_cancel(job_id):
    app = __import__('app.services', fromlist=('voice_studio',), level=0)
    voice_studio = app.voice_studio
    return {'ok': voice_studio.cancel(job_id)}



# Original qualified name: omnivoice_studio_delete
def omnivoice_studio_delete(job_id):
    app = __import__('app.services', fromlist=('voice_studio',), level=0)
    voice_studio = app.voice_studio
    return {'ok': voice_studio.delete(job_id)}



# Original qualified name: omnivoice_studio_file
def omnivoice_studio_file(job_id):
    fastapi = __import__('fastapi.responses', fromlist=('FileResponse',), level=0)
    FileResponse = fastapi.FileResponse
    app = __import__('app.services', fromlist=('voice_studio',), level=0)
    voice_studio = app.voice_studio
    job = voice_studio.get(job_id)
    if job is not None:
        if not job.file:
            raise HTTPException(status_code=404, detail=
                'Job chưa có file âm thanh.')
    else:
        raise HTTPException(status_code=404, detail='Job chưa có file âm thanh.')
    path = voice_studio.output_dir() / job.file
    if not path.exists():
        raise HTTPException(status_code=404, detail=
            'File âm thanh đã bị xoá khỏi đĩa.')
    return FileResponse(str(path), media_type='audio/wav', filename=job.file)



# Original qualified name: install_demucs
def install_demucs(background_tasks):
    state = install_states.get('demucs', {})
    if state.get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_demucs_sync)
    return {'status': 'started'}



# Original qualified name: get_demucs_status
def get_demucs_status():
    return _demucs_status_response()



# Original qualified name: install_cuda_pack
def install_cuda_pack(background_tasks):
    app = __import__('app.core', fromlist=('gpu',), level=0)
    gpu = app.gpu
    if gpu.cuda_driver_version() is None:
        return {status: 'no_gpu', message:
            'Không phát hiện GPU NVIDIA — không cần gói tăng tốc GPU.'}
    if _is_cuda_pack_ready():
        return {'status': 'already_installed'}
    state = install_states.get('cuda', {})
    if state.get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_cuda_runtime_sync)
    return {'status': 'started'}



# Original qualified name: get_cuda_status
def get_cuda_status():
    return _cuda_status_response()



# Original qualified name: install_ytdlp
def install_ytdlp(background_tasks):
    state = install_states.get('ytdlp', {})
    if state.get('status') == 'downloading':
        return {'status': 'already_installing'}
    background_tasks.add_task(download_ytdlp_sync)
    return {'status': 'started'}



# Original qualified name: get_ytdlp_status
def get_ytdlp_status():
    return _ytdlp_status_response()



# Original qualified name: list_installed_models
def list_installed_models():
    models_dir = get_settings().data_dir / 'models'
    if not models_dir.exists():
        return []
    installed = []
    for __temp_226591 in iter(WHISPER_MODELS):
        model = __temp_226591
        model_dir = models_dir / model
        if not (model_dir / 'model.bin').exists():
            continue
            __temp_226593 = (model_dir / 'config.json').exists()
        else:
            (model_dir / 'config.json').exists()
        if not __temp_226593:
            continue
            installed.append(model)
        else:
            installed.append(model)
        continue
    return installed



# Original qualified name: get_install_status
def get_install_status(target, model):
    if target == 'ffmpeg':
        return install_states['ffmpeg']
    if target == 'whisper':
        if not model:
            raise HTTPException(status_code=400, detail='Thiếu tham số model')
        return install_states['whisper'].get(model, {status: 'idle', progress: 
            0.0, message: ''})
    if target == 'edge_tts':
        return install_states.get('edge_tts', {status: 'idle', progress: 0.0,
            message: ''})
    if target == 'kokoro':
        return _kokoro_status_response()
    if target == 'demucs':
        return _demucs_status_response()
    if target == 'ytdlp':
        return _ytdlp_status_response()
    raise HTTPException(status_code=400, detail='Target không hợp lệ')



# NOT DECOMPILED: get_toolkit_profiles


# Original qualified name: get_toolkit_status
def get_toolkit_status():
    return _toolkit_status_response()



# Original qualified name: install_toolkit
def install_toolkit(body, background_tasks):
    profile = body.profile
    if profile not in TOOLKIT_PROFILES:
        raise HTTPException(status_code=400, detail='Profile không hợp lệ')
    state = install_states['toolkit']
    if state['status'] in frozenset({'installing', 'checking', 'downloading'}):
        return {'status': 'already_installing'}
    background_tasks.add_task(install_toolkit_profile_sync, profile)
    return {'status': 'started'}



# NOT DECOMPILED: test_deepseek


# NOT DECOMPILED: list_tts_voices


# NOT DECOMPILED: preview_tts_voice


# NOT DECOMPILED: test_tts_provider


# NOT DECOMPILED: _normalize_clone_audio


# NOT DECOMPILED: _transcribe_ref_audio


# NOT DECOMPILED: create_voice_clone


# NOT DECOMPILED: create_voice_design


# NOT DECOMPILED: list_voice_clones


# NOT DECOMPILED: delete_voice_clone
