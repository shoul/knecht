# -*- encoding: utf-8 -*-
from __future__ import absolute_import
import os

from .utils import Obj

from flask import Flask, request, session, g, redirect, abort, render_template, flash

from .acrblog import Engine

conf = Obj()
app = Flask('knecht')

# TODO get settings from knecht conf.py
conf.blogbase = os.getcwd() + "/repos/"
conf.blogconf = 'conf.py'


def get_bolg(session):
    try:
        blog = Engine(session)
    except Exception as e:
        print (e)
        blog = None
    return blog


@app.route('/')
def index():
    session = Obj()
    session.user = 'foo'
    session.conf = conf
    # TODO: Get user from auth
    user_drafts = '' # TODO: Get user drafts from user repo
    blog = get_bolg(session)
    drafts = blog.get_drafts()
    pages = blog.get_pages()
    entries = blog.get_entries()
    return render_template('entry_list.html', user_drafts=user_drafts, drafts=drafts, pages=pages, entries=entries)


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


def genList(path, entries):
    for e in entries:
        try:
            tags = " [%s]" % ", ".join(e.tags)
        except Exception:
            tags = ''
        yield '<li><time datetime="%s">%s</time> <a href="%s%s">%s</a>%s</li>' % (e.date, e.date, path, e.filename, e.props.title, tags)
