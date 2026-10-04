# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/browser_profile_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: note_account_used
def note_account_used(video_id, partition_id):
    if video_id:
        if not partition_id:
            return None
    else:
        return None
    _ACCOUNTS_BY_VIDEO.setdefault(video_id, set()).add(partition_id)
    return None



# Original qualified name: accounts_of_video
def accounts_of_video(video_id):
    if not video_id:
        return []
    return sorted(_ACCOUNTS_BY_VIDEO.get(video_id, set()))



# Original qualified name: forget_video_accounts
def forget_video_accounts(video_id):
    if video_id:
        _ACCOUNTS_BY_VIDEO.pop(video_id, None)
        return None
    return None



# Original qualified name: owns_account
def owns_account(db, video_id, partition_id):
    acc = db.query(FlowAccount).filter(FlowAccount.partition_id == partition_id
        ).first()
    if acc is not None:
        if not acc.browser_profile_id:
            return True
    else:
        return True
    prof = db.get(BrowserProfile, acc.browser_profile_id)
    if prof is None:
        return True
    return prof.leased_by_video_id in (None, video_id)



# Original qualified name: _account_email
def _account_email(acc):
    __temp_268428 = getattr(acc, 'email', None)
    if not __temp_268428:
        email = ''.strip().lower()
    else:
        email = __temp_268428.strip().lower()
    if not email:
        return None
    else:
        return email



# Original qualified name: _account_label
def _account_label(acc):
    __temp_268433 = getattr(acc, 'label', None)
    if not __temp_268433:
        __temp_268434 = getattr(acc, 'name', None)
        if not __temp_268434:
            __temp_268435 = getattr(acc, 'email', None)
            if not __temp_268435:
                __temp_268436 = getattr(acc, 'partition_id', None)
                if not __temp_268436:
                    __temp_268437 = getattr(acc, 'chrome_id', None)
                    if not __temp_268437:
                        return 'profile'
                    else:
                        return __temp_268437
                else:
                    return __temp_268436
            else:
                return __temp_268435
        else:
            return __temp_268434
    else:
        return __temp_268433



# NOT DECOMPILED: discover_and_sync


# Original qualified name: list_profiles
def list_profiles(db):
    import_flow_chrome_profiles(db)
    discover_and_sync(db)
    return list(db.scalars(select(BrowserProfile).order_by(BrowserProfile.
        created_at)).all())



# Original qualified name: create_profile
def create_profile(db, label):
    if not label:
        __temp_268472 = ''.strip()
    else:
        label.strip()
    if not __temp_268472:
        p = BrowserProfile(label='Profile mới', source='user')
    else:
        p = BrowserProfile(label=__temp_268472, source='user')
    db.add(p)
    db.flush()
    p.chrome_dir = 'browser-profiles/' + str(p.id)
    db.commit()
    db.refresh(p)
    return p



# Original qualified name: import_flow_chrome_profiles
def import_flow_chrome_profiles(db):
    n = 0
    for __temp_268483 in iter(db.scalars(select(FlowAccount)).all()):
        acc = __temp_268483
        if acc.partition_id.startswith('bp:'):
            continue
        if acc.browser_profile_id:
            prof = db.get(BrowserProfile, acc.browser_profile_id)
        else:
            prof = None
        if prof is None:
            if not acc.email:
                if not acc.label:
                    prof = BrowserProfile(label=acc.partition_id, email=acc.
                        email, source='imported')
                else:
                    prof = BrowserProfile(label=acc.label, email=acc.email,
                        source='imported')
            else:
                prof = BrowserProfile(label=acc.email, email=acc.email, source=
                    'imported')
            db.add(prof)
            db.flush()
            acc.browser_profile_id = prof.id
            n += 1
        if prof.chrome_dir:
            continue
            prof.chrome_dir = 'flow-chrome/' + str(acc.partition_id)
        else:
            prof.chrome_dir = 'flow-chrome/' + str(acc.partition_id)
        if not prof.source:
            prof.source = 'imported'
        else:
            prof.source = prof.source
        continue
    if not n:
        if db.dirty:
            db.commit()
            return n
        else:
            return n
    else:
        db.commit()
        return n



# NOT DECOMPILED: set_platforms


# Original qualified name: get_profile
def get_profile(db, profile_id):
    return db.get(BrowserProfile, profile_id)



# Original qualified name: _accounts_of
def _accounts_of(db, profile_id):
    out = {}
    for __temp_268513 in iter(_PLATFORM_TABLES):
        __temp_268514, __temp_268515 = __temp_268513
        platform = __temp_268514
        model = __temp_268515
        rows = db.scalars(select(model).where(model.browser_profile_id ==
            profile_id)).all()
        out[platform] = list(rows)
        continue
    return out



# NOT DECOMPILED: to_dict


# Original qualified name: to_dict.<locals>._acc
def _acc(platform, a):
    nonlocal now
    __temp_268553 = getattr(a, 'label', None)
    if not __temp_268553:
        d = {id: a.id, label: getattr(a, 'name', None), email: getattr(a,
            'email', None)}
    else:
        d = {id: a.id, label: __temp_268553, email: getattr(a, 'email', None)}
    if platform == 'publish':
        d['chrome_id'] = a.chrome_id
        d['linked'] = {youtube: a.youtube_channel, facebook: a.facebook_page,
            tiktok: a.tiktok_username}
        return d
    d['partition_id'] = a.partition_id
    enabled = bool(getattr(a, 'enabled', 1))
    __temp_268562 = getattr(a, 'exhausted_until', None)
    if __temp_268562:
        exhausted = bool(a.exhausted_until > now)
    else:
        exhausted = bool(__temp_268562)
    if not enabled:
        d['status'] = 'disabled'
    elif exhausted:
        d['status'] = 'exhausted'
    else:
        d['status'] = 'ready'
    return d



# Original qualified name: update_profile
def update_profile(db, profile_id, label, notes, status):
    p = db.get(BrowserProfile, profile_id)
    if not p:
        return None
    if label is not None:
        if not label:
            p.label = p.label
        else:
            p.label = label
    if notes is not None:
        p.notes = notes
    if status in ('ready', 'disabled'):
        p.status = status
    db.commit()
    return p



# Original qualified name: assign_account
def assign_account(db, profile_id, platform, account_id):
    model = dict(_PLATFORM_TABLES).get(platform)
    if model is not None:
        if db.get(BrowserProfile, profile_id) is None:
            return False
    else:
        return False
    acc = db.get(model, account_id)
    if acc is None:
        return False
    acc.browser_profile_id = profile_id
    db.commit()
    return True



# NOT DECOMPILED: delete_profile


# NOT DECOMPILED: _active_video_ids


# Original qualified name: reap_stale
def reap_stale(db):
    global _default_lease_video_id
    active = _active_video_ids(db)
    n = 0
    for __temp_268611 in iter(db.scalars(select(BrowserProfile).where(
        BrowserProfile.leased_by_video_id.is_not(None))).all()):
        p = __temp_268611
        if not p.leased_by_video_id not in active:
            continue
            log.info("[lease] thu hồi lease mồ côi: profile '" + str(p.label) +
                "' ← video " + str(p.leased_by_video_id))
            p.leased_by_video_id = None
        else:
            log.info("[lease] thu hồi lease mồ côi: profile '" + str(p.label) +
                "' ← video " + str(p.leased_by_video_id))
            p.leased_by_video_id = None
        p.leased_job_id = None
        p.lease_kind = None
        p.lease_heartbeat_at = None
        n += 1
        continue
    if n:
        db.commit()
    if _default_lease_video_id:
        if _default_lease_video_id not in active:
            _default_lease_video_id = None
    _reap_provider_slots(db)
    return n



# Original qualified name: _profile_of_flow_account
def _profile_of_flow_account(db, acc):
    if not acc.browser_profile_id:
        discover_and_sync(db)
        db.refresh(acc)
    if acc.browser_profile_id:
        return db.get(BrowserProfile, acc.browser_profile_id)
    return None



# NOT DECOMPILED: _flow_accounts_ready


# Original qualified name: _lease
def _lease(db, prof, video_id, job_id, partition_id, update_pin):
    prof.leased_by_video_id = video_id
    prof.leased_job_id = job_id
    prof.lease_kind = 'generate'
    prof.lease_heartbeat_at = datetime.now()
    v = db.get(Video, video_id)
    if v is not None:
        if update_pin:
            v.flow_account_id = partition_id
    db.commit()
    return None



# Original qualified name: _leased_count_excluding
def _leased_count_excluding(db, video_id):
    return int(db.query(BrowserProfile).filter(BrowserProfile.
        leased_by_video_id.is_not(None), BrowserProfile.leased_by_video_id !=
        video_id).count())



# NOT DECOMPILED: lease_acquire_flow


# NOT DECOMPILED: lease_acquire_flow_many


# NOT DECOMPILED: lease_rotate_flow


# NOT DECOMPILED: has_spare_flow_profile


# NOT DECOMPILED: lease_rotate_flow_worker


# Original qualified name: lease_release_video
def lease_release_video(db, video_id):
    global _default_lease_video_id
    n = 0
    for __temp_268694 in iter(db.scalars(select(BrowserProfile).where(
        BrowserProfile.leased_by_video_id == video_id)).all()):
        p = __temp_268694
        p.leased_by_video_id = None
        p.leased_job_id = None
        p.lease_kind = None
        p.lease_heartbeat_at = None
        n += 1
        continue
    if n:
        db.commit()
    if _default_lease_video_id == video_id:
        _default_lease_video_id = None
    return n



# Original qualified name: release_other_profiles
def release_other_profiles(db, video_id, keep_profile_id):
    global _default_lease_video_id
    n = 0
    for __temp_268700 in iter(db.scalars(select(BrowserProfile).where(
        BrowserProfile.leased_by_video_id == video_id)).all()):
        p = __temp_268700
        if keep_profile_id:
            if p.id == keep_profile_id:
                continue
                p.leased_by_video_id = None
            else:
                p.leased_by_video_id = None
        else:
            p.leased_by_video_id = None
        p.leased_job_id = None
        p.lease_kind = None
        p.lease_heartbeat_at = None
        n += 1
        continue
    if n:
        db.commit()
    if _default_lease_video_id == video_id:
        if keep_profile_id is None:
            _default_lease_video_id = None
    return n



# Original qualified name: lease_profile_for_video
def lease_profile_for_video(db, profile_id, video_id, job_id):
    p = db.get(BrowserProfile, profile_id)
    if p is not None:
        if p.status == 'disabled':
            return False
    else:
        return False
    if p.leased_by_video_id not in (None, video_id):
        return False
    p.leased_by_video_id = video_id
    p.leased_job_id = job_id
    if not p.lease_kind:
        p.lease_kind = 'generate'
    else:
        p.lease_kind = p.lease_kind
    p.lease_heartbeat_at = datetime.now()
    db.commit()
    return True



# Original qualified name: release_profile_if_held
def release_profile_if_held(db, profile_id, video_id):
    p = db.get(BrowserProfile, profile_id)
    if p is not None:
        if p.leased_by_video_id != video_id:
            return False
    else:
        return False
    p.leased_by_video_id = None
    p.leased_job_id = None
    p.lease_kind = None
    p.lease_heartbeat_at = None
    db.commit()
    return True



# Original qualified name: force_release
def force_release(db, profile_id):
    p = db.get(BrowserProfile, profile_id)
    if p:
        if not p.leased_by_video_id:
            return False
    else:
        return False
    p.leased_by_video_id = None
    p.leased_job_id = None
    p.lease_kind = None
    p.lease_heartbeat_at = None
    db.commit()
    return True



# NOT DECOMPILED: flow_admission


# Original qualified name: _reap_provider_slots
def _reap_provider_slots(db):
    active = _active_video_ids(db)
    for __temp_268720 in iter(list(_PROVIDER_SLOTS.items())):
        __temp_268721, __temp_268722 = __temp_268720
        slot = __temp_268721
        vid = __temp_268722
        if not vid:
            continue
        if not vid not in active:
            continue
            log.info('[lease] thu hồi provider slot mồ côi: ' + str(slot) +
                ' ← video ' + str(vid))
            _PROVIDER_SLOTS[slot] = None
        else:
            log.info('[lease] thu hồi provider slot mồ côi: ' + str(slot) +
                ' ← video ' + str(vid))
            _PROVIDER_SLOTS[slot] = None
        continue
    return None



# NOT DECOMPILED: provider_admission


# Original qualified name: release_provider_slots
def release_provider_slots(video_id):
    n = 0
    for __temp_268731 in iter(list(_PROVIDER_SLOTS.items())):
        __temp_268732, __temp_268733 = __temp_268731
        slot = __temp_268732
        vid = __temp_268733
        if not vid == video_id:
            continue
            _PROVIDER_SLOTS[slot] = None
        else:
            _PROVIDER_SLOTS[slot] = None
        n += 1
        continue
    return n



# NOT DECOMPILED: chrome_dir_of_partition


# Original qualified name: chrome_dir_of_profile
def chrome_dir_of_profile(db, profile_id):
    p = db.get(BrowserProfile, profile_id)
    if p:
        if not p.chrome_dir:
            return 'browser-profiles/' + str(p.id)
        else:
            return p.chrome_dir
    return None



# NOT DECOMPILED: _platforms_of


# NOT DECOMPILED: lease_chatgpt_ui_profile


# Original qualified name: combo_pin_admission
def combo_pin_admission(db, video_id, job_id, preferred_profile_id):
    reap_stale(db)
    p = db.get(BrowserProfile, preferred_profile_id)
    if p is not None:
        if p.status == 'disabled':
            return True
    else:
        return True
    if p.leased_by_video_id not in (None, video_id):
        return False
    return lease_profile_for_video(db, preferred_profile_id, video_id, job_id)



# NOT DECOMPILED: leased_partitions
