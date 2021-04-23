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
        req = "SELECT date FROM animaux, animaux_velages, velages WHERE animaux.id = animaux_velages.animal_id AND velages.id = animaux_velages.velage_id"
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
    
    
    def List_Familles(self):
        '''
        Retourner tous les noms des familles existent dans
        les bases de données dans une liste
        '''
        cursor = self.db.cursor()
        pst = cursor.execute('SELECT nom FROM familles')
        list_familles = [row[0] for row in pst]
        return list_familles


    def nmb_vivants(self):
        '''
        Retourner un dictionnaire qui contient le nombre vivant
        des animaux famille par famille
        '''
        cursor = self.db.cursor()
        req = cursor.execute(
            'SELECT * FROM familles, animaux WHERE familles.id = animaux.famille_id AND animaux.mort_ne = 0 AND animaux.decede=0')

        dic = {}
        try:
            for row in req:
                dic[row[1]] = dic.get(row[1], 0) + 1
            return dic
        except Exception as e:
            return f":(  ==> {e}"


    def nmb_morts(self):
        '''
        Return un dictionnaire qui contient le nombre
        des animaux qui sont morts famille par famille
        '''
        cursor = self.db.cursor()
        req = cursor.execute(
            'SELECT * FROM animaux, animaux_velages, velages_complications, velages, familles WHERE animaux.mort_ne == 1 AND animaux.id == animaux_velages.animal_id AND animaux_velages.velage_id == velages_complications.velage_id AND velages_complications.complication_id != 6 AND velages.id == animaux_velages.velage_id AND animaux.famille_id = familles.id')

        dic = {}
        try:
            for row in req:
                dic[row[1]] = dic.get(row[1], 0) + 1
            return dic
        except Exception as e:
            return f":(  ==> {e}"


    def nmb_deces_prematures(self):
        '''
        Return un dictionnaire qui contient le nombre
        des animaux qui sont morts famille par famille
        '''
        cursor = self.db.cursor()
        req = cursor.execute(
            "SELECT * FROM animaux, animaux_velages, velages_complications, velages, familles WHERE animaux.mort_ne == 1 AND animaux.id == animaux_velages.animal_id AND animaux_velages.velage_id == velages_complications.velage_id AND velages_complications.complication_id == 6 AND velages.id == animaux_velages.velage_id AND animaux.famille_id = familles.id")

        dic = {}
        try:
            for row in req:
                #print(row)
                dic[row[-1]] = dic.get(row[-1], 0) + 1
            return dic
        except Exception as e:
            return f":(  ==> {e}"


    def types(self, type):
        try:
            labels = self.List_Familles()
            les_animaux_vivants = []
            les_animaux_qui_sont_morts = []
            les_animaux_qui_sont_deces_prematures = []
            if type == 'les_animaux_vivants':
                for famille in labels:
                    les_animaux_vivants += [self.nmb_vivants().get(famille, 0)]
                return les_animaux_vivants
            elif type == 'les_animaux_qui_sont_morts':
                for famille in labels:
                    les_animaux_qui_sont_morts += [self.nmb_morts().get(famille, 0)]
                return les_animaux_qui_sont_morts
            elif type == 'les_animaux_qui_sont_deces_prematures':
                for famille in labels:
                    les_animaux_qui_sont_deces_prematures += [self.nmb_deces_prematures().get(famille, 0)]
                return les_animaux_qui_sont_deces_prematures
            #print(les_animaux_vivants)
            #print(les_animaux_qui_sont_morts)
            #print(les_animaux_qui_sont_deces_prematures)
        except Exception as e:
            return f":(  ==> {e}"



