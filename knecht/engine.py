#!/bin/env python2.7
# -*- encoding: utf-8 -*-

import logging as log
import io
import os

from acrylamid.core import load as loadconf
from acrylamid.readers import load as loadentries

class Engine(object):
    def __init__(self, session):
        pass

class AcrylamidEngine():
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
        '''Get unfinished user entries'''
        return self.__user_drafts

    def get_entries(self):
        '''Get all the rest entries'''
        return self.__entries

    def get_pages(self):
        '''Get static pages'''
        return self.__pages

    def get_drafts(self):
        '''Get all entries that marked as draft'''
        return self.__drafts

    def rawsource(self, entry):
        with io.open(entry.filename, 'r', encoding=entry.props['encoding'],
                errors='replace') as f:
            return ''.join(f.readlines())
