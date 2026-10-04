# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_errors.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: FbError.__str__
def __str__(self):
    return '[' + str(self.kind) + '] ' + str(self.message) + ' (fb_code=' + str(
        self.fb_code) + ')'



# NOT DECOMPILED: translate_error


# Original qualified name: should_fallback_reels
def should_fallback_reels(err):
    if isinstance(err, FbError):
        return err.kind == 'reels_fallback'
    return False

