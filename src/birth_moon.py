import datetime
from moon_phase import position, phase_index


def birth_moon(data):
    """
    @pre data
    @post 2 dict of occurences, one for all the years and one for each year

    """
    birth_moon_cycle = list(map(lambda x: phase_index(position(datetime.datetime.strptime(x[0], "%d/%m/%Y"))), data))
    occurrences = {}
    total_occurences = {}
    for i, date in enumerate(data):
        date = date[0]
        moon_phase = birth_moon_cycle[i]
        year = int(date.split("/")[-1])

        total_occurences[moon_phase] = total_occurences.get(moon_phase, 0) + 1

        if year not in occurrences:
            occurrences[year] = {moon_phase: 1} 
        else:
            occurrences[year][moon_phase] = occurrences[year].get(moon_phase, 0) + 1

    total_occurences = {key: total_occurences.get(key, 0) for key in range(8)}
    occurrences = {key: occurrences.get(key, 0) for key in sorted(occurrences.keys())}
    
    return total_occurences, occurrences
