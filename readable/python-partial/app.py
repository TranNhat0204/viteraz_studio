# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _wmi_query_disabled
def _wmi_query_disabled(*_args, **_kwargs):
    raise OSError('WMI query disabled to avoid winmgmt hang (Py3.13 Windows)')

