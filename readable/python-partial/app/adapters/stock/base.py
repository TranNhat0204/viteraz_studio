# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/stock/base.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: StockClip.orientation
def orientation(self):
    if self.height > self.width:
        return portrait
    if self.width > self.height:
        return landscape
    return square



# NOT DECOMPILED: StockClip.credit


# Original qualified name: get_setting
def get_setting(key):
    with SessionLocal() as __temp_23097:
        db = __temp_23097
        row = db.get(Setting, key)
        if row:
            if row.value:
                row.value.strip()
            else:
                """""".strip()
        else:
            """""".strip()



# NOT DECOMPILED: pick_best_file


# Original qualified name: pick_best_file.<locals>._score
def _score(f):
    nonlocal h_key
    __temp_23114 = f.get(h_key)
    if not __temp_23114:
        h = int(0)
    else:
        h = int(__temp_23114)
    if h >= TARGET_HEIGHT:
        below = 0
    else:
        below = 1
    return below, abs(h - TARGET_HEIGHT)



# NOT DECOMPILED: download_clip
