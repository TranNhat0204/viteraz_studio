# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/brand_kit_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _to_dict


# Original qualified name: _normalize
def _normalize(kit_json):
    if not kit_json:
        __temp_268348 = {}.get('config')
    else:
        kit_json.get('config')
    if not __temp_268348:
        __temp_268351 = sanitize_config({})
    else:
        sanitize_config(__temp_268348)
    if not kit_json:
        __temp_268354 = {}.get('thumbnail')
    else:
        kit_json.get('thumbnail')
    if not __temp_268354:
        return {config: __temp_268351, thumbnail: {}}
    else:
        return {config: __temp_268351, thumbnail: __temp_268354}



# NOT DECOMPILED: list_kits


# Original qualified name: get_kit
def get_kit(db, kit_id):
    k = db.get(BrandKit, kit_id)
    if not k:
        raise StudioError(E.UNKNOWN, 'Brand Kit không tồn tại', status_code=404)
    return k



# Original qualified name: create_kit
def create_kit(db, name, kit_json):
    if not name:
        name = ''.strip()
    else:
        name = name.strip()
    if not name:
        raise StudioError(E.UNKNOWN, 'Tên Brand Kit không được rỗng',
            status_code=422)
    if db.scalar(select(BrandKit).where(BrandKit.name == name)):
        raise StudioError(E.UNKNOWN, "Đã tồn tại Brand Kit '" + str(name) + "'",
            status_code=409)
    k = BrandKit(name=name, kit_json=json.dumps(_normalize(kit_json),
        ensure_ascii=False))
    db.add(k)
    db.commit()
    db.refresh(k)
    return _to_dict(k)



# Original qualified name: update_kit
def update_kit(db, kit_id, name, kit_json):
    k = get_kit(db, kit_id)
    if name:
        if name.strip():
            k.name = name.strip()
    if kit_json is not None:
        k.kit_json = json.dumps(_normalize(kit_json), ensure_ascii=False)
    db.commit()
    db.refresh(k)
    return _to_dict(k)



# Original qualified name: delete_kit
def delete_kit(db, kit_id):
    db.delete(get_kit(db, kit_id))
    db.commit()
    return None



# Original qualified name: create_from_video
def create_from_video(db, video, name):
    kit_json = {config: vsvc.get_video_config(video), thumbnail: psvc.
        get_thumbnail_config(video.project)}
    return create_kit(db, name, kit_json)



# Original qualified name: apply_kit
def apply_kit(db, kit, videos, project):
    data = _to_dict(kit)
    cfg = data['config']
    updated = []
    for __temp_268399 in iter(videos):
        v = __temp_268399
        __temp_268402 = {}
        __temp_268402.update(vsvc.get_video_config(v))
        __temp_268403 = __temp_268402
        __temp_268403.update(cfg)
        merged = __temp_268403
        vsvc.set_video_config(db, v, merged)
        updated.append(v.id)
        continue
    if project is not None:
        if data['thumbnail']:
            psvc.set_thumbnail_config(db, project, data['thumbnail'])
            return updated
        else:
            return updated
    else:
        return updated



# Original qualified name: apply_active_kit_to_video
def apply_active_kit_to_video(db, project, video):
    kit_id = psvc.get_active_brand_kit_id(project)
    if not kit_id:
        return False
    kit = db.get(BrandKit, kit_id)
    if not kit:
        return False
    data = _to_dict(kit)
    if data['config']:
        __temp_268412 = {}
        __temp_268412.update(vsvc.get_video_config(video))
        __temp_268413 = __temp_268412
        __temp_268413.update(data['config'])
        vsvc.set_video_config(db, video, __temp_268413)
    if data['thumbnail']:
        psvc.set_thumbnail_config(db, project, data['thumbnail'])
        return True
    else:
        return True

