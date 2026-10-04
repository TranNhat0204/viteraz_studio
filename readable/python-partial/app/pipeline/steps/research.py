# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/research.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _is_factual
def _is_factual(engine, config):
    flag = config.get('research_enabled')
    if flag is not None:
        return bool(flag)
    if engine.meta.get('factual'):
        return True
    b = channel_engines.bundle_engine(engine.id)
    if b:
        return bool(b.meta.get('factual'))
    else:
        return bool(b)



# NOT DECOMPILED: _build_research_prompt


# NOT DECOMPILED: _normalize_research


# NOT DECOMPILED: _normalize_research.<locals>._strlist


# Original qualified name: build_facts_block
def build_facts_block(research, language):
    if research:
        if not research.get('enabled'):
            return
    else:
        return
    __temp_256658 = research.get('facts')
    if not __temp_256658:
        facts = []
    else:
        facts = __temp_256658
    __temp_256660 = research.get('surprising')
    if not __temp_256660:
        surprising = []
    else:
        surprising = __temp_256660
    __temp_256662 = research.get('vivid_details')
    if not __temp_256662:
        vivid = []
    else:
        vivid = __temp_256662
    __temp_256664 = research.get('emotional_stakes')
    if not __temp_256664:
        stakes = ''.strip()
    else:
        stakes = __temp_256664.strip()
    if not facts:
        if not surprising:
            if not vivid:
                if not stakes:
                    return
    lines = []
    if facts:
        lines += ['━━━ VERIFIED FACTS — GROUND THE SCRIPT ONLY IN THESE ━━━',
            'You MUST base every concrete claim (dates, numbers, names, statistics, quotes) ONLY on the facts below. Do NOT invent specifics that are not listed here — if a detail is missing, speak generally instead of fabricating it. Weave these naturally into the narration; do not list them mechanically.'
            ]
        for __temp_256669 in iter(facts):
            f = __temp_256669
            __temp_256670 = f.get('point')
            if not __temp_256670:
                point = ''
            else:
                point = __temp_256670
            __temp_256671 = f.get('detail')
            if not __temp_256671:
                detail = ''
            else:
                detail = __temp_256671
            if point:
                if detail:
                    body = str(point) + ' — ' + str(detail)
                elif not point:
                    body = detail
                else:
                    body = point
            elif not point:
                body = detail
            else:
                body = point
            lines.append('- ' + str(body))
            continue
        __temp_256673 = research.get('caveats')
        if not __temp_256673:
            caveats = ''.strip()
        else:
            caveats = __temp_256673.strip()
        if caveats:
            lines.append(
                "UNCERTAIN / DISPUTED (hedge these, don't state as hard fact): " +
                str(caveats))
    if not surprising:
        if not vivid:
            if stakes:
                lines.append(
                    '━━━ STORY MATERIAL — use to make it gripping, real and emotional (still all TRUE) ━━━'
                    )
                if stakes:
                    lines.append(
                        'EMOTIONAL STAKES (build the emotion on this): ' + str(
                        stakes))
                if surprising:
                    lines.append(
                        'SURPRISING TRUTHS (great for the hook / turns): ' +
                        '; '.join(surprising))
                if vivid:
                    lines.append(
                        'VIVID CONCRETE DETAILS (drop these in so it feels real, not generic): '
                         + '; '.join(vivid))
                    return '\n'.join(lines) + '\n\n'
                else:
                    return '\n'.join(lines) + '\n\n'
            else:
                return '\n'.join(lines) + '\n\n'
        else:
            lines.append(
                '━━━ STORY MATERIAL — use to make it gripping, real and emotional (still all TRUE) ━━━'
                )
            if stakes:
                lines.append('EMOTIONAL STAKES (build the emotion on this): ' +
                    str(stakes))
            if surprising:
                lines.append('SURPRISING TRUTHS (great for the hook / turns): ' +
                    '; '.join(surprising))
            if vivid:
                lines.append(
                    'VIVID CONCRETE DETAILS (drop these in so it feels real, not generic): '
                     + '; '.join(vivid))
                return '\n'.join(lines) + '\n\n'
            else:
                return '\n'.join(lines) + '\n\n'
    else:
        lines.append(
            '━━━ STORY MATERIAL — use to make it gripping, real and emotional (still all TRUE) ━━━'
            )
        if stakes:
            lines.append('EMOTIONAL STAKES (build the emotion on this): ' + str
                (stakes))
        if surprising:
            lines.append('SURPRISING TRUTHS (great for the hook / turns): ' +
                '; '.join(surprising))
        if vivid:
            lines.append(
                'VIVID CONCRETE DETAILS (drop these in so it feels real, not generic): '
                 + '; '.join(vivid))
            return '\n'.join(lines) + '\n\n'
        else:
            return '\n'.join(lines) + '\n\n'



# NOT DECOMPILED: _write_sources_file


# NOT DECOMPILED: ResearchStep.run


# Original qualified name: ResearchStep._persist
def _persist(video_id, research):
    with SessionLocal() as __temp_256748:
        db = __temp_256748
        plan = db.query(ContentPlan).filter(ContentPlan.video_id == video_id
            ).first()
        if plan is not None:
            plan.research_json = json.dumps(research, ensure_ascii=False)
            db.commit()
            return None
        else:
            return None

