# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/adapters/tts/omnivoice_presets.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _bundled_voices_dir
def _bundled_voices_dir():
    if getattr(sys, 'frozen', False):
        return Path(getattr(sys, '_MEIPASS', '.')
            ) / 'app' / 'resources' / 'omnivoice_voices'
    return Path(__file__).resolve().parents[2] / 'resources' / 'omnivoice_voices'



# NOT DECOMPILED: _install_clone_audio


# Original qualified name: seed_presets
def seed_presets():
    app = __import__('app.db.session', fromlist=('SessionLocal',), level=0)
    SessionLocal = app.SessionLocal
    app = __import__('app.db.models', fromlist=('ClonedVoice',), level=0)
    ClonedVoice = app.ClonedVoice
    seeded = 0
    with SessionLocal() as __temp_136591:
        db = __temp_136591
        for __temp_136592 in iter(OMNIVOICE_PRESETS):
            v = __temp_136592
            vid = v['id']
            design = json.dumps(v['spec'], ensure_ascii=False)
            row = db.get(ClonedVoice, vid)
            if row is None:
                db.add(ClonedVoice(id=vid, name=v['name'], gender=v.get(
                    'gender'), lang='vi', engine='omnivoice', design_json=
                    design, is_preset=1))
            else:
                (__temp_136599, __temp_136600, __temp_136601, __temp_136602,
                    __temp_136603, __temp_136604) = v['name'], v.get('gender'
                    ), 'vi', 'omnivoice', design, 1
                row.name = __temp_136599
                row.gender = __temp_136600
                row.lang = __temp_136601
                row.engine = __temp_136602
                row.design_json = __temp_136603
                row.is_preset = __temp_136604
            seeded += 1
            continue
        for __temp_136605 in iter(OMNIVOICE_CLONE_PRESETS):
            v = __temp_136605
            vid = v['id']
            if not _install_clone_audio(vid, v['file']):
                continue
                row = db.get(ClonedVoice, vid)
            else:
                row = db.get(ClonedVoice, vid)
            if row is None:
                db.add(ClonedVoice(id=vid, name=v['name'], gender=v.get(
                    'gender'), lang=v['lang'], engine='omnivoice', ref_text=v[
                    'ref_text'], design_json=None, is_preset=1))
            else:
                (__temp_136613, __temp_136614, __temp_136615, __temp_136616,
                    __temp_136617, __temp_136618) = (v['name'], v.get('gender'),
                    'omnivoice', v['ref_text'], None, 1)
                row.name = __temp_136613
                row.gender = __temp_136614
                row.engine = __temp_136615
                row.ref_text = __temp_136616
                row.design_json = __temp_136617
                row.is_preset = __temp_136618
                if not row.lang:
                    row.lang = v['lang']
            seeded += 1
            continue
        db.commit()
        if seeded:
            log.info('Seed ' + str(seeded) + ' giọng OmniVoice ship sẵn (' +
                str(len(OMNIVOICE_PRESETS)) + ' design + ' + str(len(
                OMNIVOICE_CLONE_PRESETS)) + ' clone).')
            return seeded
        else:
            return seeded

