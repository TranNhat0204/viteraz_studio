# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/seo.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _build_messages
def _build_messages(old_title, transcript, lang_code, platform, tone, n_titles):
    lang = _LANG_NAME.get(lang_code, lang_code)
    if not platform:
        plat = _PLATFORM_NAME.get(platform, 'TikTok')
    else:
        plat = _PLATFORM_NAME.get(platform, platform)
    system_msg = 'You are a world-class short-form video SEO & copywriting expert for ' + str(plat) + ', writing in ' + str(lang) + """.
    You are given the ORIGINAL title (often in another language) and a transcript of the video. Your job is to localize and rewrite it into high-CTR metadata, fully IN """ + str(lang) + ' (the same language as the subtitles), with a ' + str(tone) + """ tone.
    
    STRICT RULES:
    - titles: """ + str(n_titles) + ' DISTINCT viral titles in ' + str(lang) + """ for A/B testing — each takes a clearly different angle (curiosity gap, emotion, numbers/list, bold claim, question). Rewrite/localize the original meaning into native, scroll-stopping titles. Each < 65 characters. NO false clickbait, NO quotes, NO hashtags inside titles.
    - description: 1–2 natural sentences in """ + str(lang) + """ summarizing the value + a soft call-to-action.
    - hashtags: 12 relevant hashtags in """ + str(lang) + """ (mix broad + niche + trending), each starting with '#', no spaces.
    - hooks: 3 ultra-short opening lines (3–8 words) in """ + str(lang) + """ to grab attention in the first 1 second.
    
    Return ONLY a valid minified JSON object, no markdown, no commentary:
    {"titles":["..","..",".."],"description":"..","hashtags":["#..",".."],"hooks":["..","..",".."]}"""
    if not old_title:
        user_msg = 'ORIGINAL TITLE:\n' + str('(none)'
            ) + """
    
    TRANSCRIPT (may be long, summarize the gist):
    """ + str(
            transcript[None:3500])
    else:
        user_msg = 'ORIGINAL TITLE:\n' + str(old_title
            ) + """
    
    TRANSCRIPT (may be long, summarize the gist):
    """ + str(
            transcript[None:3500])
    return [{role: 'system', content: system_msg}, {role: 'user', content:
        user_msg}]



# NOT DECOMPILED: _parse


# NOT DECOMPILED: _call_provider


# NOT DECOMPILED: generate_seo


# Original qualified name: _build_youtube_messages
def _build_youtube_messages(title, transcript, lang_code, niche, tone, is_short, n_titles):
    lang = _LANG_NAME.get(lang_code, lang_code)
    if is_short:
        fmt = 'YouTube Shorts (vertical, < 60s)'
    else:
        fmt = 'YouTube long-form video'
    if not niche:
        __temp_23029 = ''.strip()
    else:
        niche.strip()
    if __temp_23029:
        niche_note = ' for a channel about: ' + str(niche) + '.'
    else:
        niche_note = '.'
    desc_rule = (
        "- description: a natural, keyword-rich YouTube description IN {lang}. Structure: (1) a strong 1-2 sentence HOOK summarizing the video's value with the main keyword FRONT-LOADED; (2) 2-3 sentences on what the viewer will learn/see; (3) a short soft call-to-action to like & subscribe. Keep it ~60-110 words, no markdown, no emoji spam, no fake claims."
        .format(lang=lang))
    system_msg = 'You are a world-class YouTube SEO strategist writing in ' + str(lang) + ', producing metadata for a ' + str(fmt) + str(niche_note) + ' Tone: ' + str(tone) + """.
    
    STRICT RULES:
    - titles: """ + str(n_titles) + ' DISTINCT high-CTR YouTube titles in ' + str(lang) + """ for A/B testing — each a clearly different angle (curiosity gap, number/list, bold claim, question, benefit). Each < 70 characters. Front-load the main keyword. NO clickbait lies, NO surrounding quotes, NO hashtags inside titles.
    """ + str(desc_rule) + """
    - tags: 12-15 SEO keyword phrases in """ + str(lang) + """ for the YouTube tags field (plain phrases, NO '#', mix broad + specific + long-tail).
    - hashtags: 3-5 YouTube hashtags in """ + str(lang) + """, each starting with '#', no spaces.
    
    Return ONLY a valid minified JSON object, no markdown, no commentary:
    {"titles":[".."],"description":"..","tags":["..",".."],"hashtags":["#..",".."]}"""
    if not title:
        user_msg = ('VIDEO TITLE / IDEA:\n' + str('(none)') +
            """
    
    NARRATION SCRIPT (summarize the gist, extract the key topics):
    """
             + str(transcript[None:5000]))
    else:
        user_msg = ('VIDEO TITLE / IDEA:\n' + str(title) +
            """
    
    NARRATION SCRIPT (summarize the gist, extract the key topics):
    """
             + str(transcript[None:5000]))
    return [{role: 'system', content: system_msg}, {role: 'user', content:
        user_msg}]



# NOT DECOMPILED: _parse_youtube


# NOT DECOMPILED: generate_youtube_seo
