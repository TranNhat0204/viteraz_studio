# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/channel_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: is_channel_url
def is_channel_url(url):
    u = url.lower()
    if not 'list=' in u:
        if '/playlist' in u:
            return True
    else:
        return True
    if not 'space.bilibili.com' in u:
        if '/favlist' in u:
            return True
    else:
        return True
    if not 'youtube.com/@' in u:
        if not '/channel/' in u:
            if not '/c/' in u:
                if 'youtube.com/user/' in u:
                    return True
            else:
                return True
        else:
            return True
    else:
        return True
    if not '/@' in u:
        if '/user/' in u:
            if not _VIDEO_PATH_RE.search(u):
                return True
    elif not _VIDEO_PATH_RE.search(u):
        return True
    return False



# NOT DECOMPILED: list_channel_videos


# NOT DECOMPILED: _expand_ytdlp


# NOT DECOMPILED: _expand_ytdlp.<locals>._run


# NOT DECOMPILED: _expand_douyin
