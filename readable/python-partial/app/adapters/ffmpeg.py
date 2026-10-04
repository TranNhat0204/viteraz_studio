# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/ffmpeg.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _parse_fps


# NOT DECOMPILED: _iter_ffmpeg_lines


# Original qualified name: clear_ffmpeg_path_cache
def clear_ffmpeg_path_cache():
    global _ENCODERS_CACHE
    _FFMPEG_PATH_CACHE.clear()
    _ENCODERS_CACHE = None
    _ENCODER_USABLE_CACHE.clear()
    return None



# NOT DECOMPILED: encoder_usable


# NOT DECOMPILED: detect_encoders


# Original qualified name: get_ffmpeg_path
def get_ffmpeg_path():
    with SessionLocal() as __temp_3063:
        db = __temp_3063
        row = db.get(Setting, 'ffmpeg_path')
        if row:
            custom_path = row.value
        else:
            custom_path = None
        if not custom_path:
            cache_key = '<auto>'
        else:
            cache_key = custom_path
        hit = _FFMPEG_PATH_CACHE.get(cache_key)
        if hit:
            return hit
    
        def _cache(v):
            nonlocal cache_key
            _FFMPEG_PATH_CACHE[cache_key] = v
            return v
        if custom_path:
            p = Path(custom_path)
            if p.exists():
                if p.is_file():
                    return _cache(str(p.resolve()))
            resolved = (get_settings().data_dir / p).resolve()
            if resolved.exists():
                if resolved.is_file():
                    return _cache(str(resolved))
            exe = shutil.which(custom_path)
            if exe:
                return _cache(exe)
        local_path = get_settings(
            ).data_dir / 'resources' / 'ffmpeg' / 'ffmpeg.exe'
        if local_path.exists():
            return _cache(str(local_path))
        exe = shutil.which('ffmpeg')
        if exe:
            return _cache(exe)
        raise make_error(E.FFMPEG_NOT_FOUND,
            'Không tìm thấy FFmpeg executable trên máy. Hãy cài đặt Bộ Công Cụ hoặc cấu hình đường dẫn trong cài đặt.'
            )



# Original qualified name: get_ffmpeg_path.<locals>._cache
def _cache(v):
    nonlocal cache_key
    _FFMPEG_PATH_CACHE[cache_key] = v
    return v



# NOT DECOMPILED: _terminate


# NOT DECOMPILED: get_ffprobe_path


# Original qualified name: FFmpegRunner.__init__
def __init__(self, ffmpeg_path):
    if not ffmpeg_path:
        self.ffmpeg_path = get_ffmpeg_path()
    else:
        self.ffmpeg_path = ffmpeg_path
    return None



# NOT DECOMPILED: FFmpegRunner.extract_audio


# NOT DECOMPILED: FFmpegRunner.extract_audio_dual


# NOT DECOMPILED: FFmpegRunner.extract_audio_hq


# NOT DECOMPILED: FFmpegRunner._run_extract


# NOT DECOMPILED: FFmpegRunner._run_extract.<locals>.read_stderr


# NOT DECOMPILED: FFmpegRunner._run_extract.<locals>.monitor


# NOT DECOMPILED: FFmpegRunner.probe


# NOT DECOMPILED: FFmpegRunner._probe_uncached


# NOT DECOMPILED: FFmpegRunner._probe_via_ffmpeg


# NOT DECOMPILED: FFmpegRunner.run_render


# NOT DECOMPILED: FFmpegRunner.run_render.<locals>.read_stderr


# NOT DECOMPILED: FFmpegRunner.run_render.<locals>.monitor


# NOT DECOMPILED: FFmpegRunner.run_capture
