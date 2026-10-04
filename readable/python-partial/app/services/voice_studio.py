# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/voice_studio.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: output_dir
def output_dir():
    global _OUT_DIR
    if _OUT_DIR is None:
        app = __import__('app.config', fromlist=('get_settings',), level=0)
        get_settings = app.get_settings
        d = get_settings().data_dir / 'voice_studio'
        d.mkdir(parents=True, exist_ok=True)
        _OUT_DIR = d
    return _OUT_DIR



# Original qualified name: Job.public
def public(self):
    d = asdict(self)
    d.pop('text', None)
    if self.file:
        d['file_path'] = str(output_dir() / self.file)
    else:
        d['file_path'] = ''
    return d



# Original qualified name: _index_path
def _index_path():
    return output_dir() / _INDEX



# NOT DECOMPILED: _load


# NOT DECOMPILED: _save


# Original qualified name: _WavAppender.__init__
def __init__(self, path):
    self._path = path
    self._w = None
    self._sr = 24000
    self._width = 2
    self._frames = 0
    return None



# Original qualified name: _WavAppender.append
def append(self, part_path, gap_ms):
    with wave.open(part_path, 'rb') as __temp_277528:
        r = __temp_277528
        nch = r.getnchannels()
        width = r.getsampwidth()
        sr = r.getframerate()
        data = r.readframes(r.getnframes())
        if self._w is None:
            self._sr = sr
            self._width = width
            self._w = wave.open(self._path, 'wb')
            self._w.setnchannels(nch)
            self._w.setsampwidth(width)
            self._w.setframerate(sr)
        elif gap_ms > 0:
            silence = b'\x00' * (int(self._sr * gap_ms / 1000.0) * self._width)
            self._w.writeframes(silence)
            self._frames += int(self._sr * gap_ms / 1000.0)
            self._frames = self._frames
        self._w.writeframes(data)
        self._frames += len(data) // max(1, self._width)
        self._frames = self._frames
        return None



# Original qualified name: _WavAppender.close
def close(self):
    if self._w is None:
        return 0.0
    self._w.close()
    self._w = None
    return round(self._frames / float(self._sr), 2)



# Original qualified name: _split
def _split(text):
    app = __import__('app.api.system', fromlist=('_studio_split',), level=0)
    _studio_split = app._studio_split
    return _studio_split(text, CHUNK_CHARS)



# NOT DECOMPILED: _safe_name


# NOT DECOMPILED: submit


# NOT DECOMPILED: list_jobs


# Original qualified name: get
def get(job_id):
    _load()
    return _JOBS.get(job_id)



# Original qualified name: cancel
def cancel(job_id):
    job = get(job_id)
    if job is not None:
        if job.status in _TERMINAL:
            return False
    else:
        return False
    if job.status == 'running':
        job.status = 'cancelling'
    else:
        job.status = 'cancelled'
    if job.status == 'cancelled':
        job.finished_at = time.time()
    _save()
    return True



# NOT DECOMPILED: delete


# NOT DECOMPILED: _run_worker


# NOT DECOMPILED: _run_job
