#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from knecht import app, conf
from knecht.acrblog import Engine

conf.blogbase = os.getcwd() + "/test_blog/"
conf.blogconf = conf.blogbase + "conf.py"

try:
    conf.blog = Engine()
    conf.blog.refresh(conf)
except Exception as e:
    print (e)
    conf.blog = None

app.config.from_object({})
app.run(debug=True, use_reloader=False, port=8000)

