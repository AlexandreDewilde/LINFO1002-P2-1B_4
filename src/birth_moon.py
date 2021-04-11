import datetime
from moon_phase import position, phase


def birth_moon(data):
    birth_moon_cycle = map(lambda x: phase(position(datetime.datetime.strptime(x[0], "%d/%m/%Y"))), data)
    occurrences = {}
    for date in birth_moon_cycle:
        occurrences[date] = occurrences.get(date,0) + 1
    return list(occurrences.values())
