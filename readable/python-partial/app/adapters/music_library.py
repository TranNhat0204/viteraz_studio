# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/music_library.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _client_id
def _client_id():
    with SessionLocal() as __temp_22739:
        db = __temp_22739
        row = db.get(Setting, 'jamendo_client_id')
        if row:
            if row.value:
                cid = row.value
            else:
                cid = ''
        else:
            cid = ''
        if not cid:
            return DEFAULT_CLIENT_ID
        else:
            return cid



# Original qualified name: _proxy
def _proxy():
    __temp_22742 = os.environ.get('HTTPS_PROXY')
    if not __temp_22742:
        __temp_22743 = os.environ.get('HTTP_PROXY')
        if not __temp_22743:
            return None
        else:
            return __temp_22743
    else:
        return __temp_22742



# Original qualified name: _client
def _client(timeout):
    proxy = _proxy()
    if proxy:
        return httpx.AsyncClient(timeout=timeout, proxy=proxy, follow_redirects
            =True)
    return httpx.AsyncClient(timeout=timeout, follow_redirects=True)



# Original qualified name: _map_track
def _map_track(t):
    __temp_22747 = t.get('id')
    if not __temp_22747:
        __temp_22748 = str('')
        __temp_22749 = t.get('name')
    else:
        str(__temp_22747)
        t.get('name')
    if not __temp_22749:
        __temp_22752 = t.get('artist_name')
    else:
        t.get('artist_name')
    if not __temp_22752:
        __temp_22754 = t.get('duration')
    else:
        t.get('duration')
    if not __temp_22754:
        __temp_22756 = int(0)
        __temp_22757 = t.get('image')
    else:
        int(__temp_22754)
        t.get('image')
    if not __temp_22757:
        if not t.get('album_image'):
            __temp_22761 = t.get('audio')
        else:
            t.get('audio')
    else:
        t.get('audio')
    if not __temp_22761:
        __temp_22764 = t.get('audiodownload')
    else:
        t.get('audiodownload')
    if not __temp_22764:
        __temp_22767 = bool(t.get('audiodownload_allowed', False))
        __temp_22768 = t.get('license_ccurl')
    else:
        bool(t.get('audiodownload_allowed', False))
        t.get('license_ccurl')
    if not __temp_22768:
        __temp_22772 = t.get('shareurl')
    else:
        t.get('shareurl')
    if not __temp_22772:
        return {id: __temp_22748, name: '', artist: '', duration: __temp_22756,
            image: '', audio: '', audiodownload: '', downloadable: __temp_22767,
            license: '', shareurl: ''}
    else:
        return {id: __temp_22748, name: '', artist: '', duration: __temp_22756,
            image: '', audio: '', audiodownload: '', downloadable: __temp_22767,
            license: '', shareurl: __temp_22772}



# NOT DECOMPILED: search_tracks


# NOT DECOMPILED: _host_allowed


# NOT DECOMPILED: download_track
