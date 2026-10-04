# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/db/session.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _attach_sqlite_pragmas
def _attach_sqlite_pragmas(engine):
    event.listens_for(engine, 'connect')
    
    
    def __temp_227992(dbapi_conn, _):
        cur = dbapi_conn.cursor()
        cur.execute('PRAGMA journal_mode=WAL')
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('PRAGMA synchronous=NORMAL')
        cur.close()
        return None
    
    
    _set_sqlite_pragma = __temp_227992()
    return None



# Original qualified name: _attach_sqlite_pragmas.<locals>._set_sqlite_pragma
def _set_sqlite_pragma(dbapi_conn, _):
    cur = dbapi_conn.cursor()
    cur.execute('PRAGMA journal_mode=WAL')
    cur.execute('PRAGMA foreign_keys=ON')
    cur.execute('PRAGMA synchronous=NORMAL')
    cur.close()
    return None



# Original qualified name: get_engine
def get_engine():
    global _engine_url, _SessionMaker, _engine
    db_url = get_settings().db_url
    if _engine is not None:
        if _engine_url != db_url:
            if _engine is not None:
                _engine.dispose()
                _engine = create_engine(db_url, connect_args={
                    'check_same_thread': False}, future=True)
            else:
                _engine = create_engine(db_url, connect_args={
                    'check_same_thread': False}, future=True)
            _attach_sqlite_pragmas(_engine)
            _engine_url = db_url
            _SessionMaker = None
    else:
        if _engine is not None:
            _engine.dispose()
            _engine = create_engine(db_url, connect_args={'check_same_thread': 
                False}, future=True)
        else:
            _engine = create_engine(db_url, connect_args={'check_same_thread': 
                False}, future=True)
        _attach_sqlite_pragmas(_engine)
        _engine_url = db_url
        _SessionMaker = None
    return _engine



# Original qualified name: get_sessionmaker
def get_sessionmaker():
    global _SessionMaker
    if _SessionMaker is None:
        _SessionMaker = sessionmaker(bind=get_engine(), autoflush=False,
            expire_on_commit=False, future=True)
    return _SessionMaker



# Original qualified name: SessionLocal
def SessionLocal():
    return get_sessionmaker()()



# NOT DECOMPILED: session_scope


# Original qualified name: _alembic_config
def _alembic_config():
    sys = __import__('sys', fromlist=None, level=0)
    if getattr(sys, 'frozen', False):
        base = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parents[2]))
        ini_path = base / 'alembic.ini'
        script_location = base / 'alembic_migrations'
    else:
        backend_dir = Path(__file__).resolve().parents[2]
        ini_path = backend_dir / 'alembic.ini'
        script_location = backend_dir / 'alembic'
    cfg = Config(str(ini_path))
    cfg.set_main_option('script_location', str(script_location))
    cfg.set_main_option('sqlalchemy.url', get_settings().db_url)
    cfg.attributes['vs_db_url'] = get_settings().db_url
    return cfg



# Original qualified name: _has_existing_schema_without_alembic
def _has_existing_schema_without_alembic():
    engine = get_engine()
    inspector = inspect(engine)
    tables = set(inspector.get_table_names())
    __temp_228041 = bool(tables - {'alembic_version'})
    if __temp_228041:
        return 'alembic_version' not in tables
    else:
        return __temp_228041



# Original qualified name: _stamp_existing_schema
def _stamp_existing_schema():
    cfg = _alembic_config()
    command.stamp(cfg, 'head')
    return None



# Original qualified name: _upgrade_schema
def _upgrade_schema():
    cfg = _alembic_config()
    command.upgrade(cfg, 'head')
    return None



# NOT DECOMPILED: _db_revision


# NOT DECOMPILED: _revision_is_known


# NOT DECOMPILED: _ensure_compat_columns


# NOT DECOMPILED: init_db


# NOT DECOMPILED: get_session


# NOT DECOMPILED: db_ts
