import sqlite3
from typing import List, Tuple


class DB:
    """
    Class acting as an interface to the database
    """

    def __init__(self, database_name: str) -> None:
        self.database_name: str = database_name
        self.connect()


    def connect(self) -> None:
        """
        Create a connection to the database
        """
        self.db: sqlite3.Connection = sqlite3.connect(self.database_name, check_same_thread=False)

    
    def close(self) -> None:
        """
        Close the database connection
        """
        self.db.close()
        

    def get_families(self) -> List[Tuple[int, str]]:
        """
        Get all families in the db
        Returns:
            List[Tuple[int, str]] : List of families with their ids and names
        """
        with self.db as cursor:
            req: str = "SELECT id, nom FROM familles"
            return cursor.execute(req).fetchall()


    def get_births(self) -> List[str]:
        """
        For each animals in the database get its birthdate if its born in the farm
        Returns:
            List[str]: list of all animals birthdates as string in "dd:mm:yyyy" format
        """
        with self.db as cursor:
            # This requests fetch all birth dates for each animal
            req: str = "SELECT date FROM animaux, animaux_velages, velages WHERE animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id ORDER BY date"
            return [row[0] for row in cursor.execute(req).fetchall()]


    def get_all_premature_deaths(self) -> List[Tuple[str]]:
        """
        Get all animals death prematurely
        Returns:
            List[Tuple[str]]: list of tuple with date of births as unique element in string format "dd:mm:yyyy" of all animals death prematurely
        """
        with self.db as cursor:
            req: str = "SELECT date FROM animaux, animaux_velages, velages_complications, velages WHERE animaux.mort_ne = 1 AND animaux.id = animaux_velages.animal_id AND animaux_velages.velage_id = velages_complications.velage_id AND velages_complications.complication_id = 6 AND velages.id = animaux_velages.velage_id"
            return cursor.execute(req).fetchall()
    

    def get_all_premature_deaths_family(self) -> List[Tuple[int]]:
        """
        Get all animals death prematurely
        Returns:
            List[Tuple[int]]: list of tuple with family id as unique element in string format "" of all animals death prematurely
        """
        with self.db as cursor:
            req: str = "SELECT famille_id FROM animaux, animaux_velages, velages_complications, velages WHERE animaux.mort_ne = 1 AND animaux.id = animaux_velages.animal_id AND animaux_velages.velage_id = velages_complications.velage_id AND velages_complications.complication_id = 6 AND velages.id = animaux_velages.velage_id"
            return cursor.execute(req).fetchall()

    def get_all_living_family(self) -> List[Tuple[int]]:
        """
        Get all animals living
        Returns:
            List[Tuple[int]]: list of tuple with family id as unique element in string format "" of all animals living
        """
        with self.db as cursor:
            req: str = "SELECT famille_id FROM animaux, animaux_velages, velages WHERE animaux.presence = 1 AND animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id"
            return cursor.execute(req).fetchall()