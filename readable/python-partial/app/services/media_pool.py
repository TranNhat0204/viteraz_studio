# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/services/media_pool.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: media_dir
def media_dir(root_path):
    d = ProjectFS(root_path).assets_dir() / 'media'
    d.mkdir(parents=True, exist_ok=True)
    return d



# Original qualified name: index_path
def index_path(root_path):
    return media_dir(root_path) / INDEX_NAME



# NOT DECOMPILED: read_index


# Original qualified name: write_index
def write_index(root_path, items):
    p = index_path(root_path)
    tmp = p.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding=
        'utf-8')
    tmp.replace(p)
    return None



# NOT DECOMPILED: with_media_pool
