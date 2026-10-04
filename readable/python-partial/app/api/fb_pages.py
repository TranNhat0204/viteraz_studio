# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/fb_pages.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _upsert_page_snapshot


# NOT DECOMPILED: page_to_dict


# NOT DECOMPILED: post_to_dict


# NOT DECOMPILED: fetch_available_pages


# NOT DECOMPILED: import_selected_pages


# NOT DECOMPILED: connect_token


# NOT DECOMPILED: list_pages


# NOT DECOMPILED: update_page


# NOT DECOMPILED: update_page_proxy


# NOT DECOMPILED: refresh_stats


# NOT DECOMPILED: get_page_avatar


# NOT DECOMPILED: sync_page_posts


# Original qualified name: delete_page
def delete_page(page_id, db):
    page = db.get(FbPage, page_id)
    if page is None:
        raise StudioError(E.UNKNOWN, 'Page không tồn tại', status_code=404)
    db.query(FbContentCalendarItem).filter(FbContentCalendarItem.fb_page_id ==
        page_id).delete(synchronize_session=False)
    db.query(FbPageDailySnapshot).filter(FbPageDailySnapshot.fb_page_id == page_id
        ).delete(synchronize_session=False)
    db.query(ScheduleConfig).filter(ScheduleConfig.fb_page_id == page_id).update({
        ScheduleConfig.fb_page_id: None, ScheduleConfig.post_enabled: 0},
        synchronize_session=False)
    db.query(FbPost).filter(FbPost.fb_page_id == page_id).update({FbPost.
        fb_page_id: None}, synchronize_session=False)
    db.query(FbToken).filter(FbToken.page_id == page.page_id).delete()
    db.query(FbTokenPageAccess).filter(FbTokenPageAccess.page_id == page.page_id
        ).delete()
    db.delete(page)
    db.commit()
    return {'ok': True}



# NOT DECOMPILED: add_token_to_pool


# NOT DECOMPILED: list_tokens


# NOT DECOMPILED: reactivate_token


# Original qualified name: get_fb_settings
def get_fb_settings(db):
    return fb_settings.get_fb_settings(db)



# NOT DECOMPILED: put_settings


# NOT DECOMPILED: delete_token


# NOT DECOMPILED: list_posts


# NOT DECOMPILED: publish_now


# Original qualified name: retry_post
def retry_post(post_id, db):
    post = db.get(FbPost, post_id)
    if post is None:
        raise StudioError(E.UNKNOWN, 'Bài không tồn tại', status_code=404)
    if post.status not in ('failed', 'cancelled'):
        raise StudioError(E.UNKNOWN, 'Chỉ có thể thử lại bài lỗi hoặc đã huỷ.',
            status_code=409)
    post.status = 'ready'
    post.retry_count = 0
    post.error_message = None
    db.commit()
    return {ok: True, post: post_to_dict(post)}



# Original qualified name: unstick_posts
def unstick_posts(db):
    recovered = fb_publish_service.resolve_stuck(db)
    return {ok: True, recovered: recovered}



# Original qualified name: cancel_post
def cancel_post(post_id, db):
    post = db.get(FbPost, post_id)
    if post is None:
        raise StudioError(E.UNKNOWN, 'Bài không tồn tại', status_code=404)
    if post.status not in ('ready', 'draft', 'failed'):
        raise StudioError(E.UNKNOWN,
            'Không thể huỷ bài đang xử lý hoặc đã giao cho Facebook.',
            status_code=409)
    post.status = 'cancelled'
    post.error_message = None
    db.commit()
    return {ok: True, post: post_to_dict(post)}



# Original qualified name: reschedule_post
def reschedule_post(post_id, body, db):
    post = db.get(FbPost, post_id)
    if post is None:
        raise StudioError(E.UNKNOWN, 'Bài không tồn tại', status_code=404)
    if post.status in ('processing', 'posted', 'scheduled'):
        raise StudioError(E.UNKNOWN,
            'Không thể đổi lịch bài đang xử lý hoặc đã giao cho Facebook.',
            status_code=409)
    schedule_time = body.schedule_time.replace(tzinfo=None)
    if schedule_time <= datetime.now():
        raise StudioError(E.UNKNOWN,
            'Giờ đăng phải ở tương lai; dùng Đăng ngay nếu muốn xuất bản bây giờ.',
            status_code=422)
    post.schedule_time = schedule_time
    if post.status in ('failed', 'cancelled', 'draft'):
        post.status = 'ready'
        post.error_message = None
        post.retry_count = 0
    db.commit()
    return {ok: True, post: post_to_dict(post)}



# NOT DECOMPILED: list_calendar


# NOT DECOMPILED: create_calendar_item


# Original qualified name: suggest_calendar
def suggest_calendar(fb_page_id, start_date, days, per_day, db):
    if not start_date:
        start_date = datetime.now().strftime('%Y-%m-%d')
    days = max(1, min(days, 90))
    per_day = max(1, min(per_day, 25))
    items = fb_calendar_service.suggest_slots(db, fb_page_id=fb_page_id,
        start_date=start_date, days=days, per_day=per_day)
    return {'items': items}



# NOT DECOMPILED: update_calendar_item


# Original qualified name: delete_calendar_item
def delete_calendar_item(item_id, db):
    fb_calendar_service.delete_calendar_item(db, item_id)
    return {'ok': True}



# Original qualified name: update_pillars
def update_pillars(page_id, body, db):
    page = db.get(FbPage, page_id)
    if page is None:
        raise StudioError(E.UNKNOWN, 'Page không tồn tại', status_code=404)
    raw = body.get('pillars')
    if isinstance(raw, str):
        json = __import__('json', fromlist=None, level=0)
        _json = json
        if raw.strip():
            raw = _json.loads(raw)
        else:
            raw = []
    if raw:
        page.pillars_json = json.dumps(raw, ensure_ascii=False)
    else:
        page.pillars_json = None
    db.commit()
    return {ok: True, pillars_json: page.pillars_json}



# Original qualified name: fb_research_overview
def fb_research_overview(db):
    channels = fb_research_service.linked_channels(db)
    stats = fb_research_service.channel_status(db)
    return {channels: channels, stats: stats}



# NOT DECOMPILED: fb_research_suggest


# NOT DECOMPILED: fb_research_approve_idea


# Original qualified name: fb_research_approve_post
def fb_research_approve_post(post_id, db):
    return fb_research_service.approve_post_card(post_id)



# Original qualified name: fb_research_reject_idea
def fb_research_reject_idea(idea_id, db):
    return fb_research_service.reject_video_idea(idea_id)



# Original qualified name: fb_research_reject_post
def fb_research_reject_post(post_id):
    return fb_research_service.reject_post_card(post_id)



# NOT DECOMPILED: fb_stats


# Original qualified name: fb_stats.<locals>._count_when
def _count_when(condition):
    return func.coalesce(func.sum(case((condition, 1), else_=0)), 0)

