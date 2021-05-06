from typing import List, Dict

def occurences_months_by_year(lst_date : List[str]) -> Dict[int, List[int]]:
    """
    Args:
        lst_date (List[str]): a list of date in format: "dd/mm/yyyy"
    Returns:
        A dict with key as year and a list of occurences of every months in the lst_date for key year
    """
    occurences = {}
    for date in lst_date:
        _, months, year = map(int, date.split("/"))

        if year not in occurences:
            occurences[year] = [0] * 12
        
        occurences[year][months-1] += 1
    
    return occurences
