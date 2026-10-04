# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/agents/architect_job.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _row
def _row(db, channel_url):
    key = yt.normalize_channel_url(channel_url)
    row = db.query(CompetitorAnalysis).filter(CompetitorAnalysis.channel_url == key
        ).first()
    if row is None:
        row = CompetitorAnalysis(channel_url=key)
        db.add(row)
        db.commit()
        db.refresh(row)
        return row
    else:
        return row



# NOT DECOMPILED: _load_state


# NOT DECOMPILED: _save_artifact


# NOT DECOMPILED: public_state


# NOT DECOMPILED: run_job


# NOT DECOMPILED: research_from_source_kind


# NOT DECOMPILED: commit


# NOT DECOMPILED: job_to_dict


# NOT DECOMPILED: list_jobs


# Original qualified name: get_job
def get_job(db, job_id):
    job = db.get(Job, job_id)
    if job is not None:
        if job.step_name != 'channel_architect':
            raise StudioError(E.UNKNOWN, 'Job dựng kênh không tồn tại',
                status_code=404)
    else:
        raise StudioError(E.UNKNOWN, 'Job dựng kênh không tồn tại', status_code=404
            )
    return job_to_dict(db, job)

