# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/agents/channel_architect.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: harvest


# NOT DECOMPILED: harvest.<locals>.one


# Original qualified name: _validate_forensics
def _validate_forensics(art):
    if not isinstance(art, dict):
        return ['không phải JSON object']
    errors = []
    __temp_265406 = art.get('hook_type')
    if not __temp_265406:
        __temp_265407 = str('')
    else:
        str(__temp_265406)
    if __temp_265407 not in _HOOK_TYPES:
        errors.append('hook_type phải là một trong: ' + str(', '.join(_HOOK_TYPES))
            )
        beats = art.get('beat_map')
    else:
        beats = art.get('beat_map')
    if isinstance(beats, list):
        if not beats:
            errors.append(
                'beat_map rỗng — đây là phần quan trọng nhất, phải đo từ mốc [mm:ss]'
                )
            return errors
        else:
            return errors
    else:
        errors.append(
            'beat_map rỗng — đây là phần quan trọng nhất, phải đo từ mốc [mm:ss]')
        return errors



# NOT DECOMPILED: _fold_stray_keys


# NOT DECOMPILED: _validate_portrait


# NOT DECOMPILED: _validate_config


# Original qualified name: _validate_master_part
def _validate_master_part(art):
    if not art:
        text = str('')
    else:
        text = str(art)
    if len(text.strip()) < 800:
        return ['phần này quá ngắn (' + str(len(text.strip())) +
            ' ký tự) — chưa đủ chiều sâu']
    return []



# NOT DECOMPILED: _strip_model_invariants


# NOT DECOMPILED: assemble_master_prompt


# NOT DECOMPILED: normalize_audit


# Original qualified name: _json_step_parse
def _json_step_parse(raw):
    return ideation_service.extract_json_object(raw)



# Original qualified name: _parse_portrait
def _parse_portrait(raw):
    return _fold_stray_keys(ideation_service.extract_json_object(raw),
        _PORTRAIT_NESTING, _PORTRAIT_TOP_KEYS)



# Original qualified name: _parse_config
def _parse_config(raw):
    return _fold_stray_keys(ideation_service.extract_json_object(raw),
        _CONFIG_NESTING, _CONFIG_TOP_KEYS)



# Original qualified name: _engine_catalog
def _engine_catalog():
    out = []
    for __temp_265533 in iter(channel_engines.list_engines()):
        engine = __temp_265533
        if not engine.meta:
            meta = {}
        else:
            meta = engine.meta
        if not meta.get('hidden'):
            if meta.get('test_mode'):
                continue
                __temp_265537 = meta.get('niche')
                __temp_265538 = meta.get('visual_style')
                __temp_265539 = meta.get('engine_kind', 'ai')
                __temp_265540 = meta.get('tags')
            else:
                meta.get('niche')
                meta.get('visual_style')
                meta.get('engine_kind', 'ai')
                meta.get('tags')
        else:
            continue
            meta.get('niche')
            meta.get('visual_style')
            meta.get('engine_kind', 'ai')
            meta.get('tags')
        if not __temp_265540:
            out.append({id: engine.id, name: engine.name, niche: __temp_265537,
                visual_style: __temp_265538, engine_kind: __temp_265539, tags: []})
        else:
            out.append({id: engine.id, name: engine.name, niche: __temp_265537,
                visual_style: __temp_265538, engine_kind: __temp_265539, tags:
                __temp_265540})
        continue
    return out



# Original qualified name: build_steps
def build_steps(language, channel_name):
    lang_line = ("OUTPUT LANGUAGE for all descriptive fields: language code '" +
        str(language) + "'.\n")
    steps = []
    
    
    def build_portrait(ctx):
        nonlocal lang_line
        analyses = ctx.artifacts['forensics']
        __temp_265556 = ctx.inputs.get('comments')
        if not __temp_265556:
            comments = []
        else:
            comments = __temp_265556
        __temp_265558 = ctx.inputs.get('channel_title')
        if not __temp_265558:
            body = [lang_line, 'CHANNEL: ' + str('') + '\n', 
                'PER-VIDEO FORENSIC ANALYSES (' + str(len(analyses)) +
                ' video):\n', json.dumps(analyses, ensure_ascii=False)]
        else:
            body = [lang_line, 'CHANNEL: ' + str(__temp_265558) + '\n', 
                'PER-VIDEO FORENSIC ANALYSES (' + str(len(analyses)) +
                ' video):\n', json.dumps(analyses, ensure_ascii=False)]
        if comments:
            body.append(
                """
        
        TOP AUDIENCE COMMENTS (đọc để biết khán giả ở lại vì gì và đang đòi nội dung gì — KHÔNG trích nguyên văn):
        """
                 + json.dumps(comments[None:60], ensure_ascii=False))
            return skills.load_many(('01-channel-portrait', 'human-voice')
                ), ''.join(body)
        else:
            return skills.load_many(('01-channel-portrait', 'human-voice')
                ), ''.join(body)
    
    
    steps.append(Step(key='portrait', label='Dựng chân dung kênh', build=
        build_portrait, parse=_parse_portrait, validate=_validate_portrait,
        retries=1, temperature=0.3, reasoning_effort='none',
        retry_reasoning_effort='high', max_tokens=6000, weight=1.5))
    
    
    def build_config(ctx):
        nonlocal lang_line
        return (skills.load('02-channel-config'), lang_line +
            """CHANNEL PORTRAIT (kênh nguồn — học cách làm, không mang chủ đề):
        """
             + json.dumps(ctx.artifacts['portrait'], ensure_ascii=False) +
            """
        
        ENGINE CATALOG (chỉ được chọn id trong danh sách này, hoặc null):
        """
             + json.dumps(_engine_catalog(), ensure_ascii=False))
    
    
    steps.append(Step(key='config', label='Quyết định cấu hình kênh mới', build
        =build_config, parse=_parse_config, validate=_validate_config, retries=
        1, temperature=0.4, reasoning_effort='none', retry_reasoning_effort=
        'high', max_tokens=4000, weight=1.0))
    
    
    def build_master_a(ctx):
        nonlocal channel_name, lang_line
        return skills.load_many(('master-prompt-blueprint', 'brand-identity')), 'CHANNEL NAME: ' + str(channel_name) + '\n' + str(lang_line) + """
        CHANNEL CONFIG (kênh bạn đang viết master prompt cho):
        """ + json.dumps(ctx.artifacts['config'], ensure_ascii=False) + """
        
        CHANNEL PORTRAIT (nguồn cảm hứng về CÁCH LÀM):
        """ + json.dumps(ctx.artifacts['portrait'], ensure_ascii=False) + """
        
        TASK: viết PHẦN A của master prompt — mục 1 đến 16 theo blueprint.
        KHÔNG viết mục 2 (INPUT CONTRACT): phần mềm tự chèn khối đó. Bỏ qua nó, đi thẳng từ mục 1 sang mục 3.
        KHÔNG viết mục 17 trở đi — đó là phần B, viết ở lượt sau.
        Trả về DUY NHẤT nội dung các mục đó, không lời dẫn, không bọc trong khối code."""
    
    
    def __temp_265584(raw):
        return master_prompt.strip_wrapper(raw)
    
    
    steps.append(Step(key='master_a', label=
        'Master prompt · phần A (danh tính + luật)', build=build_master_a,
        parse=__temp_265584, validate=_validate_master_part, retries=1,
        temperature=0.6, reasoning_effort='high', max_tokens=9000, weight=2.5))
    
    
    def build_master_b(ctx):
        nonlocal channel_name, lang_line
        return skills.load_many(('master-prompt-blueprint', 'fact-integrity', 'retention-architecture', 'human-voice')), 'CHANNEL NAME: ' + str(channel_name) + '\n' + str(lang_line) + """
        CHANNEL CONFIG:
        """ + json.dumps(ctx.artifacts['config'], ensure_ascii=False) + """
        
        PHẦN A ĐÃ VIẾT (nối tiếp mạch này, đừng lặp lại nó):
        """ + str(ctx.artifacts['master_a'])[None:8000] + """
        
        TASK: viết PHẦN B của master prompt — mục 17 đến 25 theo blueprint.
        KHÔNG viết mục 20B (luật đọc thành tiếng) và KHÔNG viết mục 26 (STRICT OUTPUT FORMAT): phần mềm tự chèn hai khối đó nguyên văn.
        Trả về DUY NHẤT nội dung các mục đó, không lời dẫn, không bọc trong khối code."""
    
    
    def __temp_265592(raw):
        return master_prompt.strip_wrapper(raw)
    
    
    steps.append(Step(key='master_b', label=
        'Master prompt · phần B (tay nghề + tự kiểm)', build=build_master_b,
        parse=__temp_265592, validate=_validate_master_part, retries=1,
        temperature=0.6, reasoning_effort='high', max_tokens=9000, weight=2.5))
    
    
    def build_audit(ctx):
        nonlocal lang_line
        return skills.load('quality-rubric'), lang_line + """Chấm MASTER PROMPT dưới đây theo rubric 10 chiều ở trên. Chấm tài liệu này có ÉP ĐƯỢC hành vi hay không, chứ không chấm văn hay dở.
        
        """ + str(ctx.artifacts['assembled'])[None:30000] + """
        
        Trả về DUY NHẤT: {"scores": {"D1": 0, ..., "D10": 0}, "notes": "điểm yếu lớn nhất và cách sửa"}"""
    
    
    steps.append(Step(key='audit', label='Tự chấm theo rubric 10 chiều', build=
        build_audit, parse=_json_step_parse, retries=1, temperature=0.2,
        reasoning_effort='none', retry_reasoning_effort='high', max_tokens=3000,
        weight=1.0))
    return steps



# Original qualified name: build_steps.<locals>.build_portrait
def build_portrait(ctx):
    nonlocal lang_line
    analyses = ctx.artifacts['forensics']
    __temp_265601 = ctx.inputs.get('comments')
    if not __temp_265601:
        comments = []
    else:
        comments = __temp_265601
    __temp_265603 = ctx.inputs.get('channel_title')
    if not __temp_265603:
        body = [lang_line, 'CHANNEL: ' + str('') + '\n', 
            'PER-VIDEO FORENSIC ANALYSES (' + str(len(analyses)) + ' video):\n',
            json.dumps(analyses, ensure_ascii=False)]
    else:
        body = [lang_line, 'CHANNEL: ' + str(__temp_265603) + '\n', 
            'PER-VIDEO FORENSIC ANALYSES (' + str(len(analyses)) + ' video):\n',
            json.dumps(analyses, ensure_ascii=False)]
    if comments:
        body.append(
            """
    
    TOP AUDIENCE COMMENTS (đọc để biết khán giả ở lại vì gì và đang đòi nội dung gì — KHÔNG trích nguyên văn):
    """
             + json.dumps(comments[None:60], ensure_ascii=False))
        return skills.load_many(('01-channel-portrait', 'human-voice')), ''.join(
            body)
    else:
        return skills.load_many(('01-channel-portrait', 'human-voice')), ''.join(
            body)



# Original qualified name: build_steps.<locals>.build_config
def build_config(ctx):
    nonlocal lang_line
    return skills.load('02-channel-config'
        ), lang_line + """CHANNEL PORTRAIT (kênh nguồn — học cách làm, không mang chủ đề):
    """ + json.dumps(
        ctx.artifacts['portrait'], ensure_ascii=False
        ) + """
    
    ENGINE CATALOG (chỉ được chọn id trong danh sách này, hoặc null):
    """ + json.dumps(
        _engine_catalog(), ensure_ascii=False)



# Original qualified name: build_steps.<locals>.build_master_a
def build_master_a(ctx):
    nonlocal channel_name, lang_line
    return skills.load_many(('master-prompt-blueprint', 'brand-identity')), 'CHANNEL NAME: ' + str(channel_name) + '\n' + str(lang_line) + """
    CHANNEL CONFIG (kênh bạn đang viết master prompt cho):
    """ + json.dumps(ctx.artifacts['config'], ensure_ascii=False) + """
    
    CHANNEL PORTRAIT (nguồn cảm hứng về CÁCH LÀM):
    """ + json.dumps(ctx.artifacts['portrait'], ensure_ascii=False) + """
    
    TASK: viết PHẦN A của master prompt — mục 1 đến 16 theo blueprint.
    KHÔNG viết mục 2 (INPUT CONTRACT): phần mềm tự chèn khối đó. Bỏ qua nó, đi thẳng từ mục 1 sang mục 3.
    KHÔNG viết mục 17 trở đi — đó là phần B, viết ở lượt sau.
    Trả về DUY NHẤT nội dung các mục đó, không lời dẫn, không bọc trong khối code."""



# Original qualified name: build_steps.<locals>.build_master_b
def build_master_b(ctx):
    nonlocal channel_name, lang_line
    return skills.load_many(('master-prompt-blueprint', 'fact-integrity', 'retention-architecture', 'human-voice')), 'CHANNEL NAME: ' + str(channel_name) + '\n' + str(lang_line) + """
    CHANNEL CONFIG:
    """ + json.dumps(ctx.artifacts['config'], ensure_ascii=False) + """
    
    PHẦN A ĐÃ VIẾT (nối tiếp mạch này, đừng lặp lại nó):
    """ + str(ctx.artifacts['master_a'])[None:8000] + """
    
    TASK: viết PHẦN B của master prompt — mục 17 đến 25 theo blueprint.
    KHÔNG viết mục 20B (luật đọc thành tiếng) và KHÔNG viết mục 26 (STRICT OUTPUT FORMAT): phần mềm tự chèn hai khối đó nguyên văn.
    Trả về DUY NHẤT nội dung các mục đó, không lời dẫn, không bọc trong khối code."""



# Original qualified name: build_steps.<locals>.build_audit
def build_audit(ctx):
    nonlocal lang_line
    return skills.load('quality-rubric'), lang_line + """Chấm MASTER PROMPT dưới đây theo rubric 10 chiều ở trên. Chấm tài liệu này có ÉP ĐƯỢC hành vi hay không, chứ không chấm văn hay dở.
    
    """ + str(ctx.artifacts['assembled'])[None:30000] + """
    
    Trả về DUY NHẤT: {"scores": {"D1": 0, ..., "D10": 0}, "notes": "điểm yếu lớn nhất và cách sửa"}"""



# NOT DECOMPILED: _forensics_one


# NOT DECOMPILED: fetch_audience_comments


# NOT DECOMPILED: run


# NOT DECOMPILED: _run_until


# NOT DECOMPILED: _make_call


# NOT DECOMPILED: _make_call.<locals>.call
