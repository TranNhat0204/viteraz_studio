# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/cast_refine_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: enabled
def enabled(profile):
    if _HARD_DISABLED:
        return False
    if not profile:
        return bool({}.get(PROFILE_KEY))
    else:
        return bool(profile.get(PROFILE_KEY))



# Original qualified name: _norm
def _norm(s):
    if not s:
        return ''.strip().lower()
    else:
        return s.strip().lower()



# Original qualified name: _schema
def _schema():
    return {'mode': 'named' | 'archetype', 'characters': [{'name':
        '<tên dùng trong kịch bản>', 'matches':
        '<tên cũ trong dàn tạm nếu là CÙNG một người, else null>', 'is_main':
        true, 'description':
        '<mô tả vẽ lại: tuổi, giới, sắc tộc, tóc, mặt, dáng, trang phục đặc trưng>'
        }]}



# NOT DECOMPILED: build_prompt


# NOT DECOMPILED: merge


# NOT DECOMPILED: refine
