# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/market_research_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: research_required
def research_required(engine):
    __temp_274798 = marketing_playbook.get_playbook(engine).get('evidence')
    if not __temp_274798:
        evidence = {}
    else:
        evidence = __temp_274798
    __temp_274801 = bool(engine.meta.get('factual'))
    if not __temp_274801:
        return evidence.get('mode') == 'required'
    else:
        return __temp_274801



# Original qualified name: _clean
def _clean(value):
    if not value:
        return re.sub('\\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', ''))
            ).strip()
    else:
        return re.sub('\\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', value))
            ).strip()



# Original qualified name: _domain
def _domain(url):
    __temp_274811 = urlparse(url)
    if not __temp_274811.hostname:
        return ''.lower().removeprefix('www.')
    else:
        return __temp_274811.hostname.lower().removeprefix('www.')



# NOT DECOMPILED: _credibility


# NOT DECOMPILED: _search


# NOT DECOMPILED: build_brief
