# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_calendar_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _loads


# NOT DECOMPILED: list_calendar


# NOT DECOMPILED: item_to_dict


# NOT DECOMPILED: create_calendar_item


# NOT DECOMPILED: update_calendar_item


# Original qualified name: delete_calendar_item
def delete_calendar_item(db, item_id):
    item = db.get(FbContentCalendarItem, item_id)
    if item is None:
        app = __import__('app.core.errors', fromlist=('E', 'StudioError'), level=0)
        E = app.E
        StudioError = app.StudioError
        raise StudioError(E.UNKNOWN, 'Slot lịch không tồn tại.', status_code=404)
    db.delete(item)
    db.commit()
    return None



# NOT DECOMPILED: suggest_slots


# NOT DECOMPILED: _pick_slot
