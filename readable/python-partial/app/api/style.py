# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/style.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: list_style_presets
def list_style_presets(db):
    return {'presets': svc.list_presets(db)}



# Original qualified name: create_style_preset
def create_style_preset(body, db):
    return svc.create_preset(db, body.name, body.style, body.is_default)



# Original qualified name: update_style_preset
def update_style_preset(preset_id, body, db):
    return svc.update_preset(db, preset_id, body.name, body.style, body.is_default)



# Original qualified name: delete_style_preset
def delete_style_preset(preset_id, db):
    svc.delete_preset(db, preset_id)
    return {'deleted': preset_id}



# NOT DECOMPILED: apply_style


# NOT DECOMPILED: render_video_frame
