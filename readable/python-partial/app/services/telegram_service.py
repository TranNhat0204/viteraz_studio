# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/telegram_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: watch_recap
def watch_recap(video_id):
    _recap_watch.add(video_id)
    return None



# Original qualified name: is_recap_watched
def is_recap_watched(video_id):
    return video_id in _recap_watch



# Original qualified name: clear_recap_watch
def clear_recap_watch(video_id):
    _recap_watch.discard(video_id)
    return None



# Original qualified name: _extract_urls
def _extract_urls(text):
    if not text:
        return _URL_RE.findall('')
    else:
        return _URL_RE.findall(text)



# Original qualified name: _spawn
def _spawn(coro):
    task = asyncio.create_task(coro)
    _BG_TASKS.add(task)
    task.add_done_callback(_BG_TASKS.discard)
    return None



# NOT DECOMPILED: _get


# NOT DECOMPILED: _config


# Original qualified name: is_enabled
def is_enabled():
    __temp_276680, __temp_276681, __temp_276682 = _config()
    token = __temp_276680
    _chats = __temp_276681
    enabled = __temp_276682
    if enabled:
        return bool(token)
    else:
        return bool(enabled)



# NOT DECOMPILED: _api


# NOT DECOMPILED: send_message


# NOT DECOMPILED: send_photo


# NOT DECOMPILED: _send_card


# NOT DECOMPILED: _wait_image


# NOT DECOMPILED: _idea_image_path


# NOT DECOMPILED: _post_image_path


# NOT DECOMPILED: send_test


# NOT DECOMPILED: _idea_text


# Original qualified name: _idea_keyboard
def _idea_keyboard(idea_id):
    return {'inline_keyboard': [[{text: '✅ Duyệt', callback_data: 'ap:' + str(
        idea_id)}, {text: '❌ Bỏ', callback_data: 'rj:' + str(idea_id)}]]}



# NOT DECOMPILED: notify_new_idea


# NOT DECOMPILED: _post_text


# Original qualified name: _post_keyboard
def _post_keyboard(post_id):
    return {'inline_keyboard': [[{text: '✅ Duyệt', callback_data: 'pa:' + str(
        post_id)}, {text: '❌ Bỏ', callback_data: 'pr:' + str(post_id)}]]}



# NOT DECOMPILED: notify_new_post


# Original qualified name: _produce_keyboard
def _produce_keyboard(video_id):
    return {'inline_keyboard': [[{text: '🎬 Sản xuất', callback_data: 'pv:' +
        str(video_id)}]]}



# NOT DECOMPILED: _idea_script_text


# NOT DECOMPILED: _video_script_text


# Original qualified name: _review_keyboard
def _review_keyboard(kind, obj_id):
    if kind == 'idea':
        act = 'sda'
    else:
        act = 'sd'
    if kind == 'idea':
        sed = 'sei'
    else:
        sed = 'sev'
    return {'inline_keyboard': [[{text: '✅ Duyệt & Sản xuất', callback_data: 
        str(act) + ':' + str(obj_id)}], [{text: '✏️ Sửa kịch bản',
        callback_data: str(sed) + ':' + str(obj_id)}], [{text: '❌ Bỏ',
        callback_data: 'srej:' + str(obj_id)}]]}



# NOT DECOMPILED: notify_script_for_review


# NOT DECOMPILED: _apply_script_edit


# NOT DECOMPILED: _cmd_save_edited_script


# NOT DECOMPILED: notify_script_ready


# NOT DECOMPILED: notify_video_status


# Original qualified name: _list_channels
def _list_channels(kind):
    app = __import__('app.db.models', fromlist=('Project', 'ScheduleConfig'),
        level=0)
    Project = app.Project
    ScheduleConfig = app.ScheduleConfig
    app = __import__('app.services', fromlist=('project_service',), level=0)
    project_service = app.project_service
    psvc = project_service
    out = []
    with SessionLocal() as __temp_276938:
        db = __temp_276938
        projs = db.query(Project).filter(Project.kind == kind).order_by(Project
            .created_at.asc()).all()
        for __temp_276944 in iter(projs):
            p = __temp_276944
            if kind == 'recap':
                __temp_276945 = psvc._load_default_config(p)
                if not __temp_276945:
                    ready = bool({}.get('pipeline'))
                else:
                    ready = bool(__temp_276945.get('pipeline'))
            else:
                cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id ==
                    p.id).first()
                if cfg:
                    ready = bool(cfg.engine_id)
                else:
                    ready = bool(cfg)
            if not p.name:
                out.append((p.id, p.id[None:8], ready))
            else:
                out.append((p.id, p.name, ready))
            continue
        return out



# NOT DECOMPILED: _channel_keyboard


# Original qualified name: _format_keyboard
def _format_keyboard(kind, pid):
    return {'inline_keyboard': [[{text: '📱 Dọc (9:16)', callback_data: str(kind
        ) + ':' + str(pid) + ':doc'}, {text: '🖥 Ngang (16:9)', callback_data: 
        str(kind) + ':' + str(pid) + ':ngang'}]]}



# NOT DECOMPILED: _send_channel_picker


# Original qualified name: _fmt_label
def _fmt_label(fmt):
    if fmt == 'doc':
        return 'dọc 9:16'
    return 'ngang 16:9'



# NOT DECOMPILED: _cmd_story


# NOT DECOMPILED: _cmd_story_pick_chapters


# NOT DECOMPILED: _cmd_status


# NOT DECOMPILED: _say


# NOT DECOMPILED: _cmd_generate_idea


# NOT DECOMPILED: _cmd_generate_video


# NOT DECOMPILED: _cmd_generate_post


# Original qualified name: _ai_action_keyboard
def _ai_action_keyboard(pid):
    return {'inline_keyboard': [[{text: '💡 Ý tưởng (duyệt)', callback_data: 
        'ci:' + str(pid)}], [{text: '🎬 Tạo video ngay', callback_data: 'cv:' +
        str(pid)}], [{text: '📝 Bài viết Facebook', callback_data: 'cp:' + str(
        pid)}]]}



# NOT DECOMPILED: _run_recap


# NOT DECOMPILED: _run_recap.<locals>._say


# Original qualified name: _recap_target_get
def _recap_target_get(cid):
    item = _recap_target.get(cid)
    if not item:
        return None
    __temp_277087, __temp_277088 = item
    pid = __temp_277087
    ts = __temp_277088
    if time.time() - ts > _RECAP_TTL:
        _recap_target.pop(cid, None)
        return None
    return pid



# NOT DECOMPILED: _maybe_handle_recap_link


# NOT DECOMPILED: _answer_callback


# NOT DECOMPILED: _edit_text


# NOT DECOMPILED: _handle_callback


# NOT DECOMPILED: _handle_message


# NOT DECOMPILED: _handle_update


# NOT DECOMPILED: _poll_once


# NOT DECOMPILED: _ensure_commands


# NOT DECOMPILED: _run_loop


# Original qualified name: start
def start():
    global _task, _stop
    if _task is not None:
        if not _task.done():
            return None
    _stop = asyncio.Event()
    _task = asyncio.create_task(_run_loop())
    return None



# NOT DECOMPILED: stop
