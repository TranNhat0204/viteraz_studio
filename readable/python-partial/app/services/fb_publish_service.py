# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_publish_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _bounded_int


# Original qualified name: FbPublishContext.__init__
def __init__(self, db, strategy, block_size, proxy_global, max_posts_per_day, min_gap_minutes):
    self.db = db
    self.exclude = set()
    self.strategy = strategy
    self.block_size = block_size
    self.proxy_global = proxy_global
    self.max_posts_per_day = max_posts_per_day
    self.min_gap_minutes = min_gap_minutes
    return None



# NOT DECOMPILED: publish_due


# NOT DECOMPILED: publish_due.<locals>.run_one


# NOT DECOMPILED: _publish_one


# Original qualified name: _resolve_stuck
def _resolve_stuck(db):
    threshold = datetime.now() - timedelta(minutes=STUCK_MIN)
    stuck = db.execute(select(FbPost).where(FbPost.status == 'processing', 
        FbPost.updated_at < threshold)).scalars().all()
    n = 0
    for __temp_271926 in iter(stuck):
        p = __temp_271926
        p.status = 'ready'
        p.updated_at = datetime.now()
        n += 1
        continue
    if n:
        db.commit()
        log.info('[fb_publish] khôi phục ' + str(n) +
            ' bài stuck (processing > ' + str(STUCK_MIN) + "') sang ready")
        return n
    else:
        return n



# NOT DECOMPILED: publish_now_in_session


# NOT DECOMPILED: publish_now
