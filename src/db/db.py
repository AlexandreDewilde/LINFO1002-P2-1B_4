import sqlite3


class DB:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connect()


    def connect(self):
        """
        Create the connexion to the database
        """
        self.db = sqlite3.connect(self.database_name, check_same_thread=False)


    def get_all_births(self):
        """
        Get all birthdates from velages tables
        """
        req = "SELECT date FROM animaux, animaux_velages, velages WHERE animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id ORDER BY date"
        with self.db as cursor:
            return cursor.execute(req).fetchall()

    
    def get_all_animals_with_complications(self):
        req = "SELECT * FROM animaux LEFT OUTER JOIN animaux_velages ON animaux_velages.animal_id = animaux.id LEFT OUTER JOIN velages_complications ON velages_complications.velage_id = animaux_velages.velage_id"
        with self.db as cursor:
            return cursor.execute(req).fetchall()

    
    def get_all_premature_deaths(self):
        req = "SELECT date FROM animaux, animaux_velages, velages_complications, velages WHERE animaux.mort_ne = 1 AND animaux.id = animaux_velages.animal_id AND animaux_velages.velage_id = velages_complications.velage_id AND velages_complications.complication_id = 6 AND velages.id = animaux_velages.velage_id"
        with self.db as cursor:
            return cursor.execute(req).fetchall()
    




