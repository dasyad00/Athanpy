import datetime
import configparser

from core.praytimes import PrayTimes

prayTimes = PrayTimes()

class SettingsManager():
    lat = 0
    lon = 0
    tz = 0
    calcCode = ''
    times = {}

    def refreshVariables(setupfunction):
        cfg = configparser.ConfigParser()
        if ( cfg.read('athanpy.cfg') != [] ):
            pass
        else:
            setupfunction()
            cfg.read('athanpy.cfg')
        
        SettingsManager.lat = float(cfg['Location'].get('latitude'))
        SettingsManager.lon = float(cfg['Location'].get('longitude'))
        SettingsManager.tz  = float(cfg['Location'].get('timezone'))
        SettingsManager.calcCode  = cfg['Location'].get('calcCode')

    def calcTimes():
        prayTimes.setMethod(SettingsManager.calcCode)
        # getTimes(self, date, coords, timezone)
        SettingsManager.times = prayTimes.getTimes(datetime.date.today(),
                (SettingsManager.lat, SettingsManager.lon), SettingsManager.tz)

