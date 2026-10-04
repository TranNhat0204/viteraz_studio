# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/publish_profile_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: get_login_status


# NOT DECOMPILED: to_dict


# Original qualified name: list_profiles
def list_profiles(db):
    return list(db.scalars(select(PublishProfile).order_by(PublishProfile.
        created_at)).all())



# Original qualified name: get_profile
def get_profile(db, profile_id):
    p = db.get(PublishProfile, profile_id)
    if not p:
        raise StudioError(E.UNKNOWN, 'Profile đăng bài không tồn tại',
            status_code=404)
    return p



# Original qualified name: create_profile
def create_profile(db, name, chrome_id):
    if not name:
        name = ''.strip()
    else:
        name = name.strip()
    if not chrome_id:
        chrome_id = ''.strip()
    else:
        chrome_id = chrome_id.strip()
    if name:
        if not chrome_id:
            raise StudioError(E.UNKNOWN, 'Thiếu tên hoặc ID Chrome của Profile',
                status_code=422)
    else:
        raise StudioError(E.UNKNOWN, 'Thiếu tên hoặc ID Chrome của Profile',
            status_code=422)
    count = db.scalar(select(PublishProfile).select_from(PublishProfile).
        with_only_columns(PublishProfile.id))
    existing_count = len(db.scalars(select(PublishProfile.id)).all())
    if existing_count >= 3:
        raise StudioError(E.UNKNOWN,
            'Đã đạt giới hạn tối đa 3 Profiles để đảm bảo an toàn, không thể tạo thêm.'
            , status_code=400)
    if db.scalar(select(PublishProfile).where(PublishProfile.chrome_id ==
        chrome_id)):
        raise StudioError(E.UNKNOWN, "Profile Chrome ID '" + str(chrome_id) +
            "' đã tồn tại", status_code=409)
    p = PublishProfile(name=name, chrome_id=chrome_id)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p



# Original qualified name: update_profile
def update_profile(db, profile_id, name, youtube_channel, facebook_page, tiktok_username):
    p = get_profile(db, profile_id)
    if name is not None:
        p.name = name.strip()
    if youtube_channel is not None:
        if youtube_channel.strip():
            p.youtube_channel = youtube_channel.strip()
        else:
            p.youtube_channel = None
    if facebook_page is not None:
        if facebook_page.strip():
            p.facebook_page = facebook_page.strip()
        else:
            p.facebook_page = None
    if tiktok_username is not None:
        if tiktok_username.strip():
            p.tiktok_username = tiktok_username.strip()
        else:
            p.tiktok_username = None
    db.commit()
    db.refresh(p)
    return p



# Original qualified name: delete_profile
def delete_profile(db, profile_id):
    p = get_profile(db, profile_id)
    db.delete(p)
    db.commit()
    return None

