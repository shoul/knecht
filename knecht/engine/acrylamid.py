#!/bin/env python2.7
# -*- encoding: utf-8 -*-
from __future__ import absolute_import

import logging as log
import io
import os

from . import Engine, Entry

from acrylamid.core import load as loadconf
from acrylamid.readers import load as loadentries

class AcrylamidEngine(Engine):
    def __init__(self, session):
        # TODO retrieve user drafts from SCM
        self.__user_drafts = []
        try:
            path = os.path.join(session.conf.blogbase, session.user, session.conf.blogconf)
            self.conf = loadconf(path)
            (self.__entries, self.__pages, _, self.__drafts) = loadentries(self.conf)
        except Exception as e:
            log.critical("fail to initialize Acrylamid: %s" % str(e))
            raise e

    def get_user_drafts(self):
        return self.__user_drafts

    def get_entries(self):
        return self._wrap_entries(self.__entries)

    def get_pages(self):
        return self._wrap_entries(self.__pages)

    def get_drafts(self):
        return self._wrap_entries(self.__drafts)

    def _wrap_entries(self, entries):
        for e in entries:
            yield Entry(e.props.title, e.date, e.filename)
        raise StopIteration()

    def store_entry(self, entry):
        pass

    def preview(self, entry=None):
        pass

    def deploy(self):
        pass

    def get_entry_content(self, entry):
        # TODO get entry encoding
        with io.open(entry.path, 'r', encoding='utf-8', errors='replace') as f:
            return ''.join(f.readlines())
