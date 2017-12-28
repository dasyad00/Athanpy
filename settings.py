import datetime
import configparser

from praytimes import PrayTimes

class SettingsManager():
    def __init__(self):
        self.prayTimes = PrayTimes()

    def refreshVariables(self, setupfunction):
        cfg = configparser.ConfigParser()
        if ( cfg.read('athanpy.cfg') != [] ):
            pass
        else:
            self.lat = 0
            self.lon = 0
            self.tz  = 0
            self.calcCode  = ''
            setupfunction()
            cfg.read('athanpy.cfg')
        
        self.lat = float(cfg['Location'].get('latitude'))
        self.lon = float(cfg['Location'].get('longitude'))
        self.tz  = float(cfg['Location'].get('timezone'))
        self.calcCode  = cfg['Location'].get('calcCode')

    def calcTimes(self):
        self.prayTimes.setMethod(self.calcCode)
        # getTimes(self, date, coords, timezone)
        self.times = self.prayTimes.getTimes(datetime.date.today(),
                (self.lat, self.lon), self.tz)

