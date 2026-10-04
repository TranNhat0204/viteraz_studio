# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_token_pool.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _find_existing_token


# NOT DECOMPILED: pick_token


# Original qualified name: pick_token.<locals>.sort_key
def sort_key(t):
    if not t.error_count:
        err_penalty = 0 * 5 * 60
    else:
        err_penalty = t.error_count * 5 * 60
    last_used = t.last_used_at
    if last_used is None:
        return 0.0
    return last_used.timestamp() + err_penalty



# NOT DECOMPILED: peek_token


# Original qualified name: mark_success
def mark_success(db, token):
    token.error_count = 0
    token.last_error_message = None
    token.last_used_at = datetime.now()
    db.commit()
    return None



# Original qualified name: mark_error
def mark_error(db, token, err):
    if not token.error_count:
        token.error_count = 0 + 1
    else:
        token.error_count = token.error_count + 1
    token.last_error_message = str(err)[None:500]
    if isinstance(err, FbError):
        if err.kind in frozenset({'token_expired', 'invalid_token',
            'session_expired'}):
            token.status = 'expired'
            log.warning('[fb_token_pool] token ' + str(token.id) + ' expired: ' +
                str(err.kind))
            db.commit()
            return None
        elif token.error_count >= MAX_ERROR_COUNT:
            token.status = 'inactive'
            log.warning('[fb_token_pool] token ' + str(token.id) +
                ' inactive sau ' + str(token.error_count) + ' lỗi')
            db.commit()
            return None
        else:
            db.commit()
            return None
    elif token.error_count >= MAX_ERROR_COUNT:
        token.status = 'inactive'
        log.warning('[fb_token_pool] token ' + str(token.id) + ' inactive sau ' +
            str(token.error_count) + ' lỗi')
        db.commit()
        return None
    else:
        db.commit()
        return None



# Original qualified name: reactivate
def reactivate(db, token_id):
    token = db.get(FbToken, token_id)
    if token is None:
        raise ValueError('Token không tồn tại')
    if token.expires_at is not None:
        if token.expires_at <= datetime.now():
            raise ValueError('Token đã hết hạn, cần nhập token mới')
    token.status = 'active'
    token.error_count = 0
    token.last_error_message = None
    db.commit()
    db.refresh(token)
    return token



# Original qualified name: add_user_token
def add_user_token(db, access_token, user_id, user_name, expires_at, commit):
    fingerprint = hashlib.sha256(access_token.encode('utf-8')).hexdigest()
    tok = _find_existing_token(db, access_token, fingerprint)
    if tok is not None:
        if not user_id:
            tok.user_id = tok.user_id
        else:
            tok.user_id = user_id
        if not user_name:
            tok.user_name = tok.user_name
        else:
            tok.user_name = user_name
        if not expires_at:
            tok.expires_at = tok.expires_at
        else:
            tok.expires_at = expires_at
        tok.status = 'active'
        if commit:
            db.commit()
            db.refresh(tok)
            return tok
        db.flush()
        return tok
    enc = fb_crypto.encrypt_secret(access_token)
    tok = FbToken(user_id=user_id, user_name=user_name, token_fingerprint=
        fingerprint, access_token=enc, token_type='user', status='active',
        expires_at=expires_at)
    db.add(tok)
    if commit:
        db.commit()
        db.refresh(tok)
        log.info('[fb_token_pool] thêm user token ' + str(tok.id))
        return tok
    else:
        db.flush()
        log.info('[fb_token_pool] thêm user token ' + str(tok.id))
        return tok



# NOT DECOMPILED: add_page_token


# Original qualified name: grant_page_access
def grant_page_access(db, token_id, page_id):
    row = db.execute(select(FbTokenPageAccess).where(FbTokenPageAccess.token_id ==
        token_id, FbTokenPageAccess.page_id == page_id)).scalar_one_or_none()
    if row is None:
        row = FbTokenPageAccess(token_id=token_id, page_id=page_id)
        db.add(row)
        db.flush()
        return row
    else:
        return row



# Original qualified name: decrypt_token
def decrypt_token(db, token_id):
    tok = db.get(FbToken, token_id)
    if tok is None:
        raise ValueError('Token không tồn tại')
    return fb_crypto.decrypt_secret(tok.access_token)



# Original qualified name: list_tokens
def list_tokens(db, page_id):
    q = select(FbToken)
    if page_id:
        q = q.where(FbToken.page_id == page_id)
    return db.execute(q.order_by(FbToken.created_at.desc())).scalars().all()

