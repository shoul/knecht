# -*- encoding: utf-8 -*-
from __future__ import absolute_import

import os
import subprocess
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
                session=s,
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


@app.route('/edit/<user>/<path:file_path>', methods=['GET', 'POST'])
def edit(user, file_path):
    '''Edit or create file'''

    session = _get_session()
    conf = session['engine']
    form = request.form
    try:
        # get_branch(user, filename)
        pass
    except:
        pass
        # make_branch(user, filename)
    # change_brance(file_branche)

    files = conf.get_drafts() + conf.get_entries() + conf.get_pages()
    # TODO: Add list of user_drafts like below
    #+ conf.get_user_drafts

    # get_branch(user, file)
    if request.method == 'POST':
        # TODO: Make new branch to edit this file
        content = request.form.get('content')

        if request.form.get('preview'):
            # commit()
            # acrylamid_compile(preview)
            # preview(file_path)
            return render_template('form.html', content=content)

        if request.form.get('save'):
            # commti()
            # arcylamid_compile(deploy)
            # merge branche
            # delete preview
            return redirect('/')
    else:
        for _file in files:
            if (file_path == _file.filename):
                return render_template('form.html', content=conf.rawsource(_file))
        # Give epty template

