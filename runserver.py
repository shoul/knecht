#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from knecht import app

app.config.from_object({})
app.run(debug=True, use_reloader=False, port=8000)

