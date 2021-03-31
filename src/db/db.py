import sqlite3


class DB:
    def __init__(self, database_name):
        print(database_name)
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

    #def get_all_premature_death_birth(self):
    #     """

    #     """
    #     req = "SELECT date FROM velages, animaux WHERE animaux.mort_ne == 1 AND animaux.id == velages.id"
    #     with self.db as cursor:
    #         return cursor.execute(req).fetchall()


    def get_all_animals_familly_name(self):
        req = "SELECT * FROM animaux, familles WHERE familles.id == animaux.famille_id"
        with self.db as cursor:
            return cursor.execute(req).fetchall()
    
    # def get_all_animals_with_father_id(self):
    #     req = "SELECT id, mort_ne, pere_id FROM animaux, velages WHERE animaux.id == velages.id"
    #     with self.db as cursor:
    #         return cursor.execute(req).fetchall()

