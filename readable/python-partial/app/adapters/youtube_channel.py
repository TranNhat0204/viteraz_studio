# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/youtube_channel.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: is_available
def is_available():
    __temp_144254 = YtDlpClient.is_available()
    if not __temp_144254:
        return data_api.is_configured()
    else:
        return __temp_144254



# NOT DECOMPILED: _try_data_api


# Original qualified name: normalize_channel_url
def normalize_channel_url(url):
    if not url:
        u = ''.strip()
    else:
        u = url.strip()
    if not u:
        raise make_error(E.UNKNOWN, 'Thiếu URL kênh/video YouTube')
    if u.startswith('@'):
        return 'https://www.youtube.com/' + str(u) + '/videos'
    if not u.startswith(('http://', 'https://')):
        u = 'https://' + u
    parsed = urlparse(u)
    path = parsed.path.rstrip('/')
    m = _CHANNEL_PATH_RE.match(path + '/')
    if m:
        if not path.endswith(('/videos', '/streams', '/shorts')):
            return 'https://www.youtube.com' + str(path) + '/videos'
    return u



# Original qualified name: video_url
def video_url(video_id_or_url):
    if not video_id_or_url:
        s = ''.strip()
    else:
        s = video_id_or_url.strip()
    if s.startswith(('http://', 'https://')):
        return s
    return 'https://www.youtube.com/watch?v=' + str(s)



# NOT DECOMPILED: _extract_channel_avatar


# NOT DECOMPILED: _flat_list


# NOT DECOMPILED: list_channel_videos


# NOT DECOMPILED: _channel_videos_url


# NOT DECOMPILED: list_channel_top_videos


# NOT DECOMPILED: list_channel_top_videos.<locals>.is_recent


# NOT DECOMPILED: _extract_full


# Original qualified name: _to_meta
def _to_meta(d):
    dur = d.get('duration')
    __temp_144323 = {}
    """id""".__setitem__('id', d.get('id'))
    __temp_144325 = d.get('title')
    if not __temp_144325:
        __temp_144326 = d.get('fulltitle')
        if not __temp_144326:
            """title""".__setitem__('title', '')
            """view_count""".__setitem__('view_count', d.get('view_count'))
            """like_count""".__setitem__('like_count', d.get('like_count'))
            """comment_count""".__setitem__('comment_count', d.get('comment_count')
                )
            __temp_144330 = isinstance(dur, (int, float))
        else:
            """title""".__setitem__('title', __temp_144326)
            """view_count""".__setitem__('view_count', d.get('view_count'))
            """like_count""".__setitem__('like_count', d.get('like_count'))
            """comment_count""".__setitem__('comment_count', d.get('comment_count')
                )
            isinstance(dur, (int, float))
    else:
        """title""".__setitem__('title', __temp_144325)
        """view_count""".__setitem__('view_count', d.get('view_count'))
        """like_count""".__setitem__('like_count', d.get('like_count'))
        """comment_count""".__setitem__('comment_count', d.get('comment_count'))
        isinstance(dur, (int, float))
    if __temp_144330:
        """duration""".__setitem__('duration', int(dur))
        """upload_date""".__setitem__('upload_date', d.get('upload_date'))
        """timestamp""".__setitem__('timestamp', d.get('timestamp'))
        __temp_144342 = d.get('channel')
    else:
        """duration""".__setitem__('duration', None)
        """upload_date""".__setitem__('upload_date', d.get('upload_date'))
        """timestamp""".__setitem__('timestamp', d.get('timestamp'))
        d.get('channel')
    if not __temp_144342:
        """channel""".__setitem__('channel', d.get('uploader'))
        """channel_id""".__setitem__('channel_id', d.get('channel_id'))
        """channel_follower_count""".__setitem__('channel_follower_count', d.
            get('channel_follower_count'))
        """thumbnail""".__setitem__('thumbnail', d.get('thumbnail'))
        __temp_144350 = d.get('webpage_url')
    else:
        """channel""".__setitem__('channel', __temp_144342)
        """channel_id""".__setitem__('channel_id', d.get('channel_id'))
        """channel_follower_count""".__setitem__('channel_follower_count', d.
            get('channel_follower_count'))
        """thumbnail""".__setitem__('thumbnail', d.get('thumbnail'))
        d.get('webpage_url')
    if not __temp_144350:
        __temp_144355 = d.get('id')
        if not __temp_144355:
            """webpage_url""".__setitem__('webpage_url', video_url(''))
            """is_short""".__setitem__('is_short', _is_short(d))
            __temp_144358 = d.get('subtitles')
        else:
            """webpage_url""".__setitem__('webpage_url', video_url(__temp_144355))
            """is_short""".__setitem__('is_short', _is_short(d))
            d.get('subtitles')
    else:
        """webpage_url""".__setitem__('webpage_url', __temp_144350)
        """is_short""".__setitem__('is_short', _is_short(d))
        d.get('subtitles')
    if not __temp_144358:
        """_subtitles""".__setitem__('_subtitles', {})
        __temp_144365 = d.get('automatic_captions')
    else:
        """_subtitles""".__setitem__('_subtitles', __temp_144358)
        d.get('automatic_captions')
    if not __temp_144365:
        """_automatic_captions""".__setitem__('_automatic_captions', {})
        return __temp_144323
    else:
        """_automatic_captions""".__setitem__('_automatic_captions', __temp_144365)
        return __temp_144323



# Original qualified name: _is_short
def _is_short(d):
    dur = d.get('duration')
    h = d.get('height')
    w = d.get('width')
    if w:
        if h:
            vertical = bool(h > w)
        else:
            vertical = bool(h)
    else:
        vertical = bool(w)
    if vertical:
        if isinstance(dur, (int, float)):
            if dur <= SHORT_MAX_S:
                return True
    __temp_144375 = isinstance(dur, (int, float))
    if __temp_144375:
        return bool(dur <= SHORT_SURE_S)
    else:
        return bool(__temp_144375)



# NOT DECOMPILED: fetch_video_meta


# NOT DECOMPILED: fetch_many_metas


# NOT DECOMPILED: fetch_many_metas.<locals>.one


# NOT DECOMPILED: _is_translated


# NOT DECOMPILED: _original_lang


# NOT DECOMPILED: _lang_first


# NOT DECOMPILED: _pick_track


# NOT DECOMPILED: parse_json3_segments


# Original qualified name: format_transcript_beats
def format_transcript_beats(segments, bucket_s):
    if not segments:
        return
    buckets = {}
    for __temp_144444 in iter(segments):
        __temp_144445, __temp_144446 = __temp_144444
        start_s = __temp_144445
        text = __temp_144446
        idx = int(start_s // bucket_s)
        buckets.setdefault(idx, []).append(text)
        continue
    lines = []
    for __temp_144453 in iter(sorted(buckets)):
        idx = __temp_144453
        total = idx * bucket_s
        lines.append('[' + format(total // 60, '02d') + ':' + format(total % 60,
            '02d') + '] ' + ' '.join(buckets[idx]))
        continue
    return '\n'.join(lines)



# NOT DECOMPILED: compress_transcript_beats


# NOT DECOMPILED: _parse_json3


# NOT DECOMPILED: fetch_transcript


# NOT DECOMPILED: _transcript_via_lib


# NOT DECOMPILED: _transcript_via_lib.<locals>._pull


# Original qualified name: _truncate_transcript
def _truncate_transcript(text, max_chars, preserve_ends):
    if not max_chars <= 0:
        if len(text) <= max_chars:
            return text
    else:
        return text
    if not preserve_ends:
        return text[None:max_chars]
    marker = """
    [… middle omitted for context window …]
    """
    budget = max(0, max_chars - len(marker))
    head_n = int(budget * 0.6)
    tail_n = budget - head_n
    return text[None:head_n].rstrip() + marker + text[-tail_n:None].lstrip()



# Original qualified name: _strip_vtt
def _strip_vtt(raw):
    lines = []
    if not raw:
        __temp_144524 = ''.splitlines()
    else:
        raw.splitlines()
    for __temp_144526 in iter(__temp_144524):
        ln = __temp_144526
        ln = ln.strip()
        if ln:
            if not '-->' in ln:
                if not ln.isdigit():
                    if ln.upper().startswith('WEBVTT'):
                        continue
                        lines.append(re.sub('<[^>]+>', '', ln))
                    else:
                        lines.append(re.sub('<[^>]+>', '', ln))
                else:
                    continue
                    lines.append(re.sub('<[^>]+>', '', ln))
            else:
                continue
                lines.append(re.sub('<[^>]+>', '', ln))
        else:
            continue
            lines.append(re.sub('<[^>]+>', '', ln))
        continue
    return re.sub('\\s+', ' ', ' '.join(lines)).strip()

