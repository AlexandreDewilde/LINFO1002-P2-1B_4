def list_deces_prematures_family(famillies_ids, list_birth):
    """crée une liste des morts prématurés pour chaque famille
    Args:
        list_birth (List[tuple]): Une liste de tuple contenant l'id de chaque famille d'animaux mort prématurément
    Returns:
        Une liste contenant le nombre de morts prématurés par famille 
    """
    #print(list_birth)
    dic = {}
    for i in range(len(list_birth)):
        dic[list_birth[i][0]] = dic.get(list_birth[i][0], 0) +1


    l = famillies_ids
    for i in range(len(l)):
        l[i] = dic.get(l[i], 0)
    return l
#print(list_deces_prematures_family())
