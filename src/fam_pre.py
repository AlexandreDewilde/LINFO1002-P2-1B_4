from typing import List


def list_deces_prematures_family(families_ids, list_birth) -> List[int]:
    """crée une liste des morts prématurés pour chaque famille
    Args:
        list_birth (List[tuple]): Une liste de tuple contenant l'id de chaque famille d'animaux mort prématurément
    Returns:
        Une liste contenant le nombre de morts prématurés par famille 
    """
    deaths_by_family = {family_id: 0 for family_id in families_ids}
    for animal_family in list_birth:
        deaths_by_family[animal_family[0]] += 1

    return list(deaths_by_family.values())
