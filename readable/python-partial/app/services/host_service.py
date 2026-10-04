# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/host_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _norm_name
def _norm_name(s):
    if not s:
        return ''.strip().lower()
    else:
        return s.strip().lower()



# Original qualified name: _get_config
def _get_config(db, project_id):
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



# NOT DECOMPILED: _load_profile


# Original qualified name: _save_profile
def _save_profile(db, cfg, profile):
    if profile:
        cfg.channel_profile_json = json.dumps(profile, ensure_ascii=False)
    else:
        cfg.channel_profile_json = None
    db.commit()
    return None



# Original qualified name: get_host_id
def get_host_id(db, project_id):
    cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id == project_id
        ).first()
    if cfg is None:
        return None
    __temp_272977 = _load_profile(cfg).get(_HOST_KEY)
    if not __temp_272977:
        return None
    else:
        return __temp_272977



# Original qualified name: get_host
def get_host(db, project_id):
    hid = get_host_id(db, project_id)
    if not hid:
        cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id ==
            project_id).first()
        if cfg is not None:
            if _load_profile(cfg).get(_HOST_MIGRATION_KEY):
                return None
        legacy = db.query(Character).filter(Character.project_id == project_id,
            Character.name.ilike('host'), Character.ref_image_path.isnot(None),
            Character.source.in_(('user', 'import', 'uploaded'))).order_by(
            Character.created_at.asc()).all()
        if len(legacy) == 1:
            set_host_id(db, project_id, legacy[0].id)
            log.info('[host] tự phục hồi host legacy cho kênh ' + str(
                project_id) + ': ' + str(legacy[0].id[None:8]))
            return legacy[0]
        return None
    c = db.get(Character, hid)
    if c is not None:
        if c.project_id != project_id:
            clear_host(db, project_id)
            return None
    else:
        clear_host(db, project_id)
        return None
    if not c.enabled:
        log.info('[host] kênh ' + str(project_id) + ": host '" + str(c.name) +
            "' đang bị tắt trong thư viện → bỏ qua.")
        return None
    return c



# Original qualified name: get_host_role
def get_host_role(db, project_id):
    cfg = db.query(ScheduleConfig).filter(ScheduleConfig.project_id == project_id
        ).first()
    if cfg is None:
        return ROLE_NARRATOR
    return normalize_role(_load_profile(cfg).get(_ROLE_KEY))



# Original qualified name: normalize_role
def normalize_role(raw):
    if not raw:
        role = str('').strip().lower()
    else:
        role = str(raw).strip().lower()
    if role in ROLES:
        return role
    return ROLE_NARRATOR



# NOT DECOMPILED: host_info_dict


# NOT DECOMPILED: cast_without_host


# Original qualified name: merge_host_into_cast
def merge_host_into_cast(cast, host_info, extra):
    out = cast_without_host(cast, host_info)
    if host_info:
        __temp_273037 = {}
        __temp_273037.update(host_info)
        if not extra:
            __temp_273039 = __temp_273037
            __temp_273039.update({})
            out.insert(0, __temp_273039)
            return out
        else:
            __temp_273041 = __temp_273037
            __temp_273041.update(extra)
            out.insert(0, __temp_273041)
            return out
    else:
        return out



# Original qualified name: ensure_host_in_cast
def ensure_host_in_cast(db, project_id, cast):
    if not project_id:
        return cast
    host = get_host(db, project_id)
    if host is None:
        return cast
    return merge_host_into_cast(cast, host_info_dict(host, role=get_host_role(
        db, project_id)))



# Original qualified name: set_host_id
def set_host_id(db, project_id, character_id):
    cfg = _get_config(db, project_id)
    profile = _load_profile(cfg)
    if character_id:
        profile[_HOST_KEY] = character_id
        profile[_HOST_MIGRATION_KEY] = True
    else:
        profile.pop(_HOST_KEY, None)
        profile[_HOST_MIGRATION_KEY] = True
    _save_profile(db, cfg, profile)
    return None



# Original qualified name: clear_host
def clear_host(db, project_id):
    set_host_id(db, project_id, None)
    return None



# Original qualified name: select_existing_host
def select_existing_host(db, project_id, character_id):
    c = db.get(Character, character_id)
    if c is not None:
        if c.project_id != project_id:
            raise StudioError(E.UNKNOWN, 'Nhân vật không thuộc kênh này.',
                status_code=404)
    else:
        raise StudioError(E.UNKNOWN, 'Nhân vật không thuộc kênh này.',
            status_code=404)
    if not c.ref_image_path:
        raise StudioError(E.PRECONDITION_MISSING,
            'Hãy tải ảnh nhân vật trước khi đặt làm host.', status_code=422)
    set_host_id(db, project_id, c.id)
    return c



# Original qualified name: promote_video_character
def promote_video_character(db, video_id, index):
    app = __import__('app.services', fromlist=('character_service',), level=0)
    character_service = app.character_service
    app = __import__('app.services', fromlist=('character_portrait_service',),
        level=0)
    character_portrait_service = app.character_portrait_service
    portraits = character_portrait_service
    __temp_273058, __temp_273059, __temp_273060 = portraits._video_context(db,
        video_id)
    _ = __temp_273058
    project = __temp_273059
    cast = __temp_273060
    if 0 <= index:
        if not index < len(cast):
            raise StudioError(E.UNKNOWN,
                'Nhân vật không tồn tại trong video này.', status_code=404)
    else:
        raise StudioError(E.UNKNOWN, 'Nhân vật không tồn tại trong video này.',
            status_code=404)
    ch = cast[index]
    if portraits.portrait_status(ch) != portraits.ST_READY:
        __temp_273065 = ch.get('name')
        if not __temp_273065:
            raise StudioError(E.PRECONDITION_MISSING, "'" + str('Nhân vật') +
                "' chưa có chân dung thật — hãy vẽ chân dung trước khi đặt làm nhân vật đại diện kênh."
                , status_code=422)
            character_service.promote_cast_to_library(db, video_id, only=[index])
            __temp_273070, __temp_273071, __temp_273072 = portraits._video_context(
                db, video_id)
            _ = __temp_273070
        else:
            raise StudioError(E.PRECONDITION_MISSING, "'" + str(__temp_273065) +
                "' chưa có chân dung thật — hãy vẽ chân dung trước khi đặt làm nhân vật đại diện kênh."
                , status_code=422)
            character_service.promote_cast_to_library(db, video_id, only=[index])
            __temp_273077, __temp_273078, __temp_273079 = portraits._video_context(
                db, video_id)
            _ = __temp_273077
    character_service.promote_cast_to_library(db, video_id, only=[index])
    __temp_273083, __temp_273084, __temp_273085 = portraits._video_context(db,
        video_id)
    _ = __temp_273083
    _ = __temp_273084
    cast = __temp_273085
    __temp_273086 = cast[index].get('character_id')
    if not __temp_273086:
        cid = str('')
    else:
        cid = str(__temp_273086)
    if cid:
        row = db.get(Character, cid)
    else:
        row = None
    if row is None:
        raise StudioError(E.UNKNOWN,
            'Không nhấc được nhân vật lên thư viện kênh.', status_code=500)
    host = select_existing_host(db, project.id, row.id)
    log.info('[host] kênh ' + str(project.id) + ": đặt '" + str(host.name) +
        "' (từ video " + str(video_id[None:8]) + ') làm nhân vật đại diện kênh.')
    return host



# Original qualified name: host_to_dict
def host_to_dict(c, role):
    if c is None:
        return None
    d = character_service.char_to_dict(c)
    d['is_host'] = True
    d['role'] = normalize_role(role)
    d['locked'] = True
    d['is_placeholder'] = is_placeholder(c.ref_image_path)
    return d



# Original qualified name: set_host_from_character
def set_host_from_character(db, project_id, name, description, ref_image_path, source):
    existing = get_host(db, project_id)
    if existing is not None:
        fields = {'source': source}
        if name:
            fields['name'] = name
        if description:
            fields['description'] = description
        if ref_image_path:
            fields['ref_image_path'] = ref_image_path
        character_service.update_character(db, existing.id, fields)
        db.refresh(existing)
        return existing
    if not name:
        __temp_273100 = 'Host'.strip()
    else:
        name.strip()
    if not description:
        c = character_service.create_character(db, project_id, name=
            __temp_273100, description='', ref_image_path=ref_image_path,
            source=source)
    else:
        c = character_service.create_character(db, project_id, name=
            __temp_273100, description=description, ref_image_path=
            ref_image_path, source=source)
    set_host_id(db, project_id, c.id)
    return c



# Original qualified name: set_host_role
def set_host_role(db, project_id, role):
    role = normalize_role(role)
    cfg = _get_config(db, project_id)
    profile = _load_profile(cfg)
    profile[_ROLE_KEY] = role
    _save_profile(db, cfg, profile)
    log.info('[host] kênh ' + str(project_id) + ': vai host = ' + str(role) + '.')
    return role



# NOT DECOMPILED: update_host_fields


# NOT DECOMPILED: _rename_host_in_pending_casts


# NOT DECOMPILED: generate_host
