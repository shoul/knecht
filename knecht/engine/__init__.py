#!/bin/env python2.7
# -*- encoding: utf-8 -*-

import abc

# TODO add a global entry cache?

class Engine(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, session):
        '''constructor'''

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
    def store_file(self, file_path, content):
        '''stores the content into a file
           will do all the messy work'''

    @abc.abstractmethod
    def finish_file(self, file_path):
        '''stores the content into a file
           will do all the messy work'''

    @abc.abstractmethod
    def get_file_content(self, file_path):
        '''retrieves the entry content'''

    @abc.abstractmethod
    def preview(self, file_path=None):
        '''renders a preview'''

    @abc.abstractmethod
    def deploy(self):
        '''deploys rendered content'''


class Entry(object):
    def __init__(self, title=None, date=None, path=None):
        self._title = title
        self._date = date
        self._path = path

    @property
    def title(self):
        return self._title

    @property
    def date(self):
        return self._date

    @property
    def path(self):
        return self._path

