import sqlite3
import os
import pathlib
from generate_race import generate_race

def main():
        # Connection to database, it will be created if it doesn't exist
    db = sqlite3.connect(os.path.join(pathlib.Path(__file__).parent.absolute(), "database.db"))
    cursor = db.cursor()

    # Start the sql script that will create tables and columns
    with open(os.path.join(pathlib.Path(__file__).parent.absolute(), "create_db.sql")) as f:
        db_creation = f.read()

    cursor.executescript(db_creation)
    db.commit()


    insert_files = ["insert_animaux_types.sql", "insert_animaux_velages.sql", "insert_animaux.sql", "insert_complications.sql", "insert_familles.sql", "insert_types.sql", "insert_velages_complications.sql", "insert_velages.sql"]

    # Run the insertions files to insert data in the database
    for insert_file in insert_files:
        with open(os.path.join(pathlib.Path(__file__).parent.absolute(), f"./1002-sql-data/{insert_file}")) as f:
            insert_content = f.read()
        
        cursor.executescript(insert_content)
        db.commit()

    # Start the scripts that generate race for each animal according to their ancestor
    generate_race(db)

    db.close()


if __name__ == '__main__':
    main()
