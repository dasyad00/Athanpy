#!/usr/bin/python
from core.settings import SettingsManager as settings

import os
import threading
import sched, time
from datetime import datetime, timedelta

import simpleaudio as sa

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox

class AlarmDaemon(QThread):
    def __init__(self, mainReference):
        QThread.__init__(self)
        self.scheduler = sched.scheduler(time.time, time.sleep)
#        self.settingsmgr = SettingsManager()
        self.play_sound = None
        self.mainW = mainReference

    def __del__(self):
        self.wait()

    def run(self):
        self.scheduler.run()

    def alarm_action(self, alarm_text, alarm_sound):
        self.play_sound = alarm_sound.play()
        print(alarm_text)
        self.schedule_alarm(settings.times)
        # TODO show pop up message/notification
        popUp = QMessageBox.information(self.mainW,
                "AthanPy", alarm_text, QMessageBox.Ok)
        if popUp == QMessageBox.Ok:
            self.stop_sound()
        #popUp = QMessageBox()
        #popUp.setIcon(QMessageBox.Information)
        #popUp.setText(str(message))
        #popUp.setWindowTitle("AthanPy")
        #popUp.setStandardButtons(QMessageBox.Close)
        #popUp.buttonClicked.connect(self.stop_sound)
        #popUp.exec_()
        #input('Press enter to stop')
        #self.stop_sound()

    # TODO use PrayTims class to get Athan names
    def schedule_alarm(self, times, nextDay=False):
#        now = time.strftime("%H:%M")
        now = datetime.now()
        athan_settings = settings.reminder_athan
        iqomah_settings = settings.reminder_iqomah
        for p in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
            athan_time = datetime.today()
            athan_time = athan_time.replace(
                hour=int(times[p.lower()][0:2]),
                minute=int(times[p.lower()][3:]),
                second=0,
                microsecond=0
            )
            if nextDay:
                athan_time += timedelta(days=1)

            if now < athan_time:
                # TODO let user choose between dialog and notification 
                athan_sound = None 
                if p == 'Fajr':
                    athan_sound = sa.WaveObject.from_wave_file('audio/athan_makkah_fajr.wav')
                else:
                    athan_sound = sa.WaveObject.from_wave_file('audio/athan_makkah.wav')
                self.next_alarm = self.scheduler.enterabs(
                    athan_time.timestamp(), 1, self.alarm_action, argument={
                        p, athan_sound, 'Athan: Time for ' + p + '!'})
                print('Athan for ', p, ' set at:', athan_time)
                break
            elif iqomah_settings[p.lower() + '_enabled'] == '1':
                iqomah_time = athan_time + timedelta(
                    minutes=int(iqomah_settings[p.lower() + '_time']))
                if now < iqomah_time:
                    iqomah_sound = sa.WaveObject.from_wave_file('audio/iqomah_misharyrashid.wav')
                    self.next_alarm = self.scheduler.enterabs(
                        iqomah_time.timestamp(), 1, self.alarm_action, argument={
                            p, iqomah_sound, 'Iqomah: ' + p + ' prayer has started!'})
                    print('Iqomah for ', p, ' set at:', athan_time)
                    break
        else:
            # Only runs when program is run after Isha
            settings.calcTimes(True)
            self.schedule_alarm(settings.times, nextDay=True)

    def stop_sound(self):
        if self.play_sound is not None:
            if self.play_sound.is_playing:
                self.play_sound.stop()
                return True
        print("It's not playing")
        return False

    def stop_alarm(self, action):
        self.scheduler.cancel(self.next_alarm)
        print(self.scheduler.empty)
        print('alarm stopped')

#    def quit(source):
#        gtk.main_quit()

#print('making daemon')
#alarm = AlarmDaemon()
#alarm.main()
#print('end')
