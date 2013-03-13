# -*- encoding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask, request, session, g, redirect, abort, render_template, flash
from .engine import Engine
from .utils import load_config, Metadata

# TODO add logging features http://flask.pocoo.org/docs/errorhandling/#application-errors

conf = load_config('KNECHT_CONFIG')

app = Flask('knecht')
app.config.from_object(conf._raw)

@app.route('/')
def index():
    s = _get_session()
    return render_template('entry_list.html',
                basepath='/edit/' + s.user,
                user_drafts=s.engine.get_user_drafts(),
                drafts=s.engine.get_drafts(),
                pages=s.engine.get_pages(),
                entries=s.engine.get_entries())


@app.route('/edit/<user>/<path:file_path>', methods=['GET', 'POST'])
def edit(user, file_path):
    '''Setup Edit form and fill it with file content'''
    s = _get_session()

    if file_path.strip('/').split('/')[-1] == 'new':
        return render_template('form.html', content=new_entry(s))

    try:
        # TODO adjust preview and finish URIs in form.html
        return render_template('form.html', content=s.engine.get_file_content(file_path))
    except Exception as e:
        print e
        redirect('/')

    # TODO move preview code into own method (save_and_preview)
    #      and call it asynchronously? Use fancy user feedback.

    if request.method == 'POST':
        content = request.form.get('content')
        try:
            s.engine.store_file(file_path, content)
        except Exception as e:
            print e
            # TODO something messed the commit up
            #      there is no way to solve this exception
            # return message to user and send stacktrace to admin

        try:
            s.engine.preview(file_path)
        except Exception as e:
            print e
            # TODO the file content could be faulty and cause an
            #      render error
            # return user feedback

        # TODO move edit_finish code into own method

        if request.form.get('save'):
            try:
                s.engine.finish_file(file_path)
            except Exception as e:
                print e
                # TODO something messed the final merge completely up
                #      there is no way to solve this exception
                # return user feedback and send stacktrace to admin

            # TODO provide user feedback that everything went well
            return redirect('/')
        # faulty request
        abort(500)


def new_entry(s):
    '''Make a new enty in blog engine'''

    import datetime
    import hashlib
    h = hashlib.new('ripemd160')
    now = datetime.datetime.now().strftime('%d.%m.%Y, %H:%M')
    h.update(now)
    base_headers = [
    '-' * 3,
    'title: %s' % 'NEW ENTRY',
    'date: %s' % now,
    'author: %s' % s.user,
    'tags: []',
    'filters: ',
    'permalink: ',
    'type: ',
    'encoding:',
    'lang:',
    'draft: False',
    'layout:',
    '-' * 3, ]

    # TODO: save file with base content in new branch
    tmp_name = h.hexdigest()

    return '\n'.join(base_headers)


def _get_session():
    # TODO Get user from auth
    user = 'foo'
    # TODO cache sessions
    s = Metadata( { 'user' : str, 'conf' : Metadata, 'engine' : Engine } )
    s.user = user
    s.conf = conf
    try:
        s.engine = conf.engine(s)
    except Exception as e:
        # TODO add logging
        print e
        abort(500)
    return s
