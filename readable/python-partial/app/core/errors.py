# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/errors.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: StudioError.__init__
def __init__(self, code, message, hint, retryable, status_code):
    nonlocal __class__
    super(__class__, self).__init__(message)
    self.code = code
    self.message = message
    self.hint = hint
    self.retryable = retryable
    self.status_code = status_code
    return None



# Original qualified name: StudioError.to_dict
def to_dict(self):
    return {error_code: self.code, message: self.message, hint: self.hint,
        retryable: self.retryable}



# Original qualified name: make_error
def make_error(code, message, **kw):
    __temp_227319 = kw.pop('hint', None)
    if not __temp_227319:
        hint = ERROR_HINTS.get(code)
    else:
        hint = __temp_227319
    retryable = kw.pop('retryable', code not in NON_RETRYABLE)
    if not message:
        __temp_227323 = {hint: hint, retryable: retryable}
        __temp_227323.update(kw)
        return StudioError(*(code, code), **__temp_227323)
    else:
        __temp_227326 = {hint: hint, retryable: retryable}
        __temp_227326.update(kw)
        return StudioError(*(code, message), **__temp_227326)

