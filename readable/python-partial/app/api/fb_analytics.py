# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/api/fb_analytics.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: _loads


# NOT DECOMPILED: _parse_ts


# Original qualified name: _avatar_url
def _avatar_url(page):
    avatar = page.avatar_url
    if avatar:
        if avatar.startswith('http'):
            if 'facebook.com/' in avatar:
                if '/picture' not in avatar:
                    if 'fbcdn' not in avatar:
                        avatar = '/api/v1/fb/pages/' + str(page.id) + '/avatar'
        else:
            avatar = '/api/v1/fb/pages/' + str(page.id) + '/avatar'
    else:
        avatar = '/api/v1/fb/pages/' + str(page.id) + '/avatar'
    return avatar



# Original qualified name: _get_channel_info
def _get_channel_info(db, page):
    cfg = db.query(ScheduleConfig).filter(ScheduleConfig.fb_page_id == page.id
        ).first()
    if not cfg:
        return None, False, None
    project = db.get(Project, cfg.project_id)
    if not project:
        return None, False, None
    app = __import__('app.services', fromlist=('channel_engines',
        'host_service'), level=0)
    channel_engines = app.channel_engines
    host_service = app.host_service
    if cfg.engine_id:
        engine = channel_engines.get_engine(cfg.engine_id)
    else:
        engine = None
    host = host_service.get_host(db, cfg.project_id)
    profile = _loads(cfg.channel_profile_json)
    host_dict = None
    if host:
        host_dict = {id: host.id, name: host.name, description: host.
            description, ref_image_path: host.ref_image_path}
    if engine:
        channel = {project_id: cfg.project_id, project_name: project.name, kind:
            project.kind, engine_id: cfg.engine_id, engine_name: engine.name,
            host_character: host_dict, channel_profile: profile, series_arc:
            cfg.series_arc, post_enabled: bool(cfg.post_enabled), recent_titles:
            _loads(cfg.recent_titles_json, []), recent_post_topics: _loads(cfg.
            recent_post_topics_json, [])}
    else:
        channel = {project_id: cfg.project_id, project_name: project.name, kind:
            project.kind, engine_id: cfg.engine_id, engine_name: None,
            host_character: host_dict, channel_profile: profile, series_arc:
            cfg.series_arc, post_enabled: bool(cfg.post_enabled), recent_titles:
            _loads(cfg.recent_titles_json, []), recent_post_topics: _loads(cfg.
            recent_post_topics_json, [])}
    is_ai = project.kind == 'ai'
    return channel, is_ai, cfg.project_id



# Original qualified name: _compute_health_score
def _compute_health_score(posts_30d, followers, total_likes, total_comments, total_shares, total_posts, type_counts, follower_growth_pct):
    if posts_30d > 0:
        consistency = min(100, int(posts_30d / 30 * 100 * 3.33))
    else:
        consistency = 0
    if followers > 0:
        if total_posts > 0:
            eng_rate = (total_likes + total_comments + total_shares) / (followers *
                total_posts) * 100
        else:
            eng_rate = 0
    else:
        eng_rate = 0
    engagement_score = min(100, int(eng_rate * 20))
    avg_likes = total_likes / max(1, total_posts)
    avg_shares = total_shares / max(1, total_posts)
    if avg_likes > 0:
        virality = avg_shares / max(1, avg_likes) * 100
    else:
        virality = 0
    virality_score = min(100, int(virality * 5))
    if follower_growth_pct is None:
        reach_growth = 0
    else:
        reach_growth = max(0, min(100, int(50 + follower_growth_pct * 10)))
    overall = int(consistency * 0.25 + engagement_score * 0.35 + virality_score *
        0.2 + reach_growth * 0.2)
    return {overall: min(100, overall), consistency: consistency,
        engagement_rate: engagement_score, virality_index: virality_score,
        reach_growth: reach_growth}



# NOT DECOMPILED: _compute_engagement_velocity


# NOT DECOMPILED: _get_competitor_data


# NOT DECOMPILED: _compute_sentiment


# NOT DECOMPILED: _predict_follower_growth


# NOT DECOMPILED: _compute_viral_lifecycle


# NOT DECOMPILED: _build_audience_persona


# NOT DECOMPILED: _build_heatmap


# NOT DECOMPILED: _compute_content_roi


# Original qualified name: _build_ai_recommendations
def _build_ai_recommendations(health, type_counts, total_posts, posts_30d, eng_rate, channel_profile, series_arc, competitor_data):
    niche = channel_profile.get('niche', '')
    __temp_208772, __temp_208773, __temp_208774, __temp_208775 = [], [], [], []
    strengths = __temp_208772
    weaknesses = __temp_208773
    opportunities = __temp_208774
    threats = __temp_208775
    action_items = []
    if eng_rate > 3:
        strengths.append('Engagement Rate ' + format(eng_rate, '.1f') +
            '% — cao hơn trung bình ngành (1-3%)')
    if total_posts > 20:
        strengths.append('Đã đăng ' + str(total_posts) +
            ' bài — khối lượng nội dung tốt')
        __temp_208779 = type_counts.get('video', 0)
        __temp_208780 = type_counts.get('reel', 0)
    else:
        type_counts.get('video', 0)
        type_counts.get('reel', 0)
    if __temp_208779 + __temp_208780 > total_posts * 0.5:
        strengths.append(
            'Tỷ lệ Video/Reel cao — phù hợp thuật toán Facebook ưu tiên video')
    if health['virality_index'] > 60:
        strengths.append('Chỉ số lan truyền cao — bài được chia sẻ nhiều')
    if health['consistency'] > 70:
        strengths.append('Đăng đều đặn (' + str(posts_30d) +
            ' bài/30 ngày) — thuật toán ưu tiên')
    if posts_30d < 10:
        weaknesses.append('Tần suất đăng thấp: chỉ ' + str(posts_30d) +
            ' bài/30 ngày — nên tối thiểu 15 bài')
    if eng_rate < 1:
        weaknesses.append('Engagement Rate chỉ ' + format(eng_rate, '.1f') +
            '% — dưới trung bình (1-3%)')
        __temp_208788 = type_counts.get('reel', 0)
    else:
        type_counts.get('reel', 0)
    if __temp_208788 == 0:
        weaknesses.append(
            'Chưa có Reel ngắn — đang bỏ lỡ format reach cao nhất trên Facebook')
    if health['content_diversity'] < 40:
        weaknesses.append(
            'Nội dung đơn điệu — cần đa dạng hoá format (Video/Reel/Photo/Text)')
        __temp_208792 = type_counts.get('reel', 0)
    else:
        type_counts.get('reel', 0)
    if __temp_208792 == 0:
        opportunities.append(
            'Thêm Reel 15-30 giây — Facebook đang ưu tiên phân phối Reel hơn bài viết'
            )
    if niche:
        opportunities.append('Ngách "' + str(niche) +
            '" đang có trend tăng trưởng — tận dụng keywords hot')
    if competitor_data:
        top_comp = competitor_data[0]
        if top_comp.get('follower_count', 0) > 0:
            opportunities.append('Đối thủ "' + str(top_comp.get('channel_title',
                'N/A')) + '" có ' + format(top_comp['follower_count'], ',') +
                ' followers — nghiên cứu format thành công để áp dụng')
            opportunities.append(
                'Đăng vào khung giờ vàng (xem Heatmap ở trên) để tối đa organic reach'
                )
        else:
            opportunities.append(
                'Đăng vào khung giờ vàng (xem Heatmap ở trên) để tối đa organic reach'
                )
    else:
        opportunities.append(
            'Đăng vào khung giờ vàng (xem Heatmap ở trên) để tối đa organic reach')
    if eng_rate < 1:
        threats.append(
            'Engagement thấp kéo dài → Facebook giảm phân phối → vòng xoáy tiêu cực'
            )
    if posts_30d < 5:
        threats.append(
            'Đăng quá ít → thuật toán "quên" kênh — followers unfollow dần')
        threats.append(
            'Cạnh tranh ngày càng cao trên Facebook — cần liên tục cải tiến chất lượng'
            )
        __temp_208805 = type_counts.get('reel', 0)
    else:
        threats.append(
            'Cạnh tranh ngày càng cao trên Facebook — cần liên tục cải tiến chất lượng'
            )
        type_counts.get('reel', 0)
    if __temp_208805 == 0:
        action_items.append({title: 'Thêm Reel ngắn 15-30s', priority: 'high',
            icon: '🎬', description:
            'Facebook ưu tiên Reel trong thuật toán phân phối. Thêm 2-3 Reel/tuần để tăng reach 50-200%.'
            , action_type: 'update_profile'})
    if posts_30d < 15:
        action_items.append({title: 'Tăng tần suất đăng lên 15+ bài/tháng',
            priority: 'high', icon: '📅', description: 'Hiện tại chỉ ' + str(
            posts_30d) +
            ' bài/tháng. Mục tiêu: 1 bài/ngày để consistency score đạt 80+.',
            action_type: 'update_schedule'})
    if health['content_diversity'] < 50:
        action_items.append({title: 'Đa dạng hoá nội dung', priority: 'medium',
            icon: '🎨', description:
            'Kết hợp Video + Reel + Photo + Text thay vì chỉ 1 loại để diversity score tăng 70+.'
            , action_type: 'update_profile'})
        action_items.append({title: 'Phân tích đối thủ cùng ngách', priority:
            'medium', icon: '🔍', description:
            'Phân tích kênh đối thủ để học hỏi format & chủ đề hiệu quả.',
            action_type: 'navigate_competitor'})
    else:
        action_items.append({title: 'Phân tích đối thủ cùng ngách', priority:
            'medium', icon: '🔍', description:
            'Phân tích kênh đối thủ để học hỏi format & chủ đề hiệu quả.',
            action_type: 'navigate_competitor'})
    if not series_arc:
        action_items.append({title: 'Thiết lập định hướng dài hạn', priority:
            'low', icon: '🎯', description:
            'Cài đặt series_arc trong AI Studio để AI sinh nội dung nhất quán, có chủ đề xuyên suốt.'
            , action_type: 'update_profile'})
        topic_ideas = []
    else:
        topic_ideas = []
    formats = [{format: 'reel', label: 'Reel ngắn 30s'}, {format: 'video',
        label: 'Video chuyên sâu 3-5 phút'}, {format: 'text', label:
        'Bài viết SEO kèm ảnh AI'}]
    for __temp_208826 in iter(formats):
        f = __temp_208826
        if niche:
            topic_ideas.append({title: 'Top xu hướng ' + str(niche) +
                ' tuần này', hook: 
                'Bạn đã biết về trend mới nhất trong lĩnh vực ' + str(niche) +
                '? Hãy cùng khám phá!', format: f['format'], format_label: f[
                'label']})
            continue
            topic_ideas.append({title: 'Nội dung giá trị cho followers', hook:
                'Chia sẻ kiến thức hữu ích để tăng tương tác tự nhiên!', format:
                f['format'], format_label: f['label']})
        else:
            topic_ideas.append({title: 'Nội dung giá trị cho followers', hook:
                'Chia sẻ kiến thức hữu ích để tăng tương tác tự nhiên!', format:
                f['format'], format_label: f['label']})
        continue
    if not strengths:
        __temp_208833 = ['Kênh mới — nhiều tiềm năng phát triển!']
    if not weaknesses:
        return {swot: {strengths: __temp_208833, weaknesses: [
            'Chưa đủ dữ liệu để đánh giá chi tiết'], opportunities:
            opportunities, threats: threats}, action_items: action_items[None:5
            ], topic_ideas: topic_ideas}
    else:
        return {swot: {strengths: __temp_208833, weaknesses: weaknesses,
            opportunities: opportunities, threats: threats}, action_items:
            action_items[None:5], topic_ideas: topic_ideas}



# NOT DECOMPILED: get_page_analytics


# NOT DECOMPILED: clone_viral_post
