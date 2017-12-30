#!/usr/bin/python

# Doha, Qatar - 25.3, 51.5, 3
from datetime import date
from core.praytimes import PrayTimes
from core.settings import SettingsManager

import configparser

prayTimes = PrayTimes()
settings = SettingsManager()
cfg = configparser.ConfigParser()

def setup_wizard():
    cfg['Location'] = {}

    text = ''
    while text == '':
        text = input("Insert latitude:  > ")
    cfg['Location']['latitude'] = text

    text = ''
    while text == '':
        text = input("Insert longitude: > ")
    cfg['Location']['longitude'] = text

    text = ''
    while text == '':
        text = input("Insert timezone:  > ")
    cfg['Location']['timezone'] = text

    print("Choose a method")
    for method in PrayTimes.methods:
        print(method)
    cfg['Location']['calcCode'] = input("> ")

    with open('athanpy.cfg', 'w') as cfgfile:
        cfg.write(cfgfile)

settings.refreshVariables(setup_wizard)
settings.calcTimes()

# Does not work
#print("from athanterm.py: ", str(calcCode))
#prayTimes = PrayTimes(str(calcCode))
#cfg.read('athanpy.cfg')

#print("Settings chosen: ", lat, lon, tz)
# getTimes(self, date, coords, timezone)
times = settings.times
for i in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha', 'Midnight']:
    print(i + ': ' + times[i.lower()])
