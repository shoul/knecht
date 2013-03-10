#!/bin/env python2.7
# -*- encoding: utf-8 -*-

import abc

class Engine(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_user_drafts(self):
        '''Get unfinished user entries'''

    @abc.abstractmethod
    def get_entries(self):
        '''Get all the rest entries'''

    @abc.abstractmethod
    def get_pages(self):
        '''Get static pages'''

    @abc.abstractmethod
    def get_drafts(self):
        '''Get all entries that marked as draft'''

    @abc.abstractmethod
    def store_entry(self, entry):
        '''stores the content'''

    @abc.abstractmethod
    def preview(self, entry=None):
        '''renders a preview'''

    @abc.abstractmethod
    def deploy(self):
        '''deploys rendered content'''


# TODO create own Entry class to abstract from Acrylamid
# properties: title, date, filepath
# methods: content(raw)

# TODO add a global entry cache?

