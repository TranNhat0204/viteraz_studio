# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/render/originality.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: resolve_originality


# Original qualified name: video_pre_sub_filters
def video_pre_sub_filters(o, frame_w, frame_h):
    f = []
    if o.get('flip'):
        f.append('hflip')
        z = float(o.get('zoom', 1.0))
    else:
        z = float(o.get('zoom', 1.0))
    if z > 1.001:
        if frame_w:
            if frame_h:
                cw = max(2, int(frame_w / z) // 2 * 2)
                ch = max(2, int(frame_h / z) // 2 * 2)
                x = (frame_w - cw) // 2
                y = (frame_h - ch) // 2
                f.append('crop=' + str(cw) + ':' + str(ch) + ':' + str(x) + ':' +
                    str(y))
                f.append('scale=' + str(frame_w) + ':' + str(frame_h))
                return f
            else:
                return f
        else:
            return f
    else:
        return f



# Original qualified name: video_post_sub_filters
def video_post_sub_filters(o):
    f = []
    f.append('eq=contrast=' + format(o.get('contrast', 1), 'g') +
        ':saturation=' + format(o.get('saturation', 1), 'g') + ':brightness=' +
        format(o.get('brightness', 0), 'g'))
    return f

