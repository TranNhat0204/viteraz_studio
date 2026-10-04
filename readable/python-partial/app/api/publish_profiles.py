# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/publish_profiles.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: list_profiles


# Original qualified name: create_profile
def create_profile(body, db):
    p = svc.create_profile(db, body.name, body.chrome_id)
    return svc.to_dict(p)



# Original qualified name: update_profile
def update_profile(profile_id, body, db):
    p = svc.update_profile(db, profile_id, name=body.name, youtube_channel=body
        .youtube_channel, facebook_page=body.facebook_page, tiktok_username=
        body.tiktok_username)
    return svc.to_dict(p)



# Original qualified name: delete_profile
def delete_profile(profile_id, db):
    svc.delete_profile(db, profile_id)
    return {'deleted': profile_id}

