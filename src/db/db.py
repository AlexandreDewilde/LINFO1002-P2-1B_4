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

    
    def get_all_velages(self):
        """
        Get all rows from velages tables
        """
        req = "SELECT * FROM velages"
        with self.db as cursor:
            return cursor.execute(req).fetchall()

    def get_all_births(self):
        """
        Get all rows from velages tables
        """
        req = "SELECT date FROM velages"
        with self.db as cursor:
            return cursor.execute(req).fetchall()

    def get_all_premature_death_birth(self):
        """

        """
        req = "SELECT * FROM animaux, animaux_velages, velages_complications, velages WHERE animaux.mort_ne == 1 AND animaux.id == animaux_velages.animal_id AND animaux_velages.velage_id == velages_complications.velage_id AND velages_complications.complication_id == 6 AND velages.id == animaux_velages.animal_id"
        with self.db as cursor:
            return cursor.execute(req).fetchall()


    def get_all_animals_premature_w_familly_name(self):
        req = "SELECT * FROM animaux, animaux_velages, velages_complications, velages, familles WHERE animaux.mort_ne == 1 AND animaux.id == animaux_velages.animal_id AND animaux_velages.velage_id == velages_complications.velage_id AND velages.id == animaux_velages.animal_id AND animaux.famille_id == familles.id"
        with self.db as cursor:
            return cursor.execute(req).fetchall()

    def get_all_animals_w_family_name(self):
        req = "SELECT * FROM animaux, familles WHERE animaux.id == animaux_velages.animal_id AND animaux.famille_id == familles.id"
        with self.db as cursor:
            return cursor.execute(req).fetchall()
    

