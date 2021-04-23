import sqlite3
import os
import pathlib
from generate_race import generate_race


db = sqlite3.connect(os.path.join(pathlib.Path(__file__).parent.absolute(), "database.db"))
cursor = db.cursor()


with open(os.path.join(pathlib.Path(__file__).parent.absolute(), "create_db.sql")) as f:
    db_creation = f.read()

cursor.executescript(db_creation)
db.commit()


insert_files = ["insert_animaux_types.sql", "insert_animaux_velages.sql", "insert_animaux.sql", "insert_complications.sql", "insert_familles.sql", "insert_types.sql", "insert_velages_complications.sql", "insert_velages.sql"]


for insert_file in insert_files:
    with open(os.path.join(pathlib.Path(__file__).parent.absolute(), f"./1002-sql-data/{insert_file}")) as f:
        insert_content = f.read()
    
    cursor.executescript(insert_content)
    db.commit()


db.close()

generate_race()