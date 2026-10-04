# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/media/flow_watermark.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _setting_enabled


# Original qualified name: is_flow_watermark_enabled
def is_flow_watermark_enabled(media_type):
    if not _setting_enabled('flow_watermark_removal_enabled', False):
        return False
    if media_type == 'image':
        suffix = 'images'
    else:
        suffix = 'videos'
    return _setting_enabled('flow_watermark_removal_' + str(suffix), True)



# Original qualified name: geometry_key
def geometry_key(media_type, width, height):
    return str(media_type) + ':' + str(int(width)) + 'x' + str(int(height))



# NOT DECOMPILED: _state_file


# NOT DECOMPILED: _read_json


# NOT DECOMPILED: _write_json


# NOT DECOMPILED: remember_geometry


# Original qualified name: locked_detection
def locked_detection(media_type, width, height):
    if not width <= 0:
        if height <= 0:
            return None
    else:
        return None
    with _STATE_LOCK as __temp_228222:
        __temp_228225 = _read_json(_GEOMETRY_FILE).get(geometry_key(media_type,
            width, height))
        if not __temp_228225:
            entry = {}
        else:
            entry = __temp_228225
        if not entry.get('samples'):
            __temp_228229 = []
            __temp_228230 = []
        else:
            []
        for __temp_228232 in iter(__temp_228229):
            s = __temp_228232
            if not isinstance(s, list):
                continue
                __temp_228234 = len(s)
            else:
                len(s)
            if not __temp_228234 == 3:
                continue
                __temp_228230.append(s)
            else:
                __temp_228230.append(s)
            continue
        rows = __temp_228230
        if len(rows) < _GEOMETRY_MIN_AGREE:
            return None
        arr = np.asarray(rows, dtype=np.float64)
        centres = np.stack([arr[slice(None, None), 0] + arr[slice(None, None), 
            2] / 2.0, arr[slice(None, None), 1] + arr[slice(None, None), 2] / 
            2.0], axis=1)
        med_centre = np.median(centres, axis=0)
        keep = np.hypot(centres[slice(None, None), 0] - med_centre[0], centres[
            slice(None, None), 1] - med_centre[1]) <= 10.0
        if int(keep.sum()) < _GEOMETRY_MIN_AGREE:
            return None
        med = np.median(arr[keep], axis=0)
        size = max(15, int(round(float(med[2]))) | 1)
        x = max(0, min(width - size, int(round(float(med[0])))))
        y = max(0, min(height - size, int(round(float(med[1])))))
        return Detection(x, y, size, 0.0, frame_width=width, frame_height=height)
    s = __temp_228222.__exit__



# NOT DECOMPILED: _ledger_stamp


# Original qualified name: ledger_says_clean
def ledger_says_clean(path):
    stamp = _ledger_stamp(path)
    if stamp is None:
        return False
    with _STATE_LOCK as __temp_228263:
        _read_json(_LEDGER_FILE).get(str(path.resolve()).lower())



# Original qualified name: ledger_mark_clean
def ledger_mark_clean(path):
    stamp = _ledger_stamp(path)
    if stamp is None:
        return None
    with _STATE_LOCK as __temp_228271:
        book = _read_json(_LEDGER_FILE)
        book[str(path.resolve()).lower()] = stamp
        if len(book) > _LEDGER_KEEP:
            book = dict(list(book.items())[-_LEDGER_KEEP:None])
        _write_json(_LEDGER_FILE, book)
        return None



# Original qualified name: pending_add
def pending_add(path, media_type, width, height):
    stamp = _ledger_stamp(path)
    if stamp is None:
        return None
    with _STATE_LOCK as __temp_228283:
        book = _read_json(_PENDING_FILE)
        book[str(path.resolve()).lower()] = {stamp: stamp, key: geometry_key(
            media_type, width, height), media: media_type, w: int(width), h:
            int(height), at: int(time.time())}
        _write_json(_PENDING_FILE, book)
        return None



# Original qualified name: pending_drop
def pending_drop(path):
    key = str(path.resolve()).lower()
    with _STATE_LOCK as __temp_228299:
        book = _read_json(_PENDING_FILE)
        if book.pop(key, None) is not None:
            _write_json(_PENDING_FILE, book)
            return None
        else:
            return None



# Original qualified name: pending_for
def pending_for(media_type, width, height):
    want = geometry_key(media_type, width, height)
    with _STATE_LOCK as __temp_228306:
        book = _read_json(_PENDING_FILE)
        out = []
        stale = []
        for __temp_228312 in iter(book.items()):
            __temp_228313, __temp_228314 = __temp_228312
            raw = __temp_228313
            meta = __temp_228314
            if isinstance(meta, dict):
                if meta.get('key') != want:
                    continue
                    path = Path(raw)
                else:
                    path = Path(raw)
            else:
                continue
                path = Path(raw)
            if not path.is_file():
                stale.append(raw)
                continue
                out.append(path)
            else:
                out.append(path)
            continue
        if stale:
            with _STATE_LOCK as __temp_228324:
                book = _read_json(_PENDING_FILE)
                for __temp_228326 in iter(stale):
                    raw = __temp_228326
                    book.pop(raw, None)
                    continue
                _write_json(_PENDING_FILE, book)
                return out
                return out
        return out



# Original qualified name: pending_count
def pending_count():
    with _STATE_LOCK as __temp_228330:
        len(_read_json(_PENDING_FILE))



# Original qualified name: _sparkle_mask
def _sparkle_mask(size):
    size = max(21, int(size) | 1)
    ss = 4
    n = size * ss
    axis = (np.arange(n, dtype=np.float32) + 0.5) / n * 2.0 - 1.0
    __temp_228338, __temp_228339 = np.meshgrid(axis, axis)
    xx = __temp_228338
    yy = __temp_228339
    implicit = np.power(np.abs(xx) / 0.93, 0.6666666666666666) + np.power(np.
        abs(yy), 0.6666666666666666)
    coverage = np.clip((1.025 - implicit) * 20.0, 0.0, 1.0)
    return coverage.reshape(size, ss, size, ss).mean(axis=(1, 3)).astype(np.float32
        )



# Original qualified name: _luma
def _luma(rgb):
    a = rgb.astype(np.float32, copy=False)
    return a[Ellipsis, 0] * 0.2126 + a[Ellipsis, 1] * 0.7152 + a[Ellipsis, 2
        ] * 0.0722



# Original qualified name: _ncc_at
def _ncc_at(luma, mask, x, y):
    __temp_228349, __temp_228350 = mask.shape
    h = __temp_228349
    w = __temp_228350
    patch = luma[slice(y, y + h), slice(x, x + w)]
    if patch.shape != mask.shape:
        return -1.0
    p = patch - float(patch.mean())
    m = mask - float(mask.mean())
    denom = math.sqrt(float(np.sum(p * p)) * float(np.sum(m * m)))
    if denom > 1e-06:
        return float(np.sum(p * m) / denom)
    return 0.0



# Original qualified name: _has_logo_contrast
def _has_logo_contrast(luma, mask, x, y):
    patch = luma[slice(y, y + mask.shape[0]), slice(x, x + mask.shape[1])]
    if patch.shape != mask.shape:
        return False
    outside = mask < 0.02
    core = mask > 0.35
    if np.any(core):
        if not np.any(outside):
            return False
    else:
        return False
    background = float(patch[outside].mean())
    delta = float(patch[core].mean()) - background
    if delta <= 0.0:
        return False
    return delta >= max(1.5, min(20.0, (255.0 - background) * 0.22))



# Original qualified name: _cached_detection
def _cached_detection(luma, media_type):
    __temp_228370, __temp_228371 = luma.shape
    h = __temp_228370
    w = __temp_228371
    key = media_type, w, h
    with _CACHE_LOCK as __temp_228372:
        hit = _LOCATION_CACHE.get(key)
        if hit is None:
            return None
        score = _ncc_at(luma, _sparkle_mask(hit.size), hit.x, hit.y)
        if score >= 0.47:
            if _has_logo_contrast(luma, _sparkle_mask(hit.size), hit.x, hit.y):
                return Detection(hit.x, hit.y, hit.size, score, hit.gain)
        return None



# NOT DECOMPILED: detect_watermark


# Original qualified name: residual_sparkle
def residual_sparkle(rgb, threshold):
    luma = _luma(rgb)
    __temp_228428, __temp_228429 = luma.shape
    h = __temp_228428
    w = __temp_228429
    short = min(w, h)
    if short < 240:
        return None
    best = None
    for __temp_228431 in iter((0.045, 0.051, 0.058, 0.066, 0.073, 0.08, 0.09)):
        ratio = __temp_228431
        size = max(15, int(round(short * ratio)) | 1)
        mask = _sparkle_mask(size)
        cx = int(round(w - 0.126 * short - size / 2))
        cy = int(round(h - 0.126 * short - size / 2))
        radius = max(12, int(round(short * 0.055)))
        for __temp_228446 in iter(range(max(0, cy - radius), min(h - size, cy +
            radius) + 1, 2)):
            y = __temp_228446
            for __temp_228450 in iter(range(max(0, cx - radius), min(w - size, 
                cx + radius) + 1, 2)):
                x = __temp_228450
                score = _ncc_at(luma, mask, x, y)
                if best is not None:
                    if not score > best.ncc:
                        continue
                        best = Detection(x, y, size, score, frame_width=w,
                            frame_height=h)
                    else:
                        best = Detection(x, y, size, score, frame_width=w,
                            frame_height=h)
                else:
                    best = Detection(x, y, size, score, frame_width=w,
                        frame_height=h)
                continue
            continue
        continue
    if best is not None:
        if best.ncc < threshold:
            return None
    else:
        return None
    patch = luma[slice(best.y, best.y + best.size), slice(best.x, best.x + best
        .size)]
    template = _sparkle_mask(best.size)
    outside = template < 0.02
    core = template > 0.35
    if np.any(core):
        if not np.any(outside):
            return None
    else:
        return None
    if float(patch[core].mean() - patch[outside].mean()) < 1.0:
        return None
    return best



# NOT DECOMPILED: _detect_watermark_relaxed


# Original qualified name: _restore_roi
def _restore_roi(rgb, detection, require_improvement):
    size = detection.size
    y = detection.y
    x = detection.x
    template = _sparkle_mask(size)
    before = _ncc_at(_luma(rgb), template, x, y)
    pad_px = max(5, int(round(size * 0.14)))
    y0 = max(0, y - pad_px)
    x0 = max(0, x - pad_px)
    y1 = min(rgb.shape[0], y + size + pad_px)
    x1 = min(rgb.shape[1], x + size + pad_px)
    observed = rgb[slice(y0, y1), slice(x0, x1)].astype(np.float32)
    coverage = np.zeros(observed.shape[None:2], dtype=np.float32)
    oy = y - y0
    ox = x - x0
    coverage[slice(oy, oy + size), slice(ox, ox + size)] = template
    best = None
    for __temp_228509 in iter(np.linspace(0.42, 0.92, 11, dtype=np.float32)):
        gain = __temp_228509
        alpha = np.clip(coverage * gain, 0.0, 0.94)[Ellipsis, None]
        restored = np.clip((observed - alpha * 255.0) / np.maximum(1.0 - alpha,
            0.06), 0, 255)
        lum = _luma(restored)
        score = abs(_ncc_at(lum, coverage, 0, 0))
        rough = float(np.mean(np.abs(np.diff(lum, axis=0))) + np.mean(np.abs(np
            .diff(lum, axis=1))))
        objective = score + rough / 900.0
        if best is not None:
            if not objective < best[0]:
                continue
                best = objective, float(gain), restored
            else:
                best = objective, float(gain), restored
        else:
            best = objective, float(gain), restored
        continue
    if best is None:
        return None
    __temp_228526, __temp_228527, __temp_228528 = best
    _ = __temp_228526
    gain = __temp_228527
    restored = __temp_228528
    alpha = np.clip(coverage * gain, 0.0, 1.0)[Ellipsis, None]
    __temp_228530, __temp_228531 = np.ogrid[slice(None, coverage.shape[0]),
        slice(None, coverage.shape[1])]
    gy = __temp_228530
    gx = __temp_228531
    cy = oy + (size - 1) / 2.0
    cx = ox + (size - 1) / 2.0
    distance = np.sqrt((gx - cx) ** 2 + (gy - cy) ** 2)
    fill_radius = size * 0.64
    core = distance <= fill_radius
    filled = restored.copy()
    if np.any(~core):
        horizontal = observed.copy()
        vertical = observed.copy()
        h_weight = np.zeros(core.shape, dtype=np.float32)
        v_weight = np.zeros(core.shape, dtype=np.float32)
        for __temp_228540 in iter(range(core.shape[0])):
            row = __temp_228540
            inside = np.flatnonzero(core[row])
            if not inside.size:
                continue
                left = max(0, int(inside[0]) - 2)
            else:
                left = max(0, int(inside[0]) - 2)
            right = min(core.shape[1] - 1, int(inside[-1]) + 2)
            span = max(1, right - left)
            t = ((inside - left) / span).astype(np.float32)[slice(None, None), None
                ]
            horizontal[row, inside] = observed[row, left] * (1.0 - t) + observed[
                row, right] * t
            reliability = 1.0 / (1.0 + float(np.mean(np.abs(observed[row, left] -
                observed[row, right]))))
            h_weight[row, inside] = reliability
            continue
        for __temp_228554 in iter(range(core.shape[1])):
            col = __temp_228554
            inside = np.flatnonzero(core[slice(None, None), col])
            if not inside.size:
                continue
                top = max(0, int(inside[0]) - 2)
            else:
                top = max(0, int(inside[0]) - 2)
            bottom = min(core.shape[0] - 1, int(inside[-1]) + 2)
            span = max(1, bottom - top)
            t = ((inside - top) / span).astype(np.float32)[slice(None, None), None]
            vertical[inside, col] = observed[top, col] * (1.0 - t) + observed[
                bottom, col] * t
            reliability = 1.0 / (1.0 + float(np.mean(np.abs(observed[top, col] -
                observed[bottom, col]))))
            v_weight[inside, col] = reliability
            continue
        weight_sum = np.maximum(h_weight + v_weight, 1e-06)[Ellipsis, None]
        directional = (horizontal * h_weight[Ellipsis, None] + vertical *
            v_weight[Ellipsis, None]) / weight_sum
        filled[core] = directional[core]
        for __temp_228569 in iter(range(8)):
            _ = __temp_228569
            pad = np.pad(filled, ((1, 1), (1, 1), (0, 0)), mode='edge')
            neighbours = (pad[slice(None, -2), slice(1, -1)] + pad[slice(2,
                None), slice(1, -1)] + pad[slice(1, -1), slice(None, -2)] + pad
                [slice(1, -1), slice(2, None)]) * 0.25
            filled[core] = filled[core] * 0.72 + neighbours[core] * 0.28
            continue
        core_blend = np.clip((fill_radius + 2.5 - distance) / 3.5, 0.0, 1.0)[
            Ellipsis, None]
    else:
        core_blend = np.clip((fill_radius + 2.5 - distance) / 3.5, 0.0, 1.0)[
            Ellipsis, None]
    restored = restored * (1.0 - core_blend) + filled * core_blend
    blend = np.clip(np.maximum(alpha * 1.35, core_blend), 0.0, 1.0)
    candidate = rgb.copy()
    candidate[slice(y0, y1), slice(x0, x1)] = np.clip(observed * (1.0 - blend) +
        restored * blend, 0, 255).astype(np.uint8)
    after = _ncc_at(_luma(candidate), template, x, y)
    if require_improvement:
        if abs(after) > max(0.2, abs(before) * 0.48):
            return None
    return candidate, before, after



# NOT DECOMPILED: _process_image_sync


# Original qualified name: _sample_video_sync
def _sample_video_sync(path):
    av = __import__('av', fromlist=None, level=0)
    samples = []
    with av.open(str(path)) as __temp_228654:
        container = __temp_228654
        stream = container.streams.video[0]
        if not stream.frames:
            total = int(0)
        else:
            total = int(stream.frames)
        targets = [0]
        if total > 6:
            targets += [total // 2, max(0, total - 3)]
        target_i = 0
        for __temp_228662 in iter(enumerate(container.decode(stream))):
            __temp_228663, __temp_228664 = __temp_228662
            index = __temp_228663
            frame = __temp_228664
            if index >= targets[target_i]:
                samples.append(frame.to_ndarray(format='rgb24'))
                target_i += 1
                if target_i >= len(targets):
                    break
                    if not total <= 0:
                        continue
                    if not index in (0, 12, 24):
                        continue
                    if samples:
                        if index != 0:
                            samples.append(frame.to_ndarray(format='rgb24'))
                            __temp_228670 = len(samples)
                        else:
                            len(samples)
                    else:
                        samples.append(frame.to_ndarray(format='rgb24'))
                        len(samples)
                    if not __temp_228670 >= 3:
                        continue
                    break
                else:
                    if not total <= 0:
                        continue
                    if not index in (0, 12, 24):
                        continue
                    if samples:
                        if index != 0:
                            samples.append(frame.to_ndarray(format='rgb24'))
                            __temp_228677 = len(samples)
                        else:
                            len(samples)
                    else:
                        samples.append(frame.to_ndarray(format='rgb24'))
                        len(samples)
                    if not __temp_228677 >= 3:
                        continue
                    break
            else:
                if not total <= 0:
                    continue
                if not index in (0, 12, 24):
                    continue
                if samples:
                    if index != 0:
                        samples.append(frame.to_ndarray(format='rgb24'))
                        __temp_228684 = len(samples)
                    else:
                        len(samples)
                else:
                    samples.append(frame.to_ndarray(format='rgb24'))
                    len(samples)
                if not __temp_228684 >= 3:
                    continue
                break
        return samples



# NOT DECOMPILED: _video_detection


# NOT DECOMPILED: _run_ffmpeg


# Original qualified name: _video_dims
def _video_dims(path):
    av = __import__('av', fromlist=None, level=0)
    with av.open(str(path)) as __temp_228739:
        container = __temp_228739
        frame = next(container.decode(video=0))



# Original qualified name: _write_video_mask
def _write_video_mask(path, found):
    PIL = __import__('PIL', fromlist=('Image',), level=0)
    Image = PIL.Image
    mask = np.zeros((found.frame_height, found.frame_width), dtype=np.uint8)
    sparkle = _sparkle_mask(found.size) > 0.025
    for __temp_228746 in iter(range(2)):
        _ = __temp_228746
        p = np.pad(sparkle, 1, mode='constant')
        sparkle = p[slice(1, -1), slice(1, -1)] | p[slice(None, -2), slice(1, -1)
            ] | p[slice(2, None), slice(1, -1)] | p[slice(1, -1), slice(None, -2)
            ] | p[slice(1, -1), slice(2, None)]
        continue
    y1 = min(found.frame_height, found.y + found.size)
    x1 = min(found.frame_width, found.x + found.size)
    mask[slice(found.y, y1), slice(found.x, x1)] = sparkle[slice(None, y1 -
        found.y), slice(None, x1 - found.x)] * 255
    Image.fromarray(mask).save(path, format='PNG', compress_level=1)
    return None



# Original qualified name: _video_residual
def _video_residual(path, found):
    av = __import__('av', fromlist=None, level=0)
    with av.open(str(path)) as __temp_228754:
        container = __temp_228754
        frame = next(container.decode(video=0))
        rgb = frame.to_ndarray(format='rgb24')
        return _ncc_at(_luma(rgb), _sparkle_mask(found.size), found.x, found.y)



# NOT DECOMPILED: _process_video


# NOT DECOMPILED: _clear_pending


# NOT DECOMPILED: postprocess_flow_asset
