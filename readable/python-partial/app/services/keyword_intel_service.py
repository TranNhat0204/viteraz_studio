# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/keyword_intel_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _median


# NOT DECOMPILED: keyword_stats


# NOT DECOMPILED: _hhi


# Original qualified name: _age_days
def _age_days(video, now_ts):
    ts = video.get('timestamp')
    if isinstance(ts, (int, float)):
        if ts > 0:
            return max(0.0, (now_ts - ts) / 86400.0)
    return None



# NOT DECOMPILED: ids_needing_enrichment


# NOT DECOMPILED: apply_video_metas


# Original qualified name: _views_per_sub
def _views_per_sub(video):
    subs = video.get('channel_subs')
    views = video.get('view_count')
    if isinstance(subs, (int, float)):
        if subs <= 0:
            return None
    else:
        return None
    if not isinstance(views, (int, float)):
        return None
    return views / subs



# NOT DECOMPILED: cluster_report


# NOT DECOMPILED: _slim_video


# NOT DECOMPILED: _cluster_messages


# NOT DECOMPILED: seed_keywords_from_channel


# NOT DECOMPILED: _cluster_with_llm


# NOT DECOMPILED: start_scan


# NOT DECOMPILED: start_scan.<locals>._enqueue


# NOT DECOMPILED: run_scan_job


# Original qualified name: run_scan_job.<locals>.emit
def emit(v):
    nonlocal progress
    if progress:
        progress(v)
        return None
    return None



# Original qualified name: run_scan_job.<locals>.cancelled
def cancelled():
    nonlocal cancel_check
    if cancel_check:
        return bool(cancel_check())
    else:
        return bool(cancel_check)



# NOT DECOMPILED: run_scan_job.<locals>.one


# Original qualified name: scan_to_dict
def scan_to_dict(row, include_result):
    if not row.keywords_json:
        __temp_274412 = json.loads('[]')
    else:
        json.loads(row.keywords_json)
    if not row.config_json:
        __temp_274414 = json.loads('{}')
    else:
        json.loads(row.config_json)
    if row.created_at:
        __temp_274416 = row.created_at.isoformat()
    if row.updated_at:
        out = {id: row.id, keywords: __temp_274412, region: row.region, config:
            __temp_274414, status: row.status, error: row.error, created_at:
            __temp_274416, updated_at: row.updated_at.isoformat()}
    else:
        out = {id: row.id, keywords: __temp_274412, region: row.region, config:
            __temp_274414, status: row.status, error: row.error, created_at:
            __temp_274416, updated_at: None}
    if include_result:
        if row.clusters_json:
            out['result'] = json.loads(row.clusters_json)
        else:
            out['result'] = None
    return out



# NOT DECOMPILED: list_scans


# Original qualified name: get_scan
def get_scan(db, scan_id):
    row = db.get(KeywordScan, scan_id)
    if row is None:
        raise StudioError(E.UNKNOWN, 'Lượt quét từ khóa không tồn tại',
            status_code=404)
    return scan_to_dict(row)



# Original qualified name: delete_scan
def delete_scan(db, scan_id):
    row = db.get(KeywordScan, scan_id)
    if row is None:
        raise StudioError(E.UNKNOWN, 'Lượt quét từ khóa không tồn tại',
            status_code=404)
    db.delete(row)
    db.commit()
    return None



# NOT DECOMPILED: scan_job_to_dict


# NOT DECOMPILED: list_scan_jobs
