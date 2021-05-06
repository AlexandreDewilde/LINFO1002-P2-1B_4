def list_deces_prematures(list_birth):
    """
    Args:
        list_birth (List[tuple]): list of prematures deaths containing date with format: "dd:mm:yyyy"
    Returns:
        A list containing the number of premature deaths by months
    """
    dic = {}
    for i in range(len(list_birth)):
        dic[list_birth[i][0][3:5]] = dic.get(list_birth[i][0][3:5], 0) + 1
    l = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for i in range(len(l)):
        l[i] = dic.get(l[i], 0)
    return l
