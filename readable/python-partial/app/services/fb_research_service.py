# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/fb_research_service.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _loads


# Original qualified name: _linked_pairs
def _linked_pairs(db):
    return db.query(ScheduleConfig, FbPage).join(FbPage, FbPage.id ==
        ScheduleConfig.fb_page_id).filter(ScheduleConfig.fb_page_id.isnot(None)
        ).order_by(ScheduleConfig.updated_at.desc()).all()



# NOT DECOMPILED: linked_channels


# NOT DECOMPILED: idea_to_card


# NOT DECOMPILED: post_to_card


# NOT DECOMPILED: suggest_for_channel


# NOT DECOMPILED: suggest_all


# NOT DECOMPILED: approve_video_idea


# Original qualified name: approve_post_card
def approve_post_card(post_id):
    with SessionLocal() as __temp_272233:
        db = __temp_272233
        post = db.get(PostCard, post_id)
        if post is None:
            raise StudioError(E.UNKNOWN,
                'Bài viết không tồn tại ở Research Hub', status_code=404)
        pl = _loads(post.payload_json, {})
        if not pl.get('image_path'):
            if not _loads(post.images_json, []):
                raise StudioError(E.UNKNOWN,
                    'Bài chưa có ảnh bìa. Hãy mở trang Duyệt bài và bấm Sinh ảnh AI trước khi duyệt.'
                    , status_code=409)
        approved = aipost.approve_post(db, post_id)
        {post_id: post_id, status: approved.status, message:
            'Bài đã vào hàng đợi đăng.'}



# Original qualified name: reject_video_idea
def reject_video_idea(idea_id):
    with SessionLocal() as __temp_272246:
        db = __temp_272246
        idea = db.get(IdeaCard, idea_id)
        if idea is None:
            raise StudioError(E.UNKNOWN, 'Ý tưởng không tồn tại', status_code=404)
        if idea.status != 'proposed':
            raise StudioError(E.UNKNOWN,
                'Ý tưởng đã xử lý, không còn loại được.', status_code=409)
        idea.status = 'rejected'
        db.commit()
        {idea_id: idea_id, status: 'rejected'}



# Original qualified name: reject_post_card
def reject_post_card(post_id):
    with SessionLocal() as __temp_272254:
        db = __temp_272254
        post = db.get(PostCard, post_id)
        if post is None:
            raise StudioError(E.UNKNOWN, 'Bài viết không tồn tại', status_code=404)
        if post.status not in frozenset({'proposed', 'ready'}):
            raise StudioError(E.UNKNOWN,
                'Bài viết đã xử lý, không còn loại được.', status_code=409)
        post.status = 'rejected'
        db.commit()
        {post_id: post_id, status: 'rejected'}



# NOT DECOMPILED: channel_status
