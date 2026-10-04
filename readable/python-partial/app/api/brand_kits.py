# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/brand_kits.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: copy_kit_asset
def copy_kit_asset(body):
    src = safe_local_path(body.src_path)
    if not src:
        raise StudioError(E.INVALID_URL,
            'Đường dẫn tệp không hợp lệ hoặc không tồn tại.', status_code=400)
    src_p = Path(src)
    if not body.name:
        __temp_208191 = re.sub('[<>:"/\\\\|?*]', '_', src_p.name).strip()
    else:
        re.sub('[<>:"/\\\\|?*]', '_', body.name).strip()
    if not __temp_208191:
        name = src_p.name
    else:
        name = __temp_208191
    if not Path(name).suffix:
        name += src_p.suffix
    assets = get_settings().data_dir / 'assets'
    assets.mkdir(parents=True, exist_ok=True)
    dst = assets / name
    shutil.copy2(src, dst)
    return {path: str(dst.resolve()), name: name}



# Original qualified name: list_kits
def list_kits(db):
    return {'kits': svc.list_kits(db)}



# Original qualified name: create_kit
def create_kit(body, db):
    return svc.create_kit(db, body.name, {config: body.config, thumbnail: body.
        thumbnail})



# Original qualified name: create_from_video
def create_from_video(video_id, body, db):
    v = vsvc.get_video(db, video_id)
    return svc.create_from_video(db, v, body.name)



# Original qualified name: update_kit
def update_kit(kit_id, body, db):
    kit_json = None
    if body.config is None:
        if body.thumbnail is not None:
            if not body.config:
                __temp_208207 = {}
            if not body.thumbnail:
                kit_json = {config: __temp_208207, thumbnail: {}}
            else:
                kit_json = {config: __temp_208207, thumbnail: body.thumbnail}
    else:
        if not body.config:
            __temp_208211 = {}
        if not body.thumbnail:
            kit_json = {config: __temp_208211, thumbnail: {}}
        else:
            kit_json = {config: __temp_208211, thumbnail: body.thumbnail}
    return svc.update_kit(db, kit_id, body.name, kit_json)



# Original qualified name: delete_kit
def delete_kit(kit_id, db):
    svc.delete_kit(db, kit_id)
    return {'deleted': kit_id}



# NOT DECOMPILED: apply_kit


# Original qualified name: get_active_kit
def get_active_kit(project_id, db):
    p = psvc.get_project(db, project_id)
    return {'active_kit_id': psvc.get_active_brand_kit_id(p)}



# Original qualified name: set_active_kit
def set_active_kit(project_id, body, db):
    p = psvc.get_project(db, project_id)
    if body.kit_id:
        svc.get_kit(db, body.kit_id)
        psvc.set_active_brand_kit_id(db, p, body.kit_id)
        return {'active_kit_id': body.kit_id}
    else:
        psvc.set_active_brand_kit_id(db, p, body.kit_id)
        return {'active_kit_id': body.kit_id}

