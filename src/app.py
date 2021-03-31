import sqlite3
import os
import pathlib

from flask import Flask
from flask import render_template, redirect, url_for

from config import DEBUG
from db.db import DB
from birth_moon import birth_moon


app = Flask(__name__)

db = DB(os.path.join(pathlib.Path(__file__).parent.absolute(), "db/database.db"))

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", birth_moon=birth_moon(db.get_all_births()))


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.png'))



if __name__ == "__main__":
    print(len(db.get_all_animals_familly_name()))
    app.run(debug=DEBUG)