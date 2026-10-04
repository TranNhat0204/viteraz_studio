# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/flow_accounts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: list_accounts


# Original qualified name: create_account
def create_account(body, db):
    a = svc.create_account(db, body.partition_id, body.label, body.email)
    return svc.to_dict(a, db)



# Original qualified name: reorder
def reorder(body, db):
    svc.reorder(db, body.ordered_ids)
    return {'ok': True}



# Original qualified name: account_stats
def account_stats(account_id, db):
    a = svc.get_account(db, account_id)
    return svc.to_dict(a, db)



# NOT DECOMPILED: refresh_credits


# Original qualified name: update_account
def update_account(account_id, body, db):
    if 'video_engine' in body.model_fields_set:
        video_engine_kwarg = body.video_engine
    else:
        video_engine_kwarg = Ellipsis
    a = svc.update_account(db, account_id, label=body.label, email=body.email,
        enabled=body.enabled, daily_image_cap=body.daily_image_cap,
        video_engine=video_engine_kwarg)
    return svc.to_dict(a, db)



# Original qualified name: clear_exhausted
def clear_exhausted(account_id, db):
    a = svc.clear_exhausted(db, account_id)
    return svc.to_dict(a, db)



# Original qualified name: clear_cooldown
def clear_cooldown(account_id, db):
    a = svc.clear_cooldown(db, account_id)
    return svc.to_dict(a, db)



# Original qualified name: delete_account
def delete_account(account_id, db):
    svc.delete_account(db, account_id)
    return {'deleted': account_id}

