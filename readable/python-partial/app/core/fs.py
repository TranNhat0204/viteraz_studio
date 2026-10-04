# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/fs.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: safe_name
def safe_name(name):
    name = re.sub('[<>:"/\\\\|?*]', '_', name).strip().rstrip('.')
    if not name:
        return 'project'
    else:
        return name



# NOT DECOMPILED: strip_accents


# Original qualified name: video_dir_name
def video_dir_name(video_id, order_index, title):
    if not video_id:
        vid = str('').strip()
    else:
        vid = str(video_id).strip()
    if not title:
        slug = re.sub('[^A-Za-z0-9]+', ' ', strip_accents(str(''))).strip()
    else:
        slug = re.sub('[^A-Za-z0-9]+', ' ', strip_accents(str(title))).strip()
    slug = re.sub('\\s+', ' ', slug)
    if len(slug) > _MAX_TITLE_CHARS:
        cut = slug[None:_MAX_TITLE_CHARS]
        if ' ' in cut:
            slug = cut[None:cut.rfind(' ')]
        else:
            slug = cut
    slug = slug.strip()
    if slug:
        if slug.lower() in _WIN_RESERVED:
            return vid
    else:
        return vid
    if order_index is not None:
        prefix = format(int(order_index) + 1, '03d') + ' - '
    else:
        prefix = ''
    return str(prefix) + str(slug) + ' [' + str(vid[None:_SHORT_ID_LEN]) + ']'



# Original qualified name: ProjectFS.__init__
def __init__(self, root):
    self.root = Path(root)
    return None



# Original qualified name: ProjectFS.ensure
def ensure(self):
    (self.root / 'videos').mkdir(parents=True, exist_ok=True)
    return self



# Original qualified name: ProjectFS.videos_root
def videos_root(self):
    return self.root / 'videos'



# NOT DECOMPILED: ProjectFS.find_video_dir


# Original qualified name: ProjectFS.video_dir
def video_dir(self, video_id):
    found = self.find_video_dir(video_id)
    if found is not None:
        return found
    __temp_227413 = self.videos_root()
    if not video_id:
        d = __temp_227413 / str('').strip()
    else:
        d = __temp_227413 / str(video_id).strip()
    d.mkdir(parents=True, exist_ok=True)
    return d



# NOT DECOMPILED: ProjectFS.name_video_dir


# Original qualified name: ProjectFS.source_mp4
def source_mp4(self, vid):
    return self.video_dir(vid) / 'source.mp4'



# Original qualified name: ProjectFS.timeline_mp4
def timeline_mp4(self, vid):
    return self.video_dir(vid) / 'timeline.mp4'



# Original qualified name: ProjectFS.audio_wav
def audio_wav(self, vid):
    return self.video_dir(vid) / 'audio.wav'



# Original qualified name: ProjectFS.audio_source
def audio_source(self, vid):
    return self.video_dir(vid) / 'audio.source.wav'



# Original qualified name: ProjectFS.audio_vocals
def audio_vocals(self, vid):
    return self.video_dir(vid) / 'audio.vocals.wav'



# Original qualified name: ProjectFS.audio_music
def audio_music(self, vid):
    return self.video_dir(vid) / 'audio.music.wav'



# Original qualified name: ProjectFS.subtitle_original
def subtitle_original(self, vid):
    return self.video_dir(vid) / 'subtitle.original.srt'



# Original qualified name: ProjectFS.subtitle_translated
def subtitle_translated(self, vid):
    return self.video_dir(vid) / 'subtitle.translated.srt'



# Original qualified name: ProjectFS.subtitle_premium
def subtitle_premium(self, vid):
    return self.video_dir(vid) / 'subtitle.premium.srt'



# Original qualified name: ProjectFS.subtitle_words
def subtitle_words(self, vid):
    return self.video_dir(vid) / 'subtitle.words.json'



# Original qualified name: ProjectFS.voiceover
def voiceover(self, vid):
    return self.video_dir(vid) / 'voiceover.wav'



# Original qualified name: ProjectFS.conform_map
def conform_map(self, vid):
    return self.video_dir(vid) / 'conform.json'



# Original qualified name: ProjectFS.voice_fit
def voice_fit(self, vid):
    return self.video_dir(vid) / 'voice_fit.json'



# Original qualified name: ProjectFS.preview
def preview(self, vid):
    return self.video_dir(vid) / 'preview.mp4'



# Original qualified name: ProjectFS.thumbnail
def thumbnail(self, vid):
    return self.video_dir(vid) / 'thumbnail.jpg'



# Original qualified name: ProjectFS.thumbnail_generated
def thumbnail_generated(self, vid):
    return self.video_dir(vid) / 'thumbnail.generated.png'



# Original qualified name: ProjectFS.export_dir
def export_dir(self, vid):
    d = self.video_dir(vid) / 'export'
    d.mkdir(parents=True, exist_ok=True)
    return d



# Original qualified name: ProjectFS.assets_dir
def assets_dir(self):
    d = self.root / 'assets'
    d.mkdir(parents=True, exist_ok=True)
    return d



# Original qualified name: ProjectFS.characters_dir
def characters_dir(self):
    d = self.root / 'characters'
    d.mkdir(parents=True, exist_ok=True)
    return d



# Original qualified name: ProjectFS.idea_dir
def idea_dir(self, idea_id):
    d = self.root / 'ideas' / idea_id
    d.mkdir(parents=True, exist_ok=True)
    return d



# Original qualified name: ProjectFS.post_dir
def post_dir(self, post_id):
    d = self.root / 'posts' / post_id
    d.mkdir(parents=True, exist_ok=True)
    return d



# Original qualified name: ProjectFS.output_root
def output_root(self):
    d = self.root / 'output'
    d.mkdir(parents=True, exist_ok=True)
    return d



# NOT DECOMPILED: cleanup_duplicate_dist_info
