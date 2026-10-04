# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/chatgpt_accounts.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: list_accounts


# Original qualified name: create_account
def create_account(body, db):
    a = svc.create_account(db, body.partition_id, body.label, body.email)
    return svc.to_dict(a)



# Original qualified name: reorder
def reorder(body, db):
    svc.reorder(db, body.ordered_ids)
    return {'ok': True}



# Original qualified name: update_account
def update_account(account_id, body, db):
    a = svc.update_account(db, account_id, label=body.label, email=body.email,
        enabled=body.enabled)
    return svc.to_dict(a)



# Original qualified name: clear_exhausted
def clear_exhausted(account_id, db):
    a = svc.clear_exhausted(db, account_id)
    return svc.to_dict(a)



# NOT DECOMPILED: set_credentials


# Original qualified name: credentials_status
def credentials_status(account_id):
    return {account_id: account_id, has_credentials: chatgpt_credentials.
        has_credentials(account_id)}



# Original qualified name: clear_credentials
def clear_credentials(account_id):
    chatgpt_credentials.clear_credentials(account_id)
    return {'cleared': account_id}



# Original qualified name: delete_account
def delete_account(account_id, db):
    chatgpt_credentials.clear_credentials(account_id)
    svc.delete_account(db, account_id)
    return {'deleted': account_id}

