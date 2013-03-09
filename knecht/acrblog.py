#!/bin/env python2.7
# -*- encoding: utf-8 -*-

import logging as log
import io

from acrylamid.core import load as loadconf
from acrylamid.readers import load as loadentries

class Engine():
    def __init__(self):
        self.__drafts = []
        self.__entries = []
        self.__pages = []
        self.conf = None

    def getEntries(self):
        return self.__entries

    def getPages(self):
        return self.__pages

    def getDrafts(self):
        return self.__drafts

    def refresh(self, conf):
        print conf.blogconf
        try:
            self.conf = loadconf(conf.blogconf)
            (self.__entries, self.__pages, _, self.__drafts) = loadentries(self.conf)
        except Exception as e:
            log.critical("%s in `conf.py`" % e.__class__.__name__)
            raise Exception("fail to initialize Acrylamid")

    def rawsource(self, entry):
        with io.open(entry.filename, 'r', encoding=entry.props['encoding'],
                errors='replace') as f:
            return ''.join(f.readlines())
