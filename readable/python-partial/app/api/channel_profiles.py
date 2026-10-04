# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/channel_profiles.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _load


# Original qualified name: _save
def _save(db, items):
    row = db.get(Setting, _KEY)
    blob = json.dumps(items, ensure_ascii=False)
    if row:
        row.value = blob
        db.commit()
        return None
    else:
        db.add(Setting(key=_KEY, value=blob))
        db.commit()
        return None



# Original qualified name: list_profiles
def list_profiles(db):
    return {'profiles': _load(db)}



# Original qualified name: create_profile
def create_profile(body, db):
    if not body.name:
        name = ''.strip()
    else:
        name = body.name.strip()
    if not name:
        raise StudioError(E.UNKNOWN, 'Tên profile không được trống',
            status_code=422)
    items = _load(db)
    __temp_208284 = uuid.uuid4()
    if not body.config:
        profile = {id: __temp_208284.hex, name: name, config: sanitize_config({
            }), created_at: datetime.utcnow().isoformat()}
    else:
        profile = {id: __temp_208284.hex, name: name, config: sanitize_config(
            body.config), created_at: datetime.utcnow().isoformat()}
    items.append(profile)
    _save(db, items)
    return profile



# NOT DECOMPILED: update_profile


# NOT DECOMPILED: delete_profile
