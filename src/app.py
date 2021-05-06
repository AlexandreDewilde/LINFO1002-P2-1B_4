import sqlite3
import os
import pathlib
from typing import Dict, Union, List, Tuple

from flask import Flask
from flask import render_template, redirect, url_for

from config import DEBUG
from db import DB
from moon_phases import moon_phases_by_years
from moon_phase import moon_phases_lst
from occurences import occurences_months_by_year
from fam_pre import list_family


app: Flask = Flask(__name__)

db: DB = DB(os.path.join(pathlib.Path(__file__).parent.absolute(), "db/database.db"))


@app.route("/")
@app.route("/index")
def index():
    """
    Render the index html page
    """
    # Fetch data for charts
    families: List[Tuple[int, str]] = db.get_families()
    families_ids: List[int] = [family[0] for family in families]
    families_names: List[str] = [family[1] for family in families]

    births_moon_cycle_by_year: Dict[int, str] = moon_phases_by_years(db.get_births())

    graph_data: Dict[str, Union[list, dict]] = {
        "birth_moon_labels": moon_phases_lst,
        "birth_moon_by_years": births_moon_cycle_by_year,

        "premature_deaths_montly_by_months": occurences_months_by_year(db.get_all_premature_deaths()),

        "families_labels": families_names,
        "families_deaths": list_family(families_ids, db.get_all_premature_deaths_family()),
        "families_alives": list_family(families_ids, db.get_all_living_family()),
    }

    return render_template("index.html", graph_data=graph_data)


@app.route('/about')
def about():
    """
    Render the about page
    """
    return render_template("about.html")


@app.route('/favicon.ico')
def favicon():
    """
    Redirect to the favicon
    """
    return redirect(url_for('static', filename='images/favicon.png'))


@app.errorhandler(404)
def not_found(e):
    """
    Render the 404 page
    """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=DEBUG)