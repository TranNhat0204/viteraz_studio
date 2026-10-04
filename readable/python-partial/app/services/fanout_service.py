# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fanout_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: resolve_fanout_preset
def resolve_fanout_preset(config):
    return fanout



# Original qualified name: _child_source_url
def _child_source_url(primary, lang):
    return str(primary.source_url) + '#vlang=' + str(lang)



# Original qualified name: _child_title
def _child_title(primary, lang):
    if not primary.title:
        __temp_271438 = ''.strip()
    else:
        primary.title.strip()
    if not __temp_271438:
        base = '(video)'
    else:
        base = __temp_271438
    return str(base) + ' [' + str(lang.upper()) + ']'



# Original qualified name: _normalize_langs
def _normalize_langs(langs, primary_lang):
    out = []
    seen = {primary_lang}
    if not langs:
        __temp_271443 = []
    for __temp_271444 in iter(__temp_271443):
        l = __temp_271444
        if not l:
            l = ''.strip()
        else:
            l = l.strip()
        if l:
            if l in seen:
                continue
                seen.add(l)
                out.append(l)
            else:
                seen.add(l)
                out.append(l)
        else:
            continue
            seen.add(l)
            out.append(l)
        continue
    return out



# Original qualified name: plan_fanout
def plan_fanout(db, primary, langs, base_config, lang_overrides):
    __temp_271453 = base_config.get('dst_lang')
    if not __temp_271453:
        primary_lang = 'vi'
    else:
        primary_lang = __temp_271453
    extra = _normalize_langs(langs, primary_lang)
    if not lang_overrides:
        lang_overrides = {}
    __temp_271457 = vsvc.get_fanout_plan(primary).get('children')
    if not __temp_271457:
        prev_children = {}
    else:
        prev_children = __temp_271457
    __temp_271464 = db.scalar(select(Video.order_index).where(Video.project_id ==
        primary.project_id).order_by(Video.order_index.desc()).limit(1))
    if not __temp_271464:
        base_order = 0
    else:
        base_order = __temp_271464
    root_path = primary.project.root_path
    new_children = {}
    for __temp_271467 in iter(enumerate(extra)):
        __temp_271468, __temp_271469 = __temp_271467
        i = __temp_271468
        lang = __temp_271469
        __temp_271472 = {}
        __temp_271472.update(sanitize_config(base_config))
        __temp_271474 = __temp_271472
        __temp_271474.update({'dst_lang': lang})
        child_cfg = __temp_271474
        __temp_271475 = lang_overrides.get(lang)
        if not __temp_271475:
            ov = {}
        else:
            ov = __temp_271475
        for __temp_271477 in iter(_OVERRIDE_KEYS):
            k = __temp_271477
            if not ov.get(k):
                continue
                child_cfg[k] = ov[k]
            else:
                child_cfg[k] = ov[k]
            continue
        prev = prev_children.get(lang)
        if prev:
            child = db.get(Video, prev['video_id'])
        else:
            child = None
        if child is None:
            child = Video(project_id=primary.project_id, source_url=
                _child_source_url(primary, lang), platform=primary.platform,
                title=_child_title(primary, lang), author=primary.author,
                duration_ms=primary.duration_ms, cover_url=primary.cover_url,
                overall_status='pending', order_index=base_order + i + 1)
            db.add(child)
            db.flush()
            child.folder_path = str(ProjectFS(root_path).name_video_dir(child.
                id, order_index=child.order_index, title=child.title))
            for __temp_271489 in iter(STEP_NAMES):
                name = __temp_271489
                db.add(VideoStep(video_id=child.id, step_name=name, status=
                    'pending'))
                continue
            dispatched = False
        else:
            dispatched = bool(prev.get('dispatched'))
        vsvc.set_video_config(db, child, child_cfg)
        vsvc.set_fanout_child(db, child, primary.id, lang)
        new_children[lang] = {video_id: child.id, dispatched: dispatched}
        continue
    plan = {primary_lang: primary_lang, preset: resolve_fanout_preset(
        base_config), children: new_children}
    vsvc.set_fanout_plan(db, primary, plan)
    db.commit()
    return plan



# Original qualified name: _seed_one
def _seed_one(root_path, primary_id, child_id):
    fs = ProjectFS(root_path)
    pairs = [(fs.source_mp4(primary_id), fs.source_mp4(child_id)), (fs.
        audio_wav(primary_id), fs.audio_wav(child_id)), (fs.audio_source(
        primary_id), fs.audio_source(child_id)), (fs.audio_vocals(primary_id),
        fs.audio_vocals(child_id)), (fs.audio_music(primary_id), fs.audio_music
        (child_id)), (fs.subtitle_original(primary_id), fs.subtitle_original(
        child_id))]
    fs.video_dir(child_id)
    for __temp_271516 in iter(pairs):
        __temp_271517, __temp_271518 = __temp_271516
        src = __temp_271517
        dst = __temp_271518
        if not src.exists():
            continue
            __temp_271520 = dst.exists()
        else:
            dst.exists()
        if __temp_271520:
            if not dst.stat().st_size != src.stat().st_size:
                continue
                shutil.copy2(src, dst)
            else:
                shutil.copy2(src, dst)
        else:
            shutil.copy2(src, dst)
        continue
    with SessionLocal() as __temp_271528:
        db = __temp_271528
        db.query(SubtitleSegment).filter(SubtitleSegment.video_id == child_id, 
            SubtitleSegment.kind == 'original').delete()
        rows = db.query(SubtitleSegment).filter(SubtitleSegment.video_id ==
            primary_id, SubtitleSegment.kind == 'original').order_by(
            SubtitleSegment.seq).all()
        for __temp_271536 in iter(rows):
            r = __temp_271536
            db.add(SubtitleSegment(video_id=child_id, kind='original', seq=r.
                seq, start_ms=r.start_ms, end_ms=r.end_ms, text=r.text, edited=
                0, meta_json=r.meta_json))
            continue
        prep_output = {download: str(fs.source_mp4(child_id).resolve()),
            extract_audio: str(fs.audio_wav(child_id).resolve()), transcribe:
            str(fs.subtitle_original(child_id).resolve())}
        for __temp_271549 in iter(_PREP_STEPS):
            name = __temp_271549
            row = db.query(VideoStep).filter(VideoStep.video_id == child_id, 
                VideoStep.step_name == name).first()
            if not row:
                row = VideoStep(video_id=child_id, step_name=name)
                db.add(row)
                row.status = 'success'
            else:
                row.status = 'success'
            row.progress = 100.0
            row.output_path = prep_output.get(name)
            row.finished_at = datetime.utcnow()
            continue
        db.commit()
        return None



# NOT DECOMPILED: maybe_seed_children
