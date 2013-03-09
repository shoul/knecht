# -*- encoding: utf-8 -*-

from .utils import Obj

from flask import Flask, request, session, g, redirect, \
        abort, render_template, flash

conf = Obj()
app = Flask('knecht')

@app.route('/')
def index():
    entries = genList('/edit/', conf.blog.getEntries())
    return '<ul>%s<ul>' % ''.join(entries)

@app.route('/edit/<path:file_path>')
def edit(file_path):
    for e in conf.blog.getEntries():
        if (file_path == e.filename):
            return '<textarea rows="50" cols="100">%s</textarea>' % conf.blog.rawsource(e)

def genList(path, entries):
    for e in entries:
        try:
            tags = " [%s]" % ", ".join(e.tags)
        except Exception:
            tags = ''
        yield '<li><time datetime="%s">%s</time> <a href="%s%s">%s</a>%s</li>' % (e.date, e.date, path, e.filename, e.props.title, tags)
