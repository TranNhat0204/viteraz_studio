# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/creator.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _transcript_text


# NOT DECOMPILED: generate_seo


# Original qualified name: get_seo
def get_seo(video_id, db):
    v = vsvc.get_video(db, video_id)
    return vsvc.get_video_seo(v)



# Original qualified name: save_seo
def save_seo(video_id, body, db):
    v = vsvc.get_video(db, video_id)
    seo = vsvc.get_video_seo(v)
    for __temp_208489 in iter(('titles', 'description', 'hashtags', 'hooks',
        'chosen_title_index')):
        k = __temp_208489
        val = getattr(body, k, None)
        if val is None:
            continue
            seo[k] = val
        else:
            seo[k] = val
        continue
    vsvc.set_video_seo(db, v, seo)
    return seo



# NOT DECOMPILED: _base_image


# NOT DECOMPILED: generate_thumbnail


# Original qualified name: get_thumb_config
def get_thumb_config(project_id, db):
    return psvc.get_thumbnail_config(psvc.get_project(db, project_id))



# NOT DECOMPILED: put_thumb_config
