# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/news_crawler_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: guess_category


# NOT DECOMPILED: _article_to_dict


# NOT DECOMPILED: parse_feed_xml


# NOT DECOMPILED: fetch_feed


# Original qualified name: store_articles
def store_articles(db, items, project_id):
    created_ids = []
    for __temp_275651 in iter(items):
        item = __temp_275651
        existing = db.query(NewsArticle).filter(NewsArticle.url == item['url']
            ).first()
        if existing:
            dirty = False
            if existing.image_url is None:
                if item.get('image_url'):
                    existing.image_url = item['image_url']
                    dirty = True
            if existing.category in (None, '', 'world'):
                if item.get('category') not in (None, '', 'world'):
                    existing.category = item['category']
                    dirty = True
            if existing.summary_origin is None:
                if item.get('summary_origin'):
                    existing.summary_origin = item['summary_origin']
                    dirty = True
            if dirty:
                db.flush()
                continue
                article = NewsArticle(project_id=project_id, source=item[
                    'source'], url=item['url'], guid=item.get('guid'),
                    title_origin=item['title_origin'], summary_origin=item.get(
                    'summary_origin'), image_url=item.get('image_url'),
                    published_at=item.get('published_at'), category=item.get(
                    'category', 'world'))
            else:
                continue
                article = NewsArticle(project_id=project_id, source=item[
                    'source'], url=item['url'], guid=item.get('guid'),
                    title_origin=item['title_origin'], summary_origin=item.get(
                    'summary_origin'), image_url=item.get('image_url'),
                    published_at=item.get('published_at'), category=item.get(
                    'category', 'world'))
        else:
            article = NewsArticle(project_id=project_id, source=item['source'],
                url=item['url'], guid=item.get('guid'), title_origin=item[
                'title_origin'], summary_origin=item.get('summary_origin'),
                image_url=item.get('image_url'), published_at=item.get(
                'published_at'), category=item.get('category', 'world'))
        db.add(article)
        db.flush()
        created_ids.append(article.id)
        continue
    return created_ids



# NOT DECOMPILED: crawl_now


# NOT DECOMPILED: list_articles


# NOT DECOMPILED: list_topics


# NOT DECOMPILED: _unpack_meta


# Original qualified name: _unpack_meta.<locals>._prop
def _prop(prop):
    nonlocal soup
    el = soup.find('meta', attrs={'property': prop})
    if el:
        if el.get('content'):
            return el['content'].strip()
    el = soup.find('meta', attrs={'name': prop})
    if el:
        if el.get('content'):
            return el['content'].strip()
    return None



# NOT DECOMPILED: _unpack_meta.<locals>._first


# NOT DECOMPILED: _load_meta


# NOT DECOMPILED: fetch_article_full_text


# NOT DECOMPILED: read_article
