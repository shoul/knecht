#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from knecht import app

app.run(debug=True, use_reloader=False, port=8000)
