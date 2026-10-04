# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/proc.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: no_window_kwargs
def no_window_kwargs(low_priority):
    if sys.platform == 'win32':
        flags = _CREATE_NO_WINDOW
        if low_priority:
            flags |= _BELOW_NORMAL_PRIORITY
        return {'creationflags': flags}
    if low_priority:
        if hasattr(os, 'nice'):
    
            def __temp_227664():
                return os.nice(5)
            return {'preexec_fn': __temp_227664}
    return {}



# NOT DECOMPILED: kill_tree


# NOT DECOMPILED: terminate_proc


# Original qualified name: cancelled_error
def cancelled_error(where):
    if where:
        return make_error(E.CANCELLED, 'Đã huỷ theo yêu cầu' + str(' — ' +
            where) + '.')
    else:
        return make_error(E.CANCELLED, 'Đã huỷ theo yêu cầu' + str('') + '.')



# NOT DECOMPILED: safe_wait_proc


# NOT DECOMPILED: safe_wait_proc.<locals>.monitor


# NOT DECOMPILED: safe_communicate_proc


# NOT DECOMPILED: safe_communicate_proc.<locals>.monitor
