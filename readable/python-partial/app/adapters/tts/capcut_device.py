# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/capcut_device.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _read_int_setting


# NOT DECOMPILED: _gen_numeric_id


# Original qualified name: _new_device_row
def _new_device_row(reason, default_iid):
    return CapcutDevice(device_id=_gen_numeric_id(), tdid=_gen_numeric_id(),
        iid=default_iid, active=1, use_count=0, rotated_reason=reason)



# NOT DECOMPILED: _default_iid


# Original qualified name: _should_rotate
def _should_rotate(dev, max_age_hours, max_uses):
    if dev.use_count is not None:
        if dev.use_count >= max_uses:
            return usage
    created = dev.created_at
    if created is not None:
        if datetime.utcnow() - created >= timedelta(hours=max_age_hours):
            return age
    return None



# Original qualified name: get_active_device
def get_active_device():
    with SessionLocal() as __temp_23465:
        db = __temp_23465
        max_age = _read_int_setting(db, 'capcut_device_max_age_hours',
            _DEFAULT_MAX_AGE_HOURS)
        max_uses = _read_int_setting(db, 'capcut_device_max_uses',
            _DEFAULT_MAX_USES)
        dev = db.query(CapcutDevice).filter(CapcutDevice.active == 1).order_by(
            CapcutDevice.created_at.desc()).first()
        if dev is None:
            dev = _new_device_row('init', _default_iid())
            db.add(dev)
            db.flush()
            log.info('capcut-tts: created first device (' + str(dev.device_id[
                None:6]) + '...)')
        else:
            reason = _should_rotate(dev, max_age, max_uses)
            if reason:
                dev.active = 0
                if not dev.iid:
                    new = _new_device_row(reason, _default_iid())
                else:
                    new = _new_device_row(reason, dev.iid)
                db.add(new)
                db.flush()
                log.info('capcut-tts: rotated device (' + str(reason) + ') ' +
                    str(dev.device_id[None:6]) + '... -> ' + str(new.device_id[
                    None:6]) + '...')
                dev = new
        if not dev.use_count:
            dev.use_count = 0 + 1
        else:
            dev.use_count = dev.use_count + 1
        dev.last_used_at = datetime.utcnow()
        override = {device_id: dev.device_id, tdid: dev.tdid}
        if dev.iid:
            override['iid'] = dev.iid
        db.commit()



# Original qualified name: force_rotate
def force_rotate(reason):
    with SessionLocal() as __temp_23490:
        db = __temp_23490
        for __temp_23494 in iter(db.query(CapcutDevice).filter(CapcutDevice.
            active == 1).all()):
            row = __temp_23494
            row.active = 0
            continue
        new = _new_device_row(reason, _default_iid())
        db.add(new)
        db.flush()
        override = {device_id: new.device_id, tdid: new.tdid}
        if new.iid:
            override['iid'] = new.iid
        db.commit()
        log.info('capcut-tts: forced device rotation (' + str(reason) + ') -> ' +
            str(new.device_id[None:6]) + '...')

