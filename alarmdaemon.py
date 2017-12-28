#!/usr/bin/python
from settings import SettingsManager

import os
import threading
import sched, time
import datetime

import simpleaudio as sa

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import signal

APPINDICATOR_ID = 'ATHANPY_INDICATOR'

class AlarmDaemon():
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.settingsmgr = SettingsManager()

    def main(self):
        indicator = appindicator.Indicator.new(APPINDICATOR_ID, gtk.STOCK_INFO, appindicator.IndicatorCategory.SYSTEM_SERVICES)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        indicator.set_menu(self.build_menu())
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        gtk.main()

    def build_menu(self):
        menu = gtk.Menu()
        item_start = gtk.MenuItem('Start')
        item_start.connect('activate', self.start_alarm)
        item_stop = gtk.MenuItem('Stop')
        item_stop.connect('activate', self.stop_alarm)
        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', quit)
        menu.append(item_start)
        menu.append(item_stop)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def alarm_action(self, athan_name):
        athan_sound = sa.WaveObject.from_wave_file('audio/athan_makkah.wav')
        self.play_athan = athan_sound.play()
        print('Time for ', athan_name, '!')
        input('Press enter to stop')
        self.play_athan.stop()
        if athan_name == 'Isha':
            self.settingsmgr.calcTimes()
            self.schedule_alarm(self.settingsmgr.times)

    # TODO use PrayTims class to get Athan names
    def schedule_alarm(self, times):
#        now = time.strftime("%H:%M")
        now = datetime.datetime.now()
        for p in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha', 'Midnight']:
            athan_time = datetime.datetime.today()
            athan_time = athan_time.replace(
                hour=int(times[p.lower()][0:2]),
                minute=int(times[p.lower()][3:]),
                second=0,
                microsecond=0
            )
            if now < athan_time:
                self.next_alarm = self.scheduler.enterabs(
                        athan_time.timestamp(), 1, self.alarm_action, argument={p})
                print('Athan for ', p, ' set at:', athan_time)
                self.start_alarm('activate')
                break

    def start_alarm(self, action):
        daemon = threading.Thread(target=self.scheduler.run)
        daemon.start()

    def stop_alarm(self, action):
        self.play_athan.stop()
        self.scheduler.cancel(self.next_alarm)
        print('alarm stopped')

    def quit(source):
        gtk.main_quit()

#print('making daemon')
#alarm = AlarmDaemon()
#alarm.main()
#print('end')
