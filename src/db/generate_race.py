import sqlite3
import os
import pathlib
from typing import List, Tuple, Dict


def get_races(db: sqlite3.Connection, id_: int) -> List[Tuple[int, float]]:
    """
    Args:
        db (sqlite3.Connection): a databse connection
        id_ (int): an id representing the animal
    Returns:
        List[Tuple[int, float]]: The list of races id and percentage in a tuple of the animal if it exists in the database 
    """
    with db as cursor:
        return cursor.execute("SELECT type_id, pourcentage FROM animaux_types WHERE animal_id = ?", (id_,)).fetchall()


def get_parents(db: sqlite3.Connection, id_: int) -> Tuple[int, int]:
    """
    Args:
        db (sqlite3.Connection): a database connection
        id_ (int): an id representing the animal
    Returns:
        Tuple[int, int]: The parents id of id passed in parameter in a tuple
    """
    with db as cursor:
        return cursor.execute("SELECT pere_id, mere_id FROM animaux, animaux_velages, velages WHERE animaux.id = ? AND animaux.id = animaux_velages.animal_id AND animaux_velages.velage_id = velages.id", (id_,)).fetchone()


def get_animals(db: sqlite3.Connection) -> List[int]:
    """
    Args:
        db (sqlite3.Connection): a database connection
    Returns:
        List[int] A list of all animals ids in the db
    """
    with db as cursor:
        return [el[0] for el in cursor.execute("SELECT id FROM animaux").fetchall()]


def calculate_races(parents_races: List[Tuple[int, float]]) -> List[Tuple[int, float]]:
    """
    Calculate races with percentage for an animals with its parents races
    Args:
        parents_races (list): list of parents races
    Returns:
        List[tuple]: A list of races and percentage of this race in tuple
    """
    races_dict: Dict[int, float] = {}
    for race in parents_races:
        races_dict[race[0]] = races_dict.get(race[0], 0) + race[1]
    
    # Convert dict to a list of tuple and divide by 2 the percentage
    return [(race[0], race[1] / 2) for race in races_dict.items()]


def insert_races(db: sqlite3.Connection, animal_id, races: List[Tuple[int, float]]) -> None:
    """
    Insert races for an animal in the database

    Args:
        db (sqlite3.Connection): database connection
        animal_id (int): the animal id
        races: list of its races and percentage of the races in a tuple
    """
    for race in races:
        with db as cursor:
            cursor.execute("INSERT INTO animaux_types VALUES (?, ?, ?)", (animal_id, race[0], race[1]))


def set_races(db: sqlite3.Connection, animal_id: int) -> List[Tuple[int, float]]:
    """
    Calculate races recursively of the animal_id and of its ancestors if it doesn't already exists in the database

    Args:
        db (sqlite3.Connection): a database connection
        animal_id (int): the animal id to set origin
    
    Returns:
        List[tuple]: The types of the animal in a list of tuple
    """
    father, mother = get_parents(db, animal_id)
    races_mom: List[Tuple[int, float]] = get_races(db, mother)
    races_father: List[Tuple[int, float]] = get_races(db, father)

    # When the parents doesn't have races set, calculte their first
    if not len(races_mom):
        races_mom: List[Tuple[int, float]] = set_races(db, mother)
    
    if not len(races_father):
        races_father: List[Tuple[int, float]] = set_races(db, father)

    races: List[Tuple[int, float]] = calculate_races(races_mom + races_father)

    insert_races(db, animal_id, races)

    return races


def generate_race(db: sqlite3.Connection):
    """
    Generate race for every animals in the db according its ancestors
    Args:
        db (sqlite3.Connection): a database connection
    """

    #Fetch all animals
    animals: List[int] = get_animals(db)

    for animal_id in animals:
        if len(get_races(db, animal_id)) == 0:
            set_races(db, animal_id)
