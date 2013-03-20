# -*- encoding: utf-8 -*-

import logging
from logging import INFO, DEBUG, WARN

logger = None
info = debug = warn = critical = error = fatal = exception = None
i = d = w = c = e = f = x = None

__all__ = [ 'info', 'debug', 'warn', 'critical', 'error', 'fatal', 'exception',
            'i', 'd', 'w', 'c', 'e', 'f', 'x',
            'logger',
            'INFO', 'DEBUG', 'WARN' ]

def init(name, level=logging.WARN):
    global info, debug, warn, critical, error, fatal, exception, \
            i, d, w, c, e, f, x, \
            logger

    logger = logging.getLogger(name)
    h = logging.StreamHandler()
    h.setLevel(level)
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    h.setFormatter(fmt)
    logger.addHandler(h)

    i = info = logger.info
    d = debug = logger.debug
    w = warn = logger.warn
    c = critical = logger.critical
    e = error = logger.error
    f = fatal = logger.fatal
    x = exception = logger.exception

def setLevel(level):
    global logger
    logger.setLevel(level)
