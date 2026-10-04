# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/whisper_engine.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: align_model_name


# Original qualified name: _is_dense_script
def _is_dense_script(src_lang):
    if not src_lang:
        return str('').strip().lower().replace('_', '-').split('-')[0
            ] in _DENSE_SCRIPT_LANGS
    else:
        return str(src_lang).strip().lower().replace('_', '-').split('-')[0
            ] in _DENSE_SCRIPT_LANGS



# NOT DECOMPILED: _compute_type_setting


# Original qualified name: _worker_env
def _worker_env():
    os = __import__('os', fromlist=None, level=0)
    __temp_144115 = {}
    __temp_144115.update(os.environ)
    __temp_144117 = __temp_144115
    __temp_144117.update({PYTHONIOENCODING: 'utf-8', PYTHONUTF8: '1'})
    return __temp_144117



# Original qualified name: _worker_cmd
def _worker_cmd(worker_args):
    if getattr(sys, 'frozen', False):
        __temp_144120 = [sys.executable, 'whisper-worker']
        __temp_144120.extend(worker_args)
        return __temp_144120, str(Path(sys.executable).parent)
    __temp_144124 = [sys.executable, '-u', '-m', 'app.workers.whisper_proc']
    __temp_144124.extend(worker_args)
    return __temp_144124, str(Path(__file__).parent.parent.parent)



# Original qualified name: WhisperServer.__init__
def __init__(self, model_dir, device, batch_size, cpu_threads, compute_type):
    self.model_dir = model_dir
    self.device = device
    self.batch_size = batch_size
    self.cpu_threads = cpu_threads
    self.compute_type = compute_type
    self.device_used = device
    self._proc = None
    self._lock = asyncio.Lock()
    self._start_lock = asyncio.Lock()
    self._inbox = None
    self._reader = None
    self._stderr_task = None
    self._idle_task = None
    self._last_used = time.monotonic()
    self.unsupported = False
    self.pending = 0
    self._stderr_tail = deque(maxlen=20)
    return None



# Original qualified name: WhisperServer.alive
def alive(self):
    if self._proc is not None:
        return self._proc.returncode is None
    else:
        return self._proc is not None



# NOT DECOMPILED: WhisperServer._start


# NOT DECOMPILED: WhisperServer.stop


# NOT DECOMPILED: WhisperServer._idle_watch


# NOT DECOMPILED: WhisperServer._read_stdout


# NOT DECOMPILED: WhisperServer._read_stderr


# NOT DECOMPILED: WhisperServer._death_report


# NOT DECOMPILED: WhisperServer._send


# NOT DECOMPILED: WhisperServer._await_message


# NOT DECOMPILED: WhisperServer.transcribe


# NOT DECOMPILED: WhisperServer._transcribe_locked


# NOT DECOMPILED: _pool_limit


# NOT DECOMPILED: _evict_other_models_if_ram_tight


# NOT DECOMPILED: shutdown_servers


# Original qualified name: WhisperEngine.__init__
def __init__(self, model_name, prefer_smaller):
    self.configured_model = model_name
    self.model_name = model_name
    self.prefer_smaller = prefer_smaller
    self.model_dir = get_settings().data_dir / 'models' / model_name
    self._last_worker_death = ''
    self._resolve_installed_model()
    return None



# NOT DECOMPILED: WhisperEngine._resolve_installed_model


# NOT DECOMPILED: WhisperEngine._resolve_installed_model.<locals>._pick


# Original qualified name: WhisperEngine._is_model_valid
def _is_model_valid(self, model_name):
    path = get_settings().data_dir / 'models' / model_name
    __temp_144202 = path.exists()
    if __temp_144202:
        return (path / 'model.bin').exists()
    else:
        return __temp_144202



# Original qualified name: WhisperEngine.check_model_files
def check_model_files(self):
    if not self._is_model_valid(self.model_name):
        raise make_error(E.WHISPER_MODEL_DOWNLOAD_FAILED, 'Mô hình Whisper (' +
            str(self.model_name) + ') chưa được tải xuống đầy đủ.', hint=
            'Mở Bộ Công Cụ trong tab Cài đặt để tải cấu hình phù hợp.')
    return None



# NOT DECOMPILED: WhisperEngine.transcribe


# NOT DECOMPILED: WhisperEngine._server


# NOT DECOMPILED: WhisperEngine._load_result_file


# NOT DECOMPILED: WhisperEngine._transcribe_oneshot


# NOT DECOMPILED: WhisperEngine._transcribe_oneshot.<locals>.read_stdout


# NOT DECOMPILED: WhisperEngine._transcribe_oneshot.<locals>.read_stderr


# NOT DECOMPILED: WhisperEngine._transcribe_oneshot.<locals>.monitor
