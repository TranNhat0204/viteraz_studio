# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/browser_profiles.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: list_profiles


# Original qualified name: create_profile
def create_profile(body, db):
    p = svc.create_profile(db, body.label)
    return svc.to_dict(db, p)



# Original qualified name: set_platforms
def set_platforms(profile_id, body, db):
    p = svc.set_platforms(db, profile_id, body.platforms)
    if p is None:
        raise HTTPException(status_code=404, detail='Profile không tồn tại')
    return svc.to_dict(db, p)



# Original qualified name: discover
def discover(db):
    imported = svc.import_flow_chrome_profiles(db)
    created = svc.discover_and_sync(db)
    return {'created': created + imported}



# Original qualified name: update_profile
def update_profile(profile_id, body, db):
    p = svc.update_profile(db, profile_id, label=body.label, notes=body.notes,
        status=body.status)
    if p is None:
        raise HTTPException(status_code=404, detail='Profile không tồn tại')
    return svc.to_dict(db, p)



# Original qualified name: assign_account
def assign_account(profile_id, body, db):
    if not svc.assign_account(db, profile_id, body.platform, body.account_id):
        raise HTTPException(status_code=404, detail=
            'Profile hoặc tài khoản không tồn tại')
    p = svc.get_profile(db, profile_id)
    return svc.to_dict(db, p)



# Original qualified name: force_release
def force_release(profile_id, db):
    if not svc.force_release(db, profile_id):
        raise HTTPException(status_code=409, detail=
            'Profile không có lease đang giữ')
    p = svc.get_profile(db, profile_id)
    return svc.to_dict(db, p)



# Original qualified name: delete_profile
def delete_profile(profile_id, db):
    __temp_208262, __temp_208263 = svc.delete_profile(db, profile_id)
    ok = __temp_208262
    reason = __temp_208263
    if not ok:
        if reason == 'leased':
            code = 409
        else:
            code = 404
        if reason == 'leased':
            msg = 'Profile đang phục vụ một video — dừng video trước khi xoá.'
        else:
            msg = 'Profile không tồn tại'
        raise HTTPException(status_code=code, detail=msg)
    return {'deleted': profile_id}

