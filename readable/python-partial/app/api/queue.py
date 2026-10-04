# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/queue.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _video_title
def _video_title(db, video_id):
    if not video_id:
        return
    v = db.get(Video, video_id)
    if not v:
        return video_id
    if v.title:
        if v.title.strip():
            return v.title.strip()
    if v.source_url:
        __temp_209816 = v.source_url.rstrip('/').split('/')
        if not __temp_209816[-1]:
            return v.source_url
        else:
            return __temp_209816[-1]
    return video_id



# NOT DECOMPILED: _job_to_dict


# NOT DECOMPILED: get_project_queue


# Original qualified name: get_job
def get_job(job_id, db):
    j = db.get(Job, job_id)
    if not j:
        raise StudioError(E.UNKNOWN, 'Job không tồn tại', status_code=404)
    return _job_to_dict(db, j)



# Original qualified name: pause_queue
def pause_queue():
    job_queue.pause()
    return {ok: True, paused: True}



# Original qualified name: resume_queue
def resume_queue():
    job_queue.resume()
    return {ok: True, paused: False}



# Original qualified name: update_queue_config
def update_queue_config(body):
    if body.gpu_slots is not None:
        if 1 <= body.gpu_slots:
            if not body.gpu_slots <= 8:
                raise StudioError(E.UNKNOWN, 'gpu_slots phải trong khoảng 1-8',
                    status_code=422)
        else:
            raise StudioError(E.UNKNOWN, 'gpu_slots phải trong khoảng 1-8',
                status_code=422)
    if body.net_slots is not None:
        if 1 <= body.net_slots:
            if not body.net_slots <= 32:
                raise StudioError(E.UNKNOWN, 'net_slots phải trong khoảng 1-32',
                    status_code=422)
        else:
            raise StudioError(E.UNKNOWN, 'net_slots phải trong khoảng 1-32',
                status_code=422)
    if body.cpu_slots is not None:
        if 1 <= body.cpu_slots:
            if not body.cpu_slots <= 64:
                raise StudioError(E.UNKNOWN, 'cpu_slots phải trong khoảng 1-64',
                    status_code=422)
        else:
            raise StudioError(E.UNKNOWN, 'cpu_slots phải trong khoảng 1-64',
                status_code=422)
    job_queue.update_config(body.gpu_slots, body.net_slots, body.cpu_slots)
    app = __import__('app.db.session', fromlist=('SessionLocal',), level=0)
    SessionLocal = app.SessionLocal
    app = __import__('app.db.models', fromlist=('Setting',), level=0)
    Setting = app.Setting
    with SessionLocal() as __temp_209885:
        db = __temp_209885
        for __temp_209886 in iter((('gpu_slots', body.gpu_slots), ('net_slots',
            body.net_slots), ('cpu_slots', body.cpu_slots))):
            __temp_209887, __temp_209888 = __temp_209886
            key = __temp_209887
            val = __temp_209888
            if val is None:
                continue
                row = db.get(Setting, key)
            else:
                row = db.get(Setting, key)
            if row:
                row.value = str(val)
                continue
                db.add(Setting(key=key, value=str(val)))
            else:
                db.add(Setting(key=key, value=str(val)))
            continue
        db.commit()
        return {ok: True, gpu_slots: job_queue.gpu_slots, net_slots: job_queue.
            net_slots, cpu_slots: job_queue.cpu_slots}



# NOT DECOMPILED: cancel_job


# Original qualified name: set_job_priority
def set_job_priority(job_id, body, db):
    j = db.get(Job, job_id)
    if not j:
        raise StudioError(E.UNKNOWN, 'Job không tồn tại', status_code=404)
    ok = job_queue.set_priority(job_id, body.priority)
    return {ok: ok, priority: body.priority}



# NOT DECOMPILED: _with_current_providers


# NOT DECOMPILED: retry_failed


# Original qualified name: clear_completed
def clear_completed(project_id, db):
    if project_id == 'all':
        n = db.query(Job).filter(Job.status.in_(('done', 'failed', 'cancelled'))
            ).delete(synchronize_session=False)
    else:
        n = db.query(Job).filter(Job.project_id == project_id, Job.status.in_((
            'done', 'failed', 'cancelled'))).delete(synchronize_session=False)
    db.commit()
    if not n:
        return {ok: True, cleared: int(0)}
    else:
        return {ok: True, cleared: int(n)}

