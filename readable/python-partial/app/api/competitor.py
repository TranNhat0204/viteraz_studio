# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/competitor.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: analyze


# Original qualified name: list_analyses
def list_analyses(db):
    return {'analyses': svc.list_analyses(db)}



# Original qualified name: get_analysis
def get_analysis(analysis_id, db):
    return svc.get_analysis(db, analysis_id)



# Original qualified name: delete_analysis
def delete_analysis(analysis_id, db):
    svc.delete_analysis(db, analysis_id)
    return {'ok': True}



# NOT DECOMPILED: skeleton


# NOT DECOMPILED: channel_dna


# Original qualified name: list_channel_dna_jobs
def list_channel_dna_jobs(channel_url, active_only, db):
    return {'jobs': svc.list_channel_dna_jobs(db, channel_url=channel_url,
        active_only=active_only)}



# Original qualified name: get_channel_dna_job
def get_channel_dna_job(job_id, db):
    return svc.get_channel_dna_job(db, job_id)



# Original qualified name: apply_channel_dna
def apply_channel_dna(body, db):
    if not body.dna:
        return svc.apply_channel_dna(db, body.project_id, {}, language=body.
            language, long_target_sec=body.long_target_sec, short_target_sec=
            body.short_target_sec)
    else:
        return svc.apply_channel_dna(db, body.project_id, body.dna, language=
            body.language, long_target_sec=body.long_target_sec,
            short_target_sec=body.short_target_sec)



# Original qualified name: clone_channel
def clone_channel(body, db):
    if not body.dna:
        return svc.clone_channel_from_dna(db, channel_url=body.channel_url, dna
            ={}, name=body.name, engine_id=body.engine_id, output_folder=body.
            output_folder, language=body.language, long_target_sec=body.
            long_target_sec, short_target_sec=body.short_target_sec)
    else:
        return svc.clone_channel_from_dna(db, channel_url=body.channel_url, dna
            =body.dna, name=body.name, engine_id=body.engine_id, output_folder=
            body.output_folder, language=body.language, long_target_sec=body.
            long_target_sec, short_target_sec=body.short_target_sec)



# NOT DECOMPILED: import_batch


# Original qualified name: list_import_jobs
def list_import_jobs(project_id, running_only):
    return {'jobs': svc.list_batch_jobs(project_id, running_only=running_only)}



# Original qualified name: get_import_job
def get_import_job(job_id):
    job = svc.get_batch_job(job_id)
    if job is None:
        raise StudioError(E.UNKNOWN, 'Job không tồn tại hoặc đã hết hạn.',
            status_code=404)
    return job



# NOT DECOMPILED: trend_radar


# NOT DECOMPILED: cluster_topics


# Original qualified name: source_status
def source_status():
    return {data_api: youtube_data_api.is_configured(), ytdlp: YtDlpClient.
        is_available()}



# NOT DECOMPILED: test_youtube_key


# Original qualified name: competitor_settings
def competitor_settings():
    return competitor_settings_svc.get_config()



# NOT DECOMPILED: test_llm


# NOT DECOMPILED: trending


# NOT DECOMPILED: keyword_scan


# NOT DECOMPILED: architect


# Original qualified name: architect_jobs
def architect_jobs(active_only, db):
    return {'jobs': architect_job.list_jobs(db, active_only=active_only)}



# Original qualified name: architect_job_detail
def architect_job_detail(job_id, db):
    return architect_job.get_job(db, job_id)



# Original qualified name: architect_state
def architect_state(channel_url, db):
    return architect_job.public_state(db, svc.yt.normalize_channel_url(channel_url)
        )



# Original qualified name: architect_commit
def architect_commit(body, db):
    if not body.project_id:
        if not body.name:
            __temp_208442 = ''.strip()
        else:
            body.name.strip()
        if not __temp_208442:
            raise StudioError(E.UNKNOWN, 'Thiếu tên cho kênh mới.', status_code=422
                )
    __temp_208445 = svc.yt.normalize_channel_url(body.channel_url)
    if not body.name:
        __temp_208446 = ''.strip()
    else:
        body.name.strip()
    if not body.output_folder:
        return architect_job.commit(db, channel_url=__temp_208445, name=
            __temp_208446, output_folder=''.strip(), engine_id=body.engine_id,
            project_id=body.project_id, overwrite_master_prompt=bool(body.
            overwrite_master_prompt))
    else:
        return architect_job.commit(db, channel_url=__temp_208445, name=
            __temp_208446, output_folder=body.output_folder.strip(), engine_id=
            body.engine_id, project_id=body.project_id, overwrite_master_prompt
            =bool(body.overwrite_master_prompt))



# NOT DECOMPILED: keyword_seed


# Original qualified name: keyword_scan_jobs
def keyword_scan_jobs(active_only, db):
    return {'jobs': keyword_intel_service.list_scan_jobs(db, active_only=
        active_only)}



# Original qualified name: list_keyword_scans
def list_keyword_scans(db):
    return {'scans': keyword_intel_service.list_scans(db)}



# Original qualified name: get_keyword_scan
def get_keyword_scan(scan_id, db):
    return keyword_intel_service.get_scan(db, scan_id)



# Original qualified name: delete_keyword_scan
def delete_keyword_scan(scan_id, db):
    keyword_intel_service.delete_scan(db, scan_id)
    return {'ok': True}



# NOT DECOMPILED: keyword_suggest
