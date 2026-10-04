# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/ytdlp_client.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _ensure_local_ytdlp


# NOT DECOMPILED: _patch_bilibili_referer


# Original qualified name: _patch_bilibili_referer.<locals>._patched
def _patched(self, *args, **kwargs):
    nonlocal _orig
    __temp_182529 = kwargs.get('headers')
    if not __temp_182529:
        h = dict({})
    else:
        h = dict(__temp_182529)
    h['Referer'] = 'https://www.bilibili.com/'
    kwargs['headers'] = h
    __temp_182534 = [self]
    __temp_182534.extend(args)
    __temp_182536 = {}
    __temp_182536.update(kwargs)
    return _orig(*tuple(__temp_182534), **__temp_182536)



# Original qualified name: _is_412
def _is_412(exc):
    s = str(exc)
    if '412' in s:
        if not 'Precondition' in s:
            return 'blocked by server' in s
        else:
            return 'Precondition' in s
    else:
        return '412' in s



# NOT DECOMPILED: YtDlpClient.is_available


# NOT DECOMPILED: YtDlpClient._require


# NOT DECOMPILED: YtDlpClient._ffmpeg_dir


# NOT DECOMPILED: YtDlpClient.get_info


# NOT DECOMPILED: YtDlpClient._extract_info


# NOT DECOMPILED: YtDlpClient.download


# Original qualified name: YtDlpClient.download.<locals>.hook
def hook(d):
    nonlocal cancel_check, loop, on_progress
    if cancel_check:
        if cancel_check():
            raise _CancelledDownload()
    if d.get('status') == 'downloading':
        if on_progress:
            __temp_182579 = d.get('total_bytes')
            if not __temp_182579:
                __temp_182580 = d.get('total_bytes_estimate')
                if not __temp_182580:
                    total = 0
                else:
                    total = __temp_182580
            else:
                total = __temp_182579
            __temp_182581 = d.get('downloaded_bytes')
            if not __temp_182581:
                done = 0
            else:
                done = __temp_182581
            if total:
                __temp_182582 = d.get('speed')
                if not __temp_182582:
                    spd = 0 / 1024
                else:
                    spd = __temp_182582 / 1024
                __temp_182583 = d.get('eta')
                if not __temp_182583:
                    eta = 0
                else:
                    eta = __temp_182583
                frac = 0.05 + 0.9 * min(done / total, 1.0)
                msg = str(done // 1048576) + 'MB / ' + str(total // 1048576
                    ) + 'MB · ' + format(spd, '.0f') + 'KB/s · còn ~' + str(eta
                    ) + 's'
                loop.call_soon_threadsafe(on_progress, frac, msg)
                return None
            return None
    if d.get('status') == 'finished':
        if on_progress:
            loop.call_soon_threadsafe(on_progress, 0.96, 'Đang ghép video + audio…'
                )
            return None
        return None
    return None



# NOT DECOMPILED: YtDlpClient._run_download


# NOT DECOMPILED: YtDlpClient._normalize
