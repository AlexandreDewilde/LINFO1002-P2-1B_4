from db.db import DB

d = DB("db/database.db")

def list_deces_prematures():
    """
    Returns:
        Une liste contenant le nombre de morts prématurés
    """
    list_birth = d.get_all_premature_deaths()
    #print(list_birth)
    dic = {}
    for i in range(len(list_birth)):
        dic[list_birth[i][0][3:5]] = dic.get(list_birth[i][0][3:5], 0) + 1
    #print(dic)
    l = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for i in range(len(l)):
        if l[i] in dic:
            l[i] = dic[l[i]]
        else:
            l[i] = 0
    return l
#print(list_deces_prematures())
