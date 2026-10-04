# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/download.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: DownloadStep.run


# NOT DECOMPILED: DownloadStep._run_hybrid


# NOT DECOMPILED: DownloadStep._run_ytdlp


# NOT DECOMPILED: DownloadStep._fetch_thumbnail


# NOT DECOMPILED: DownloadStep._download_thumbnail


# Original qualified name: DownloadStep._save_meta
def _save_meta(self, ctx, info, thumbnail_path):
    app = __import__('app.core.events', fromlist=('bus',), level=0)
    bus = app.bus
    app = __import__('app.config', fromlist=('get_settings',), level=0)
    get_settings = app.get_settings
    with SessionLocal() as __temp_255751:
        db = __temp_255751
        v = db.get(Video, ctx.video_id)
        if v:
            __temp_255753 = info.get('title')
            if not __temp_255753:
                v.title = v.title
            else:
                v.title = __temp_255753
            __temp_255754 = info.get('author')
            if not __temp_255754:
                v.author = v.author
            else:
                v.author = __temp_255754
            __temp_255755 = info.get('duration_ms')
            if not __temp_255755:
                v.duration_ms = v.duration_ms
            else:
                v.duration_ms = __temp_255755
            __temp_255756 = info.get('aweme_id')
            if not __temp_255756:
                v.aweme_id = v.aweme_id
            else:
                v.aweme_id = __temp_255756
            __temp_255757 = info.get('cover_url')
            if not __temp_255757:
                v.cover_url = v.cover_url
            else:
                v.cover_url = __temp_255757
            if info.get('platform'):
                if not v.platform:
                    v.platform = info.get('platform')
            if thumbnail_path:
                v.thumbnail_path = thumbnail_path
            db.commit()
            settings = get_settings()
        else:
            settings = get_settings()
        thumbnail_url = None
        if thumbnail_path:
            thumbnail_url = 'http://127.0.0.1:' + str(settings.port
                ) + '/api/v1/videos/' + str(ctx.video_id
                ) + '/preview/thumbnail?token=' + str(settings.token)
        bus.video_meta(ctx.project_id, ctx.video_id, title=info.get('title'),
            author=info.get('author'), duration_ms=info.get('duration_ms'),
            cover_url=info.get('cover_url'), thumbnail_path=thumbnail_url)
        return None



# NOT DECOMPILED: DownloadStep._download_stream


# NOT DECOMPILED: DownloadStep._stream_attempt
