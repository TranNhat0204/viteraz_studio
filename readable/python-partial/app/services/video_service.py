# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/video_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: detect_platform
def detect_platform(url):
    value = url.lower()
    if not 'douyin.com' in value:
        if 'iesdouyin' in value:
            return douyin
    else:
        return douyin
    if 'tiktok.com' in value:
        return tiktok
    if not 'youtube.com' in value:
        if 'youtu.be' in value:
            return youtube
    else:
        return youtube
    if not 'bilibili.com' in value:
        if 'b23.tv' in value:
            return bilibili
    else:
        return bilibili
    return None



# Original qualified name: parse_urls
def parse_urls(raw):
    valid = []
    invalid = []
    seen = set()
    for __temp_277159 in iter(raw):
        item = __temp_277159
        for __temp_277162 in iter(re.split('[\\s,]+', item.strip())):
            token = __temp_277162
            if not token:
                continue
                __temp_277163 = _URL_RE.match(token)
            else:
                _URL_RE.match(token)
            if not __temp_277163:
                invalid.append(token)
                continue
                platform = detect_platform(token)
            else:
                platform = detect_platform(token)
            if not platform:
                invalid.append(token)
                continue
            if not token not in seen:
                continue
                seen.add(token)
                valid.append(ParsedUrl(url=token, platform=platform))
            else:
                seen.add(token)
                valid.append(ParsedUrl(url=token, platform=platform))
            continue
        continue
    return valid, invalid



# Original qualified name: _create_steps
def _create_steps(db, video_id, statuses):
    if not statuses:
        statuses = {}
    for __temp_277176 in iter(STEP_NAMES):
        name = __temp_277176
        status = statuses.get(name, 'pending')
        db.add(VideoStep(video_id=video_id, step_name=name, status=status))
        continue
    return None



# NOT DECOMPILED: parse_srt


# Original qualified name: parse_srt.<locals>.parse_ms
def parse_ms(t_str):
    t_str = t_str.strip().replace(',', '.')
    subparts = t_str.split(':')
    if len(subparts) == 3:
        __temp_277223, __temp_277224, __temp_277225 = subparts
        h = __temp_277223
        m = __temp_277224
        s = __temp_277225
        return int((int(h) * 3600 + int(m) * 60 + float(s)) * 1000)
    return 0



# Original qualified name: import_urls
def import_urls(db, project, urls):
    __temp_277231, __temp_277232 = parse_urls(urls)
    valid = __temp_277231
    invalid = __temp_277232
    existing = set(db.scalars(select(Video.source_url).where(Video.project_id ==
        project.id)))
    imported = []
    duplicated = []
    __temp_277244 = db.scalar(select(Video.order_index).where(Video.project_id ==
        project.id).order_by(Video.order_index.desc()).limit(1))
    if not __temp_277244:
        base_order = 0
    else:
        base_order = __temp_277244
    for __temp_277246 in iter(enumerate(valid)):
        __temp_277247, __temp_277248 = __temp_277246
        i = __temp_277247
        entry = __temp_277248
        if entry.url in existing:
            duplicated.append(entry.url)
            continue
            existing.add(entry.url)
            v = Video(project_id=project.id, source_url=entry.url, platform=
                entry.platform, overall_status='pending', order_index=
                base_order + i + 1)
        else:
            existing.add(entry.url)
            v = Video(project_id=project.id, source_url=entry.url, platform=
                entry.platform, overall_status='pending', order_index=
                base_order + i + 1)
        db.add(v)
        db.flush()
        v.folder_path = str(ProjectFS(project.root_path).name_video_dir(v.id,
            order_index=v.order_index, title=v.title))
        _create_steps(db, v.id)
        imported.append(v)
        continue
    db.commit()
    for __temp_277262 in iter(imported):
        v = __temp_277262
        db.refresh(v)
        continue
    return {imported: imported, duplicated: duplicated, invalid: invalid}



# NOT DECOMPILED: extract_thumbnail


# NOT DECOMPILED: import_local_videos


# Original qualified name: get_video
def get_video(db, video_id):
    v = db.get(Video, video_id)
    if not v:
        raise StudioError(E.VIDEO_NOT_FOUND, 'Video không tồn tại', status_code=404
            )
    return v



# NOT DECOMPILED: _load_metadata


# Original qualified name: get_video_config
def get_video_config(v):
    cfg = _load_metadata(v).get('config')
    if isinstance(cfg, dict):
        return cfg
    return {}



# Original qualified name: set_video_config
def set_video_config(db, v, config):
    meta = _load_metadata(v)
    meta['config'] = sanitize_config(config)
    v.metadata_json = json.dumps(meta, ensure_ascii=False)
    db.commit()
    return meta['config']



# Original qualified name: get_video_seo
def get_video_seo(v):
    seo = _load_metadata(v).get('seo')
    if isinstance(seo, dict):
        return seo
    return {}



# Original qualified name: set_video_seo
def set_video_seo(db, v, seo):
    meta = _load_metadata(v)
    meta['seo'] = seo
    v.metadata_json = json.dumps(meta, ensure_ascii=False)
    db.commit()
    return seo



# Original qualified name: get_video_export
def get_video_export(v):
    info = _load_metadata(v).get('export')
    if isinstance(info, dict):
        return info
    return {}



# NOT DECOMPILED: set_video_export


# Original qualified name: get_fanout_plan
def get_fanout_plan(v):
    plan = _load_metadata(v).get('fanout_plan')
    if isinstance(plan, dict):
        return plan
    return {}



# Original qualified name: set_fanout_plan
def set_fanout_plan(db, v, plan):
    meta = _load_metadata(v)
    meta['fanout_plan'] = plan
    v.metadata_json = json.dumps(meta, ensure_ascii=False)
    db.commit()
    return plan



# Original qualified name: get_fanout_child
def get_fanout_child(v):
    info = _load_metadata(v).get('fanout_child')
    if isinstance(info, dict):
        return info
    return {}



# Original qualified name: set_fanout_child
def set_fanout_child(db, v, parent_id, lang):
    meta = _load_metadata(v)
    meta['fanout_child'] = {parent_id: parent_id, lang: lang}
    v.metadata_json = json.dumps(meta, ensure_ascii=False)
    db.commit()
    return None



# NOT DECOMPILED: effective_config


# Original qualified name: list_videos
def list_videos(db, project_id):
    return list(db.scalars(select(Video).where(Video.project_id == project_id).
        order_by(Video.order_index)))



# NOT DECOMPILED: steps_of


# NOT DECOMPILED: video_to_dict
