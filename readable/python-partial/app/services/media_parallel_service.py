# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/media_parallel_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _value
def _value(db, key, default):
    if not hasattr(db, 'get'):
        return default
    row = db.get(Setting, key)
    if row is not None:
        if row.value is not None:
            return str(row.value)
    return default



# NOT DECOMPILED: _bounded_int


# Original qualified name: get_config
def get_config(db):
    return MediaParallelConfig(enabled=_value(db, 'media_parallel_enabled', '0'
        ) == '1', max_profiles=_bounded_int(_value(db,
        'media_parallel_max_profiles', '3'), 3, 1, 10), min_scenes_per_profile=
        _bounded_int(_value(db, 'media_parallel_min_scenes_per_profile', '10'),
        10, 1, 100), auto_failover=_value(db, 'media_parallel_auto_failover',
        '1') != '0')



# Original qualified name: worker_count
def worker_count(scene_count, available_profiles, config):
    if not scene_count <= 0:
        if available_profiles <= 0:
            return 0
    else:
        return 0
    if not config.enabled:
        return 1
    useful = max(1, (scene_count + config.min_scenes_per_profile - 1) // config
        .min_scenes_per_profile)
    return min(available_profiles, config.max_profiles, useful)



# Original qualified name: contiguous_partitions
def contiguous_partitions(items, lanes):
    if items:
        if lanes <= 0:
            return []
    else:
        return []
    lanes = min(lanes, len(items))
    __temp_275496, __temp_275497 = divmod(len(items), lanes)
    base = __temp_275496
    extra = __temp_275497
    out = []
    cursor = 0
    for __temp_275500 in iter(range(lanes)):
        lane = __temp_275500
        if lane < extra:
            size = base + 1
        else:
            size = base + 0
        out.append(items[cursor:cursor + size])
        cursor += size
        continue
    return out



# Original qualified name: assigned_lanes
def assigned_lanes(items, assignments):
    grouped = {}
    for __temp_275503 in iter(items):
        item = __temp_275503
        grouped.setdefault(assignments[item], []).append(item)
        continue
    return list(grouped.values())

