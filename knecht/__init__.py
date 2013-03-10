# -*- encoding: utf-8 -*-
from __future__ import absolute_import

import os
from flask import Flask, request, session, g, redirect, abort, render_template, flash
from .utils import Obj
from .engine.acrylamid import AcrylamidEngine

# TODO add logging features http://flask.pocoo.org/docs/errorhandling/#application-errors

app = Flask('knecht')

# TODO get settings from knecht conf.py
conf = Obj()
conf.blogbase = os.getcwd() + "/repos/"
conf.blogconf = 'conf.py'
conf.engine = AcrylamidEngine

@app.route('/')
def index():
    s = _get_session()
    return render_template('entry_list.html',
                user_drafts=s.engine.get_user_drafts(),
                drafts=s.engine.get_drafts(),
                pages=s.engine.get_pages(),
                entries=s.engine.get_entries())

def _get_session():
    # TODO: Get user from auth
    user = 'foo'
    # TODO: cache sessions
    s = Obj()
    s.user = user
    s.conf = conf
    try:
        s.engine = conf.engine(s)
    except Exception as e:
        # TODO add logging
        print e
        abort(500)
    return s


#def edit(file_path):
#    for e in conf.blog.getEntries():
#        if (file_path == e.filename):
#            return '<textarea rows="50" cols="100">%s</textarea>' % conf.blog.rawsource(e)


@app.route('/edit/<user>/<path:file_path>', methods=['GET', 'POST'])
def edit(user, file_path):
    '''Edit or create file'''

    # get_branch(user, file)
    if request.method == 'POST':
        #if request.form.button == 'preview':
            # commit()
            # acrylamid_compile(preview)
            # preview(file_path)
        # if request.form.button == 'save':
            # commti()
            # arcylamid_compile(deploy)
            # merge branche
            # delete preview
        pass
    else:
        # Give epty template
        pass

    try:
        # get_branch(user, filename)
        pass
    except:
        pass
        # make_branch(user, filename)
    # change_brance(file_branche)

