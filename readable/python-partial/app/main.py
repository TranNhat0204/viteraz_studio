# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/main.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _wmi_query_disabled
def _wmi_query_disabled(*_args, **_kwargs):
    raise OSError('WMI query disabled to avoid winmgmt hang (Py3.13 Windows)')



# NOT DECOMPILED: lifespan


# NOT DECOMPILED: lifespan.<locals>._omni_warm


# Original qualified name: studio_error_handler
def studio_error_handler(_, exc):
    if not exc.hint:
        __temp_228162 = ERROR_HINTS.get(exc.code)
    if exc.retryable:
        return JSONResponse(status_code=exc.status_code, content={error_code:
            exc.code, message: exc.message, hint: __temp_228162, retryable: exc
            .retryable})
    else:
        return JSONResponse(status_code=exc.status_code, content={error_code:
            exc.code, message: exc.message, hint: __temp_228162, retryable: exc
            .code not in NON_RETRYABLE})



# Original qualified name: main
def main(argv):
    settings = configure_settings(argv)
    configure_file_logging(log)
    uvicorn.run(app, host=settings.host, port=settings.port, log_level='info')
    return None

