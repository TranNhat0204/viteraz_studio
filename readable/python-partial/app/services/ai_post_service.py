# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/ai_post_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: post_to_dict


# NOT DECOMPILED: list_posts


# Original qualified name: get_post
def get_post(db, post_id):
    return db.get(PostCard, post_id)



# Original qualified name: save_post
def save_post(db, project_id, payload, source, chain_prev_id, seq, status):
    post = PostCard(project_id=project_id, status=status, source=source,
        chain_prev_id=chain_prev_id, seq=seq, payload_json=json.dumps(payload,
        ensure_ascii=False))
    db.add(post)
    db.commit()
    db.refresh(post)
    return post



# Original qualified name: set_status
def set_status(db, post_id, status):
    post = db.get(PostCard, post_id)
    if post is None:
        raise StudioError(E.UNKNOWN, 'Bài viết không tồn tại', status_code=404)
    post.status = status
    db.commit()
    db.refresh(post)
    return post



# NOT DECOMPILED: _read_export_seo


# Original qualified name: _selected_seo_title
def _selected_seo_title(seo, fallback):
    __temp_265790 = seo.get('titles')
    if not __temp_265790:
        titles = []
    else:
        titles = __temp_265790
    if isinstance(titles, list):
        if not titles:
            return fallback
    else:
        return fallback
    index = seo.get('chosen_title_index', 0)
    if isinstance(index, int):
        if 0 <= index:
            if not index < len(titles):
                index = 0
        else:
            index = 0
    else:
        index = 0
    if not titles[index]:
        return str(fallback).strip()
    else:
        return str(titles[index]).strip()



# NOT DECOMPILED: _video_post_payload


# NOT DECOMPILED: create_post_from_video


# NOT DECOMPILED: update_post


# NOT DECOMPILED: approve_post


# Original qualified name: run_quality_check
def run_quality_check(db, post_id):
    post = db.get(PostCard, post_id)
    if post is None:
        raise StudioError(E.UNKNOWN, 'Bài viết không tồn tại', status_code=404)
    payload = _loads(post.payload_json, {})
    payload['quality_status'] = 'passed'
    post.payload_json = json.dumps(payload, ensure_ascii=False)
    db.commit()
    db.refresh(post)
    return post



# Original qualified name: mark_published
def mark_published(db, post_id):
    post = db.get(PostCard, post_id)
    if post is None:
        raise StudioError(E.UNKNOWN, 'Bài viết không tồn tại', status_code=404)
    post.status = 'published'
    post.published_at = datetime.now()
    db.commit()
    db.refresh(post)
    return post



# Original qualified name: _recent_topics
def _recent_topics(db, project_id, limit):
    rows = db.query(PostCard).filter(PostCard.project_id == project_id).order_by(
        PostCard.seq.desc(), PostCard.created_at.desc()).limit(limit).all()
    topics = []
    for __temp_265969 in iter(rows):
        r = __temp_265969
        t = _loads(r.payload_json, {}).get('topic')
        if not t:
            continue
            topics.append(t)
        else:
            topics.append(t)
        continue
    return topics



# Original qualified name: _all_topics
def _all_topics(db, project_id):
    rows = db.query(PostCard).filter(PostCard.project_id == project_id).order_by(
        PostCard.seq.desc(), PostCard.created_at.desc()).all()
    topics = []
    seen = set()
    for __temp_265983 in iter(rows):
        r = __temp_265983
        t = _loads(r.payload_json, {}).get('topic')
        if not t:
            continue
        if not t not in seen:
            continue
            seen.add(t)
            topics.append(t)
        else:
            seen.add(t)
            topics.append(t)
        continue
    return topics



# Original qualified name: _latest_chain_post
def _latest_chain_post(db, project_id):
    return db.query(PostCard).filter(PostCard.project_id == project_id).order_by(
        PostCard.seq.desc(), PostCard.created_at.desc()).first()



# Original qualified name: has_pending_post
def has_pending_post(db, project_id):
    return db.query(PostCard).filter(PostCard.project_id == project_id,
        PostCard.status.in_(_PENDING_STATUSES)).count() > 0



# Original qualified name: publish_now
def publish_now(db, post_id, fb_page_id, content_type):
    app = __import__('app.services', fromlist=('fb_queue',), level=0)
    fb_queue = app.fb_queue
    post = db.get(PostCard, post_id)
    if post is None:
        raise StudioError(E.UNKNOWN, 'Bài viết không tồn tại', status_code=404)
    target_page_id = fb_page_id
    if not target_page_id:
        cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id == post
            .project_id).first()
        if cfg:
            target_page_id = cfg.fb_page_id
        else:
            target_page_id = None
    if not target_page_id:
        return {ok: False, error: 'Bài chưa được gán Fanpage'}
    queued = fb_queue.enqueue_post_card(db, post.id, target_page_id,
        schedule_time=datetime.now(), content_type=content_type)
    if queued is None:
        page = db.get(FbPage, target_page_id)
        if page is None:
            return {ok: False, error: 'Fanpage đã chọn không tồn tại'}
        if page.status != 'active':
            return {ok: False, error: 'Fanpage đang ' + str(page.status) +
                ', cần kết nối lại'}
        if page.fb_post_mode == 'off':
            return {ok: False, error: 'Fanpage đang tắt đăng bài'}
        return {ok: False, error: 'Không thể đưa bài vào hàng đợi Facebook'}
    post.status = 'ready'
    db.commit()
    return {ok: True, queued: True, post_id: queued.id, queue_id: queued.id,
        status: queued.status, message:
        'Bài đã vào hàng đợi và sẽ được worker đăng nền.'}



# NOT DECOMPILED: generate_next_post


# NOT DECOMPILED: ensure_next_post
