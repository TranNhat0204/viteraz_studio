# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/competitor_analysis_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _median


# NOT DECOMPILED: _age_days


# Original qualified name: _sat_log
def _sat_log(ratio, saturate):
    if not ratio <= 1:
        if saturate <= 1:
            return 0.0
    else:
        return 0.0
    return min(1.0, math.log10(ratio) / math.log10(saturate))



# Original qualified name: _recency_boost
def _recency_boost(age_days):
    if age_days is None:
        return 0.3
    if age_days <= _RECENCY_FULL_DAYS:
        return 1.0
    if age_days >= _RECENCY_ZERO_DAYS:
        return 0.0
    span = _RECENCY_ZERO_DAYS - _RECENCY_FULL_DAYS
    return max(0.0, 1.0 - (age_days - _RECENCY_FULL_DAYS) / span)



# NOT DECOMPILED: _multiplier_band


# Original qualified name: _maturity
def _maturity(age_days):
    if age_days is None:
        return 1.0
    if age_days >= _MATURITY_REF_DAYS:
        return 1.0
    ratio = math.log1p(max(0.0, age_days)) / math.log1p(_MATURITY_REF_DAYS)
    return max(_MATURITY_FLOOR, min(1.0, ratio))



# Original qualified name: _views_norm
def _views_norm(v):
    return v['view_count'] / _maturity(v.get('age_days'))



# Original qualified name: _usable_as_baseline
def _usable_as_baseline(v):
    age = v.get('age_days')
    if not age is None:
        return age >= _BASELINE_MIN_AGE_DAYS
    else:
        return age is None



# NOT DECOMPILED: _apply_local_baselines


# NOT DECOMPILED: compute_analysis


# NOT DECOMPILED: compute_analysis.<locals>._bucket_median


# NOT DECOMPILED: compute_analysis.<locals>._eng_ratio


# NOT DECOMPILED: channel_stats


# NOT DECOMPILED: _public_video


# NOT DECOMPILED: analyze_channel


# NOT DECOMPILED: _profile_block_for_skeleton


# NOT DECOMPILED: normalize_source_brief


# Original qualified name: normalize_source_brief.<locals>._pairs
def _pairs(key, fields):
    nonlocal raw
    out = []
    if not raw.get(key):
        __temp_270477 = []
    for __temp_270478 in iter(__temp_270477):
        item = __temp_270478
        if not isinstance(item, dict):
            continue
            __temp_270480 = item.get(fields[0])
        else:
            item.get(fields[0])
        if not __temp_270480:
            a = str('').strip()
        else:
            a = str(__temp_270480).strip()
        if not a:
            continue
            __temp_270486 = item.get(fields[1])
        else:
            item.get(fields[1])
        if not __temp_270486:
            out.append({fields[0]: a, fields[1]: str('').strip()})
        else:
            out.append({fields[0]: a, fields[1]: str(__temp_270486).strip()})
        continue
    return out[None:20]



# NOT DECOMPILED: _is_empty_praise


# NOT DECOMPILED: rank_comments


# NOT DECOMPILED: comment_noise_ratio


# NOT DECOMPILED: normalize_audience_read


# NOT DECOMPILED: normalize_audience_read.<locals>._rows


# NOT DECOMPILED: fetch_video_comments


# NOT DECOMPILED: _audience_prompt_block


# Original qualified name: _skeleton_messages
def _skeleton_messages(video_meta, transcript, language, channel_profile, engine, video_format, existing_titles, recent_titles, mode, comments):
    if engine is not None:
        system = engine.body
    else:
        system = (
            "You are a senior YouTube content strategist. You reverse-engineer why a competitor's video works (its hook, structure, angle, emotional beats) and turn that into an ORIGINAL content skeleton for another creator's channel."
            )
    src = """COMPETITOR VIDEO (analyse it, do not copy it):
    - Title: """ + str(
        video_meta.get('title')) + '\n- Channel: ' + str(video_meta.get('channel')
        ) + '\n- Views: ' + str(video_meta.get('view_count')
        ) + ' · outlier x' + str(video_meta.get('outlier_score')
        ) + ' · duration ' + str(video_meta.get('duration')) + 's\n'
    if transcript:
        tr = (
            """
    TRANSCRIPT WITH TIMESTAMPS (competitor's spoken content — use it to understand structure, pacing and, in cover mode, WHAT FACTS the video states; NEVER to copy wording, phrasing or sentence order):
    ""\"
    """
             + transcript + '\n"""\n')
    else:
        tr = """
    (No transcript available — infer structure from the title/packaging, and say so in 'why_it_worked'.)
    """
    is_cover = mode == 'cover'
    if is_cover:
        step2 = """STEP 2 · BUILD THE EPISODE for the TARGET channel, ON THE SAME SUBJECT. KEEP the subject, the people and the documented events — those belong to the world, not to that creator. REPLACE everything else: the angle, the structure, the wording and the voice must be the target channel's own, following its identity below. Never reuse a sentence, a turn of phrase or the ordering of reveals.
    
    STEP 3 · EXTRACT A SOURCE BRIEF: the FACTS the video states about this subject — names, dates, figures, claims. Facts only, never phrasing. Mark how verifiable they are: this is one creator's account, it is UNVERIFIED, and the writing step will treat it as claims that need attribution rather than as established truth.
    """
    else:
        step2 = """STEP 2 · BUILD AN ORIGINAL SKELETON for the TARGET channel. KEEP the architecture (same hook type, same number of loops, same proportional beat_map). REPLACE the subject and every detail with the target channel's own niche and direction. The competitor's topic, names, facts and phrasing must NOT appear.
    """
    if not is_cover:
        parts = ['TASK — TWO STEPS, ONE ANSWER.\n\n',
            """STEP 1 · READ THE COMPETITOR (teardown). Work out the RETENTION ARCHITECTURE of the video below: which hook type it opens with, how long the hook runs, where each curiosity loop opens and closes, how the runtime splits across beats, and where the opening promise is paid off. Use the [mm:ss] marks to measure this, do not guess.
    
    """
            , step2, src, tr]
    else:
        parts = ['TASK — THREE STEPS, ONE ANSWER.\n\n',
            """STEP 1 · READ THE COMPETITOR (teardown). Work out the RETENTION ARCHITECTURE of the video below: which hook type it opens with, how long the hook runs, where each curiosity loop opens and closes, how the runtime splits across beats, and where the opening promise is paid off. Use the [mm:ss] marks to measure this, do not guess.
    
    """
            , step2, src, tr]
    audience = _audience_prompt_block(comments, video_meta.get('view_count'))
    if audience:
        parts.append(audience)
    if engine is not None:
        if not channel_profile:
            parts.append(ideation_service.build_channel_context_blocks(engine,
                channel_profile, language=language, video_format=video_format,
                existing_titles=existing_titles, recent_titles=recent_titles,
                channel_hook={}.get('channel_hook'), series_mode=
                ideation_service.resolve_series_mode(engine, channel_profile)))
        else:
            parts.append(ideation_service.build_channel_context_blocks(engine,
                channel_profile, language=language, video_format=video_format,
                existing_titles=existing_titles, recent_titles=recent_titles,
                channel_hook=channel_profile.get('channel_hook'), series_mode=
                ideation_service.resolve_series_mode(engine, channel_profile)))
        extra_keys = (
            """,
      "beat_plan": [{"label": "beat name in the channel language", "share": 0, "role": "what this beat does"}],
      "teardown": """
             + _TEARDOWN_SPEC.replace('\n', '\n  '))
    else:
        parts.append(_profile_block_for_skeleton(channel_profile))
        extra_keys = (
            """,
      "beat_plan": [{"label": "beat name in the channel language", "share": 0, "role": "what this beat does"}],
      "teardown": """
             + _TEARDOWN_SPEC.replace('\n', '\n  '))
    if is_cover:
        extra_keys += ',\n  "source_brief": ' + _SOURCE_BRIEF_SPEC.replace('\n',
            '\n  ')
    if audience:
        extra_keys += ',\n  "audience_read": ' + _AUDIENCE_READ_SPEC.replace('\n',
            '\n  ')
    __temp_270610 = ideation_service._IDEA_JSON_SPEC[None:-2].rstrip()
    if is_cover:
        parts.append(
            """
    
    Return ONLY a single JSON object (no markdown fences, no prose before or after) with exactly these keys:
    """
             + __temp_270610 + extra_keys +
            """
    }
    
    RULES for the extra keys:
    """ +
            """- beat_plan is the competitor's beat_map MAPPED ONTO THE SAME SUBJECT but YOUR ordering of reveals. Keep the proportions that work; do not keep their sequence of surprises.
    """
             +
            """- 'outline' must be the same beats written as plain sentences, in the same order — it stays the human-readable view of beat_plan.
    - teardown describes the COMPETITOR video, not yours. Never put competitor wording anywhere else in the answer.
    """
            )
    else:
        parts.append(
            """
    
    Return ONLY a single JSON object (no markdown fences, no prose before or after) with exactly these keys:
    """
             + __temp_270610 + extra_keys +
            """
    }
    
    RULES for the extra keys:
    """ +
            """- beat_plan is the competitor's beat_map MAPPED ONTO YOUR NEW SUBJECT. Keep the same number of beats and the same proportions; 'share' is percent of runtime and every share must sum to 100.
    """
             +
            """- 'outline' must be the same beats written as plain sentences, in the same order — it stays the human-readable view of beat_plan.
    - teardown describes the COMPETITOR video, not yours. Never put competitor wording anywhere else in the answer.
    """
            )
    if is_cover:
        parts.append(
            """- source_brief holds FACTS ONLY: names, dates, places, figures, stated claims. Not one sentence of the video's own phrasing.
    - Be honest in 'verifiability': you are reading ONE creator's account, which is unverified — not a primary document. If a claim would need a report, a court record or an official statement to stand up, say 'low'.
    - Leave a list empty rather than guessing. A missing date is fine; an invented one ends a channel.
    """
            )
    if audience:
        parts.append(
            """- audience_read summarises THE COMMENTS ABOVE, not your opinion of the audience. Leave a list empty rather than inventing a gap nobody raised.
    - 'gaps' and 'objections' are the two that change what you write. Fill them first.
    - Paraphrase every viewer_story; never copy a comment's wording, and never carry over names, workplaces or other details that identify a real person.
    - 'noise_ratio' is your estimate of how much of that comment section was empty praise with no usable signal, from 0 to 1.
    """
            )
        return system, ''.join(parts)
    else:
        return system, ''.join(parts)



# Original qualified name: _skeleton_transcript_budget
def _skeleton_transcript_budget(provider):
    budget = ai_provider.max_turn_chars(provider) - _SKELETON_PROMPT_OVERHEAD_CHARS
    return max(_MIN_TRANSCRIPT_CHARS, min(_SKELETON_TRANSCRIPT_CHARS, budget))



# NOT DECOMPILED: normalize_beat_plan


# NOT DECOMPILED: _ngrams


# NOT DECOMPILED: originality_score


# NOT DECOMPILED: extract_skeleton


# Original qualified name: _micro_messages
def _micro_messages(meta, transcript, language):
    system = (
        'You are a forensic YouTube writing analyst. Study repeatable PATTERNS in delivery, pacing, structure and audience relationship. Do not quote, reconstruct, imitate distinctive passages, or preserve the source wording. Describe abstract techniques that another creator can apply to new subject matter. Return strict JSON only.'
        )
    source = {title: meta.get('title'), views: meta.get('view_count'),
        duration_seconds: meta.get('duration'), upload_date: meta.get(
        'upload_date')}
    if transcript:
        transcript_part = (
            'FULL AVAILABLE TRANSCRIPT (analyse patterns only; never quote it):\n"""\n'
             + transcript + '\n"""')
    else:
        transcript_part = (
            'NO TRANSCRIPT. Infer packaging/likely structure only and mark confidence low.'
            )
    if not language:
        user = 'OUTPUT LANGUAGE for descriptive notes: ' + str('vi') + '\nVIDEO METADATA:\n' + str(json.dumps(source, ensure_ascii=False)) + '\n\n' + str(transcript_part) + """
    
    Analyse this one video at sentence/beat level. Return ONE JSON object with exactly: hook_pattern (abstract formula, never source wording), beat_map (array), voice_notes, sentence_stats, pace, audience_relationship, devices (array), evidence_style, ending_pattern, packaging_notes, confidence (0..1), limitations (array)."""
    else:
        user = 'OUTPUT LANGUAGE for descriptive notes: ' + str(language) + '\nVIDEO METADATA:\n' + str(json.dumps(source, ensure_ascii=False)) + '\n\n' + str(transcript_part) + """
    
    Analyse this one video at sentence/beat level. Return ONE JSON object with exactly: hook_pattern (abstract formula, never source wording), beat_map (array), voice_notes, sentence_stats, pace, audience_relationship, devices (array), evidence_style, ending_pattern, packaging_notes, confidence (0..1), limitations (array)."""
    return system, user



# Original qualified name: _engine_catalog_for_prompt
def _engine_catalog_for_prompt():
    out = []
    for __temp_270710 in iter(channel_engines.list_engines()):
        engine = __temp_270710
        if not engine.meta:
            meta = {}
        else:
            meta = engine.meta
        if not meta.get('hidden'):
            if meta.get('test_mode'):
                continue
                __temp_270714 = meta.get('niche')
                __temp_270715 = meta.get('visual_style')
                __temp_270716 = meta.get('engine_kind', 'ai')
                __temp_270717 = meta.get('tags')
            else:
                meta.get('niche')
                meta.get('visual_style')
                meta.get('engine_kind', 'ai')
                meta.get('tags')
        else:
            continue
            meta.get('niche')
            meta.get('visual_style')
            meta.get('engine_kind', 'ai')
            meta.get('tags')
        if not __temp_270717:
            out.append({id: engine.id, name: engine.name, niche: __temp_270714,
                visual_style: __temp_270715, engine_kind: __temp_270716, tags: []})
        else:
            out.append({id: engine.id, name: engine.name, niche: __temp_270714,
                visual_style: __temp_270715, engine_kind: __temp_270716, tags:
                __temp_270717})
        continue
    return out



# NOT DECOMPILED: _synthesis_messages


# NOT DECOMPILED: _safe_obj


# NOT DECOMPILED: _clamp_confidence


# Original qualified name: _transcript_budget
def _transcript_budget(provider):
    turn_limit = ai_provider.max_turn_chars(provider)
    budget = turn_limit - _MICRO_PROMPT_OVERHEAD_CHARS
    return max(_MIN_TRANSCRIPT_CHARS, min(_DNA_TRANSCRIPT_CHARS, budget))



# NOT DECOMPILED: _analyse_dna_video


# NOT DECOMPILED: _dna_cache_age_hours


# Original qualified name: _save_dna
def _save_dna(db, channel_url, dna, channel):
    key = yt.normalize_channel_url(channel_url)
    row = db.query(CompetitorAnalysis).filter(CompetitorAnalysis.channel_url == key
        ).first()
    if row is None:
        row = CompetitorAnalysis(channel_url=key)
        db.add(row)
        __temp_270770 = channel.get('channel_title')
    else:
        channel.get('channel_title')
    if not __temp_270770:
        row.channel_title = row.channel_title
    else:
        row.channel_title = __temp_270770
    __temp_270772 = channel.get('channel_id')
    if not __temp_270772:
        row.channel_id = row.channel_id
    else:
        row.channel_id = __temp_270772
    __temp_270773 = channel.get('channel_follower_count')
    if not __temp_270773:
        row.channel_follower_count = row.channel_follower_count
    else:
        row.channel_follower_count = __temp_270773
    row.dna_json = json.dumps(dna, ensure_ascii=False)
    db.commit()
    db.refresh(row)
    return row



# NOT DECOMPILED: extract_channel_dna


# Original qualified name: extract_channel_dna.<locals>.emit
def emit(value):
    nonlocal progress
    if progress:
        progress(value)
        return None
    return None



# Original qualified name: extract_channel_dna.<locals>.ensure_not_cancelled
def ensure_not_cancelled():
    nonlocal cancel_check
    if cancel_check:
        if cancel_check():
            raise make_error(E.UNKNOWN, 'Tác vụ học DNA đã bị huỷ.')
        return None
    return None



# Original qualified name: apply_channel_dna
def apply_channel_dna(db, project_id, dna, language, long_target_sec, short_target_sec):
    app = __import__('app.services', fromlist=('ai_studio_service',), level=0)
    ai_studio_service = app.ai_studio_service
    project = db.get(Project, project_id)
    if project is not None:
        if project.kind != 'ai':
            raise StudioError(E.PROJECT_NOT_FOUND, 'Kênh AI không tồn tại',
                status_code=404)
    else:
        raise StudioError(E.PROJECT_NOT_FOUND, 'Kênh AI không tồn tại',
            status_code=404)
    cfg = ai_studio_service.get_or_create_config(db, project_id)
    profile = ai_studio_service._loads(cfg.channel_profile_json, {})
    __temp_270811 = dna.get('channel_orientation')
    if not __temp_270811:
        orientation = str('').strip()
    else:
        orientation = str(__temp_270811).strip()
    if orientation:
        profile['channel_orientation'] = orientation
    if isinstance(dna.get('_source'), dict):
        profile['_competitor_source'] = dna.get('_source')
    else:
        profile['_competitor_source'] = {}
    if not language:
        lang = dna.get('language')
    else:
        lang = language
    if lang:
        cfg.language = str(lang).strip()
    if long_target_sec is not None:
        profile['long_target_sec'] = int(long_target_sec)
    elif 'long_target_sec' in dna:
        profile['long_target_sec'] = dna['long_target_sec']
    if short_target_sec is not None:
        profile['short_target_sec'] = int(short_target_sec)
    elif 'short_target_sec' in dna:
        profile['short_target_sec'] = dna['short_target_sec']
    cfg.channel_profile_json = json.dumps(profile, ensure_ascii=False)
    db.commit()
    db.refresh(cfg)
    return ai_studio_service.config_to_dict(cfg)



# NOT DECOMPILED: clone_channel_from_dna


# NOT DECOMPILED: _loads


# NOT DECOMPILED: analysis_to_dict


# Original qualified name: _cache_age_hours
def _cache_age_hours(row):
    if not row.updated_at:
        ref = row.created_at
    else:
        ref = row.updated_at
    if ref is None:
        return 1000000000.0
    return max(0.0, (datetime.utcnow() - ref).total_seconds() / 3600.0)



# Original qualified name: get_cached
def get_cached(db, channel_url):
    key = yt.normalize_channel_url(channel_url)
    return db.query(CompetitorAnalysis).filter(CompetitorAnalysis.channel_url ==
        key).first()



# NOT DECOMPILED: channel_dna_job_to_dict


# Original qualified name: get_channel_dna_job
def get_channel_dna_job(db, job_id):
    job = db.get(Job, job_id)
    if job is not None:
        if not job.job_type != 'background_task':
            if job.step_name != 'competitor_dna':
                raise StudioError(E.UNKNOWN, 'Job học DNA không tồn tại',
                    status_code=404)
        else:
            raise StudioError(E.UNKNOWN, 'Job học DNA không tồn tại',
                status_code=404)
    else:
        raise StudioError(E.UNKNOWN, 'Job học DNA không tồn tại', status_code=404)
    return channel_dna_job_to_dict(db, job)



# NOT DECOMPILED: list_channel_dna_jobs


# NOT DECOMPILED: save_snapshots


# Original qualified name: prune_snapshots
def prune_snapshots(db, keep_days):
    app = __import__('app.db.models', fromlist=('CompetitorSnapshot',), level=0)
    CompetitorSnapshot = app.CompetitorSnapshot
    cutoff = datetime.utcnow() - timedelta(days=keep_days)
    deleted = db.query(CompetitorSnapshot).filter(CompetitorSnapshot.
        captured_at < cutoff).delete(synchronize_session=False)
    db.commit()
    if not deleted:
        return int(0)
    else:
        return int(deleted)



# NOT DECOMPILED: apply_real_velocity


# Original qualified name: reach_score
def reach_score(view_count):
    if isinstance(view_count, (int, float)):
        if view_count <= 0:
            return 0.0
    else:
        return 0.0
    return round(min(1.0, math.log10(view_count) / math.log10(
        _REACH_SATURATION_VIEWS)), 4)



# Original qualified name: radar_rank
def radar_rank(video, mode):
    __temp_271062 = video.get('key_score')
    if not __temp_271062:
        key = float(0)
    else:
        key = float(__temp_271062)
    if mode != 'reach':
        return key
    return round(_W_RADAR_KEY_REACH * key + _W_RADAR_REACH * reach_score(video.
        get('view_count')), 4)



# Original qualified name: _all_idea_titles
def _all_idea_titles(db, project_id, limit):
    app = __import__('app.db.models', fromlist=('IdeaCard',), level=0)
    IdeaCard = app.IdeaCard
    rows = db.query(IdeaCard).filter(IdeaCard.project_id == project_id).order_by(
        IdeaCard.seq.desc()).limit(limit).all()
    titles = []
    for __temp_271075 in iter(rows):
        row = __temp_271075
        title = _loads(row.payload_json, {}).get('title')
        if not title:
            continue
            titles.append(str(title))
        else:
            titles.append(str(title))
        continue
    return titles



# Original qualified name: save_analysis
def save_analysis(db, channel_url, result, max_videos):
    key = yt.normalize_channel_url(channel_url)
    row = db.query(CompetitorAnalysis).filter(CompetitorAnalysis.channel_url == key
        ).first()
    if row is None:
        row = CompetitorAnalysis(channel_url=key)
        db.add(row)
        row.channel_title = result.get('channel_title')
    else:
        row.channel_title = result.get('channel_title')
    row.channel_id = result.get('channel_id')
    row.channel_follower_count = result.get('channel_follower_count')
    row.channel_avatar = result.get('channel_avatar')
    row.baseline_long = result.get('baseline_long')
    row.baseline_short = result.get('baseline_short')
    row.sample_size = result.get('sample_size')
    row.max_videos = max_videos
    __temp_271097 = result.get('videos')
    if not __temp_271097:
        row.videos_json = json.dumps([], ensure_ascii=False)
    else:
        row.videos_json = json.dumps(__temp_271097, ensure_ascii=False)
    db.commit()
    db.refresh(row)
    return row



# NOT DECOMPILED: list_analyses


# Original qualified name: get_analysis
def get_analysis(db, analysis_id):
    row = db.get(CompetitorAnalysis, analysis_id)
    if row is None:
        raise StudioError(E.UNKNOWN, 'Phân tích không tồn tại', status_code=404)
    return analysis_to_dict(row, include_videos=True)



# Original qualified name: delete_analysis
def delete_analysis(db, analysis_id):
    row = db.get(CompetitorAnalysis, analysis_id)
    if row is None:
        raise StudioError(E.UNKNOWN, 'Phân tích không tồn tại', status_code=404)
    db.delete(row)
    db.commit()
    return None



# NOT DECOMPILED: analyze_channel_cached


# NOT DECOMPILED: import_skeleton_as_idea


# Original qualified name: _now_iso
def _now_iso():
    return datetime.utcnow().isoformat()



# NOT DECOMPILED: _job_public


# NOT DECOMPILED: _prune_jobs


# Original qualified name: get_batch_job
def get_batch_job(job_id):
    job = _BATCH_JOBS.get(job_id)
    if job:
        return _job_public(job)
    return None



# NOT DECOMPILED: list_batch_jobs


# NOT DECOMPILED: start_batch_import


# NOT DECOMPILED: _run_batch_import


# NOT DECOMPILED: trend_radar


# NOT DECOMPILED: _cluster_messages


# NOT DECOMPILED: cluster_topics
