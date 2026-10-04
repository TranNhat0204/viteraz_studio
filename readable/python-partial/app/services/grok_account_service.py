# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/grok_account_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _quota_cooldown_until
def _quota_cooldown_until():
    return datetime.now() + timedelta(hours=24)



# Original qualified name: _status
def _status(a, now):
    if not a.enabled:
        return disabled
    if a.exhausted_until:
        if a.exhausted_until > now:
            return exhausted
    return ready



# NOT DECOMPILED: to_dict


# Original qualified name: list_accounts
def list_accounts(db):
    return list(db.scalars(select(GrokAccount).order_by(GrokAccount.order_index,
        GrokAccount.created_at)).all())



# Original qualified name: get_account
def get_account(db, account_id):
    a = db.get(GrokAccount, account_id)
    if not a:
        raise StudioError(E.UNKNOWN, 'Tài khoản Grok không tồn tại',
            status_code=404)
    return a



# Original qualified name: create_account
def create_account(db, partition_id, label, email):
    if not partition_id:
        partition_id = ''.strip()
    else:
        partition_id = partition_id.strip()
    if not partition_id:
        raise StudioError(E.UNKNOWN, 'Thiếu partition_id tài khoản Grok',
            status_code=422)
    if db.scalar(select(GrokAccount).where(GrokAccount.partition_id ==
        partition_id)):
        raise StudioError(E.UNKNOWN, "Tài khoản Grok '" + str(partition_id) +
            "' đã tồn tại", status_code=409)
    __temp_272913 = db.scalar(select(GrokAccount.order_index).order_by(
        GrokAccount.order_index.desc()))
    if not __temp_272913:
        max_order = 0
    else:
        max_order = __temp_272913
    a = GrokAccount(partition_id=partition_id, label=label, email=email,
        order_index=max_order + 1)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a



# Original qualified name: update_account
def update_account(db, account_id, label, email, enabled):
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
    db.commit()
    db.refresh(a)
    return a



# Original qualified name: delete_account
def delete_account(db, account_id):
    a = get_account(db, account_id)
    db.delete(a)
    db.commit()
    return None



# Original qualified name: reorder
def reorder(db, ordered_ids):
    for __temp_272925 in iter(enumerate(ordered_ids)):
        __temp_272926, __temp_272927 = __temp_272925
        idx = __temp_272926
        aid = __temp_272927
        a = db.get(GrokAccount, aid)
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



# NOT DECOMPILED: next_available


# Original qualified name: preferred_available
def preferred_available(db, partition_id):
    a = db.scalar(select(GrokAccount).where(GrokAccount.partition_id ==
        partition_id))
    if a:
        if a.enabled:
            if a.exhausted_until:
                if not a.exhausted_until > datetime.now():
                    return a
            else:
                return a
    return None



# Original qualified name: mark_exhausted
def mark_exhausted(db, partition_id):
    a = db.scalar(select(GrokAccount).where(GrokAccount.partition_id ==
        partition_id))
    if a:
        a.exhausted_until = _quota_cooldown_until()
        db.commit()
        return None
    return None



# Original qualified name: mark_used
def mark_used(db, partition_id):
    a = db.scalar(select(GrokAccount).where(GrokAccount.partition_id ==
        partition_id))
    if a:
        a.last_used_at = datetime.now()
        db.commit()
        return None
    return None

