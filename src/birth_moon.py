import datetime



moon_day = lambda date_d: int((datetime.datetime(2021,2,27) - date_d).days % 29.530588853)

def birth_moon(data):
    birth_moon_cycle = map(lambda x: moon_day(datetime.datetime.strptime(x[0], "%d/%m/%Y")), data)
    occurrences = {}
    for date in birth_moon_cycle:
        occurrences[date] = occurrences.get(date,0) + 1
    return list(occurrences.values())


