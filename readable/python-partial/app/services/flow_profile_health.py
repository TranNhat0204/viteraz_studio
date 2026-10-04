# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/flow_profile_health.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _configured_minutes


# Original qualified name: reset_config_cache
def reset_config_cache():
    global _conf
    _conf = None
    return None



# Original qualified name: mark_sick
def mark_sick(partition_id, reason, minutes):
    if not partition_id:
        return None
    if minutes is None:
        mins = _configured_minutes()
    else:
        mins = max(0, int(minutes))
    if mins <= 0:
        return None
    until_mono = time.monotonic() + mins * 60
    until_wall = datetime.now() + timedelta(minutes=mins)
    cur = _SICK.get(partition_id)
    if cur is not None:
        if cur.until_mono > until_mono:
            return cur.until_wall
    _SICK[partition_id] = _Sick(until_mono, until_wall, reason)
    log.info('[flow_health] ' + str(partition_id) + ': tạm ngừng nhận cảnh ' +
        str(mins) + ' phút (tới ' + format(until_wall, '%H:%M') + ') — ' + str(
        reason) + '.')
    return until_wall



# Original qualified name: is_sick
def is_sick(partition_id):
    if not partition_id:
        return False
    s = _SICK.get(partition_id)
    if s is None:
        return False
    if time.monotonic() >= s.until_mono:
        _SICK.pop(partition_id, None)
        return False
    return True



# Original qualified name: sick_info
def sick_info(partition_id):
    if not is_sick(partition_id):
        return None
    s = _SICK[str(partition_id)]
    return {until: s.until_wall, reason: s.reason, seconds_left: max(int(s.
        until_mono - time.monotonic()), 0)}



# Original qualified name: clear_sick
def clear_sick(partition_id):
    if not partition_id:
        return False
    return _SICK.pop(partition_id, None) is not None



# Original qualified name: clear_all
def clear_all():
    _SICK.clear()
    return None



# NOT DECOMPILED: sick_partitions


# NOT DECOMPILED: drop_sick
