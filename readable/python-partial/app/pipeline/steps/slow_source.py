# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/slow_source.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: slow_factor
def slow_factor(config):
    if not config:
        v = str({}.get('slow_video', 'off')).strip().lower()
    else:
        v = str(config.get('slow_video', 'off')).strip().lower()
    if v in ('15', '15%', '0.85'):
        return 0.85
    if v in ('10', '10%', '0.9', '0.90'):
        return 0.9
    return None



# NOT DECOMPILED: SlowSourceStep.run


# Original qualified name: SlowSourceStep.run.<locals>._assemble
def _assemble(codec_args):
    nonlocal factor, has_audio, orig, tmp
    a = ['-y', '-i', str(orig), '-filter:v', 'setpts=PTS/' + format(factor, 'g')]
    if has_audio:
        a += ['-filter:a', 'atempo=' + format(factor, 'g'), '-c:a', 'aac',
            '-b:a', '192k']
    else:
        a += ['-an']
    __temp_256817 = []
    __temp_256817.extend(codec_args)
    __temp_256817.append('-movflags')
    __temp_256817.append('+faststart')
    __temp_256817.append(str(tmp))
    a += __temp_256817
    return a



# Original qualified name: SlowSourceStep.run.<locals>.on_prog
def on_prog(p):
    nonlocal ctx, pct
    ctx.emit_progress(p, 'Đang làm chậm video ' + str(pct) + '%: ' + str(int(p *
        100)) + '%')
    return None

