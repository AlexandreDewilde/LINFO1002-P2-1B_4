import sqlite3
import os
import pathlib


def generate_race():
    """Generate race for every animals in the db according its ancestors"""

    #Connect to the database
    db = sqlite3.connect(os.path.join(pathlib.Path(__file__).parent.absolute(), "database.db"))

    #Fetch all animals
    with db as cursor:
        animals = cursor.execute("SELECT id FROM animaux")

    def get_types(id_):
        with db as cursor:
            return cursor.execute("SELECT type_id, pourcentage FROM animaux_types WHERE animal_id = ?", (id_,)).fetchall()


    def get_parents(id_):
        with db as cursor:
            return cursor.execute("SELECT pere_id, mere_id FROM animaux, animaux_velages, velages WHERE animaux.id = ? AND animaux.id = animaux_velages.animal_id AND animaux_velages.velage_id = velages.id", (id_,)).fetchone()


    def set_origin(animal):
        father, mother = get_parents(str(animal))
        types_mom = get_types(mother)
        types_father = get_types(father)

        if not len(types_mom):
            types_mom = set_origin(mother)
        
        if not len(types_father):
            types_father = set_origin(father)
        
        types_dict = {}

        for type_element in types_father + types_mom:
            types_dict[type_element[0]] = types_dict.get(type_element[0], 0) + type_element[1]
        
        types = list(map(lambda x: (x[0], x[1] / 2), types_dict.items()))

        for type_ in types:
            with db as cursor:
                cursor.execute("INSERT INTO animaux_types VALUES (?, ?, ?)", (animal, type_[0], type_[1]))

        return types
        


    for animal in animals:
        if len(get_types(str(animal[0]))) == 0:
            set_origin(animal[0])
    
    db.close()
            
        

