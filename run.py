#!/usr/bin/python
#-*- coding: UTF-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello, world'
