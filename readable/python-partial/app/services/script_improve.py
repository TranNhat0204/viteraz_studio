# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/script_improve.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _total_gain


# Original qualified name: _split_parts
def _split_parts(script, limit):
    app = __import__('app.pipeline.steps.script', fromlist=('split_sentences',),
        level=0)
    split_sentences = app.split_sentences
    parts = []
    buf = []
    size = 0
    if not split_sentences(script):
        __temp_276401 = [script]
    for __temp_276402 in iter(__temp_276401):
        sent = __temp_276402
        if buf:
            if size + len(sent) + 1 > limit:
                parts.append('\n'.join(buf))
                size = 0
                buf = []
        buf.append(sent)
        size += len(sent) + 1
        continue
    if buf:
        parts.append('\n'.join(buf))
    if not parts:
        return [script]
    else:
        return parts



# NOT DECOMPILED: _outline_block


# Original qualified name: _norm_sentence
def _norm_sentence(text):
    if not text:
        return re.sub('[^\\w\\s]', '', ''.lower()).strip()
    else:
        return re.sub('[^\\w\\s]', '', text.lower()).strip()



# NOT DECOMPILED: _clean_seams


# NOT DECOMPILED: audit_script_lite


# NOT DECOMPILED: improve_script_lite


# NOT DECOMPILED: normalize_audit


# NOT DECOMPILED: audit_script


# NOT DECOMPILED: _audience_block


# NOT DECOMPILED: _build_revision_messages


# NOT DECOMPILED: improve_script
