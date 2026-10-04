# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/ai_scheduler.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _today_str
def _today_str(now):
    return now.strftime('%Y-%m-%d')



# NOT DECOMPILED: _is_due


# NOT DECOMPILED: _due_channels


# NOT DECOMPILED: _post_is_due


# NOT DECOMPILED: _due_post_channels


# Original qualified name: _mark_surfaced
def _mark_surfaced(project_id, day):
    with SessionLocal() as __temp_266077:
        db = __temp_266077
        cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id ==
            project_id).first()
        if cfg:
            cfg.last_surfaced_date = day
            db.commit()
            return None
        else:
            return None



# Original qualified name: _mark_post_surfaced
def _mark_post_surfaced(project_id, day):
    with SessionLocal() as __temp_266085:
        db = __temp_266085
        cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id ==
            project_id).first()
        if cfg:
            cfg.post_last_surfaced_date = day
            db.commit()
            return None
        else:
            return None



# NOT DECOMPILED: run_tick_now


# NOT DECOMPILED: fb_snapshot_daily


# NOT DECOMPILED: _run_loop


# NOT DECOMPILED: _run_publish_loop


# Original qualified name: start
def start():
    global _task, _publish_task, _stop
    if _task is not None:
        if not _task.done():
            return None
    _stop = asyncio.Event()
    _task = asyncio.create_task(_run_loop())
    _publish_task = asyncio.create_task(_run_publish_loop())
    log.info('[ai_scheduler] đã khởi động (surface mỗi ' + str(
        TICK_INTERVAL_SEC) + 's, publish mỗi ' + str(PUBLISH_TICK_INTERVAL_SEC) +
        's).')
    return None



# NOT DECOMPILED: stop
