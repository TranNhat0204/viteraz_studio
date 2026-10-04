# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_queue.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _loads


# NOT DECOMPILED: _resolve_mode


# NOT DECOMPILED: _content_package


# Original qualified name: _last_pending_schedule
def _last_pending_schedule(db, page_db_id):
    stmt = select(func.max(FbPost.schedule_time)).where(FbPost.fb_page_id ==
        page_db_id, FbPost.status.in_(('ready', 'scheduled', 'processing')))
    return db.execute(stmt).scalar()



# NOT DECOMPILED: enqueue_video


# NOT DECOMPILED: enqueue_post_card
