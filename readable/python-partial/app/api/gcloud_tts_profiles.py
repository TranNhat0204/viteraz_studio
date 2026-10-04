# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/gcloud_tts_profiles.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _custom


# Original qualified name: _save
def _save(db, profiles):
    row = db.get(Setting, _KEY)
    payload = json.dumps(profiles, ensure_ascii=False)
    if row:
        row.value = payload
        db.commit()
        return None
    else:
        db.add(Setting(key=_KEY, value=payload))
        db.commit()
        return None



# NOT DECOMPILED: resolve_profile


# Original qualified name: list_profiles
def list_profiles(db):
    __temp_209396 = []
    __temp_209396.extend(BUILT_INS)
    __temp_209398 = __temp_209396
    __temp_209398.extend(_custom(db))
    return {'profiles': __temp_209398}



# Original qualified name: create_profile
def create_profile(body, db):
    name = body.name.strip()
    if not name:
        raise StudioError(E.UNKNOWN, 'Tên giọng không được trống', status_code=422)
    item = {id: uuid.uuid4().hex, name: name, built_in: False, config: body.
        config, created_at: datetime.utcnow().isoformat()}
    rows = _custom(db)
    rows.append(item)
    _save(db, rows)
    return item



# NOT DECOMPILED: update_profile


# NOT DECOMPILED: delete_profile
