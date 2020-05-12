# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/favfruits")
def favfruits():
    return render_template("favfruits.html")

@app.route("/photos")
def photos():
    return render_template("photos.html")

#start the server
if __name__ == "__main__":
    app.debug = True
    app.run()