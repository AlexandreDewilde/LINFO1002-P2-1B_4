from typing import List, Dict


def list_occurences_family(families_ids : List[int], list_fams : List[tuple]) -> Dict[int, int]:
    """Create a list of occurences of families in list_fams
    Args:
        families_ids (List[int]): List of all families ids
        list_fams (List[tuple]): List of tuple with ids of families
    Returns:
        A list containing occurences of families in list_fams
    """
    occurences_by_family = {family_id: 0 for family_id in families_ids}
    for animal_family in list_fams:
        occurences_by_family[animal_family[0]] += 1

    return occurences_by_family
