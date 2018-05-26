from datetime import datetime, timedelta
import configparser

from core.praytimes import PrayTimes

prayTimes = PrayTimes()
cfg = configparser.ConfigParser()

class SettingsManager():
    lat = 0
    lon = 0
    tz = 0
    calcCode = ''
    times = {}
    reminder_athan = {}

    def refreshVariables(setupfunction=None):
        if ( cfg.read('athanpy.cfg') != [] ):
            pass
        else:
            setupfunction()
            cfg.read('athanpy.cfg')
        
        SettingsManager.location = {
                'country'  : cfg['Location'].get('country'),
                'province' : cfg['Location'].get('province'),
                'city'     : cfg['Location'].get('city'),
                'lat'      : float(cfg['Location'].get('latitude')),
                'lon'      : float(cfg['Location'].get('longitude')),
                'tz'       : float(cfg['Location'].get('timezone')),
                'calcCode' : cfg['Location'].get('calcCode')}
        #SettingsManager.lat = float(cfg['Location'].get('latitude'))
        #SettingsManager.lon = float(cfg['Location'].get('longitude'))
        #SettingsManager.tz  = float(cfg['Location'].get('timezone'))
        #SettingsManager.calcCode  = cfg['Location'].get('calcCode')

        SettingsManager.reminder_athan  = {}
        SettingsManager.reminder_iqomah = {}
        for name in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
            SettingsManager.reminder_athan[name.lower() + '_enabled']  = cfg['Reminder: Athan'].get(name + '_enabled')
            SettingsManager.reminder_iqomah[name.lower() + '_enabled'] = cfg['Reminder: Iqomah'].get(name + '_enabled')
            SettingsManager.reminder_iqomah[name.lower() + '_time']    = cfg['Reminder: Iqomah'].get(name + '_time')

        SettingsManager.reminder_athan['dialog_enabled']        = cfg['Reminder: Athan'].get('dialog_enabled')
        SettingsManager.reminder_athan['notification_enabled']  = cfg['Reminder: Athan'].get('notification_enabled')
        SettingsManager.reminder_iqomah['dialog_enabled']       = cfg['Reminder: Iqomah'].get('dialog_enabled')
        SettingsManager.reminder_iqomah['notification_enabled'] = cfg['Reminder: Iqomah'].get('notification_enabled')

    def apply_settings(sections):
        for section in sections:
            secTitle = section.get('title')
            if secTitle not in cfg.sections():
                cfg[secTitle] = {}
            for text in section.keys():
                if text != 'title':
                    cfg[secTitle][text] = section.get(text)

        with open('athanpy.cfg', 'w') as cfgfile:
            cfg.write(cfgfile)
            SettingsManager.refreshVariables()

    def calcTimes(nextDay=False):
        prayTimes.setMethod(SettingsManager.location['calcCode'])
        # getTimes(self, date, coords, timezone)
        time = datetime.today()
        if nextDay:
            time += timedelta(days=1)
            time = time.replace(
                hour = 0,
                minute = 0,
                second = 0,
                microsecond=0
            )
        SettingsManager.times = prayTimes.getTimes(time.date(),
                (SettingsManager.location['lat'], SettingsManager.location['lon']), SettingsManager.location['tz'])

    def load_coordinates():
        f = open("core/coordinates.csv", 'r')
        results = { '' : '' }
        for line in f:
            field = list(map(lambda x: x.strip(), line.split(',')))
            # If city recorded still in the same country, fill in city
            # If new country detected, make new dictionary
            if field[0] not in results and field[0] != '':
                results[field[0]] = { '' : ''}
                results[field[0]]['province'] = bool(field[1] != "")
            if results[field[0]]['province']:
                results[field[0]][field[1]] = { '' : '' }
                results[field[0]][field[1]][field[2]] = [ field[3], field[4] ]
            else:
                results[field[0]][field[2]] = [ field[3], field[4] ]
        return results
