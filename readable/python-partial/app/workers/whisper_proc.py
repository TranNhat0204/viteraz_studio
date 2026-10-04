# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/workers/whisper_proc.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _early_cpu_threads


# Original qualified name: format_srt_time
def format_srt_time(ms):
    h = ms // 3600000
    m = ms % 3600000 // 60000
    s = ms % 60000 // 1000
    ms_remain = ms % 1000
    return format(h, '02d') + ':' + format(m, '02d') + ':' + format(s, '02d'
        ) + ',' + format(ms_remain, '03d')



# Original qualified name: format_vtt_time
def format_vtt_time(ms):
    h = ms // 3600000
    m = ms % 3600000 // 60000
    s = ms % 60000 // 1000
    ms_remain = ms % 1000
    return format(h, '02d') + ':' + format(m, '02d') + ':' + format(s, '02d'
        ) + '.' + format(ms_remain, '03d')



# Original qualified name: _emit
def _emit(obj):
    print(json.dumps(obj, ensure_ascii=True))
    sys.stdout.flush()
    return None



# Original qualified name: _snap_to_words
def _snap_to_words(start_ms, end_ms, words):
    __temp_279423 = words[0].get('start_ms')
    if not __temp_279423:
        ws = int(0)
    else:
        ws = int(__temp_279423)
    __temp_279426 = words[-1].get('end_ms')
    if not __temp_279426:
        we_ = int(0)
    else:
        we_ = int(__temp_279426)
    new_end = end_ms
    new_start = start_ms
    if 0 < ws - start_ms:
        if ws - start_ms <= _SNAP_MAX_MS:
            new_start = ws
    if 0 < end_ms - we_:
        if end_ms - we_ <= _SNAP_MAX_MS:
            new_end = we_
    if new_end - new_start < 120:
        return start_ms, end_ms
    return new_start, new_end



# NOT DECOMPILED: _blocked_fe_class


# Original qualified name: _blocked_fe_class.<locals>.BlockedFeatureExtractor.__call__
def __call__(self, waveform, padding, chunk_length):
    nonlocal __class__, np
    if chunk_length is not None:
        self.n_samples = chunk_length * self.sampling_rate
        self.nb_max_frames = self.n_samples // self.hop_length
    if isinstance(waveform, np.ndarray):
        if waveform.ndim != 1:
            return super(__class__, self).__call__(waveform, padding=padding)
    else:
        return super(__class__, self).__call__(waveform, padding=padding)
    hop = self.hop_length
    n_fft = self.n_fft
    pad = n_fft // 2
    n = waveform.shape[0]
    if n < self.sampling_rate:
        return super(__class__, self).__call__(waveform, padding=padding)
    if waveform.dtype is not np.float32:
        waveform = waveform.astype(np.float32)
    tail = n + padding
    padded = np.zeros((1, tail + 2 * pad), dtype=np.float32)
    padded[0, slice(pad, pad + n)] = waveform
    padded[0, slice(None, pad)] = waveform[slice(pad, 0, -1)]
    padded[0, slice(pad + tail, None)] = padded[0, slice(pad + tail - 2, pad +
        tail - 2 - pad, -1)]
    n_frames = 1 + (padded.shape[1] - n_fft) // hop - 1
    window = np.hanning(n_fft + 1)[None:-1].astype('float32')
    frames = np.lib.stride_tricks.as_strided(padded, (1, n_frames, n_fft), (
        padded.strides[0], hop * padded.strides[1], padded.strides[1]))
    mag = np.empty((self.mel_filters.shape[1], n_frames), dtype=np.float32)
    for __temp_279443 in iter(range(0, n_frames, _MEL_BLOCK_FRAMES)):
        i0 = __temp_279443
        i1 = min(i0 + _MEL_BLOCK_FRAMES, n_frames)
        spec = np.fft.rfft(frames[0, slice(i0, i1), slice(None, None)] * window,
            n=n_fft, axis=-1).astype('complex64')
        mag[slice(None, None), slice(i0, i1)] = np.abs(spec.T) ** 2
        continue
    mel = self.mel_filters @ mag
    np.clip(mel, 1e-10, None, out=mel)
    np.log10(mel, out=mel)
    np.maximum(mel, mel.max() - 8.0, out=mel)
    mel += 4.0
    mel /= 4.0
    return mel



# NOT DECOMPILED: _install_blocked_features


# NOT DECOMPILED: load_model


# Original qualified name: load_model.<locals>._ct
def _ct(dev):
    nonlocal compute_type
    if compute_type:
        return compute_type
    if dev == 'cuda':
        return 'int8_float16'
    return 'int8'



# Original qualified name: load_model.<locals>._build
def _build(dev):
    nonlocal WhisperModel, _ct, model_dir_path
    return WhisperModel(str(model_dir_path), device=dev, compute_type=_ct(dev),
        cpu_threads=_CPU_THREADS, num_workers=1)



# NOT DECOMPILED: _make_batched


# NOT DECOMPILED: transcribe_one


# NOT DECOMPILED: classify_error


# NOT DECOMPILED: _validate_inputs


# NOT DECOMPILED: _write_result


# NOT DECOMPILED: serve


# NOT DECOMPILED: one_shot


# Original qualified name: main
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--serve', action='store_true', help=
        'Chế độ thường trú: nạp model 1 lần, phục vụ nhiều yêu cầu qua stdin.')
    parser.add_argument('--audio-path')
    parser.add_argument('--model-dir-path', required=True)
    parser.add_argument('--device', default='cpu')
    parser.add_argument('--compute-type', default=None)
    parser.add_argument('--cpu-threads', type=int, default=0)
    parser.add_argument('--src-lang', default='auto')
    parser.add_argument('--out-srt')
    parser.add_argument('--out-vtt')
    parser.add_argument('--out-result', default=None)
    parser.add_argument('--word-timestamps', action='store_true')
    parser.add_argument('--snap-words', action='store_true')
    parser.add_argument('--no-vad', action='store_true')
    parser.add_argument('--no-condition-prev', action='store_true', help=
        'Tắt condition_on_previous_text (đường CĂN TIMING).')
    parser.add_argument('--greedy-temp', action='store_true', help=
        'Ghim temperature=[0.0] — tái lập được và nhanh hơn nhiều lần. CHỈ cho đường CĂN TIMING, không dùng cho phụ đề.'
        )
    parser.add_argument('--batch-size', type=int, default=1)
    parser.add_argument('--beam-size', type=int, default=5)
    args = parser.parse_known_args()[0]
    if args.serve:
        serve(Path(args.model_dir_path), args.device, args.compute_type)
        return None
    if args.audio_path:
        if args.out_srt:
            if not args.out_vtt:
                _emit({type: 'result', status: 'failed', error_code:
                    'WHISPER_AUDIO_INVALID', error_message:
                    'Thiếu tham số --audio-path/--out-srt/--out-vtt'})
                sys.exit(2)
                one_shot(args)
                return None
            else:
                one_shot(args)
                return None
        else:
            _emit({type: 'result', status: 'failed', error_code:
                'WHISPER_AUDIO_INVALID', error_message:
                'Thiếu tham số --audio-path/--out-srt/--out-vtt'})
            sys.exit(2)
            one_shot(args)
            return None
    else:
        _emit({type: 'result', status: 'failed', error_code:
            'WHISPER_AUDIO_INVALID', error_message:
            'Thiếu tham số --audio-path/--out-srt/--out-vtt'})
        sys.exit(2)
        one_shot(args)
        return None

