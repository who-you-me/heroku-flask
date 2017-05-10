# -*- coding: utf-8 -*-

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/profile")
def profile():
    import sys
    if True:
        if True:
            if True:
               if True:
                    print("Trueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!")
    return "hoge"
##aaaa
