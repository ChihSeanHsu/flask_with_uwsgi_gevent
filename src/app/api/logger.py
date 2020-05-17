import logging
import logging.config
import os
import platform

from flask import logging as flask_logging

HAS_CREATE = False

class HostnameFilter(logging.Filter):
    hostname = platform.node()

    def filter(self, record):
        record.hostname = HostnameFilter.hostname
        return True


def get_logger(name):
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s [%(hostname)s][%(threadName)s][%(name)s] %(message)s (%(filename)s: %(lineno)d)'
    )

    handler = logging.StreamHandler()
    handler.addFilter(HostnameFilter())
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler)

    level = getattr(logging, os.environ.get('LOG_LEVEL', 'INFO'))
    logger.setLevel(level)

    if name == 'main':
        flask_logging.default_handler = handler

    return logger