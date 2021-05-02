from typing import List


def list_family(families_ids, list_fams) -> List[int]:
    """crée une liste des morts prématurés ou des vivants pour chaque famille
    Args:
        list_fams (List[tuple]): Une liste de tuple contenant l'id de chaque famille d'animaux mort prématurément ou des vivants
    Returns:
        Une liste contenant le nombre de morts prématurés par famille ou une liste contenant le nombre de vivants par famille
    """
    deaths_by_family = {family_id: 0 for family_id in families_ids}
    for animal_family in list_fams:
        deaths_by_family[animal_family[0]] += 1

    return list(deaths_by_family.values())
