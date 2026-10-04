# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/video_format.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: normalize
def normalize(value):
    if value is None:
        return None
    v = str(value).strip().lower()
    if v in _VALID:
        return v
    if v in ('16:9', 'horizontal', 'landscape', 'ngang'):
        return LONG
    if v in ('9:16', 'vertical', 'portrait', 'doc', 'dọc'):
        return SHORT
    return None



# Original qualified name: resolve
def resolve(value):
    if normalize(value) == SHORT:
        return _SHORT
    return _LONG



# Original qualified name: aspect_for
def aspect_for(value):
    return resolve(value).aspect



# NOT DECOMPILED: orientation_hint
