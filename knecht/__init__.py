# -*- encoding: utf-8 -*-

from flask import Flask, request, session, g, redirect, abort, render_template, flash

from knecht.engine import Engine
from knecht.utils import load_config, Metadata
from knecht import log

log.init(__name__)

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

'''
-- /new (edit_form mit angepasseten POST uris)
-- save_new (pfad erstellen lassen, inhalt von save aufrufen)
-- redirecte nach /edit/gerade_eben_erstellter_pfad_dynamisch

--> /new (edit_form mit angepasseten POST uris)
--> save_new (pfad erstellen lassen, inhalt von save aufrufen)
--> redirecte nach /edit/gerade_eben_erstellter_pfad_dynamisch '''


@app.route('/edit/edit_new_file', methods=['GET', 'POST'])
def new():
    '''Make a new enty in blog engine'''
    s = _get_session()

    if request.method == 'POST':
        if not request.form.get('file_name'):
            return render_template('form.html', edit_new_file=True,
                content=request.form.get('content'),
                message="Ops, we need a file_name.")

        # TODO:
        # * Make branch
        # * Save new file
        # * commit

        # TODO: save file with base content in new branch
        path = '/'.join(['edit', s.user, request.form.get('file_name')])
        redirect('/%s' % path)

    import datetime
    base_headers = [
        '-' * 3,
        'title: %s' % 'NEW ENTRY',
        'date: %s' % datetime.datetime.now().strftime('%d.%m.%Y, %H:%M'),
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

    return render_template('form.html', edit_new_file=True, content='\n'.join(base_headers))



@app.route('/edit/<user>/<path:file_path>', methods=['GET', 'POST'])
def edit(user, file_path):
    '''Setup Edit form and fill it with file content'''
    s = _get_session()

    try:
        # TODO adjust preview and finish URIs in form.html
        return render_template('form.html', content=s.engine.get_file_content(file_path))
    except Exception as e:
        log.x('fail to retrieve content from: %s' % file_path)
        return redirect('/')

    # TODO move preview code into own method (save_and_preview)
    #      and call it asynchronously? Use fancy user feedback.

    if request.method == 'POST':
        try:
            s.engine.store_file(file_path, new_content)
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
            save(file_path)
        # faulty request
        abort(500)


def save():
    '''Save blog and redirect to edit uri'''

    try:
        s.engine.finish_file(file_path)
    except Exception as e:
        print e
        # TODO something messed the final merge completely up
        #      there is no way to solve this exception
        # return user feedback and send stacktrace to admin

    # TODO provide user feedback that everything went well
    return redirect('/')


def _get_session():
    # TODO Get user from auth
    user = 'foo'
    # TODO cache sessions
    s = Metadata( { 'user' : str, 'conf' : Metadata, 'engine' : Engine } )
    s.user = user
    s.conf = conf
    try:
        s.engine = conf.engine(s)
    except Exception:
        log.x('fail to initialize session: User = %s' % s.user)
        abort(500)
    return s
