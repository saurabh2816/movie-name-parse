#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import os
import PTN

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo":PTN.parse("10.Days.with.Dad.2020.480p.Farsi.Subbed.HivaMovie.mkv")})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
