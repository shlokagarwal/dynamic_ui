#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:51:24 2019

@author: shlokagarwal
"""

import time

from flask import Flask
from flask_cors import CORS




app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def home():
    return "Hello, World!"



@app.route("/Teneo")
def home1():
    json = {
            "app_name": "Teneo",
            "width": "500px",
            "height": "310px",
            "innerCode":  "http://127.0.0.1:5500/som.html"
            }
    return json



    
if __name__ == "__main__":


    app.run(debug=True)