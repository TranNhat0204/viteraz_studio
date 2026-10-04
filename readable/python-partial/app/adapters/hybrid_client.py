# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/hybrid_client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: HybridVideoClient._get_hybrid


# NOT DECOMPILED: HybridVideoClient.get_video_info


# NOT DECOMPILED: HybridVideoClient._retry_douyin_with_fresh_ttwid


# NOT DECOMPILED: HybridVideoClient._first_url


# NOT DECOMPILED: HybridVideoClient._normalize_author


# Original qualified name: HybridVideoClient._duration_ms
def _duration_ms(node):
    __temp_3372 = node.get('duration')
    if not __temp_3372:
        duration = node.get('duration_ms')
    else:
        duration = __temp_3372
    if isinstance(duration, (int, float)):
        if duration < 36000:
            return int(duration * 1000)
        return int(duration)
    video_data = node.get('video_data')
    if isinstance(video_data, dict):
        __temp_3379 = video_data.get('duration')
        if not __temp_3379:
            duration = video_data.get('duration_ms')
        else:
            duration = __temp_3379
        if isinstance(duration, (int, float)):
            if duration < 36000:
                return int(duration * 1000)
            return int(duration)
    return None



# Original qualified name: HybridVideoClient._normalize
def _normalize(data, platform):
    if not data:
        d = {}
    else:
        d = data
    if isinstance(d, dict):
        node = d.get('data', d)
    else:
        node = {}
    if not isinstance(node, dict):
        node = {}
    if isinstance(node.get('video_data'), dict):
        video_data = node.get('video_data')
    else:
        video_data = {}
    if isinstance(node.get('cover_data'), dict):
        cover_data = node.get('cover_data')
    else:
        cover_data = {}
    __temp_3399 = HybridVideoClient._first_url(video_data.get('nwm_video_url_HQ'))
    if not __temp_3399:
        __temp_3401 = HybridVideoClient._first_url(video_data.get('nwm_video_url'))
        if not __temp_3401:
            __temp_3403 = HybridVideoClient._first_url(video_data.get('url'))
            if not __temp_3403:
                __temp_3405 = HybridVideoClient._first_url(node.get(
                    'nwm_video_url_HQ'))
                if not __temp_3405:
                    download_url = HybridVideoClient._first_url(node.get(
                        'nwm_video_url'))
                else:
                    download_url = __temp_3405
            else:
                download_url = __temp_3403
        else:
            download_url = __temp_3401
    else:
        download_url = __temp_3399
    __temp_3409 = HybridVideoClient._first_url(cover_data.get('origin_cover'))
    if not __temp_3409:
        __temp_3411 = HybridVideoClient._first_url(cover_data.get('cover'))
        if not __temp_3411:
            cover_url = HybridVideoClient._first_url(node.get('cover'))
        else:
            cover_url = __temp_3411
    else:
        cover_url = __temp_3409
    if not node.get('platform'):
        __temp_3415 = node.get('desc')
    else:
        node.get('desc')
    if not __temp_3415:
        __temp_3417 = node.get('title')
        __temp_3419 = HybridVideoClient._normalize_author(node.get('author'))
        __temp_3420 = HybridVideoClient._duration_ms(node)
        __temp_3421 = node.get('video_id')
    else:
        HybridVideoClient._normalize_author(node.get('author'))
        HybridVideoClient._duration_ms(node)
        node.get('video_id')
    if not __temp_3421:
        if not node.get('aweme_id'):
            __temp_3427 = node.get('item_id')
            __temp_3428 = isinstance(video_data, dict)
        else:
            isinstance(video_data, dict)
    else:
        isinstance(video_data, dict)
    if __temp_3428:
        return {platform: platform, download_url: download_url, title:
            __temp_3417, author: __temp_3419, duration_ms: __temp_3420,
            aweme_id: __temp_3427, cover_url: cover_url, resolution: video_data
            .get('resolution'), _raw_keys: list(node.keys())}
    else:
        return {platform: platform, download_url: download_url, title:
            __temp_3417, author: __temp_3419, duration_ms: __temp_3420,
            aweme_id: __temp_3427, cover_url: cover_url, resolution: None,
            _raw_keys: list(node.keys())}

