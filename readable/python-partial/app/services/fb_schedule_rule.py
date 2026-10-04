# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_schedule_rule.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: ScheduleRule.from_dict


# Original qualified name: ScheduleRule.to_dict
def to_dict(self):
    return {min_interval_min: self.min_interval_min, max_per_day: self.
        max_per_day, time_window: [self.time_window[0].isoformat(), self.
        time_window[1].isoformat()]}



# Original qualified name: clamp_max_per_day
def clamp_max_per_day(value):
    if not value:
        return DEFAULT_MAX_PER_DAY
    return max(MAX_PER_DAY_CLAMP[0], min(MAX_PER_DAY_CLAMP[1], value))



# Original qualified name: _hours_between
def _hours_between(window):
    end = window[1].hour
    start = window[0].hour
    if end < start:
        return list(range(start, 24)) + list(range(0, end + 1))
    return list(range(start, end + 1))



# NOT DECOMPILED: _weighted_hour


# NOT DECOMPILED: pick_publish_time


# Original qualified name: compute_next_schedule
def compute_next_schedule(now, last_post_at, rule, rng):
    if isinstance(rule, ScheduleRule):
        r = rule
    else:
        r = ScheduleRule.from_dict(rule)
    return pick_publish_time(now, last_post_at, r, rng=rng)



# NOT DECOMPILED: validate_schedule_time
