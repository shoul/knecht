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
        self._session = session
        try:
            self._root = os.path.join(session.conf.blogbase, session.user)
            confile = os.path.join(self._root, session.conf.blogconf)
            self.conf = loadconf(confile)
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

    def store_file(self, file_path, content):
        log.trace("some messy work to do: " + file_path)
        pass

    def finish_file(self, file_path):
        log.trace("some messy work to do: " + file_path)
        pass

    def get_file_content(self, file_path):
        # TODO sanitize file_path
        # TODO if file in user_drafts get it from scm
        # TODO get entry encoding

        with io.open(os.path.join(self._root, file_path), 'r', encoding='utf-8', errors='replace') as f:
            return ''.join(f.readlines())

        raise IOError("file not found: %s " % file_path)

    def preview(self, file_path=None):
        log.trace("some messy work to do: " + file_path)
        pass

    def deploy(self):
        log.trace("some messy work to do")
        pass

