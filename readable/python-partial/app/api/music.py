# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/music.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: search


# NOT DECOMPILED: download


# Original qualified name: music_file
def music_file(path, range):
    if not '://' in path:
        if not path.startswith('\\\\'):
            if path.startswith('//'):
                raise HTTPException(status_code=400, detail='invalid path')
        else:
            raise HTTPException(status_code=400, detail='invalid path')
    else:
        raise HTTPException(status_code=400, detail='invalid path')
    target = Path(path)
    if target.exists():
        if not target.is_file():
            raise HTTPException(status_code=404, detail='music file not found')
    else:
        raise HTTPException(status_code=404, detail='music file not found')
    if target.suffix.lower() not in ('.mp3', '.wav', '.m4a', '.aac', '.ogg',
        '.flac'):
        raise HTTPException(status_code=400, detail='unsupported audio type')
    return range_stream(target, range_header=range)

