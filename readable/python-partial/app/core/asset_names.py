# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/asset_names.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: strip_accents


# Original qualified name: slug
def slug(s, n, default):
    if not s:
        out = re.sub('[^a-zA-Z0-9]+', '_', strip_accents('').strip().lower()
            ).strip('_')
    else:
        out = re.sub('[^a-zA-Z0-9]+', '_', strip_accents(s).strip().lower()).strip(
            '_')
    if not out[None:n]:
        return default
    else:
        return out[None:n]



# Original qualified name: placeholder_stem
def placeholder_stem(stem):
    return str(stem) + str(PLACEHOLDER_MARK)



# Original qualified name: is_placeholder
def is_placeholder(path):
    if not path:
        raw = str('').strip()
    else:
        raw = str(path).strip()
    if not raw:
        return False
    return Path(raw).stem.endswith(PLACEHOLDER_MARK)

