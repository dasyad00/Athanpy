import configparser

class SettingsManager():
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

