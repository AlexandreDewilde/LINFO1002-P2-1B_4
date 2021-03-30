import sqlite3
import os

from flask import Flask
from flask import render_template, redirect, url_for

from config import DEBUG
from db.db import DB


app = Flask(__name__)

db = DB("./db/database.db")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.png'))



if __name__ == "__main__":
    app.run(debug=DEBUG)