# -*- encoding: utf-8 -*-

import imp
import os

from importlib import import_module
from types import ModuleType

from knecht.engine import Engine
from knecht import log


def load_config(env_var):
    c = Metadata({
        '_raw' : ModuleType,
        'repos' : str,
        'blogconf' : str,
        'engine' : Engine
    })
    c._raw = imp.new_module('config')

    # defaults
    _ns = c._raw.__dict__
    _ns['ENGINE'] = 'knecht.engine.acrylamid.AcrylamidEngine'
    _ns['BLOGCONF'] = 'conf.py'

    try:
        filepath = os.getenv(env_var, os.path.join(os.getcwd(), 'conf.py'))
        c._raw.__file__ = filepath
        execfile(filepath, _ns)
    except Exception, e:
        e.strerror = 'fail to load configuration file: (%s)' % e.strerror
        raise

    for key in dir(c._raw):
        if key.isupper() and key.lower() in c._allowed_keys:
            k = key.lower()
            v = getattr(c._raw, key)
            if k in ('engine'):
                v = v.rsplit('.', 1)
                c[k] = getattr(import_module(*v), v[-1])
            else:
                c[k] = v

    #validate
    for k in ('repos', 'engine'):
        try:
            if not c[k]:
                raise KeyError()
        except KeyError:
            raise AttributeError('incomplete configuration file: %s, missing settings for : %s'
                    % (filepath, k.upper()))

    log.setLevel(log.INFO if getattr(c._raw, 'DEBUG', False) else log.WARN)

    return c


"""Configurable metadata container
borrowed from https://bitbucket.org/keimlink/metadata
+ fixed _check_value (issubclass)
"""

class Metadata(dict):
    """Metadata container class.

    Accepts only preconfigured keys and enforces type for key's value.
    """
    def __init__(self, allowed_keys, mapping=None):
        """Use the allowed_keys argument to set the keys dictionary.

        The optional mapping parameter can be used to set the attributes
        on initialization.

        Example:

        >>> ALLOWED_KEYS = {
        ...     'id': int,
        ...     'name': str
        ... }
        >>> m = Metadata(ALLOWED_KEYS)
        >>> m.name = 'foo'
        >>> m.id = '23'
        Traceback (most recent call last):
          ...
        TypeError: attribute "id" only allows type "int"
        >>> m.id = 23
        >>> m.name, m.id
        ('foo', 23)
        >>> m.bar = 'baz'
        Traceback (most recent call last):
          ...
        AttributeError: attribute "bar" not allowed
        """
        if '_allowed_keys' in allowed_keys:
            raise KeyError('_allowed_keys is a reserved key')
        super(Metadata, self).__init__(self, _allowed_keys=allowed_keys)
        if mapping is not None:
            try:
                mapping = mapping.items()
            except AttributeError:
                pass
            for key, value in mapping:
                self[key] = value

    def _check_key(self, key):
        """Checks if key is allowed."""
        if key not in self['_allowed_keys']:
            raise AttributeError('attribute "%s" not allowed' % key)

    def _check_value(self, key, value):
        """Checks if value is of type configured for key."""
        attr_type = self['_allowed_keys'][key]
        if not isinstance(value, attr_type) \
                and not (isinstance(value, type) and issubclass(value, attr_type)):
            raise TypeError('attribute "%s" only allows type "%s"'
                % (key, attr_type.__name__))

    def __setattr__(self, key, value):
        """Set key to value.

        Raises an AttributeError if an key is used which is not allowed.
        Raises a TypeError if the value of key is of the wrong type.
        """
        self[key] = value

    def __setitem__(self, key, value):
        self._check_key(key)
        self._check_value(key, value)
        super(Metadata, self).__setitem__(key, value)

    def __getattr__(self, key):
        """Returns the value of key."""
        return self[key]

    def __getitem__(self, key):
        if key is not '_allowed_keys':
            self._check_key(key)
        return super(Metadata, self).__getitem__(key)

    def __delattr__(self, key):
        """Deletes the attribute key."""
        del(self[key])

    def __delitem__(self, key):
        self._check_key(key)
        super(Metadata, self).__delitem__(key)

    def __len__(self):
        """Returns the number of attributes."""
        return len(self._allowed_keys)

    def __reversed__(self):
        raise NotImplementedError("You can't use the reversed function.")

    def __iter__(self):
        """Returns iterator for all defined keys."""
        for key in super(Metadata, self).__iter__():
            if key == '_allowed_keys':
                continue
            yield key

    def items(self):
        """Returns keys and values as tuples."""
        for key in self:
            yield (key, self[key])
