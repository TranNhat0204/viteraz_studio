# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/stock_generate.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _scene_queries


# NOT DECOMPILED: StockGenerateStep.run


# NOT DECOMPILED: StockGenerateStep._search_pick


# Original qualified name: StockGenerateStep._search_pick.<locals>._rel
def _rel(c):
    nonlocal qtok
    __temp_256918 = getattr(c, 'keywords', '')
    if not __temp_256918:
        return len(qtok & set(channel_engines.content_tokens('')))
    else:
        return len(qtok & set(channel_engines.content_tokens(__temp_256918)))



# NOT DECOMPILED: StockGenerateStep._search_pick.<locals>._score


# NOT DECOMPILED: StockGenerateStep._save_scenes
