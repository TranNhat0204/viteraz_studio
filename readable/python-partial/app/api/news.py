# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/news.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: crawl_now_endpoint


# Original qualified name: list_articles_endpoint
def list_articles_endpoint(source, q, category, limit, offset, project_id, db):
    return svc.list_articles(db, source=source, q=q, category=category, limit=
        limit, offset=offset, project_id=project_id)



# Original qualified name: list_topics_endpoint
def list_topics_endpoint(project_id, db):
    topics = svc.list_topics(db, project_id=project_id)
    return {'topics': topics}



# NOT DECOMPILED: read_article_endpoint


# NOT DECOMPILED: import_article_to_channel
