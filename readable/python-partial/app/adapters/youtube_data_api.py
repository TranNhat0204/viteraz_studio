# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/youtube_data_api.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: get_api_key
def get_api_key():
    app = __import__('app.db.session', fromlist=('SessionLocal',), level=0)
    SessionLocal = app.SessionLocal
    app = __import__('app.db.models', fromlist=('Setting',), level=0)
    Setting = app.Setting
    with SessionLocal() as __temp_144545:
        db = __temp_144545
        row = db.get(Setting, 'youtube_api_key')
        if row:
            if row.value:
                row.value.strip()
            else:
                """""".strip()
        else:
            """""".strip()



# Original qualified name: is_configured
def is_configured():
    return bool(get_api_key())



# NOT DECOMPILED: _api_error


# NOT DECOMPILED: _get


# NOT DECOMPILED: test_key


# NOT DECOMPILED: parse_iso_duration


# NOT DECOMPILED: _ts_from_iso


# NOT DECOMPILED: _best_thumb


# NOT DECOMPILED: _to_int


# Original qualified name: video_item_to_meta
def video_item_to_meta(item):
    __temp_144594 = item.get('id')
    if not __temp_144594:
        vid = str('')
    else:
        vid = str(__temp_144594)
    __temp_144597 = item.get('snippet')
    if not __temp_144597:
        sn = {}
    else:
        sn = __temp_144597
    __temp_144599 = item.get('statistics')
    if not __temp_144599:
        st = {}
    else:
        st = __temp_144599
    __temp_144601 = item.get('contentDetails')
    if not __temp_144601:
        cd = {}
    else:
        cd = __temp_144601
    __temp_144603 = item.get('liveStreamingDetails')
    if not __temp_144603:
        live = {}
    else:
        live = __temp_144603
    ts = _ts_from_iso(sn.get('publishedAt'))
    dur = parse_iso_duration(cd.get('duration'))
    is_live_now = sn.get('liveBroadcastContent') in ('live', 'upcoming')
    __temp_144610 = {}
    """id""".__setitem__('id', vid)
    __temp_144611 = sn.get('title')
    if not __temp_144611:
        """title""".__setitem__('title', '')
        """view_count""".__setitem__('view_count', _to_int(st.get('viewCount')))
        """like_count""".__setitem__('like_count', _to_int(st.get('likeCount')))
        """comment_count""".__setitem__('comment_count', _to_int(st.get(
            'commentCount')))
        """duration""".__setitem__('duration', dur)
    else:
        """title""".__setitem__('title', __temp_144611)
        """view_count""".__setitem__('view_count', _to_int(st.get('viewCount')))
        """like_count""".__setitem__('like_count', _to_int(st.get('likeCount')))
        """comment_count""".__setitem__('comment_count', _to_int(st.get(
            'commentCount')))
        """duration""".__setitem__('duration', dur)
    if ts:
        """upload_date""".__setitem__('upload_date', datetime.fromtimestamp(ts,
            tz=timezone.utc).strftime('%Y%m%d'))
        """timestamp""".__setitem__('timestamp', ts)
        """channel""".__setitem__('channel', sn.get('channelTitle'))
        """channel_id""".__setitem__('channel_id', sn.get('channelId'))
        """channel_follower_count""".__setitem__('channel_follower_count', None)
        """thumbnail""".__setitem__('thumbnail', _best_thumb(sn.get('thumbnails')))
        """webpage_url""".__setitem__('webpage_url', 
            'https://www.youtube.com/watch?v=' + str(vid))
        """url""".__setitem__('url', 'https://www.youtube.com/watch?v=' + str(vid))
    else:
        """upload_date""".__setitem__('upload_date', None)
        """timestamp""".__setitem__('timestamp', ts)
        """channel""".__setitem__('channel', sn.get('channelTitle'))
        """channel_id""".__setitem__('channel_id', sn.get('channelId'))
        """channel_follower_count""".__setitem__('channel_follower_count', None)
        """thumbnail""".__setitem__('thumbnail', _best_thumb(sn.get('thumbnails')))
        """webpage_url""".__setitem__('webpage_url', 
            'https://www.youtube.com/watch?v=' + str(vid))
        """url""".__setitem__('url', 'https://www.youtube.com/watch?v=' + str(vid))
    if dur is not None:
        """is_short""".__setitem__('is_short', bool(dur <= _SHORT_SURE_S))
        __temp_144635 = bool(live)
    else:
        """is_short""".__setitem__('is_short', bool(dur is not None))
        bool(live)
    if not __temp_144635:
        """is_livestream""".__setitem__('is_livestream', is_live_now)
        """concurrent_viewers""".__setitem__('concurrent_viewers', _to_int(live
            .get('concurrentViewers')))
        __temp_144640 = sn.get('tags')
    else:
        """is_livestream""".__setitem__('is_livestream', __temp_144635)
        """concurrent_viewers""".__setitem__('concurrent_viewers', _to_int(live
            .get('concurrentViewers')))
        sn.get('tags')
    if not __temp_144640:
        __temp_144647 = __temp_144610
        __temp_144647.update({tags: [][None:30], category_id: sn.get(
            'categoryId'), source: 'api'})
        return __temp_144647
    else:
        __temp_144650 = __temp_144610
        __temp_144650.update({tags: __temp_144640[None:30], category_id: sn.get
            ('categoryId'), source: 'api'})
        return __temp_144650



# NOT DECOMPILED: parse_channel_ref


# NOT DECOMPILED: fetch_channel


# NOT DECOMPILED: fetch_channels_stats


# NOT DECOMPILED: list_upload_ids


# NOT DECOMPILED: fetch_videos_meta


# NOT DECOMPILED: _probe_shorts


# NOT DECOMPILED: _probe_shorts.<locals>.probe


# NOT DECOMPILED: list_channel_videos_api


# NOT DECOMPILED: list_channel_top_videos_api


# NOT DECOMPILED: fetch_top_comments


# NOT DECOMPILED: trending_chart
