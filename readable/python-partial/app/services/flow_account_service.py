# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/flow_account_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _next_midnight
def _next_midnight():
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)



# Original qualified name: _today_start
def _today_start():
    return datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)



# Original qualified name: _month_start
def _month_start():
    return datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)



# Original qualified name: _status
def _status(a, now):
    app = __import__('app.services', fromlist=('flow_profile_health',), level=0)
    flow_profile_health = app.flow_profile_health
    flow_health = flow_profile_health
    if not a.enabled:
        return disabled
    if a.exhausted_until:
        if a.exhausted_until > now:
            return exhausted
    if a.cooldown_until:
        if a.cooldown_until > now:
            return cooldown
    if flow_health.is_sick(a.partition_id):
        return sick
    return ready



# Original qualified name: is_cooling
def is_cooling(a, now):
    if a.cooldown_until:
        if not now:
            return bool(a.cooldown_until > datetime.now())
        else:
            return bool(a.cooldown_until > now)
    else:
        return bool(a.cooldown_until)



# Original qualified name: usage_stats
def usage_stats(db, partition_id):
    month = _month_start()
    today = _today_start()
    
    
    def _count(kind, since):
        nonlocal db, partition_id
        __temp_272582 = db.scalar(select(func.count()).select_from(
            FlowUsageEvent).where(FlowUsageEvent.partition_id == partition_id, 
            FlowUsageEvent.kind == kind, FlowUsageEvent.created_at >= since))
        if not __temp_272582:
            return int(0)
        else:
            return int(__temp_272582)
    
    
    return {images_today: _count('image', today), videos_today: _count('video',
        today), images_month: _count('image', month), videos_month: _count(
        'video', month)}



# Original qualified name: usage_stats.<locals>._count
def _count(kind, since):
    nonlocal db, partition_id
    __temp_272594 = db.scalar(select(func.count()).select_from(FlowUsageEvent).
        where(FlowUsageEvent.partition_id == partition_id, FlowUsageEvent.kind ==
        kind, FlowUsageEvent.created_at >= since))
    if not __temp_272594:
        return int(0)
    else:
        return int(__temp_272594)



# Original qualified name: to_dict
def to_dict(a, db):
    app = __import__('app.services', fromlist=('flow_profile_health',), level=0)
    flow_profile_health = app.flow_profile_health
    flow_health = flow_profile_health
    now = datetime.now()
    sick = flow_health.sick_info(a.partition_id)
    __temp_272599 = {}
    """id""".__setitem__('id', a.id)
    """partition_id""".__setitem__('partition_id', a.partition_id)
    """label""".__setitem__('label', a.label)
    """email""".__setitem__('email', a.email)
    """enabled""".__setitem__('enabled', bool(a.enabled))
    """order_index""".__setitem__('order_index', a.order_index)
    """status""".__setitem__('status', _status(a, now))
    if a.exhausted_until:
        """exhausted_until""".__setitem__('exhausted_until', a.exhausted_until.
            isoformat())
    else:
        """exhausted_until""".__setitem__('exhausted_until', None)
    if a.cooldown_until:
        """cooldown_until""".__setitem__('cooldown_until', a.cooldown_until.
            isoformat())
        __temp_272604 = is_cooling(a, now)
    else:
        """cooldown_until""".__setitem__('cooldown_until', None)
        is_cooling(a, now)
    if __temp_272604:
        """cooldown_seconds_left""".__setitem__('cooldown_seconds_left', max(
            int((a.cooldown_until - now).total_seconds()), 0))
    else:
        """cooldown_seconds_left""".__setitem__('cooldown_seconds_left', 0)
    if a.last_used_at:
        """last_used_at""".__setitem__('last_used_at', a.last_used_at.isoformat())
    else:
        """last_used_at""".__setitem__('last_used_at', None)
    if sick:
        """sick_until""".__setitem__('sick_until', sick['until'].isoformat())
    else:
        """sick_until""".__setitem__('sick_until', None)
    if sick:
        """sick_seconds_left""".__setitem__('sick_seconds_left', sick[
            'seconds_left'])
    else:
        """sick_seconds_left""".__setitem__('sick_seconds_left', 0)
    if sick:
        """sick_reason""".__setitem__('sick_reason', sick['reason'])
    else:
        """sick_reason""".__setitem__('sick_reason', None)
    if not a.daily_image_cap:
        """daily_image_cap""".__setitem__('daily_image_cap', int(0))
        """credits""".__setitem__('credits', a.credits)
        """credits_tier""".__setitem__('credits_tier', a.credits_tier)
    else:
        """daily_image_cap""".__setitem__('daily_image_cap', int(a.daily_image_cap)
            )
        """credits""".__setitem__('credits', a.credits)
        """credits_tier""".__setitem__('credits_tier', a.credits_tier)
    if a.credits_synced_at:
        __temp_272613 = a.credits_synced_at.isoformat()
    if not a.video_engine:
        __temp_272615 = __temp_272599
        __temp_272615.update({credits_synced_at: __temp_272613, video_engine: None}
            )
        d = __temp_272615
    else:
        __temp_272617 = __temp_272599
        __temp_272617.update({credits_synced_at: __temp_272613, video_engine: a
            .video_engine})
        d = __temp_272617
    if db is not None:
        stats = usage_stats(db, a.partition_id)
        d.update(stats)
        if not a.daily_image_cap:
            cap = int(0)
        else:
            cap = int(a.daily_image_cap)
        if cap > 0:
            d['images_remaining_today'] = max(cap - stats['images_today'], 0)
        else:
            d['images_remaining_today'] = None
    return d



# Original qualified name: list_accounts
def list_accounts(db):
    return list(db.scalars(select(FlowAccount).order_by(FlowAccount.order_index,
        FlowAccount.created_at)).all())



# Original qualified name: get_account
def get_account(db, account_id):
    a = db.get(FlowAccount, account_id)
    if not a:
        raise StudioError(E.UNKNOWN, 'Tài khoản Flow không tồn tại',
            status_code=404)
    return a



# Original qualified name: create_account
def create_account(db, partition_id, label, email):
    if not partition_id:
        partition_id = ''.strip()
    else:
        partition_id = partition_id.strip()
    if not partition_id:
        raise StudioError(E.UNKNOWN, 'Thiếu partition_id tài khoản Flow',
            status_code=422)
    if db.scalar(select(FlowAccount).where(FlowAccount.partition_id ==
        partition_id)):
        raise StudioError(E.UNKNOWN, "Tài khoản Flow '" + str(partition_id) +
            "' đã tồn tại", status_code=409)
    __temp_272640 = db.scalar(select(FlowAccount.order_index).order_by(
        FlowAccount.order_index.desc()))
    if not __temp_272640:
        max_order = 0
    else:
        max_order = __temp_272640
    a = FlowAccount(partition_id=partition_id, label=label, email=email,
        order_index=max_order + 1)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a



# Original qualified name: update_account
def update_account(db, account_id, label, email, enabled, daily_image_cap, video_engine):
    a = get_account(db, account_id)
    if label is not None:
        a.label = label
    if email is not None:
        a.email = email
    if enabled is not None:
        if enabled:
            a.enabled = 1
        else:
            a.enabled = 0
    if daily_image_cap is not None:
        a.daily_image_cap = max(int(daily_image_cap), 0)
    if video_engine is not Ellipsis:
        __temp_272649 = set()
        __temp_272649.update(frozenset({None, 'omni', 'agent'}))
        valid = __temp_272649
        if video_engine in valid:
            engine_val = video_engine
        else:
            engine_val = None
        a.video_engine = engine_val
    db.commit()
    db.refresh(a)
    return a



# Original qualified name: set_credits_cache
def set_credits_cache(db, account_id, credits, tier):
    a = get_account(db, account_id)
    if credits is not None:
        if credits >= 0:
            a.credits = int(credits)
        else:
            a.credits = None
    else:
        a.credits = None
    if not tier:
        a.credits_tier = None
    else:
        a.credits_tier = tier
    a.credits_synced_at = datetime.now()
    db.commit()
    db.refresh(a)
    return a



# NOT DECOMPILED: record_usage


# Original qualified name: delete_account
def delete_account(db, account_id):
    a = get_account(db, account_id)
    profile_id = a.browser_profile_id
    partition = a.partition_id
    db.delete(a)
    db.flush()
    unpinned = db.query(Video).filter(Video.flow_account_id == partition).update({
        Video.flow_account_id: None}, synchronize_session=False)
    released = False
    if profile_id:
        if not db.scalar(select(FlowAccount).where(FlowAccount.
            browser_profile_id == profile_id)):
            prof = db.get(BrowserProfile, profile_id)
            if prof is not None:
                if prof.leased_by_video_id:
                    prof.leased_by_video_id = None
                    prof.leased_job_id = None
                    prof.lease_kind = None
                    prof.lease_heartbeat_at = None
                    released = True
    db.commit()
    if not unpinned:
        if released:
            if released:
                log.info('[flow_acct] xoá ' + str(partition) + ': gỡ pin ' +
                    str(unpinned) + ' video' + ', nhả lease profile' + '.')
                return None
            else:
                log.info('[flow_acct] xoá ' + str(partition) + ': gỡ pin ' +
                    str(unpinned) + ' video' + '' + '.')
                return None
    elif released:
        log.info('[flow_acct] xoá ' + str(partition) + ': gỡ pin ' + str(
            unpinned) + ' video' + ', nhả lease profile' + '.')
        return None
    else:
        log.info('[flow_acct] xoá ' + str(partition) + ': gỡ pin ' + str(
            unpinned) + ' video' + '' + '.')
        return None
    return None



# Original qualified name: reorder
def reorder(db, ordered_ids):
    for __temp_272679 in iter(enumerate(ordered_ids)):
        __temp_272680, __temp_272681 = __temp_272679
        idx = __temp_272680
        aid = __temp_272681
        a = db.get(FlowAccount, aid)
        if not a:
            continue
            a.order_index = idx
        else:
            a.order_index = idx
        continue
    db.commit()
    return None



# Original qualified name: clear_exhausted
def clear_exhausted(db, account_id):
    a = get_account(db, account_id)
    a.exhausted_until = None
    db.commit()
    db.refresh(a)
    return a



# Original qualified name: clear_cooldown
def clear_cooldown(db, account_id):
    app = __import__('app.services', fromlist=('flow_profile_health',), level=0)
    flow_profile_health = app.flow_profile_health
    flow_health = flow_profile_health
    a = get_account(db, account_id)
    a.cooldown_until = None
    db.commit()
    db.refresh(a)
    flow_health.clear_sick(a.partition_id)
    return a



# NOT DECOMPILED: next_available


# Original qualified name: mark_exhausted
def mark_exhausted(db, partition_id):
    a = db.scalar(select(FlowAccount).where(FlowAccount.partition_id ==
        partition_id))
    if a:
        a.exhausted_until = _next_midnight()
        db.commit()
        return None
    return None



# NOT DECOMPILED: cooldown_minutes


# Original qualified name: mark_cooldown
def mark_cooldown(db, partition_id, hard_block, minutes):
    if not partition_id:
        return None
    if minutes is None:
        mins = cooldown_minutes(db, hard_block=hard_block)
    else:
        mins = max(0, int(minutes))
    if mins <= 0:
        return None
    a = db.scalar(select(FlowAccount).where(FlowAccount.partition_id ==
        partition_id))
    if a is None:
        return None
    until = datetime.now() + timedelta(minutes=mins)
    if a.cooldown_until:
        if a.cooldown_until > until:
            return a.cooldown_until
    a.cooldown_until = until
    db.commit()
    if hard_block:
        why = 'hoạt động bất thường'
    else:
        why = 'throttle'
    log.info('[flow_acct] ' + str(partition_id) + ': nghỉ ' + str(mins) +
        ' phút (' + str(why) + ') → tới ' + format(until, '%H:%M') + '.')
    return until



# NOT DECOMPILED: cooling_accounts


# Original qualified name: mark_used
def mark_used(db, partition_id):
    a = db.scalar(select(FlowAccount).where(FlowAccount.partition_id ==
        partition_id))
    if a:
        a.last_used_at = datetime.now()
        db.commit()
        return None
    return None

