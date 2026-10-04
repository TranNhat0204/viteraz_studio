# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/marketing_playbook.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _strings


# Original qualified name: get_playbook
def get_playbook(engine):
    if not engine.meta:
        raw = {}.get('marketing')
    else:
        raw = engine.meta.get('marketing')
    if not isinstance(raw, dict):
        return {}
    pillars = []
    if not raw.get('pillars'):
        __temp_274867 = []
    for __temp_274868 in iter(__temp_274867):
        item = __temp_274868
        if not isinstance(item, dict):
            continue
            __temp_274870 = item.get('id')
        else:
            item.get('id')
        if not __temp_274870:
            pillar_id = str('').strip()
        else:
            pillar_id = str(__temp_274870).strip()
        if not pillar_id:
            continue
            __temp_274876 = item.get('weight')
        else:
            item.get('weight')
        if not __temp_274876:
            __temp_274879 = max(0, int(0))
            __temp_274880 = item.get('content_class')
        else:
            max(0, int(__temp_274876))
            item.get('content_class')
        if not __temp_274880:
            __temp_274886 = str('shareable').strip().lower()
            __temp_274887 = item.get('buyer_stage')
        else:
            str(__temp_274880).strip().lower()
            item.get('buyer_stage')
        if not __temp_274887:
            pillars.append({id: pillar_id, weight: __temp_274879, content_class:
                __temp_274886, buyer_stage: str('community').strip().lower(),
                formats: _strings(item.get('formats'))})
        else:
            pillars.append({id: pillar_id, weight: __temp_274879, content_class:
                __temp_274886, buyer_stage: str(__temp_274887).strip().lower(),
                formats: _strings(item.get('formats'))})
        continue
    if isinstance(raw.get('hook_bank'), dict):
        hooks = raw.get('hook_bank')
    else:
        hooks = {}
    if isinstance(raw.get('evidence'), dict):
        evidence = raw.get('evidence')
    else:
        evidence = {}
    if isinstance(raw.get('quality'), dict):
        quality = raw.get('quality')
    else:
        quality = {}
    __temp_274918 = raw.get('version')
    if not __temp_274918:
        __temp_274919 = int(1)
        __temp_274920 = raw.get('audience')
    else:
        int(__temp_274918)
        raw.get('audience')
    if not __temp_274920:
        return {version: __temp_274919, audience: str('').strip(), objectives:
            _strings(raw.get('objectives')), formats: _strings(raw.get(
            'formats')), pillars: pillars, hook_types: _strings(hooks.get(
            'types')), hook_examples: _strings(hooks.get('examples')), cta:
            _strings(raw.get('cta')), avoid: _strings(raw.get('avoid')),
            evidence: evidence, quality: quality}
    else:
        return {version: __temp_274919, audience: str(__temp_274920).strip(),
            objectives: _strings(raw.get('objectives')), formats: _strings(raw.
            get('formats')), pillars: pillars, hook_types: _strings(hooks.get(
            'types')), hook_examples: _strings(hooks.get('examples')), cta:
            _strings(raw.get('cta')), avoid: _strings(raw.get('avoid')),
            evidence: evidence, quality: quality}



# Original qualified name: is_ready
def is_ready(engine):
    p = get_playbook(engine)
    __temp_274954 = p.get('pillars')
    if __temp_274954:
        __temp_274955 = p.get('objectives')
        if __temp_274955:
            __temp_274956 = p.get('formats')
            if __temp_274956:
                return bool(p.get('hook_types'))
            else:
                return bool(__temp_274956)
        else:
            return bool(__temp_274955)
    else:
        return bool(__temp_274954)



# NOT DECOMPILED: prompt_block


# NOT DECOMPILED: apply_to_post
