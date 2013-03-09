#!/bin/env python2.7
# -*- encoding: utf-8 -*-

import itertools

class Obj(dict):
    """A dict with attribute-style access."""

    __setattr__ = dict.__setitem__

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __delattr__(self, name):
        try:
            del self[name]
        except KeyError:
            raise AttributeError(name)

    def __hash__(self):
        return hash(*itertools.chain(self.keys(), self.values()))

