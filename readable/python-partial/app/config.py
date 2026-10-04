# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/config.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: _default_data_dir
def _default_data_dir():
    __temp_226727 = os.environ.get('APPDATA')
    if not __temp_226727:
        base = os.path.expanduser('~')
    else:
        base = __temp_226727
    return Path(base) / 'VideoStudio'



# Original qualified name: Settings.__post_init__
def __post_init__(self):
    if self.data_dir is None:
        self.data_dir = _default_data_dir()
    self.data_dir = Path(self.data_dir)
    self.data_dir.mkdir(parents=True, exist_ok=True)
    (self.data_dir / 'logs').mkdir(parents=True, exist_ok=True)
    if self.db_path is None:
        self.db_path = self.data_dir / 'studio.db'
    self.db_path = Path(self.db_path)
    return None



# Original qualified name: Settings.db_url
def db_url(self):
    return 'sqlite:///' + str(self.db_path.as_posix())



# NOT DECOMPILED: parse_settings


# Original qualified name: get_settings
def get_settings():
    global _settings
    if _settings is None:
        _settings = parse_settings()
    return _settings



# Original qualified name: configure_settings
def configure_settings(argv):
    global _settings
    _settings = parse_settings(argv)
    return _settings



# NOT DECOMPILED: omnivoice_workspace_override


# NOT DECOMPILED: omnivoice_runtime_path


# Original qualified name: omnivoice_default_runtime_path
def omnivoice_default_runtime_path():
    return get_settings().data_dir / 'resources' / 'omnivoice'



# NOT DECOMPILED: set_omnivoice_workspace


# Original qualified name: _SettingsProxy.__getattr__
def __getattr__(self, name):
    return getattr(get_settings(), name)

