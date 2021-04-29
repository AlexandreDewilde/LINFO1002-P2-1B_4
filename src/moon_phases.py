import datetime
from typing import List, Dict

from moon_phase import position, phase_index


def moon_phases_by_years(data: List[str]) -> Dict[int, list]:
    """
    Create list occurences of moon phases for each years with a list of dates sorted represented as string and formates as "dd:mm:yy"  
    Args:
        data: a list of date as string formated as "dd:mm:yy" sorted
    Returns:
        Dict[int, list]: Return a dict with years as key and as value a list with the number of births by moon phases
    """

    occurences: Dict[int, list] = {}

    for i, date_str in enumerate(data):
        # From the date get year and convert to int
        year: int = int(date_str.split("/")[-1])

        # Convert the string date to a datetime object
        date: datetime.datetime = datetime.datetime.strptime(date_str, "%d/%m/%Y")

        # Get the moon phase associated with the date 
        moon_phase: int = phase_index(position(date))

        if year not in occurences:
            # Create a list where the index equals the moon phase,
            # all values are set to 0 except the moon phase of the current date treated
            occurences[year] = [0 if i != moon_phase else 1 for i in range(8)]
        else:
            occurences[year][moon_phase] += 1
    
    return occurences
