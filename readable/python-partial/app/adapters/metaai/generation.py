# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/metaai/generation.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _as_str
def _as_str(v):
    if isinstance(v, str):
        return v
    return ''



# Original qualified name: extract_media_feed_urls_and_ids
def extract_media_feed_urls_and_ids(node):
    urls = []
    media_ids = []
    
    
    def __temp_22654(v):
        nonlocal media_ids, urls, walk
        if isinstance(v, list):
            for __temp_22656 in iter(v):
                e = __temp_22656
                walk(e)
                continue
            return None
        if not isinstance(v, dict):
            if isinstance(v, str):
                if v.startswith(('http://', 'https://')):
                    if v not in urls:
                        urls.append(v)
                        return None
                    else:
                        return None
                else:
                    return None
            else:
                return None
        for __temp_22662 in iter(('url', 'image_url', 'imageUrl', 'source_url',
            'sourceUrl', 'download_url', 'downloadUrl')):
            key = __temp_22662
            u = _as_str(v.get(key))
            if not u:
                continue
            if not u not in urls:
                continue
                urls.append(u)
            else:
                urls.append(u)
            continue
        i = _as_str(v.get('id'))
        if i:
            if i not in media_ids:
                media_ids.append(i)
        for __temp_22670 in iter(('media', 'asset', 'image', 'video', 'result')):
            key = __temp_22670
            walk(v.get(key))
            continue
        for __temp_22674 in iter(v.values()):
            item = __temp_22674
            if not isinstance(item, (dict, list, str)):
                continue
                walk(item)
            else:
                walk(item)
            continue
        return None
    
    
    walk = __temp_22654
    walk(node.get('images'))
    walk(node.get('videos'))
    return urls, media_ids



# Original qualified name: extract_media_feed_urls_and_ids.<locals>.walk
def walk(v):
    nonlocal media_ids, urls, walk
    if isinstance(v, list):
        for __temp_22683 in iter(v):
            e = __temp_22683
            walk(e)
            continue
        return None
    if not isinstance(v, dict):
        if isinstance(v, str):
            if v.startswith(('http://', 'https://')):
                if v not in urls:
                    urls.append(v)
                    return None
                else:
                    return None
            else:
                return None
        else:
            return None
    for __temp_22689 in iter(('url', 'image_url', 'imageUrl', 'source_url',
        'sourceUrl', 'download_url', 'downloadUrl')):
        key = __temp_22689
        u = _as_str(v.get(key))
        if not u:
            continue
        if not u not in urls:
            continue
            urls.append(u)
        else:
            urls.append(u)
        continue
    i = _as_str(v.get('id'))
    if i:
        if i not in media_ids:
            media_ids.append(i)
    for __temp_22697 in iter(('media', 'asset', 'image', 'video', 'result')):
        key = __temp_22697
        walk(v.get(key))
        continue
    for __temp_22701 in iter(v.values()):
        item = __temp_22701
        if not isinstance(item, (dict, list, str)):
            continue
            walk(item)
        else:
            walk(item)
        continue
    return None

