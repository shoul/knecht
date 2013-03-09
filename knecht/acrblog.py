#!/bin/env python2.7
# -*- encoding: utf-8 -*-

import logging as log
import io
import os

from acrylamid.core import load as loadconf
from acrylamid.readers import load as loadentries

class Engine():
    def __init__(self, session):
        try:
            path = os.path.join(session.conf['blogbase'], session.user, session.conf.blogconf)
            self.conf = loadconf(path)
            (self.__entries, self.__pages, _, self.__drafts) = loadentries(self.conf)
        except Exception as e:
            log.critical("%s in `conf.py`" % e.__class__.__name__)
            raise Exception("fail to initialize Acrylamid")
        self.__user_drafts = [] # Draft in current user branche
        
    def get_user_drafts(self):
        '''Get draft from unclosed user branche'''
        pass

    def get_entries(self):
        return self.__entries

    def get_pages(self):
        return self.__pages

    def get_drafts(self):
        '''Get entrys with draft true'''
        return self.__drafts

    def rawsource(self, entry):
        with io.open(entry.filename, 'r', encoding=entry.props['encoding'],
                errors='replace') as f:
            return ''.join(f.readlines())
