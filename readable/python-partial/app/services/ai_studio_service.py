# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/ai_studio_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: get_or_create_config
def get_or_create_config(db, project_id):
    cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id == project_id
        ).first()
    if cfg is None:
        cfg = ScheduleConfig(project_id=project_id)
        db.add(cfg)
        db.commit()
        db.refresh(cfg)
        return cfg
    else:
        return cfg



# Original qualified name: config_to_dict
def config_to_dict(cfg):
    """project_id""".__setitem__('project_id', cfg.project_id)
    """enabled""".__setitem__('enabled', bool(cfg.enabled))
    """engine_id""".__setitem__('engine_id', cfg.engine_id)
    """language""".__setitem__('language', cfg.language)
    """run_time""".__setitem__('run_time', cfg.run_time)
    """approval_mode""".__setitem__('approval_mode', cfg.approval_mode)
    """video_ratio""".__setitem__('video_ratio', cfg.video_ratio)
    """channel_profile""".__setitem__('channel_profile', _loads(cfg.
        channel_profile_json, {}))
    """series_arc""".__setitem__('series_arc', cfg.series_arc)
    """next_idea_id""".__setitem__('next_idea_id', cfg.next_idea_id)
    """buffer_depth""".__setitem__('buffer_depth', cfg.buffer_depth)
    """last_surfaced_date""".__setitem__('last_surfaced_date', cfg.
        last_surfaced_date)
    """post_enabled""".__setitem__('post_enabled', bool(cfg.post_enabled))
    """post_run_time""".__setitem__('post_run_time', cfg.post_run_time)
    """post_last_surfaced_date""".__setitem__('post_last_surfaced_date', cfg.
        post_last_surfaced_date)
    """fb_page_id""".__setitem__('fb_page_id', cfg.fb_page_id)
    return {}



# NOT DECOMPILED: update_config


# Original qualified name: _effective_scope
def _effective_scope(cfg):
    profile = _loads(cfg.channel_profile_json, {})
    if cfg.engine_id:
        engine = channel_engines.get_engine(cfg.engine_id)
    else:
        engine = None
    return ideation_service.resolve_character_scope(engine, profile)



# NOT DECOMPILED: _backfill_channel_cast


# NOT DECOMPILED: video_cast


# NOT DECOMPILED: idea_portraits


# NOT DECOMPILED: ideas_to_dicts


# NOT DECOMPILED: idea_to_dict


# Original qualified name: list_ideas
def list_ideas(db, project_id, status, limit):
    q = db.query(IdeaCard).filter(IdeaCard.project_id == project_id)
    if status:
        q = q.filter(IdeaCard.status == status)
    return q.order_by(IdeaCard.created_at.desc()).limit(limit).all()



# Original qualified name: get_idea
def get_idea(db, idea_id):
    return db.get(IdeaCard, idea_id)



# Original qualified name: set_thumbnail_variant
def set_thumbnail_variant(db, idea_id, variant):
    idea = db.get(IdeaCard, idea_id)
    if idea is None:
        raise StudioError(E.UNKNOWN, 'Ý tưởng không tồn tại', status_code=404)
    payload = _loads(idea.payload_json, {})
    __temp_266297 = payload.get('thumbnail_variants')
    if not __temp_266297:
        vs = []
    else:
        vs = __temp_266297
    if isinstance(variant, int):
        if 0 <= variant:
            if not variant < len(vs):
                raise StudioError(E.UNKNOWN, 'Biến thể thumbnail không hợp lệ',
                    status_code=400)
        else:
            raise StudioError(E.UNKNOWN, 'Biến thể thumbnail không hợp lệ',
                status_code=400)
    else:
        raise StudioError(E.UNKNOWN, 'Biến thể thumbnail không hợp lệ',
            status_code=400)
    payload['thumbnail_variant'] = variant
    payload['thumbnail_path'] = vs[variant]
    idea.payload_json = json.dumps(payload, ensure_ascii=False)
    db.commit()
    db.refresh(idea)
    return idea



# Original qualified name: save_idea
def save_idea(db, project_id, payload, source, chain_prev_id, seq, status):
    idea = IdeaCard(project_id=project_id, status=status, source=source,
        chain_prev_id=chain_prev_id, seq=seq, payload_json=json.dumps(payload,
        ensure_ascii=False))
    db.add(idea)
    db.commit()
    db.refresh(idea)
    return idea



# Original qualified name: set_status
def set_status(db, idea_id, status):
    idea = db.get(IdeaCard, idea_id)
    if idea is None:
        raise StudioError(E.UNKNOWN, 'Ý tưởng không tồn tại', status_code=404)
    idea.status = status
    db.commit()
    db.refresh(idea)
    return idea



# Original qualified name: update_idea_payload
def update_idea_payload(db, idea_id, fields):
    idea = db.get(IdeaCard, idea_id)
    if idea is None:
        raise StudioError(E.UNKNOWN, 'Ý tưởng không tồn tại', status_code=404)
    payload = _loads(idea.payload_json, {})
    for __temp_266321 in iter(fields.items()):
        __temp_266322, __temp_266323 = __temp_266321
        k = __temp_266322
        v = __temp_266323
        if v is None:
            payload.pop(k, None)
            continue
            payload[k] = v
        else:
            payload[k] = v
        continue
    idea.payload_json = json.dumps(payload, ensure_ascii=False)
    db.commit()
    db.refresh(idea)
    return idea



# Original qualified name: delete_idea
def delete_idea(db, idea_id):
    idea = db.get(IdeaCard, idea_id)
    if idea is None:
        raise StudioError(E.UNKNOWN, 'Ý tưởng không tồn tại', status_code=404)
    db.delete(idea)
    db.commit()
    return None



# Original qualified name: _recent_titles
def _recent_titles(db, project_id, limit):
    rows = db.query(IdeaCard).filter(IdeaCard.project_id == project_id,
        IdeaCard.status.in_(_RECENT_STATUSES)).order_by(IdeaCard.seq.desc()).limit(
        limit).all()
    titles = []
    for __temp_266340 in iter(rows):
        r = __temp_266340
        t = _loads(r.payload_json, {}).get('title')
        if not t:
            continue
            titles.append(t)
        else:
            titles.append(t)
        continue
    return titles



# Original qualified name: _all_titles
def _all_titles(db, project_id):
    rows = db.query(IdeaCard).filter(IdeaCard.project_id == project_id).order_by(
        IdeaCard.seq.desc(), IdeaCard.created_at.desc()).all()
    titles = []
    seen = set()
    for __temp_266354 in iter(rows):
        r = __temp_266354
        t = _loads(r.payload_json, {}).get('title')
        if not t:
            continue
        if not t not in seen:
            continue
            seen.add(t)
            titles.append(t)
        else:
            seen.add(t)
            titles.append(t)
        continue
    return titles



# NOT DECOMPILED: _recent_cast_names


# NOT DECOMPILED: _sibling_vibe_titles


# NOT DECOMPILED: _resolve_niche_angles


# Original qualified name: _latest_chain_idea
def _latest_chain_idea(db, project_id):
    return db.query(IdeaCard).filter(IdeaCard.project_id == project_id).order_by(
        IdeaCard.seq.desc(), IdeaCard.created_at.desc()).first()



# Original qualified name: has_pending_idea
def has_pending_idea(db, project_id):
    return db.query(IdeaCard).filter(IdeaCard.project_id == project_id,
        IdeaCard.status.in_(_PENDING_STATUSES)).count() > 0



# NOT DECOMPILED: draft_next_idea


# NOT DECOMPILED: cast_from_imported_script


# NOT DECOMPILED: analyze_imported_script_idea


# NOT DECOMPILED: generate_next_idea


# NOT DECOMPILED: ensure_next_idea


# NOT DECOMPILED: _ai_config


# NOT DECOMPILED: channel_analytics


# NOT DECOMPILED: approve_idea


# NOT DECOMPILED: produce_video


# NOT DECOMPILED: produce_video_clips


# NOT DECOMPILED: assemble_only


# Original qualified name: _assert_no_active_job
def _assert_no_active_job(video_id):
    app = __import__('app.db.models', fromlist=('Job', 'VideoStep'), level=0)
    Job = app.Job
    VideoStep = app.VideoStep
    with SessionLocal() as __temp_266794:
        db = __temp_266794
        job = db.query(Job).filter(Job.video_id == video_id, Job.status.in_((
            'queued', 'running'))).order_by(Job.created_at).first()
        if not job:
            return None
        step = db.query(VideoStep).filter(VideoStep.video_id == video_id, 
            VideoStep.status == 'running').order_by(VideoStep.updated_at.desc()
            ).first()
        if step:
            what = _STEP_LABELS.get(step.step_name, step.step_name)
        elif not job.step_name:
            what = 'tác vụ'
        else:
            what = job.step_name
        raise StudioError(E.UNKNOWN, 'Video này đang chạy “' + str(what) +
            '” — chờ chạy xong rồi bấm lại, hoặc vào tab Hàng đợi bấm Huỷ. (Mỗi video chỉ chạy được một tác vụ tại một thời điểm.)'
            , status_code=409)



# NOT DECOMPILED: _visual_assets_ready


# Original qualified name: _visual_assets_ready.<locals>._ready
def _ready(scene):
    if scene.get('status') == 'image_ready':
        return bool(scene.get('image_path'))
    if scene.get('status') == 'done':
        __temp_266837 = scene.get('asset_path')
        if not __temp_266837:
            return bool(scene.get('image_path'))
        else:
            return bool(__temp_266837)
    return False



# Original qualified name: _ai_studio_config_for
def _ai_studio_config_for(video_id):
    app = __import__('app.db.models', fromlist=('VideoStep',), level=0)
    VideoStep = app.VideoStep
    with SessionLocal() as __temp_266842:
        db = __temp_266842
        video = db.get(Video, video_id)
        if video is None:
            raise StudioError(E.UNKNOWN, 'Video không tồn tại', status_code=404)
        project_id = video.project_id
        script_step = db.query(VideoStep).filter(VideoStep.video_id == video_id,
            VideoStep.step_name == 'script').first()
        if script_step:
            if script_step.status not in ('success', 'skipped'):
                raise StudioError(E.UNKNOWN,
                    'Chưa có kịch bản (step script chưa xong). Hãy chờ/chạy script trước.'
                    , status_code=409)
        else:
            raise StudioError(E.UNKNOWN,
                'Chưa có kịch bản (step script chưa xong). Hãy chờ/chạy script trước.'
                , status_code=409)
        cfg = get_or_create_config(db, project_id)
        config = _ai_config(cfg)
        _apply_idea_format(config, _idea_format_for_video(db, video_id),
            _idea_duration_for_video(db, video_id))
        return project_id, config



# NOT DECOMPILED: regenerate_voice


# NOT DECOMPILED: regenerate_voice_timing


# NOT DECOMPILED: regenerate_storyboard


# NOT DECOMPILED: regenerate_script


# NOT DECOMPILED: reset_idea_to_proposed


# NOT DECOMPILED: _safe_rmtree


# Original qualified name: _purge_video_soft_links
def _purge_video_soft_links(db, video_id, root):
    app = __import__('app.db.models', fromlist=('FbPost', 'PostCard'), level=0)
    FbPost = app.FbPost
    PostCard = app.PostCard
    dirs = []
    for __temp_266896 in iter(db.query(PostCard).all()):
        post = __temp_266896
        if _loads(post.payload_json, {}).get('video_id') != video_id:
            continue
        if root is not None:
            dirs.append(root / 'posts' / post.id)
            db.delete(post)
        else:
            db.delete(post)
        continue
    for __temp_266906 in iter(db.query(FbPost).filter(FbPost.video_id ==
        video_id).all()):
        fp = __temp_266906
        if not fp.status == 'posted':
            if fp.fb_object_id:
                fp.video_id = None
                fp.media_path = None
                continue
                db.delete(fp)
            else:
                db.delete(fp)
        else:
            fp.video_id = None
            fp.media_path = None
            continue
            db.delete(fp)
        continue
    return dirs



# NOT DECOMPILED: purge_idea


# NOT DECOMPILED: resume_video


# Original qualified name: _video_or_404
def _video_or_404(db, video_id):
    v = db.get(Video, video_id)
    if v is None:
        raise StudioError(E.UNKNOWN, 'Video không tồn tại', status_code=404)
    return v



# NOT DECOMPILED: _load_scenes


# NOT DECOMPILED: _purge_scene_files


# NOT DECOMPILED: _persist_scenes


# Original qualified name: update_script_line
def update_script_line(db, video_id, seq, text):
    app = __import__('app.db.models', fromlist=('SubtitleSegment',), level=0)
    SubtitleSegment = app.SubtitleSegment
    seg = db.query(SubtitleSegment).filter(SubtitleSegment.video_id == video_id,
        SubtitleSegment.kind == 'original', SubtitleSegment.seq == seq).first()
    if seg is None:
        raise StudioError(E.UNKNOWN,
            'Không tìm thấy câu kịch bản này (chưa có kịch bản gốc).',
            status_code=404)
    seg.text = text
    seg.edited = 1
    db.commit()
    if not seg.text:
        return {seq: seg.seq, start_ms: seg.start_ms, end_ms: seg.end_ms, text: ''}
    else:
        return {seq: seg.seq, start_ms: seg.start_ms, end_ms: seg.end_ms, text:
            seg.text}



# NOT DECOMPILED: replace_script


# NOT DECOMPILED: _live_script


# NOT DECOMPILED: _outline_of


# Original qualified name: _script_audit_provider
def _script_audit_provider(profile):
    __temp_267055 = profile.get('script_audit_provider')
    if not __temp_267055:
        __temp_267057 = str('').strip()
    else:
        str(__temp_267055).strip()
    if not __temp_267057:
        return _SCRIPT_AUDIT_PROVIDER_DEFAULT
    else:
        return __temp_267057



# NOT DECOMPILED: score_video_script


# NOT DECOMPILED: improve_video_script


# Original qualified name: undo_script_improvement
def undo_script_improvement(video_id):
    with SessionLocal() as __temp_267091:
        db = __temp_267091
        _video_or_404(db, video_id)
        __temp_267094, __temp_267095 = _outline_of(db, video_id)
        plan = __temp_267094
        outline = __temp_267095
        if isinstance(outline, dict):
            undo = outline.get('script_improve_undo')
        else:
            undo = None
        if isinstance(undo, dict):
            __temp_267099 = undo.get('script')
            if not __temp_267099:
                __temp_267100 = ''.strip()
            else:
                __temp_267099.strip()
            if not __temp_267100:
                raise StudioError(E.PRECONDITION_MISSING,
                    'Không có bản kịch bản nào để hoàn tác.', status_code=409)
        else:
            raise StudioError(E.PRECONDITION_MISSING,
                'Không có bản kịch bản nào để hoàn tác.', status_code=409)
        segments = replace_script(db, video_id, undo['script'])
        __temp_267106, __temp_267107 = _outline_of(db, video_id)
        plan = __temp_267106
        outline = __temp_267107
        if plan is not None:
            outline.pop('script_improve_undo', None)
            if undo.get('audit'):
                outline['script_audit'] = undo['audit']
                plan.outline_json = json.dumps(outline, ensure_ascii=False)
            else:
                outline.pop('script_audit', None)
                plan.outline_json = json.dumps(outline, ensure_ascii=False)
            db.commit()
            log.info('[ai_studio] hoàn tác cải thiện kịch bản ' + str(video_id))
            return {script: segments, audit: undo.get('audit')}
        else:
            log.info('[ai_studio] hoàn tác cải thiện kịch bản ' + str(video_id))
            return {script: segments, audit: undo.get('audit')}



# Original qualified name: _apply_scene_prompt_contract
def _apply_scene_prompt_contract(db, video_id, prompt):
    app = __import__('app.pipeline.steps.storyboard', fromlist=(
        '_apply_visual_policy_flags', '_append_visual_guardrails',
        '_ensure_style_contract', '_normalize_prompt_aspect'), level=0)
    _apply_visual_policy_flags = app._apply_visual_policy_flags
    _append_visual_guardrails = app._append_visual_guardrails
    _ensure_style_contract = app._ensure_style_contract
    _normalize_prompt_aspect = app._normalize_prompt_aspect
    video = db.get(Video, video_id)
    if video:
        cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id ==
            video.project_id).first()
    else:
        cfg = None
    if cfg:
        if cfg.engine_id:
            engine = channel_engines.get_engine(cfg.engine_id)
        else:
            engine = None
    else:
        engine = None
    if cfg:
        if cfg.language:
            language = cfg.language
        else:
            language = 'vi'
    else:
        language = 'vi'
    fmt_key = _idea_format_for_video(db, video_id)
    if fmt_key:
        aspect = vfmt.resolve(fmt_key).aspect
    else:
        aspect = None
    if aspect not in ('16:9', '9:16'):
        if engine:
            __temp_267129 = engine.meta.get('aspect_ratio')
        if not __temp_267129:
            aspect = '16:9'
        else:
            aspect = __temp_267129
    text = _ensure_style_contract(prompt, engine, lang='en')
    if engine is not None:
        text = _append_visual_guardrails(text, engine)
    return _apply_visual_policy_flags(_normalize_prompt_aspect(text, aspect),
        language)



# NOT DECOMPILED: update_scene


# NOT DECOMPILED: regenerate_scene


# NOT DECOMPILED: regenerate_scene_image


# NOT DECOMPILED: regenerate_scene_clip


# Original qualified name: _idea_format_for_video
def _idea_format_for_video(db, video_id):
    idea = db.query(IdeaCard).filter(IdeaCard.video_id == video_id).first()
    if not idea:
        return None
    payload = _loads(idea.payload_json, {})
    __temp_267196 = payload.get('format')
    if not __temp_267196:
        return vfmt.normalize(payload.get('aspect'))
    else:
        return vfmt.normalize(__temp_267196)



# NOT DECOMPILED: _idea_duration_for_video


# Original qualified name: _apply_idea_format
def _apply_idea_format(config, value, est_duration_sec):
    if vfmt.normalize(value) is None:
        return None
    fmt = vfmt.resolve(value)
    config['aspect'] = fmt.aspect
    config['video_format'] = fmt.key
    if fmt.key == 'short':
        owner_sec = config.get('short_target_sec')
    else:
        owner_sec = config.get('long_target_sec')
    if owner_sec is not None:
        config['target_sec'] = owner_sec
    elif est_duration_sec:
        config['target_sec'] = est_duration_sec
    elif fmt.target_sec is not None:
        config['target_sec'] = fmt.target_sec
    if fmt.hard_cap_sec is not None:
        if fmt.key == 'short':
            if config.get('short_target_sec') is not None:
                config['hard_cap_sec'] = config['short_target_sec'] + 10
            else:
                config['hard_cap_sec'] = fmt.hard_cap_sec
        else:
            config['hard_cap_sec'] = fmt.hard_cap_sec
        return None
    return None



# Original qualified name: _cast_from_payload
def _cast_from_payload(payload):
    cast = []
    if not payload.get('characters'):
        __temp_267217 = []
    for __temp_267218 in iter(__temp_267217):
        c = __temp_267218
        if isinstance(c, dict):
            __temp_267220 = c.get('name')
            if not __temp_267220:
                __temp_267222 = str('').strip()
            else:
                str(__temp_267220).strip()
            if not __temp_267222:
                continue
                ref = c.get('ref_path')
            else:
                ref = c.get('ref_path')
        else:
            continue
            ref = c.get('ref_path')
        __temp_267228 = c.get('character_id')
        __temp_267230 = str(c['name']).strip()
        __temp_267231 = c.get('description')
        if not __temp_267231:
            __temp_267233 = str('').strip()
            __temp_267234 = c.get('source')
        else:
            str(__temp_267231).strip()
            c.get('source')
        if not __temp_267234:
            __temp_267238 = c.get('is_main')
            __temp_267239 = c.get('role')
        else:
            c.get('is_main')
            c.get('role')
        if not __temp_267239:
            __temp_267243 = str('').strip()
            __temp_267244 = c.get('aliases')
        else:
            str(__temp_267239).strip()
            c.get('aliases')
        if not __temp_267244:
            __temp_267249 = list([])
            __temp_267250 = c.get('chapters')
        else:
            list(__temp_267244)
            c.get('chapters')
        if not __temp_267250:
            __temp_267254 = list([])
            __temp_267255 = c.get('flow_asset_id')
        else:
            list(__temp_267250)
            c.get('flow_asset_id')
        if ref:
            cast.append({character_id: __temp_267228, name: __temp_267230,
                description: __temp_267233, ref_path: ref, source: 'video',
                is_main: __temp_267238 is True, role: __temp_267243, aliases:
                __temp_267249, chapters: __temp_267254, flow_asset_id:
                __temp_267255, status: 'ready'})
        else:
            cast.append({character_id: __temp_267228, name: __temp_267230,
                description: __temp_267233, ref_path: ref, source: 'video',
                is_main: __temp_267238 is True, role: __temp_267243, aliases:
                __temp_267249, chapters: __temp_267254, flow_asset_id:
                __temp_267255, status: 'pending'})
        continue
    return cast



# NOT DECOMPILED: _loads


# NOT DECOMPILED: _clamp_int


# NOT DECOMPILED: upload_scene_asset
