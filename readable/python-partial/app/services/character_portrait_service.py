# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/character_portrait_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _slug
def _slug(s, n):
    return _slugify(s, n, default='char')



# Original qualified name: _norm_name
def _norm_name(s):
    if not s:
        return ''.strip().lower()
    else:
        return s.strip().lower()



# NOT DECOMPILED: _loads


# NOT DECOMPILED: _is_real_file


# Original qualified name: normalize_mode
def normalize_mode(raw):
    if not raw:
        mode = str('').strip().lower()
    else:
        mode = str(raw).strip().lower()
    if mode in MODES:
        return mode
    return MODE_AUTO



# Original qualified name: uses_reference
def uses_reference(mode):
    return normalize_mode(mode) in (MODE_REFERENCE, MODE_REFERENCE_SOFT)



# Original qualified name: channel_mode
def channel_mode(db, project_id):
    cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id == project_id
        ).first()
    if cfg:
        profile = _loads(cfg.channel_profile_json, {})
    else:
        profile = {}
    return normalize_mode(profile.get('character_image_mode'))



# Original qualified name: save_ext
def save_ext(filename):
    if not filename:
        ext = ''.rsplit('.', 1)[-1].lower()
    else:
        ext = filename.rsplit('.', 1)[-1].lower()
    if ext in _ALLOWED_EXT:
        return ext
    return 'png'



# Original qualified name: portrait_status
def portrait_status(ch):
    __temp_269529 = ch.get('ref_path')
    if not __temp_269529:
        __temp_269531 = _is_real_file(ch.get('flow_ref_path'))
    else:
        _is_real_file(__temp_269529)
    if __temp_269531:
        return ST_READY
    if _is_real_file(ch.get('ref_source_path')):
        return ST_REFERENCE_READY
    return ST_NEEDS_REFERENCE



# Original qualified name: decorate_cast
def decorate_cast(cast):
    for __temp_269535 in iter(cast):
        ch = __temp_269535
        if not isinstance(ch, dict):
            continue
            ch['portrait_status'] = portrait_status(ch)
        else:
            ch['portrait_status'] = portrait_status(ch)
        ch['has_reference'] = _is_real_file(ch.get('ref_source_path'))
        continue
    return cast



# NOT DECOMPILED: resolve_portraits


# Original qualified name: char_extra
def char_extra(c):
    ch = {ref_path: c.ref_image_path, ref_source_path: c.ref_source_path}
    return {ref_source_path: c.ref_source_path, has_reference: _is_real_file(c.
        ref_source_path), portrait_status: portrait_status(ch)}



# Original qualified name: _channel_context
def _channel_context(project_id):
    with SessionLocal() as __temp_269604:
        db = __temp_269604
        project = db.get(Project, project_id)
        cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id ==
            project_id).first()
        if cfg:
            engine_id = cfg.engine_id
        else:
            engine_id = None
        if cfg:
            profile = _loads(cfg.channel_profile_json, {})
        else:
            profile = {}
        if project:
            project_default = _loads(project.default_config, {})
        else:
            project_default = {}
        __temp_269615 = profile.get('language')
        if not __temp_269615:
            __temp_269616 = getattr(cfg, 'language', None)
            if not __temp_269616:
                __temp_269617 = project_default.get('language')
                if not __temp_269617:
                    lang = str('vi')
                else:
                    lang = str(__temp_269617)
            else:
                lang = str(__temp_269616)
        else:
            lang = str(__temp_269615)
        __temp_269622 = profile.get('image_provider')
        if not __temp_269622:
            __temp_269623 = project_default.get('image_provider')
            if not __temp_269623:
                provider = str('flow').lower()
            else:
                provider = str(__temp_269623).lower()
        else:
            provider = str(__temp_269622).lower()
        if provider == 'chatgpt_grok':
            provider = 'chatgpt'
        if provider not in frozenset({'chatgpt', 'flow', 'stock', 'grok', 'meta'}):
            provider = 'flow'
        if engine_id:
            engine = channel_engines.get_engine(engine_id)
        else:
            engine = None
        if project:
            __temp_269632 = normalize_mode(profile.get('character_image_mode'))
            __temp_269633 = profile.get('format')
        else:
            normalize_mode(profile.get('character_image_mode'))
            profile.get('format')
        if not __temp_269633:
            __temp_269637 = profile.get('aspect')
            if not __temp_269637:
                {engine: engine, provider: provider, lang: lang, root: project.
                    root_path, mode: __temp_269632, aspect: channel_engines.
                    portrait_aspect(engine, project_default.get('format'))}
            else:
                {engine: engine, provider: provider, lang: lang, root: project.
                    root_path, mode: __temp_269632, aspect: channel_engines.
                    portrait_aspect(engine, __temp_269637)}
        else:
            {engine: engine, provider: provider, lang: lang, root: project.
                root_path, mode: __temp_269632, aspect: channel_engines.
                portrait_aspect(engine, __temp_269633)}



# NOT DECOMPILED: stylize_portrait


# NOT DECOMPILED: _video_context


# Original qualified name: video_characters_dir
def video_characters_dir(root, video_id):
    d = ProjectFS(root).video_dir(video_id) / 'characters'
    d.mkdir(parents=True, exist_ok=True)
    return d



# Original qualified name: get_video_cast
def get_video_cast(db, video_id):
    __temp_269694, __temp_269695, __temp_269696 = _video_context(db, video_id)
    _ = __temp_269694
    _ = __temp_269695
    cast = __temp_269696
    return decorate_cast(cast)



# NOT DECOMPILED: _write_video_cast


# Original qualified name: _pick
def _pick(cast, index):
    if 0 <= index:
        if not index < len(cast):
            raise StudioError(E.UNKNOWN,
                'Nhân vật không tồn tại trong video này.', status_code=404)
    else:
        raise StudioError(E.UNKNOWN, 'Nhân vật không tồn tại trong video này.',
            status_code=404)
    return cast[index]



# Original qualified name: set_video_reference
def set_video_reference(db, video_id, index, data, filename):
    if not data:
        raise StudioError(E.UNKNOWN, 'File ảnh rỗng.', status_code=422)
    __temp_269745, __temp_269746, __temp_269747 = _video_context(db, video_id)
    _ = __temp_269745
    project = __temp_269746
    cast = __temp_269747
    ch = _pick(cast, index)
    out_dir = video_characters_dir(project.root_path, video_id)
    __temp_269750 = ch.get('name')
    if not __temp_269750:
        stem = str(index) + '_' + str(_slug('char' + str(index)))
    else:
        stem = str(index) + '_' + str(_slug(__temp_269750))
    for __temp_269753 in iter(_ALLOWED_EXT):
        ext = __temp_269753
        old = out_dir / str(stem) + '_src.' + str(ext)
        if not old.exists():
            continue
            old.unlink(missing_ok=True)
        else:
            old.unlink(missing_ok=True)
        continue
    out = out_dir / str(stem) + '_src.' + str(save_ext(filename))
    out.write_bytes(data)
    ch['ref_source_path'] = str(out.resolve())
    _write_video_cast(db, video_id, cast)
    log.info('[char_portrait] video ' + str(video_id[None:8]) +
        ": nhận ảnh tham chiếu cho '" + str(ch.get('name')) + "' → " + str(out.
        name))
    return decorate_cast(cast)[index]



# Original qualified name: set_video_portrait
def set_video_portrait(db, video_id, index, data, filename):
    if not data:
        raise StudioError(E.UNKNOWN, 'File ảnh rỗng.', status_code=422)
    __temp_269767, __temp_269768, __temp_269769 = _video_context(db, video_id)
    _ = __temp_269767
    project = __temp_269768
    cast = __temp_269769
    ch = _pick(cast, index)
    out_dir = video_characters_dir(project.root_path, video_id)
    __temp_269772 = ch.get('name')
    if not __temp_269772:
        stem = str(index) + '_' + str(_slug('char' + str(index))) + '_upload'
    else:
        stem = str(index) + '_' + str(_slug(__temp_269772)) + '_upload'
    for __temp_269775 in iter(_ALLOWED_EXT):
        ext = __temp_269775
        old = out_dir / str(stem) + '.' + str(ext)
        if not old.exists():
            continue
            old.unlink(missing_ok=True)
        else:
            old.unlink(missing_ok=True)
        continue
    out = out_dir / str(stem) + '.' + str(save_ext(filename))
    out.write_bytes(data)
    resolved = str(out.resolve())
    ch['ref_path'] = resolved
    ch['flow_ref_path'] = resolved
    ch['status'] = 'ready'
    ch['has_image'] = True
    ch['source'] = 'user'
    ch.pop('portrait_mode', None)
    ch.pop('flow_asset_id', None)
    ch.pop('entity_id', None)
    __temp_269786 = ch.get('character_id')
    if not __temp_269786:
        cid = str('')
    else:
        cid = str(__temp_269786)
    if cid:
        row = db.get(Character, cid)
        if row is not None:
            row.ref_image_path = resolved
            row.flow_asset_id = None
            row.source = 'user'
    _write_video_cast(db, video_id, cast)
    log.info('[char_portrait] video ' + str(video_id[None:8]) +
        ": user thay chân dung '" + str(ch.get('name')) + "' → " + str(out.name))
    return decorate_cast(cast)[index]



# Original qualified name: clear_video_reference
def clear_video_reference(db, video_id, index):
    __temp_269795, __temp_269796, __temp_269797 = _video_context(db, video_id)
    _ = __temp_269795
    project = __temp_269796
    cast = __temp_269797
    ch = _pick(cast, index)
    __temp_269799 = ch.pop('ref_source_path', '')
    if not __temp_269799:
        old = str('')
    else:
        old = str(__temp_269799)
    if old:
        Path(old).unlink(missing_ok=True)
        _write_video_cast(db, video_id, cast)
        return decorate_cast(cast)[index]
    else:
        _write_video_cast(db, video_id, cast)
        return decorate_cast(cast)[index]



# Original qualified name: video_reference_path
def video_reference_path(db, video_id, index):
    __temp_269809, __temp_269810, __temp_269811 = _video_context(db, video_id)
    _ = __temp_269809
    project = __temp_269810
    cast = __temp_269811
    ch = _pick(cast, index)
    __temp_269813 = ch.get('ref_source_path')
    if not __temp_269813:
        raw = str('').strip()
    else:
        raw = str(__temp_269813).strip()
    if not raw:
        raise StudioError(E.UNKNOWN, 'Nhân vật chưa có ảnh tham chiếu',
            status_code=404)
    root = Path(project.root_path).resolve()
    p = Path(raw).resolve()
    if root not in p.parents:
        raise StudioError(E.UNKNOWN, 'Đường dẫn ảnh không hợp lệ', status_code=400)
    if not p.exists():
        raise StudioError(E.UNKNOWN, 'File ảnh tham chiếu không tồn tại',
            status_code=404)
    return p



# NOT DECOMPILED: stylize_video_character


# Original qualified name: _character_or_404
def _character_or_404(db, character_id):
    c = db.get(Character, character_id)
    if c is None:
        raise StudioError(E.UNKNOWN, 'Nhân vật không tồn tại', status_code=404)
    return c



# Original qualified name: set_channel_reference
def set_channel_reference(db, character_id, data, filename):
    if not data:
        raise StudioError(E.UNKNOWN, 'File ảnh rỗng.', status_code=422)
    c = _character_or_404(db, character_id)
    project = db.get(Project, c.project_id)
    if project is not None:
        if not project.root_path:
            raise StudioError(E.UNKNOWN, 'Kênh không còn thư mục lưu trữ.',
                status_code=400)
    else:
        raise StudioError(E.UNKNOWN, 'Kênh không còn thư mục lưu trữ.',
            status_code=400)
    out_dir = ProjectFS(project.root_path).characters_dir()
    stem = _slug(c.name)
    for __temp_269859 in iter(_ALLOWED_EXT):
        ext = __temp_269859
        old = out_dir / str(stem) + '_src.' + str(ext)
        if not old.exists():
            continue
            old.unlink(missing_ok=True)
        else:
            old.unlink(missing_ok=True)
        continue
    out = out_dir / str(stem) + '_src.' + str(save_ext(filename))
    out.write_bytes(data)
    c.ref_source_path = str(out.resolve())
    db.commit()
    db.refresh(c)
    log.info('[char_portrait] kênh ' + str(c.project_id) +
        ": nhận ảnh tham chiếu cho '" + str(c.name) + "' → " + str(out.name))
    return c



# Original qualified name: clear_channel_reference
def clear_channel_reference(db, character_id):
    c = _character_or_404(db, character_id)
    if c.ref_source_path:
        Path(c.ref_source_path).unlink(missing_ok=True)
        c.ref_source_path = None
    else:
        c.ref_source_path = None
    db.commit()
    db.refresh(c)
    return c



# Original qualified name: channel_reference_path
def channel_reference_path(db, character_id):
    c = _character_or_404(db, character_id)
    project = db.get(Project, c.project_id)
    if not c.ref_source_path:
        raw = str('').strip()
    else:
        raw = str(c.ref_source_path).strip()
    if raw:
        if project is not None:
            if not project.root_path:
                raise StudioError(E.UNKNOWN, 'Nhân vật chưa có ảnh tham chiếu',
                    status_code=404)
        else:
            raise StudioError(E.UNKNOWN, 'Nhân vật chưa có ảnh tham chiếu',
                status_code=404)
    else:
        raise StudioError(E.UNKNOWN, 'Nhân vật chưa có ảnh tham chiếu',
            status_code=404)
    root = Path(project.root_path).resolve()
    p = Path(raw).resolve()
    if root not in p.parents:
        raise StudioError(E.UNKNOWN, 'Đường dẫn ảnh không hợp lệ', status_code=400)
    if not p.exists():
        raise StudioError(E.UNKNOWN, 'File ảnh tham chiếu không tồn tại',
            status_code=404)
    return p



# NOT DECOMPILED: stylize_channel_character


# NOT DECOMPILED: run_portrait_job


# Original qualified name: run_portrait_job.<locals>.checkpoint
def checkpoint(pct):
    nonlocal cancel_check, progress
    if cancel_check:
        if cancel_check():
            raise StudioError(E.CANCELLED, 'Đã huỷ vẽ chân dung nhân vật.')
    if progress:
        progress(pct)
        return None
    return None



# Original qualified name: resume_thumbnail_if_cast_ready
def resume_thumbnail_if_cast_ready(video_id):
    _maybe_resume_thumbnail(video_id)
    return None



# NOT DECOMPILED: _idea_has_real_thumbnail


# NOT DECOMPILED: _maybe_resume_thumbnail


# NOT DECOMPILED: cast_portrait_gate


# Original qualified name: _missing_message
def _missing_message(missing, total, mode):
    __temp_269981 = ', '.join(missing[None:6])
    if len(missing) > 6:
        names = __temp_269981 + '…'
    else:
        names = __temp_269981 + ''
    head = 'Còn ' + str(len(missing)) + '/' + str(total
        ) + ' nhân vật chưa có ảnh: ' + str(names) + '. '
    if uses_reference(mode):
        return (head +
            'Vui lòng vào tab Nhân vật để tải ảnh tham chiếu rồi bấm “Vẽ theo phong cách kênh” (hoặc “Để AI tự vẽ”).'
            )
    return head + 'Vui lòng vào tab Nhân vật để tạo nhân vật — bấm “🎨 Vẽ lại” để AI vẽ, hoặc “Tải ảnh lên” nếu bạn đã có ảnh sẵn.'



# Original qualified name: require_portraits
def require_portraits(db, video_id):
    gate = cast_portrait_gate(db, video_id)
    if not gate['blocking']:
        return None
    raise StudioError(E.PRECONDITION_MISSING, _missing_message(gate['missing'],
        gate['total'], gate['mode']), status_code=409)



# Original qualified name: require_portraits_before_scenes
def require_portraits_before_scenes(video_id):
    _require_full_cast(video_id, 'tạo cảnh')
    return None



# Original qualified name: require_portraits_before_storyboard
def require_portraits_before_storyboard(video_id):
    _require_full_cast(video_id, 'storyboard')
    return None



# Original qualified name: _require_full_cast
def _require_full_cast(video_id, where):
    with SessionLocal() as __temp_269991:
        db = __temp_269991
        gate = cast_portrait_gate(db, video_id)
        if not gate['blocking']:
            return None
        log.warning('[char_portrait] video ' + str(video_id[None:8]) +
            ': chặn ' + str(where) + ' — thiếu chân dung ' + str(gate['missing']))
        raise StudioError(E.PRECONDITION_MISSING, _missing_message(gate[
            'missing'], gate['total'], gate['mode']), status_code=409)



# Original qualified name: require_portraits_in_pipeline
def require_portraits_in_pipeline(video_id, cast):
    __temp_269997 = SessionLocal()
    with __temp_269997 as __temp_269998:
        db = __temp_269998
        video = db.get(Video, video_id)
        if video is not None:
            if not uses_reference(channel_mode(db, video.project_id)):
                return None
        else:
            return None
        __temp_270005 = []
        for __temp_270006 in iter(cast):
            c = __temp_270006
            if isinstance(c, dict):
                if portrait_status(c) != ST_READY:
                    __temp_270009 = c.get('name')
                    if not __temp_270009:
                        __temp_270005.append(str('?'))
                    else:
                        __temp_270005.append(str(__temp_270009))
                    continue
                else:
                    continue
            else:
                continue
        missing = __temp_270005
        if not missing:
            return None
        log.warning('[char_portrait] video ' + str(video_id[None:8]) +
            ': chặn tạo hình — thiếu chân dung ' + str(missing))
        raise StudioError(E.PRECONDITION_MISSING, _missing_message(missing, len
            (cast)), status_code=409)
    c = __temp_269997

