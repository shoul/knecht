# -*- encoding: utf-8 -*-

import logging

info = debug = warn = critical = error = fatal = exception = None
i = d = w = c = e = f = x = None

__all__ = ['info', 'debug', 'warn', 'critical', 'error', 'fatal', 'exception',
            'i', 'd', 'w', 'c', 'e', 'f', 'x' ]

def init(name, level=logging.WARN):
    global info,  debug, warn, critical, error, fatal, exception, \
            i, d, w, c, e, f, x

    log = logging.getLogger(name)
    h = logging.StreamHandler()
    h.setLevel(level)
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    h.setFormatter(fmt)
    log.addHandler(h)

    i = info = log.info
    d = debug = log.debug
    w = warn = log.warn
    c = critical = log.critical
    e = error = log.error
    f = fatal = log.fatal
    x = exception = log.exception

