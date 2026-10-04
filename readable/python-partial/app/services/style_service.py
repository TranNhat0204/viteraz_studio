# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/style_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _starter_presets
def _starter_presets():
    base = copy.deepcopy(DEFAULT_STYLE)
    yellow = copy.deepcopy(DEFAULT_STYLE)
    yellow['color']['text'] = '#FFD400'
    yellow['box']['enabled'] = False
    yellow['color']['outline'] = '#000000'
    yellow['color']['outline_width'] = 3.5
    yellow['effect'] = {type: 'fade', in_ms: 120, out_ms: 100, karaoke_color:
        '#FFD700'}
    karaoke = copy.deepcopy(DEFAULT_STYLE)
    karaoke['color']['text'] = '#FFFFFF'
    karaoke['box']['enabled'] = False
    karaoke['color']['outline_width'] = 3.0
    karaoke['effect'] = {type: 'karaoke', in_ms: 80, out_ms: 80, karaoke_color:
        '#FFD400'}
    return [{name: 'Cơ bản — chữ trắng nền đen', style: base, is_default: 1}, {
        name: 'Vàng đậm viền đen', style: yellow, is_default: 0}, {name:
        'Karaoke vàng', style: karaoke, is_default: 0}]



# Original qualified name: seed_default_presets
def seed_default_presets():
    with SessionLocal() as __temp_276574:
        db = __temp_276574
        if db.scalar(select(StylePreset.id).limit(1)):
            return None
        for __temp_276580 in iter(_starter_presets()):
            p = __temp_276580
            db.add(StylePreset(name=p['name'], style_json=json.dumps(p['style'],
                ensure_ascii=False), is_default=p['is_default']))
            continue
        db.commit()
        return None



# NOT DECOMPILED: _to_dict


# NOT DECOMPILED: list_presets


# Original qualified name: get_preset
def get_preset(db, preset_id):
    p = db.get(StylePreset, preset_id)
    if not p:
        raise StudioError(E.UNKNOWN, 'Preset không tồn tại', status_code=404)
    return p



# Original qualified name: _clear_default
def _clear_default(db):
    for __temp_276603 in iter(db.scalars(select(StylePreset).where(StylePreset.
        is_default == 1)).all()):
        p = __temp_276603
        p.is_default = 0
        continue
    return None



# Original qualified name: create_preset
def create_preset(db, name, style, is_default):
    if not name:
        name = ''.strip()
    else:
        name = name.strip()
    if not name:
        raise StudioError(E.UNKNOWN, 'Tên preset không được rỗng', status_code=422)
    if db.scalar(select(StylePreset).where(StylePreset.name == name)):
        raise StudioError(E.UNKNOWN, "Đã tồn tại preset tên '" + str(name) +
            "'", status_code=409)
    if not style:
        style = validate_style(copy.deepcopy(DEFAULT_STYLE))
    else:
        style = validate_style(style)
    if is_default:
        _clear_default(db)
        __temp_276615 = json.dumps(style, ensure_ascii=False)
    else:
        json.dumps(style, ensure_ascii=False)
    if is_default:
        p = StylePreset(name=name, style_json=__temp_276615, is_default=1)
    else:
        p = StylePreset(name=name, style_json=__temp_276615, is_default=0)
    db.add(p)
    db.commit()
    db.refresh(p)
    return _to_dict(p)



# Original qualified name: update_preset
def update_preset(db, preset_id, name, style, is_default):
    p = get_preset(db, preset_id)
    if name is not None:
        if name.strip():
            p.name = name.strip()
    if style is not None:
        p.style_json = json.dumps(validate_style(style), ensure_ascii=False)
    if is_default is not None:
        if is_default:
            _clear_default(db)
        if is_default:
            p.is_default = 1
        else:
            p.is_default = 0
    db.commit()
    db.refresh(p)
    return _to_dict(p)



# Original qualified name: delete_preset
def delete_preset(db, preset_id):
    p = get_preset(db, preset_id)
    db.delete(p)
    db.commit()
    return None



# NOT DECOMPILED: resolve_style_for_config
