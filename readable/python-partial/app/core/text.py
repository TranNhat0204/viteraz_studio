# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/text.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: ensure_terminal_punct
def ensure_terminal_punct(s):
    if not s:
        s = ''.rstrip()
    else:
        s = s.rstrip()
    if not s:
        return s
    if s[-1] in _TERMINAL_PUNCT:
        return s
    if s[-1] in _CLOSERS:
        core = s.rstrip(_CLOSERS).rstrip()
        closers = s[len(core):None]
        if core:
            if core[-1] in _TERMINAL_PUNCT:
                return core[None:-1].rstrip() + closers + core[-1]
        return s + '.'
    if s[-1].isalnum():
        return s + '.'
    return s



# NOT DECOMPILED: strip_thinking_blocks


# NOT DECOMPILED: clean_llm_script
