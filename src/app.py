import sqlite3

from flask import Flask
from flask import render_template

from config import DEBUG


app = Flask(__name__)


db = sqlite3.connect("./db/database.db", check_same_thread=False)
cursor = db.cursor()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/example")
def exemple():
    req = "SELECT * FROM animaux WHERE id == 1225"
    animal = cursor.execute(req).fetchone()
    animal_sexe = animal[2]
    return f"Le sexe de l'animal est {animal_sexe}"


if __name__ == "__main__":
    app.run(debug=DEBUG)