# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/media.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _lock_for
def _lock_for(project_id):
    if project_id not in _locks:
        _locks[project_id] = asyncio.Lock()
    return _locks[project_id]



# Original qualified name: _kind_of
def _kind_of(ext):
    e = ext.lower()
    if e in _VIDEO_EXT:
        return video
    if e in _IMAGE_EXT:
        return image
    if e in _AUDIO_EXT:
        return audio
    return None



# NOT DECOMPILED: _run_ffmpeg


# NOT DECOMPILED: _gen_thumbnail


# NOT DECOMPILED: _gen_peaks


# NOT DECOMPILED: _gen_proxy


# NOT DECOMPILED: import_media


# NOT DECOMPILED: upload_media


# NOT DECOMPILED: list_media


# NOT DECOMPILED: delete_media


# NOT DECOMPILED: analyze_media


# NOT DECOMPILED: get_media_file


# NOT DECOMPILED: logo_sweep
