# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/pipeline/steps/voice_timing.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# NOT DECOMPILED: VoiceTimingStep.run


# Original qualified name: VoiceTimingStep.run.<locals>._q
def _q(db, kind):
    nonlocal ctx
    return db.query(SubtitleSegment).filter(SubtitleSegment.video_id == ctx.
        video_id, SubtitleSegment.kind == kind).order_by(SubtitleSegment.seq).all()



# Original qualified name: _Row.__init__
def __init__(self, id_, seq, kind, text):
    __temp_260162, __temp_260163, __temp_260164, __temp_260165 = (id_, seq,
        kind, text)
    self.id = __temp_260162
    self.seq = __temp_260163
    self.kind = __temp_260164
    self.text = __temp_260165
    return None

