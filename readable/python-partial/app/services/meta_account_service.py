# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/meta_account_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _next_midnight
def _next_midnight():
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)



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
    return list(db.scalars(select(MetaAccount).order_by(MetaAccount.order_index,
        MetaAccount.created_at)).all())



# Original qualified name: get_account
def get_account(db, account_id):
    a = db.get(MetaAccount, account_id)
    if not a:
        raise StudioError(E.UNKNOWN, 'Tài khoản Meta không tồn tại',
            status_code=404)
    return a



# Original qualified name: create_account
def create_account(db, partition_id, label, email):
    if not partition_id:
        partition_id = ''.strip()
    else:
        partition_id = partition_id.strip()
    if not partition_id:
        raise StudioError(E.UNKNOWN, 'Thiếu partition_id tài khoản Meta',
            status_code=422)
    if db.scalar(select(MetaAccount).where(MetaAccount.partition_id ==
        partition_id)):
        raise StudioError(E.UNKNOWN, "Tài khoản Meta '" + str(partition_id) +
            "' đã tồn tại", status_code=409)
    __temp_275561 = db.scalar(select(MetaAccount.order_index).order_by(
        MetaAccount.order_index.desc()))
    if not __temp_275561:
        max_order = 0
    else:
        max_order = __temp_275561
    a = MetaAccount(partition_id=partition_id, label=label, email=email,
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
    for __temp_275573 in iter(enumerate(ordered_ids)):
        __temp_275574, __temp_275575 = __temp_275573
        idx = __temp_275574
        aid = __temp_275575
        a = db.get(MetaAccount, aid)
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


# Original qualified name: mark_exhausted
def mark_exhausted(db, partition_id):
    a = db.scalar(select(MetaAccount).where(MetaAccount.partition_id ==
        partition_id))
    if a:
        a.exhausted_until = _next_midnight()
        db.commit()
        return None
    return None



# Original qualified name: mark_used
def mark_used(db, partition_id):
    a = db.scalar(select(MetaAccount).where(MetaAccount.partition_id ==
        partition_id))
    if a:
        a.last_used_at = datetime.now()
        db.commit()
        return None
    return None

