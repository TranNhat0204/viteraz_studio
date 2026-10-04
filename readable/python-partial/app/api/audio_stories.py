# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/audio_stories.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: list_sources
def list_sources():
    return {'sources': svc.list_sources()}



# Original qualified name: browse_stories
def browse_stories(tab, search, genre, limit):
    stories = svc.list_stories(tab=tab, search=search, genre=genre, limit=limit)
    return {stories: stories, count: len(stories)}



# Original qualified name: preview_story
def preview_story(body):
    return svc.preview_story(body.url_or_id)



# Original qualified name: get_chapter
def get_chapter(story_id, chapter_id):
    return svc.get_chapter_content(story_id, chapter_id)



# NOT DECOMPILED: import_to_ai_creator
