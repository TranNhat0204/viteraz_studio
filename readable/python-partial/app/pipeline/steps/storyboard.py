# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/storyboard.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _clamp_opt_int


# Original qualified name: _apply_visual_policy_flags
def _apply_visual_policy_flags(prompt, language):
    if not prompt:
        text = re.sub('\\s+', ' ', str('')).strip()
    else:
        text = re.sub('\\s+', ' ', str(prompt)).strip()
    text = _strip_in_image_text(text)
    text = re.sub('\\s*--image\\s+[A-Za-z][A-Za-z_-]*', '', text, flags=re.
        IGNORECASE)
    text = re.sub('\\s*--non-voice\\b', '', text, flags=re.IGNORECASE)
    text = re.sub('\\s+', ' ', text).strip()
    if not text:
        return
    return str(text) + ' ' + str(_in_image_text_directive(language)
        ) + ' --image ' + str(_visual_language_name(language)).strip()



# Original qualified name: _provider_params
def _provider_params(provider):
    if provider == 'meta':
        return {target_ms: _META_TARGET_SCENE_MS, max_ms: _META_MAX_SCENE_MS,
            veo_max_ms: _META_VIDEO_MAX_MS, video_target_ms: _META_CLIP_MS,
            borrow: False, clip_seconds: 5, label: 'Meta AI'}
    if provider == 'stock':
        return {target_ms: _TARGET_SCENE_MS, max_ms: _MAX_SCENE_MS, veo_max_ms:
            _VEO_MAX_MS, video_target_ms: _VIDEO_TARGET_MS, borrow: False,
            clip_seconds: 8, label: 'Stock footage'}
    return {target_ms: _TARGET_SCENE_MS, max_ms: _MAX_SCENE_MS, veo_max_ms:
        _VEO_MAX_MS, video_target_ms: _VIDEO_TARGET_MS, borrow: True,
        clip_seconds: 8, label: 'Google Flow / Veo'}



# Original qualified name: plan_visual_track_simple
def plan_visual_track_simple(scenes, clip_cap_ms):
    for __temp_256961 in iter(scenes):
        s = __temp_256961
        s['render_skip'] = False
        s['render_start_ms'] = int(s.get('start_ms', 0))
        s['render_end_ms'] = int(s.get('end_ms', 0))
        s.pop('end_keyframe_seq', None)
        if s.get('media_type') == 'video':
            window = s['render_end_ms'] - s['render_start_ms']
            if window > 0:
                s['clip_dur_ms'] = min(window, clip_cap_ms)
            else:
                s['clip_dur_ms'] = clip_cap_ms
            continue
            s.pop('clip_dur_ms', None)
        else:
            s.pop('clip_dur_ms', None)
        continue
    return scenes



# NOT DECOMPILED: group_scenes


# NOT DECOMPILED: group_scenes_split_lead


# NOT DECOMPILED: _mk_scene


# NOT DECOMPILED: assign_media_types


# NOT DECOMPILED: assign_media_types_counts


# NOT DECOMPILED: plan_visual_track


# Original qualified name: split_long_scenes
def split_long_scenes(scenes, clip_ms, max_ms):
    if max_ms is not None:
        cap = max_ms
    else:
        cap = clip_ms
    out = []
    for __temp_257225 in iter(scenes):
        s = __temp_257225
        start = int(s.get('start_ms', 0))
        end = int(s.get('end_ms', 0))
        dur = end - start
        if not dur <= cap:
            if dur <= 0:
                out.append(s)
                continue
                n_parts = max(1, math.ceil(dur / clip_ms))
            else:
                n_parts = max(1, math.ceil(dur / clip_ms))
        else:
            out.append(s)
            continue
            n_parts = max(1, math.ceil(dur / clip_ms))
        __temp_257238 = s.get('text')
        if not __temp_257238:
            words = ''.split()
        else:
            words = __temp_257238.split()
        for __temp_257242 in iter(range(n_parts)):
            k = __temp_257242
            child = dict(s)
            child['start_ms'] = start + round(dur * k / n_parts)
            child['end_ms'] = start + round(dur * (k + 1) / n_parts)
            w0 = round(len(words) * k / n_parts)
            w1 = round(len(words) * (k + 1) / n_parts)
            child['text'] = ' '.join(words[w0:w1]).strip()
            out.append(child)
            continue
        continue
    for __temp_257254 in iter(enumerate(out)):
        __temp_257255, __temp_257256 = __temp_257254
        i = __temp_257255
        s = __temp_257256
        s['seq'] = i + 1
        continue
    return out



# NOT DECOMPILED: plan_visual_mode


# NOT DECOMPILED: _scene_coverage


# Original qualified name: _scene_list_for
def _scene_list_for(scenes):
    scene_list = []
    for __temp_258762 in iter(enumerate(scenes)):
        __temp_258763, __temp_258764 = __temp_258762
        idx = __temp_258763
        s = __temp_258764
        if s.get('render_skip'):
            continue
            __temp_258766 = s.get('media_type')
        else:
            s.get('media_type')
        if __temp_258766 == 'video':
            __temp_258768 = s.get('clip_dur_ms')
            if not __temp_258768:
                dur = max(4, round(int(_VIDEO_TARGET_MS) / 1000))
            else:
                dur = max(4, round(int(__temp_258768) / 1000))
            scene_list.append({seq: s['seq'], type: 'video', duration_sec: dur,
                narration: _scene_coverage(scenes, idx)})
            continue
            __temp_258778 = s.get('text')
        else:
            s.get('text')
        if not __temp_258778:
            scene_list.append({seq: s['seq'], type: 'image', narration: ''.strip()}
                )
        else:
            scene_list.append({seq: s['seq'], type: 'image', narration:
                __temp_258778.strip()})
        continue
    return scene_list



# Original qualified name: _rules_block
def _rules_block(anchor, lock, language, orientation_note):
    lang_name = _visual_language_name(language)
    if orientation_note:
        framing = '- FRAMING: ' + str(orientation_note) + """ Do NOT use aspect-ratio flags like --ar (Flow sets the aspect in the UI) — instead bake this composition into every prompt.
    """
    else:
        framing = (
            '- Do NOT use aspect-ratio flags like --ar (Flow sets aspect in UI).\n'
            )
    return """RULES (strict):
    - Begin every IMAGE prompt (and every video scene's first-frame `prompt`) with the style anchor: \"""" + str(anchor) + """"
    - End the natural-language description with the style lock: \"""" + str(lock) + """"
    - Between anchor and lock: describe the concrete beat — the cast present (their exact look/expression matching the CAST description), objects, background. A scene with no people may have an empty characters list.
    - Set `continuity_mode`: `character_only` by default (reuse identity portraits but create a NEW composition); `previous_frame` ONLY when this is a direct continuation of the same location and action; `none` for landscapes, maps, diagrams, objects or scenes with no recurring character.
    - Rotate shot design across adjacent scenes (establishing, medium, close-up, object detail, map, over-the-shoulder). Never repeat the previous framing unless continuity_mode is previous_frame.
    - VISUAL PROMPT LANGUAGE & TEXT-IN-IMAGE POLICY (STRICT):
      • Write EVERY visual description (both `prompt` and `video_prompt`) entirely in English, regardless of the narration/channel language. Translate the visual meaning; never copy non-English narration into a prompt.
      • Any text, words, signage, book titles, headlines, labels, or overlay quotes requested inside an image prompt (e.g. labeled "...", the words "...") MUST be written strictly in """ + str(lang_name) + " (code '" + str(language) + """'), matching the channel language. Never use conflicting foreign words, garbled characters, or unneeded languages inside quotes unless it is an un-translatable proper brand name.
      • After the style lock, finish EVERY `prompt` and `video_prompt` with exactly `--image """ + str(lang_name) + '`.\n' + str(framing) + """
    VIDEO SCENES (type == 'video') become a REAL generated clip of `duration_sec` seconds (Veo), so they MUST exploit motion — never a frozen image. For each video scene return TWO fields:
      • `prompt`: the OPENING still (first frame) — same anchor…content…lock format as an image prompt.
      • `video_prompt`: direction for ONE continuous shot lasting `duration_sec` seconds that visually TELLS this scene's `narration`. Make it cinematic and specific:
         - A clear temporal arc with 2–3 beats: how it BEGINS (must match the first-frame `prompt`), what MOVES / DEVELOPS in the middle, how it ENDS. Use temporal cues ("starts with…", "then…", "by the end…").
         - Exactly ONE deliberate, slow camera move that fits the channel (push-in / pull-out / pan / tilt / dolly / orbit) — state its direction and pace; no erratic or teleporting camera.
         - Concrete on-screen motion grounded in the narration: what the characters/subject DO, plus environment animation (elements drawing or appearing, particles, light, arrows/labels animating) in the CHANNEL STYLE on every frame.
         - ONE single continuous shot — NO hard cuts, NO scene change mid-clip, NO split screen.
         - NO on-screen text, captions, subtitles, watermarks or speech bubbles.
    
    """



# Original qualified name: _append_visual_guardrails
def _append_visual_guardrails(prompt, engine):
    if not engine.meta:
        __temp_258788 = {}.get('visual_guardrails')
    else:
        engine.meta.get('visual_guardrails')
    if not __temp_258788:
        guardrails = str('').strip()
    else:
        guardrails = str(__temp_258788).strip()
    if not guardrails:
        return prompt
    if guardrails.lower() in prompt.lower():
        return prompt
    if not engine.meta:
        __temp_258797 = {}.get('style_lock')
    else:
        engine.meta.get('style_lock')
    if not __temp_258797:
        lock = str('').strip()
    else:
        lock = str(__temp_258797).strip()
    if lock:
        if lock.lower() in prompt.lower():
            idx = prompt.lower().rfind(lock.lower())
            return str(prompt[None:idx].rstrip()) + ' ' + str(guardrails
                ) + ' ' + str(prompt[idx:None].lstrip())
    return str(prompt.rstrip()) + ' ' + str(guardrails)



# Original qualified name: _ensure_style_contract
def _ensure_style_contract(prompt, engine, lang):
    app = __import__('app.services.channel_engines', fromlist=(
        'ensure_style_contract',), level=0)
    ensure_style_contract = app.ensure_style_contract
    return ensure_style_contract(prompt, engine, lang=lang)



# Original qualified name: _normalize_prompt_aspect
def _normalize_prompt_aspect(prompt, aspect):
    if not prompt:
        text = re.sub('\\s+', ' ', str('')).strip()
    else:
        text = re.sub('\\s+', ' ', str(prompt)).strip()
    if aspect == '9:16':
        text = re.sub('\\b16:9\\s+widescreen\\b|\\b16:9\\b|\\bwidescreen\\b',
            '9:16 portrait', text, flags=re.I)
        if '9:16' not in text:
            text += ', portrait vertical composition, 9:16'
        return text
    text = re.sub('\\b9:16\\s+portrait\\b|\\b9:16\\b|\\bportrait\\b',
        '16:9 landscape', text, flags=re.I)
    if '16:9' not in text:
        text += ', landscape composition, 16:9'
    return text



# Original qualified name: _name_in_text
def _name_in_text(name, text):
    if not name:
        name = ''.strip()
    else:
        name = name.strip()
    if not text:
        body = ''.strip()
    else:
        body = text.strip()
    if name:
        if not body:
            return False
    else:
        return False
    return re.search('(?<!\\w)' + re.escape(name) + '(?!\\w)', body) is not None



# NOT DECOMPILED: _strip_invented_appearance


# Original qualified name: _cast_brief
def _cast_brief(fixed_cast):
    out = []
    if not fixed_cast:
        __temp_258857 = []
    for __temp_258858 in iter(__temp_258857):
        c = __temp_258858
        item = {name: c.get('name'), description: c.get('description')}
        __temp_258862 = c.get('flow_ref_path')
        if not __temp_258862:
            __temp_258864 = character_service.has_locked_portrait(c.get('ref_path')
                )
        else:
            character_service.has_locked_portrait(__temp_258862)
        if __temp_258864:
            item['appearance'] = _LOCKED_FLAG
        out.append(item)
        continue
    return out



# NOT DECOMPILED: _locked_appearance_rule


# Original qualified name: _host_directive
def _host_directive(host_name, host_role, first_seq, last_seq):
    if not host_name:
        name = ''.strip()
    else:
        name = host_name.strip()
    if not name:
        return
    if host_service.normalize_role(host_role) == host_service.ROLE_MAIN_CHARACTER:
        return 'CHANNEL HOST — PROTAGONIST: "' + str(name) + """" is this channel's recurring MAIN CHARACTER, the same person in every episode.
      - Put \"""" + str(name) + """" in MOST scenes that show a person; the episode is a story that happens to or around them.
      - Supporting characters appear ONLY in the scenes their narration actually names. Never promote a supporting character over \"""" + str(name) + """".
      - Scenes with no people (landscape, object, map, diagram) keep an EMPTY characters list — do not insert \"""" + str(name) + """" just to fill it.
    
    """
    if first_seq is not None:
        opening = 'scene ' + str(first_seq)
    else:
        opening = 'the FIRST scene'
    if last_seq is not None:
        closing = 'scene ' + str(last_seq)
    else:
        closing = 'the LAST scene'
    rules = '  1. OPENING — ' + str(opening) + ' MUST list "' + str(name) + """" among its characters. Write that scene as the narrator addressing the camera and setting up what the episode is about.
    """
    if first_seq is not None:
        if last_seq is not None:
            if first_seq != last_seq:
                rules += '  2. MIDDLE — choose 1 to 3 further scenes where the narration steps back to comment, explain or warn, and place "' + str(name) + """" there as a talking-head cutaway. No more than 3.
      3. CLOSING — """ + str(closing) + ' MUST list "' + str(name) + """" among its characters: the narrator wrapping up and speaking to the viewer.
    """
        else:
            rules += '  2. MIDDLE — choose 1 to 3 further scenes where the narration steps back to comment, explain or warn, and place "' + str(name) + """" there as a talking-head cutaway. No more than 3.
      3. CLOSING — """ + str(closing) + ' MUST list "' + str(name) + """" among its characters: the narrator wrapping up and speaking to the viewer.
    """
    else:
        rules += '  2. MIDDLE — choose 1 to 3 further scenes where the narration steps back to comment, explain or warn, and place "' + str(name) + """" there as a talking-head cutaway. No more than 3.
      3. CLOSING — """ + str(closing) + ' MUST list "' + str(name) + """" among its characters: the narrator wrapping up and speaking to the viewer.
    """
    return 'CHANNEL HOST — NARRATOR: "' + str(name) + '" is this channel\'s recurring brand face and narrator, NOT a participant in this episode\'s story. Place "' + str(name) + """" using these rules — the ones marked MUST are mandatory, not suggestions:
    """ + rules + '  - Outside those beats, NEVER place "' + str(name) + """" inside a scene that depicts the episode's own events (a crime scene, a courtroom, a historical moment, a location from the story). Those scenes belong to the episode's own cast.
    
    """



# Original qualified name: _build_prompt_messages
def _build_prompt_messages(engine, scenes, language, channel_chars, fixed_cast, orientation_note, host_directive):
    system = (engine.body +
        """
    
    RUNTIME VISUAL PROMPT POLICY (overrides any older language rule above): all image prompts, video prompts, and cast visual descriptions MUST be written in English. Use the configured channel language only for visible in-image text and the final flags `--image """
         + str(_visual_language_name(language)) + '`.')
    __temp_258880 = engine.meta.get('style_anchor')
    if not __temp_258880:
        anchor = str('').strip()
    else:
        anchor = str(__temp_258880).strip()
    __temp_258885 = engine.meta.get('style_lock')
    if not __temp_258885:
        lock = str('').strip()
    else:
        lock = str(__temp_258885).strip()
    scene_list = _scene_list_for(scenes)
    common_rules = _rules_block(anchor, lock, language, orientation_note
        ) + 'SCENES (JSON):\n' + json.dumps(scene_list, ensure_ascii=False
        ) + '\n\n'
    if fixed_cast:
        cast_brief = _cast_brief(fixed_cast)
        user = """TASK: Execute STAGE 3 of your engine — turn the narration into a visual storyboard for Google Flow. Write EVERY visual description (both first-frame `prompt` and `video_prompt`) entirely in English.
    
    FIXED CAST (use EXACTLY these recurring characters — DO NOT invent or rename any. In every scene a character appears, depict them PRECISELY per their description so they look identical across all images of the video):
    """ + json.dumps(cast_brief, ensure_ascii=False) + '\n\n' + _locked_appearance_rule(cast_brief) + host_directive + """For EACH scene write the first-frame image `prompt`; for video scenes ALSO write the `video_prompt` (the duration_sec-second shot). List which FIXED-CAST NAMES appear in each (use the exact names above; empty list if no character).
    
    """ + common_rules + """OUTPUT (strict): return ONLY ONE JSON object, no prose:
    {"scenes": [{"seq": 1, "prompt": "<first-frame/image prompt>", "video_prompt": "<ONLY for type video: the duration_sec-second shot direction>", "characters": ["<Name>"], "continuity_mode": "character_only|previous_frame|none"}, ...]}"""
        return system, user
    existing = ''
    if channel_chars:
        existing = (
            """
    EXISTING CHANNEL CHARACTERS (reuse these EXACT names when they appear; do not rename):
    """
             + json.dumps(channel_chars, ensure_ascii=False) + '\n')
    user = """TASK: Execute STAGE 3 of your engine — turn the narration into a visual storyboard with a CONSISTENT recurring cast for Google Flow (Nano Banana images / Veo video). Write EVERY visual description (both first-frame `prompt` and `video_prompt`) entirely in English.
    
    """ + str(existing) + """
    STEP A — CAST: identify the recurring characters that appear across scenes. For each, give a short stable NAME (one or two words, reused everywhere) and a detailed visual DESCRIPTION in English (age, gender, ethnicity, hair, face, build, signature clothing) precise enough to redraw the same person every time. Use multiple meaningful characters when the story benefits from them (up to 6); anonymous crowds are not cast. Reuse existing channel names.
    
    STEP B — SCENES: for EACH scene write the first-frame image `prompt`; for video scenes ALSO write the `video_prompt` (the duration_sec-second shot). List which cast NAMES appear in each.
    
    """ + host_directive + common_rules + """OUTPUT (strict): return ONLY ONE JSON object, no prose:
    {"cast": [{"name": "<Name>", "description": "<full visual description>"}, ...], "scenes": [{"seq": 1, "prompt": "<first-frame/image prompt>", "video_prompt": "<ONLY for type video: the duration_sec-second shot direction>", "characters": ["<Name>"], "continuity_mode": "character_only|previous_frame|none"}, ...]}"""
    return system, user



# Original qualified name: _chunk_scene_list
def _chunk_scene_list(scene_list, max_chars, max_items):
    batches = []
    cur = []
    cur_len = 0
    for __temp_258899 in iter(scene_list):
        s = __temp_258899
        item_len = len(json.dumps(s, ensure_ascii=False))
        if cur:
            if not cur_len + item_len > max_chars:
                if len(cur) >= max_items:
                    batches.append(cur)
                    cur_len = 0
                    cur = []
            else:
                batches.append(cur)
                cur_len = 0
                cur = []
        cur.append(s)
        cur_len += item_len
        continue
    if cur:
        batches.append(cur)
        return batches
    else:
        return batches



# Original qualified name: _scene_out_tokens
def _scene_out_tokens(scene):
    if scene.get('type') == 'video':
        base = _OUT_TOKENS_VIDEO_SCENE
    else:
        base = _OUT_TOKENS_IMAGE_SCENE
    __temp_258910 = scene.get('narration')
    if not __temp_258910:
        return base + min(150, len(str('')) // 12)
    else:
        return base + min(150, len(str(__temp_258910)) // 12)



# NOT DECOMPILED: _balanced_split


# NOT DECOMPILED: _plan_batches


# Original qualified name: _build_setup_instructions
def _build_setup_instructions(language, channel_chars, fixed_cast, anchor, lock, n_batches, orientation_note, host_directive):
    rules = _rules_block(anchor, lock, language, orientation_note)
    if fixed_cast:
        cast_brief = _cast_brief(fixed_cast)
        return """TASK: Execute STAGE 3 of your engine — turn the narration into a visual storyboard for Google Flow. Write EVERY visual description (both first-frame `prompt` and `video_prompt`) entirely in English.
    
    FIXED CAST (use EXACTLY these recurring characters — DO NOT invent or rename any. In every scene a character appears, depict them PRECISELY per their description so they look identical across all images of the video):
    """ + json.dumps(cast_brief, ensure_ascii=False) + '\n\n' + _locked_appearance_rule(cast_brief) + host_directive + """For EACH scene write the first-frame image `prompt`; for video scenes ALSO write the `video_prompt` (the duration_sec-second shot). List which FIXED-CAST NAMES appear in each.
    
    """ + rules + 'PROTOCOL: I will send the scenes in ' + str(n_batches) + """ batches (each a JSON list of scenes). After EACH batch reply with ONLY one JSON object for THOSE scenes — no prose, no markdown:
    {"scenes": [{"seq": 1, "prompt": "<first-frame/image prompt>", "video_prompt": "<ONLY for type video: the duration_sec-second shot direction>", "characters": ["<Name>"], "continuity_mode": "character_only|previous_frame|none"}, ...]}
    Keep the SAME cast, visual style and continuity across every batch."""
    existing = ''
    if channel_chars:
        existing = (
            """
    EXISTING CHANNEL CHARACTERS (reuse these EXACT names when they appear; do not rename):
    """
             + json.dumps(channel_chars, ensure_ascii=False) + '\n')
    return """TASK: Execute STAGE 3 of your engine — turn the narration into a visual storyboard with a CONSISTENT recurring cast for Google Flow (Nano Banana images / Veo video). Write EVERY visual description (both first-frame `prompt` and `video_prompt`) entirely in English.
    
    """ + str(existing) + """
    STEP A — CAST: from the FIRST batch of scenes, identify the recurring characters that will appear across the whole video. For each, give a short stable NAME (one or two words, reused everywhere) and a detailed visual DESCRIPTION in English (age, gender, ethnicity, hair, face, build, signature clothing) precise enough to redraw the same person every time. Use as many meaningful recurring characters as the story needs (up to 6); anonymous crowds are not cast. Reuse existing channel names. Define this cast ONCE on the first batch and REUSE the exact same names/looks on every later batch.
    
    STEP B — SCENES: for EACH scene write the first-frame image `prompt`; for video scenes ALSO write the `video_prompt` (the duration_sec-second shot). List which cast NAMES appear in each.
    
    """ + host_directive + rules + 'PROTOCOL: I will send the scenes in ' + str(n_batches) + """ batches (each a JSON list of scenes). On the FIRST batch reply with ONLY one JSON object {"cast": [...], "scenes": [...]}; on EVERY LATER batch reply with ONLY {"scenes": [...]} (do NOT repeat the cast). No prose, no markdown. Shape:
    {"cast": [{"name": "<Name>", "description": "<full visual description>"}, ...], "scenes": [{"seq": 1, "prompt": "<first-frame/image prompt>", "video_prompt": "<ONLY for type video: the duration_sec-second shot direction>", "characters": ["<Name>"], "continuity_mode": "character_only|previous_frame|none"}, ...]}
    Keep the SAME cast, visual style and continuity across every batch."""



# Original qualified name: _build_batch_message
def _build_batch_message(batch, idx, n_batches):
    return 'BATCH ' + str(idx + 1) + '/' + str(n_batches
        ) + ' — write the storyboard JSON for EXACTLY these ' + str(len(batch)
        ) + """ scene(s) (reply with ONLY the JSON object described above, covering these seqs):
    """ + json.dumps(
        batch, ensure_ascii=False)



# Original qualified name: _coerce_seq
def _coerce_seq(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, str):
        m = re.search('-?\\d+', value)
        if m:
            return int(m.group())
    return None



# Original qualified name: _raise_if_cancelled
def _raise_if_cancelled(ctx):
    check = getattr(ctx, 'is_cancelled', None)
    if callable(check):
        if check():
            raise make_error(E.CANCELLED, 'Đã dừng khi đang viết storyboard.')
        return None
    return None



# NOT DECOMPILED: _parse_scenes_payload


# Original qualified name: _bad_response_code
def _bad_response_code(provider):
    p = ai_provider.resolve_provider(provider)
    if p == ai_provider.PROVIDER_GEMINI:
        return E.GEMINI_BAD_RESPONSE
    if p == ai_provider.PROVIDER_CHATGPT:
        return E.CHATGPT_BAD_RESPONSE
    if ai_provider.is_endpoint_ref(p):
        return E.LLM_API_BAD_RESPONSE
    return E.DEEPSEEK_BAD_RESPONSE



# NOT DECOMPILED: _build_missing_message


# NOT DECOMPILED: _request_batch


# NOT DECOMPILED: _generate_storyboard_chunked


# Original qualified name: _news_proper_tokens
def _news_proper_tokens(text):
    out = set()
    if not text:
        __temp_259036 = re.findall("\\b[A-Z][\\w'’-]{2,}\\b", '')
    else:
        re.findall("\\b[A-Z][\\w'’-]{2,}\\b", text)
    for __temp_259038 in iter(__temp_259036):
        tok = __temp_259038
        out.add(tok.lower())
        continue
    if not text:
        __temp_259041 = re.findall('\\b\\d{2,}\\b', '')
    else:
        re.findall('\\b\\d{2,}\\b', text)
    for __temp_259043 in iter(__temp_259041):
        num = __temp_259043
        out.add(num)
        continue
    return out



# Original qualified name: _news_match_budget
def _news_match_budget(provider):
    turn_limit = ai_provider.max_turn_chars(provider)
    return max(1000, min(12000, turn_limit - _NEWS_MATCH_PROMPT_OVERHEAD))



# NOT DECOMPILED: _llm_match_news_images


# NOT DECOMPILED: _assign_news_stock_refs


# Original qualified name: _assign_news_stock_refs.<locals>._take
def _take(scene_idx, img_idx, how):
    nonlocal news_images, used_images, used_scenes, visible
    img = news_images[img_idx]
    scene = visible[scene_idx]
    scene['news_stock_ref'] = img['local_path']
    scene['news_stock_caption'] = img.get('caption', '')
    scene['news_stock_match'] = how
    used_scenes.add(scene_idx)
    used_images.add(img_idx)
    return None



# NOT DECOMPILED: _assign_news_stock_refs.<locals>._nearest_free


# Original qualified name: _strip_policy_flags
def _strip_policy_flags(text):
    t = _strip_in_image_text(text)
    t = re.sub('\\s*--image\\s+[A-Za-z]+', ' ', t, flags=re.I)
    t = re.sub('\\s*--non-voice\\b', ' ', t, flags=re.I)
    return re.sub('\\s+', ' ', t).strip()



# Original qualified name: _aspect_blind
def _aspect_blind(text):
    if not text:
        t = re.sub(
            '\\b16:9\\b|\\b9:16\\b|\\bwidescreen\\b|\\blandscape composition\\b|\\bportrait vertical composition\\b|\\blandscape\\b|\\bportrait\\b'
            , ' ', str(''), flags=re.I)
    else:
        t = re.sub(
            '\\b16:9\\b|\\b9:16\\b|\\bwidescreen\\b|\\blandscape composition\\b|\\bportrait vertical composition\\b|\\blandscape\\b|\\bportrait\\b'
            , ' ', str(text), flags=re.I)
    return re.sub('[\\s,]+', ' ', t).strip().lower()



# Original qualified name: _prompt_content_core
def _prompt_content_core(prompt, engine):
    if engine is not None:
        if not engine.meta:
            meta = {}
        else:
            meta = engine.meta
    else:
        meta = {}
    text = _aspect_blind(_strip_policy_flags(prompt))
    for __temp_259129 in iter(('style_anchor', 'style_anchor_vi', 'style_lock',
        'style_lock_vi', 'visual_guardrails')):
        key = __temp_259129
        __temp_259130 = meta.get(key)
        if not __temp_259130:
            frag = str('').strip()
        else:
            frag = str(__temp_259130).strip()
        if not frag:
            continue
            text = text.replace(_aspect_blind(frag), ' ')
        else:
            text = text.replace(_aspect_blind(frag), ' ')
        continue
    return re.sub('[\\s,.;:]+', ' ', text).strip(' ,.;:-—')



# Original qualified name: _check_prompt
def _check_prompt(label, prompt, engine, aspect, flags):
    if engine is not None:
        if not engine.meta:
            meta = {}
        else:
            meta = engine.meta
    else:
        meta = {}
    out = []
    blind = _aspect_blind(prompt)
    if _LEGACY_FALLBACK_SENTINEL in prompt.lower():
        out.append(str(label) + ': dính prompt fallback rỗng nội dung của bản cũ')
        core = _prompt_content_core(prompt, engine)
    else:
        core = _prompt_content_core(prompt, engine)
    if len(core) < _MIN_PROMPT_CONTENT_CHARS:
        out.append(str(label) +
            ': prompt không mô tả cảnh — bóc style xong chỉ còn ' + str(len(
            core)) + ' ký tự')
        __temp_259152 = meta.get('style_anchor')
    else:
        meta.get('style_anchor')
    if not __temp_259152:
        anchor = _aspect_blind('')
    else:
        anchor = _aspect_blind(__temp_259152)
    if anchor:
        if not blind.startswith(anchor[None:60]):
            out.append(str(label) + ': không mở đầu bằng style anchor của kênh')
            __temp_259158 = meta.get('style_lock')
        else:
            meta.get('style_lock')
    else:
        meta.get('style_lock')
    if not __temp_259158:
        lock = _aspect_blind('')
    else:
        lock = _aspect_blind(__temp_259158)
    if lock:
        if lock not in blind:
            out.append(str(label) + ': thiếu style lock của kênh')
            tail = re.sub('\\s*--non-voice\\b', '', prompt, flags=re.I).rstrip()
        else:
            tail = re.sub('\\s*--non-voice\\b', '', prompt, flags=re.I).rstrip()
    else:
        tail = re.sub('\\s*--non-voice\\b', '', prompt, flags=re.I).rstrip()
    if not tail.endswith(flags):
        out.append(str(label) + ': không kết thúc bằng `' + str(flags) + '`')
    if aspect == '9:16':
        want = '9:16'
    else:
        want = '16:9'
    if want not in prompt:
        out.append(str(label) + ': không mang khung hình ' + str(want))
        return out
    else:
        return out



# NOT DECOMPILED: validate_storyboard


# Original qualified name: raise_if_storyboard_invalid
def raise_if_storyboard_invalid(scenes, cast, engine, aspect, language, image_provider, where):
    problems = validate_storyboard(scenes, cast, engine, aspect, language,
        image_provider)
    if not problems:
        return None
    head = '; '.join(problems[None:8])
    if len(problems) > 8:
        more = ' (+' + str(len(problems) - 8) + ' lỗi nữa)'
    else:
        more = ''
    raise make_error(E.PRECONDITION_MISSING, str(where) +
        ': storyboard chưa chuẩn nên KHÔNG được sang bước tạo ảnh — ' + str(
        head) + str(more) + '. Hãy chạy lại bước Storyboard.')



# NOT DECOMPILED: StoryboardStep.run


# NOT DECOMPILED: StoryboardStep.run.<locals>._has_host
