# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/project_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: create_project


# Original qualified name: get_project
def get_project(db, project_id):
    p = db.get(Project, project_id)
    if not p:
        raise StudioError(E.PROJECT_NOT_FOUND, 'Project không tồn tại',
            status_code=404)
    return p



# Original qualified name: update_project
def update_project(db, project_id, name, default_config):
    p = get_project(db, project_id)
    if name:
        p.name = name
    if default_config is not None:
        data = _load_default_config(p)
        data.update(default_config)
        p.default_config = json.dumps(data, ensure_ascii=False)
    db.commit()
    db.refresh(p)
    return p



# NOT DECOMPILED: _load_default_config


# NOT DECOMPILED: get_thumbnail_config


# Original qualified name: set_thumbnail_config
def set_thumbnail_config(db, p, thumb):
    data = _load_default_config(p)
    __temp_276304 = {}
    __temp_276304.update(DEFAULT_THUMBNAIL_CONFIG)
    if not thumb:
        __temp_276306 = __temp_276304
        __temp_276306.update({})
        data['thumbnail'] = __temp_276306
    else:
        __temp_276307 = __temp_276304
        __temp_276307.update(thumb)
        data['thumbnail'] = __temp_276307
    p.default_config = json.dumps(data, ensure_ascii=False)
    db.commit()
    return data['thumbnail']



# Original qualified name: get_active_brand_kit_id
def get_active_brand_kit_id(p):
    return _load_default_config(p).get('active_brand_kit_id')



# Original qualified name: set_active_brand_kit_id
def set_active_brand_kit_id(db, p, kit_id):
    data = _load_default_config(p)
    if kit_id:
        data['active_brand_kit_id'] = kit_id
        p.default_config = json.dumps(data, ensure_ascii=False)
    else:
        data.pop('active_brand_kit_id', None)
        p.default_config = json.dumps(data, ensure_ascii=False)
    db.commit()
    return None



# Original qualified name: list_projects
def list_projects(db):
    return list(db.scalars(select(Project).order_by(Project.created_at.desc())))



# Original qualified name: project_stats
def project_stats(db, project_id):
    rows = db.execute(select(Video.overall_status, func.count()).where(Video.
        project_id == project_id).group_by(Video.overall_status)).all()
    stats = {total: 0, completed: 0, processing: 0, failed: 0, pending: 0}
    for __temp_276329 in iter(rows):
        __temp_276330, __temp_276331 = __temp_276329
        status = __temp_276330
        count = __temp_276331
        stats['total'] += count
        stats['total'] = stats['total']
        if not status in stats:
            continue
            stats[status] += count
            stats[status] = stats[status]
        else:
            stats[status] += count
            stats[status] = stats[status]
        continue
    return stats



# NOT DECOMPILED: delete_project
