import sqlite3
import os
import pathlib

from flask import Flask
from flask import render_template, redirect, url_for

from config import DEBUG
from db.db import DB
from birth_moon import birth_moon
from moon_phase import moon_phase_dict
from ma_fonction import pst

app = Flask(__name__)

db = DB(os.path.join(pathlib.Path(__file__).parent.absolute(), "db/database.db"))

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", birth_moon=birth_moon(db.get_all_births()), birth_moon_label=list(moon_phase_dict.values()), deces = pst())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.png'))

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404



if __name__ == "__main__":
    app.run(debug=DEBUG)