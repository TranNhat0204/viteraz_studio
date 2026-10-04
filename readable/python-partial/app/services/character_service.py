# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/character_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _norm
def _norm(name):
    if not name:
        return ''.strip().lower()
    else:
        return name.strip().lower()



# Original qualified name: has_locked_portrait
def has_locked_portrait(ref_path):
    pathlib = __import__('pathlib', fromlist=('Path',), level=0)
    Path = pathlib.Path
    if not ref_path:
        rp = ''.strip()
    else:
        rp = ref_path.strip()
    __temp_270022 = bool(rp)
    if __temp_270022:
        __temp_270023 = is_placeholder(rp)
        if not __temp_270023:
            return Path(rp).is_file()
        else:
            return not __temp_270023
    else:
        return __temp_270022



# NOT DECOMPILED: char_to_dict


# Original qualified name: list_characters
def list_characters(db, project_id, only_enabled):
    q = db.query(Character).filter(Character.project_id == project_id)
    if only_enabled:
        q = q.filter(Character.enabled == 1)
    return q.order_by(Character.created_at.asc()).all()



# Original qualified name: get_character
def get_character(db, character_id):
    return db.get(Character, character_id)



# NOT DECOMPILED: find_by_name


# Original qualified name: create_character
def create_character(db, project_id, name, description, ref_image_path, source, flow_asset_id):
    if not name:
        __temp_270043 = ''.strip()
    else:
        name.strip()
    if not __temp_270043:
        raise StudioError(E.UNKNOWN, 'Tên nhân vật không được trống',
            status_code=422)
    existing = find_by_name(db, project_id, name)
    if existing is not None:
        if description:
            existing.description = description
        if ref_image_path:
            existing.ref_image_path = ref_image_path
        if flow_asset_id:
            existing.flow_asset_id = flow_asset_id
        db.commit()
        db.refresh(existing)
        return existing
    __temp_270049 = name.strip()
    if not description:
        c = Character(project_id=project_id, name=__temp_270049, description=
            None, ref_image_path=ref_image_path, source=source, flow_asset_id=
            flow_asset_id)
    else:
        c = Character(project_id=project_id, name=__temp_270049, description=
            description, ref_image_path=ref_image_path, source=source,
            flow_asset_id=flow_asset_id)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c



# Original qualified name: update_character
def update_character(db, character_id, fields):
    c = db.get(Character, character_id)
    if c is None:
        raise StudioError(E.UNKNOWN, 'Nhân vật không tồn tại', status_code=404)
    for __temp_270057 in iter(('name', 'description', 'ref_image_path',
        'flow_asset_id', 'source')):
        k = __temp_270057
        if not k in fields:
            continue
        if fields[k] is None:
            continue
            setattr(c, k, fields[k])
        else:
            setattr(c, k, fields[k])
        continue
    if 'enabled' in fields:
        if fields['enabled'] is not None:
            if fields['enabled']:
                c.enabled = 1
            else:
                c.enabled = 0
    db.commit()
    db.refresh(c)
    return c



# Original qualified name: delete_character
def delete_character(db, character_id):
    c = db.get(Character, character_id)
    if c is not None:
        db.delete(c)
        db.commit()
        return None
    return None



# Original qualified name: resolve_cast
def resolve_cast(db, project_id, ai_cast):
    out = []
    seen = set()
    if not ai_cast:
        __temp_270067 = []
    for __temp_270068 in iter(__temp_270067):
        item = __temp_270068
        __temp_270069 = item.get('name')
        if not __temp_270069:
            name = ''.strip()
        else:
            name = __temp_270069.strip()
        if name:
            if _norm(name) in seen:
                continue
                seen.add(_norm(name))
                __temp_270075 = item.get('description')
            else:
                seen.add(_norm(name))
                item.get('description')
        else:
            continue
            seen.add(_norm(name))
            item.get('description')
        if not __temp_270075:
            desc = ''.strip()
        else:
            desc = __temp_270075.strip()
        existing = find_by_name(db, project_id, name)
        if existing is None:
            existing = create_character(db, project_id, name=name, description=
                desc, source='ai')
            locked = has_locked_portrait(existing.ref_image_path)
        elif desc:
            if not existing.description:
                __temp_270087 = ''.strip()
            else:
                existing.description.strip()
            if not __temp_270087:
                if not has_locked_portrait(existing.ref_image_path):
                    existing.description = desc
                    db.commit()
                    db.refresh(existing)
                    locked = has_locked_portrait(existing.ref_image_path)
                else:
                    locked = has_locked_portrait(existing.ref_image_path)
            else:
                locked = has_locked_portrait(existing.ref_image_path)
        else:
            locked = has_locked_portrait(existing.ref_image_path)
        if locked:
            if not existing.description:
                out.append({character_id: existing.id, name: existing.name,
                    description: '', ref_path: existing.ref_image_path, source:
                    existing.source, flow_asset_id: existing.flow_asset_id})
            else:
                out.append({character_id: existing.id, name: existing.name,
                    description: existing.description, ref_path: existing.
                    ref_image_path, source: existing.source, flow_asset_id:
                    existing.flow_asset_id})
        elif not existing.description:
            out.append({character_id: existing.id, name: existing.name,
                description: desc, ref_path: existing.ref_image_path, source:
                existing.source, flow_asset_id: existing.flow_asset_id})
        else:
            out.append({character_id: existing.id, name: existing.name,
                description: existing.description, ref_path: existing.
                ref_image_path, source: existing.source, flow_asset_id:
                existing.flow_asset_id})
        continue
    return out



# Original qualified name: build_video_cast
def build_video_cast(ai_cast):
    out = []
    seen = set()
    if not ai_cast:
        __temp_270106 = []
    for __temp_270107 in iter(__temp_270106):
        item = __temp_270107
        __temp_270108 = item.get('name')
        if not __temp_270108:
            name = ''.strip()
        else:
            name = __temp_270108.strip()
        if name:
            if _norm(name) in seen:
                continue
                seen.add(_norm(name))
                __temp_270114 = item.get('description')
            else:
                seen.add(_norm(name))
                item.get('description')
        else:
            continue
            seen.add(_norm(name))
            item.get('description')
        if not __temp_270114:
            out.append({character_id: None, name: name, description: ''.strip(),
                ref_path: None, source: 'video', flow_asset_id: None})
        else:
            out.append({character_id: None, name: name, description:
                __temp_270114.strip(), ref_path: None, source: 'video',
                flow_asset_id: None})
        continue
    return out



# Original qualified name: promote_cast_to_library
def promote_cast_to_library(db, video_id, only):
    shutil = __import__('shutil', fromlist=None, level=0)
    pathlib = __import__('pathlib', fromlist=('Path',), level=0)
    Path = pathlib.Path
    app = __import__('app.core.fs', fromlist=('ProjectFS',), level=0)
    ProjectFS = app.ProjectFS
    app = __import__('app.core.logging', fromlist=('log',), level=0)
    log = app.log
    app = __import__('app.services', fromlist=('character_portrait_service',),
        level=0)
    character_portrait_service = app.character_portrait_service
    portraits = character_portrait_service
    __temp_270128, __temp_270129, __temp_270130 = portraits._video_context(db,
        video_id)
    _ = __temp_270128
    project = __temp_270129
    cast = __temp_270130
    out_dir = ProjectFS(project.root_path).characters_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    promoted = []
    changed = False
    for __temp_270136 in iter(enumerate(cast)):
        __temp_270137, __temp_270138 = __temp_270136
        i = __temp_270137
        ch = __temp_270138
        if only is not None:
            if i not in only:
                continue
                __temp_270139 = ch.get('name')
            else:
                ch.get('name')
        else:
            ch.get('name')
        if not __temp_270139:
            name = str('').strip()
        else:
            name = str(__temp_270139).strip()
        if not name:
            continue
            __temp_270146 = ch.get('character_id')
        else:
            ch.get('character_id')
        if not __temp_270146:
            cid = str('')
        else:
            cid = str(__temp_270146)
        if cid:
            if db.get(Character, cid) is not None:
                continue
                __temp_270151 = portraits.portrait_status(ch)
            else:
                portraits.portrait_status(ch)
        else:
            portraits.portrait_status(ch)
        if __temp_270151 != portraits.ST_READY:
            log.info('[promote] video ' + str(video_id[None:8]) + ": bỏ qua '" +
                str(name) + "' — chưa có chân dung thật.")
            continue
            __temp_270155 = ch.get('ref_path')
        else:
            ch.get('ref_path')
        if not __temp_270155:
            src = Path(str(ch.get('flow_ref_path')))
        else:
            src = Path(str(__temp_270155))
        dst = src
        if src.resolve().parent != out_dir.resolve():
            __temp_270164 = _slug(name)
            if not src.suffix:
                dst = out_dir / str(__temp_270164) + str('.png')
            else:
                dst = out_dir / str(__temp_270164) + str(src.suffix)
            shutil.copy2(src, dst)
            __temp_270166 = ch.get('description')
        else:
            ch.get('description')
        if not __temp_270166:
            row = create_character(db, project.id, name=name, description=str(
                '').strip(), ref_image_path=str(dst.resolve()), source='ai')
        else:
            row = create_character(db, project.id, name=name, description=str(
                __temp_270166).strip(), ref_image_path=str(dst.resolve()),
                source='ai')
        ch['character_id'] = row.id
        ch['scope'] = 'channel'
        ch['ref_path'] = str(dst.resolve())
        ch['flow_ref_path'] = str(dst.resolve())
        promoted.append(row)
        changed = True
        log.info('[promote] video ' + str(video_id[None:8]) + ": '" + str(name) +
            "' → thư viện kênh (" + str(dst.name) + ').')
        continue
    if changed:
        portraits._write_video_cast(db, video_id, cast)
        return promoted
    else:
        return promoted



# Original qualified name: _slug
def _slug(s, n):
    app = __import__('app.core.asset_names', fromlist=('slug',), level=0)
    slug = app.slug
    _slugify = slug
    return _slugify(s, n, default='char')



# NOT DECOMPILED: latest_video_with_cast


# NOT DECOMPILED: channel_cast_hint
