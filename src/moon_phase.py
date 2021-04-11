#Found on gist https://gist.github.com/miklb/ed145757971096565723

"""
moonphase.py - Calculate Lunar Phase
Author: Sean B. Palmer, inamidst.com -- With some editions from Alexandre Dewilde to Translate moon phase<
Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation
"""

import math, decimal, datetime


moon_phase_dict = {
    0: "Nouvelle lune", 
    1: "Premier croissant", 
    2: "Premier Quartier", 
    3: "Lune Gibbeuse croissante", 
    4: "Pleine Lune", 
    5: "Lune Gibbeuse décroissante", 
    6: "Dernier quartier", 
    7: "Dernier croissant"
}

dec = decimal.Decimal

def position(now=None): 
    if now is None: 
        now = datetime.datetime.now()

    diff = now - datetime.datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))

    return lunations % dec(1)

def phase(pos): 
    index = (pos * dec(8)) + dec("0.5")
    index = math.floor(index)
    return moon_phase_dict[int(index) & 7]
