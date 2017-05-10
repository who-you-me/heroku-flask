# -*- coding: utf-8 -*-

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/profile")
def profile():
    # this line is too too too too too too too too too too too too too too too too long for me
    return "hoge"
