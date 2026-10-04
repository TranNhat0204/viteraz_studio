# PARTIAL DECOMPILATION: isolated functions, not a runnable module.
# Module: app/core/logging.pyc
# Original imports, classes, decorators and initialization are NOT reconstructed.


# Original qualified name: setup_logging
def setup_logging():
    logger = logging.getLogger('video-studio')
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s',
            '%H:%M:%S')
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(fmt)
        logger.addHandler(sh)
        configure_file_logging(logger)
        return logger
    else:
        configure_file_logging(logger)
        return logger



# NOT DECOMPILED: configure_file_logging
