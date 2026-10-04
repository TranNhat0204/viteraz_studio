# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/ideation_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _prompt_safe_profile


# NOT DECOMPILED: _profile_block


# NOT DECOMPILED: format_channel_override


# Original qualified name: resolve_series_mode
def resolve_series_mode(engine, profile):
    if not profile:
        prof = {}.get('series_mode')
    else:
        prof = profile.get('series_mode')
    if engine:
        meta = engine.meta.get('series_mode')
    else:
        meta = None
    if not prof:
        if not meta:
            v = str('').strip().lower()
        else:
            v = str(meta).strip().lower()
    else:
        v = str(prof).strip().lower()
    if v in ('serial', 'continuous', 'continuing', 'story', 'saga'):
        return 'serial'
    return 'anthology'



# Original qualified name: resolve_character_scope
def resolve_character_scope(engine, profile):
    if not profile:
        __temp_273569 = {}.get('character_scope')
    else:
        profile.get('character_scope')
    if not __temp_273569:
        raw = str('').strip().lower()
    else:
        raw = str(__temp_273569).strip().lower()
    if raw in ('channel', 'per_video'):
        return raw
    if resolve_series_mode(engine, profile) == 'serial':
        return 'channel'
    return 'per_video'



# NOT DECOMPILED: _history_block


# NOT DECOMPILED: _angle_bank_block


# NOT DECOMPILED: _sibling_block


# NOT DECOMPILED: _dedup_block


# Original qualified name: _format_block
def _format_block(fmt, long_target_sec, short_target_sec):
    if fmt is not None:
        if not fmt.is_short:
            dur_desc = "at the channel's usual length"
            if long_target_sec:
                minutes = round(long_target_sec / 60)
                dur_desc = 'with a target duration of about ' + str(minutes
                    ) + ' minutes (' + str(long_target_sec) + ' seconds)'
            return """
    
    VIDEO FORMAT: a LONG-FORM horizontal 16:9 video. Develop the topic in depth """ + str(dur_desc) + '. ' + vfmt.orientation_hint('16:9') + """ Apply this horizontal framing to thumbnail_prompt and every character description.
    """
    else:
        dur_desc = "at the channel's usual length"
        if long_target_sec:
            minutes = round(long_target_sec / 60)
            dur_desc = 'with a target duration of about ' + str(minutes
                ) + ' minutes (' + str(long_target_sec) + ' seconds)'
        return '\n\nVIDEO FORMAT: a LONG-FORM horizontal 16:9 video. Develop the topic in depth ' + str(dur_desc) + '. ' + vfmt.orientation_hint('16:9') + """ Apply this horizontal framing to thumbnail_prompt and every character description.
    """
    if not short_target_sec:
        target = vfmt.SHORT_MAX_SEC
    else:
        target = short_target_sec
    if target <= 30:
        min_sec = max(10, target - 10)
    else:
        min_sec = max(10, target - 15)
    return """
    
    VIDEO FORMAT: a SHORT vertical 9:16 video (""" + str(min_sec) + '–' + str(target) + """ seconds). Design the idea specifically for short-form vertical feeds (YouTube Shorts / Reels / TikTok):
    - ONE single sharp idea — no sprawling topic. A punchy hook in the first 0–2 seconds that stops the scroll.
    - Keep 'outline' to 3–5 tight beats only; the whole thing must be narratable in """ + str(min_sec) + '–' + str(target) + """s.
    - Set 'est_duration_sec' between """ + str(min_sec) + ' and ' + str(target) + '.\n- ' + vfmt.orientation_hint('9:16') + """ Apply this VERTICAL framing to thumbnail_prompt and every character description (full-height subject, centered, vertical headroom — never a wide horizontal scene).
    """



# Original qualified name: _host_block
def _host_block(host):
    if not isinstance(host, dict):
        return
    __temp_273610 = host.get('name')
    if not __temp_273610:
        name = str('').strip()
    else:
        name = str(__temp_273610).strip()
    if not name:
        return
    __temp_273615 = host.get('description')
    if not __temp_273615:
        desc = str('').strip()
    else:
        desc = str(__temp_273615).strip()
    if desc:
        ident = '  - Name: ' + str(name) + ' — ' + str(desc) + '\n'
    else:
        ident = '  - Name: ' + str(name) + '' + '\n'
    thumb = '  - Design thumbnail_concept + thumbnail_prompt so "' + str(name) + """" is the LARGE foreground subject of the thumbnail (this is the channel's recognizable face).
    """
    app = __import__('app.services.host_service', fromlist=(
        'ROLE_MAIN_CHARACTER', 'normalize_role'), level=0)
    ROLE_MAIN_CHARACTER = app.ROLE_MAIN_CHARACTER
    normalize_role = app.normalize_role
    if normalize_role(host.get('role')) == ROLE_MAIN_CHARACTER:
        return (
            """CHANNEL HOST / PROTAGONIST (the channel's brand character — the MAIN CHARACTER of every episode):
    """
             + ident + thumb +
            '  - Every episode is a story that happens TO or AROUND "' + str(
            name) + '". Build the angle and the outline so "' + str(name) +
            """" drives the events.
      - \"""" + str(name) +
            """" MUST appear in `characters` with is_main = true, using this EXACT name (never rename or redesign).
      - Supporting characters are allowed and encouraged wherever the story needs a second person (dialogue, an antagonist, a witness) — but they stay SUPPORTING; never promote one over \""""
             + str(name) + '".\n\n')
    return """CHANNEL HOST / NARRATOR (the channel's brand character — its face/mascot, usually the narrator):
    """ + ident + thumb + '  - "' + str(name) + """" is the NARRATOR / brand presence, NOT a mandatory character in every scene. You MAY feature the host in a few narrating / framing / cutaway beats, but do NOT force it into every scene.
      - The episode's actual scene cast is driven by the TOPIC and its own characters — design those normally. If you do include the host, use the EXACT name \"""" + name + """" (do not redesign/rename it).
    
    """



# Original qualified name: _hook_block
def _hook_block(channel_hook):
    if not channel_hook:
        hook = ''.strip()
    else:
        hook = channel_hook.strip()
    if not hook:
        return
    return """CHANNEL SIGNATURE HOOK (the channel's fixed branding line — keep room for it right after the opening of the script; do NOT rewrite it):
      \"""" + str(
        hook) + '"\n\n'



# NOT DECOMPILED: build_channel_context_blocks


# NOT DECOMPILED: _build_messages


# Original qualified name: _strip_md_fences
def _strip_md_fences(s):
    app = __import__('app.core.text', fromlist=('strip_thinking_blocks',), level=0)
    strip_thinking_blocks = app.strip_thinking_blocks
    if not s:
        s = strip_thinking_blocks('')
    else:
        s = strip_thinking_blocks(s)
    m = re.search('```(?:json)?\\s*(.*?)```', s, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return s



# NOT DECOMPILED: _balanced_object


# NOT DECOMPILED: _has_vietnamese


# Original qualified name: _overlay_text_in_prompt
def _overlay_text_in_prompt(thumbnail_prompt):
    if not thumbnail_prompt:
        m = re.search('\\bwords\\s+"([^"]{1,40})"', str(''))
    else:
        m = re.search('\\bwords\\s+"([^"]{1,40})"', str(thumbnail_prompt))
    if not m:
        if not thumbnail_prompt:
            m = re.search('\\btext[^"]{0,30}"([^"]{1,40})"', str(''))
        else:
            m = re.search('\\btext[^"]{0,30}"([^"]{1,40})"', str(thumbnail_prompt))
    if m:
        return m.group(1)
    return ''



# NOT DECOMPILED: _idea_language_mismatch


# NOT DECOMPILED: _repair_idea_language


# NOT DECOMPILED: _repair_json_string


# NOT DECOMPILED: _regex_extract_json_dict


# NOT DECOMPILED: _close_unclosed_containers


# NOT DECOMPILED: extract_json_object


# NOT DECOMPILED: _normalize_idea


# Original qualified name: _script_excerpt
def _script_excerpt(script):
    if not script:
        text = str('').strip()
    else:
        text = str(script).strip()
    if len(text) <= _SCRIPT_EXCERPT_CHARS:
        return text
    head = text[None:int(_SCRIPT_EXCERPT_CHARS * 0.7)]
    tail = text[-int(_SCRIPT_EXCERPT_CHARS * 0.3):None]
    return str(head) + '\n…\n' + str(tail)



# NOT DECOMPILED: _thumbnail_text_fallback


# NOT DECOMPILED: _manual_thumbnail_fallback


# NOT DECOMPILED: analyze_imported_script


# NOT DECOMPILED: extract_cast_from_script


# NOT DECOMPILED: generate_idea
