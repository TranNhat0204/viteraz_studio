# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/media/logo_zoom.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: safe_zoom_pct


# Original qualified name: safe_zoom_factor
def safe_zoom_factor():
    return 1.0 + safe_zoom_pct() / 100.0



# Original qualified name: zoom_dims
def zoom_dims(w, h, factor):
    if factor is None:
        z = safe_zoom_factor()
    else:
        z = factor
    return max(2, int(round(w * z)) // 2 * 2), max(2, int(round(h * z)) // 2 * 2)



# Original qualified name: cover_zoom_vf
def cover_zoom_vf(w, h, fps, factor):
    __temp_228792, __temp_228793 = zoom_dims(w, h, factor)
    zw = __temp_228792
    zh = __temp_228793
    if fps:
        fps_part = 'fps=' + str(fps) + ','
    else:
        fps_part = ''
    return 'scale=' + str(zw) + ':' + str(zh
        ) + ':force_original_aspect_ratio=increase:flags=lanczos,crop=' + str(w
        ) + ':' + str(h) + ',' + str(fps_part) + 'format=yuv420p,setsar=1'



# NOT DECOMPILED: zoom_crop_image
