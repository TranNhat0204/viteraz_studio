# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/competitor_migration.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _get
def _get(db, key):
    row = db.get(Setting, key)
    if row:
        if not row.value:
            return ''.strip()
        else:
            return row.value.strip()
    return ''



# Original qualified name: _set
def _set(db, key, value):
    row = db.get(Setting, key)
    if row:
        row.value = value
        return None
    db.add(Setting(key=key, value=value))
    return None



# NOT DECOMPILED: _find_existing


# NOT DECOMPILED: migrate_once
