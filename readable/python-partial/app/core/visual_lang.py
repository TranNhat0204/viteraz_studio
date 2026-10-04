# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/visual_lang.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: language_code
def language_code(language):
    if not language:
        raw = str('en').strip().lower()
    else:
        raw = str(language).strip().lower()
    base = re.split('[-_]', raw, maxsplit=1)[0]
    return _LANG_CODE_BY_NAME.get(base, base)



# Original qualified name: visual_language_name
def visual_language_name(language):
    if not language:
        raw = str('en').strip()
    else:
        raw = str(language).strip()
    __temp_227960 = language_code(raw)
    if not raw:
        return LANG_NAME_MAP.get(__temp_227960, 'English')
    else:
        return LANG_NAME_MAP.get(__temp_227960, raw)



# Original qualified name: in_image_text_directive
def in_image_text_directive(language):
    spec = _SPEC.get(language_code(language))
    if spec:
        __temp_227965, __temp_227966 = spec
        name = __temp_227965
        rule = __temp_227966
    else:
        name = visual_language_name(language)
        rule = 'using ' + str(name
            ) + ' only — no English or other language text anywhere in the image'
    return str(IN_IMAGE_TEXT_LEAD) + ' ' + str(name) + ', ' + str(rule) + '.'



# Original qualified name: strip_in_image_text_directive
def strip_in_image_text_directive(text):
    if not text:
        return IN_IMAGE_TEXT_RE.sub('', str(''))
    else:
        return IN_IMAGE_TEXT_RE.sub('', str(text))



# Original qualified name: with_in_image_text_policy
def with_in_image_text_policy(prompt, language):
    text = strip_in_image_text_directive(prompt).strip()
    if not text:
        return
    return str(text) + ' ' + str(in_image_text_directive(language))

