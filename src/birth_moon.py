import datetime
from moon_phase import position, phase_index


def birth_moon(data):
    """
    @pre data
    @post 2 dict of occurences, one for all the years and one for each year

    """
    birth_moon_cycle = list(map(lambda x: phase_index(position(datetime.datetime.strptime(x[0], "%d/%m/%Y"))), data))
    occurrences = {}
    for i, date in enumerate(data):
        date = date[0]
        moon_phase = birth_moon_cycle[i]
        year = int(date.split("/")[-1])


        if year not in occurrences:
            occurrences[year] = {k : 0 if k != moon_phase else 1 for k in range(8)} 
        else:
            occurrences[year][moon_phase] = occurrences[year].get(moon_phase, 0) + 1

    occurrences = {key: occurrences.get(key, 0) for key in sorted(occurrences.keys())}
    
    return occurrences
