#!/usr/bin/python
from praytimes import PrayTimes
from datetime import date
from settings import SettingsManager

import configparser
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

prayTimes = PrayTimes()
settingsmgr = SettingsManager()
cfg = configparser.ConfigParser()

# TODO make setup simpler than Settings Dialog
#class SetupDialog(Gtk.Dialog):
#    def __init__(self, parent):
#        Gtk.Dialog.__init__(self, "Setup", parent, 0,
#                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
#                 Gtk.STOCK_OK, Gtk.ResponseType.OK))
#        self.set_default_size(300,100)
#
#        self.grid = Gtk.Grid()
#        self.grid.set_hexpand(True)
#        self.grid.set_vexpand(True)
#        self.get_content_area().add(self.grid)

class SettingsDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Settings", parent, 0,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                 Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.set_default_size(300,100)

        self.grid = Gtk.Grid()
        self.grid.set_hexpand(True)
        self.grid.set_vexpand(True)
        self.get_content_area().add(self.grid)

        self.title = Gtk.Label("TODO Settings")
        self.title.set_hexpand(True)

        self.lblLat = Gtk.Label("Latitude: ")
        self.entLat = Gtk.Entry()
        self.entLat.set_text(str(settingsmgr.lat))

        self.lblLong = Gtk.Label("Longitude:")
        self.entLong = Gtk.Entry()
        self.entLong.set_text(str(settingsmgr.lon))

        self.lblTz = Gtk.Label("TimeZone: ")
        self.entTz = Gtk.Entry()
        self.entTz.set_text(str(settingsmgr.tz))

        self.lblCalc = Gtk.Label("Calculation Method:")
        calcCodes = prayTimes.methods
        self.boxCalcCode = Gtk.ComboBoxText()
        self.boxCalcCode.set_entry_text_column(0)
#       TODO apply changes when field is changed
#        self.boxCalcCode.connect("changed", self.applySettings)
        for code in calcCodes:
            self.boxCalcCode.append_text(code)
        if (settingsmgr.calcCode != ''):
            self.boxCalcCode.set_active(
                    list(calcCodes.keys()).index(settingsmgr.calcCode))

        self.btnApply = Gtk.Button(label="Apply")
        self.btnApply.connect("clicked", self.applySettings)

        self.grid.add(self.title)
        self.grid.attach(self.lblLat, 0, 1, 1, 1)
        self.grid.attach(self.entLat, 1, 1, 1, 1)
        self.grid.attach(self.lblLong, 0, 2, 1, 1)
        self.grid.attach(self.entLong, 1, 2, 1, 1)
        self.grid.attach(self.lblTz, 0, 3, 1, 1)
        self.grid.attach(self.entTz, 1, 3, 1, 1)
        self.grid.attach(self.lblCalc, 0, 4, 2, 1)
        self.grid.attach(self.boxCalcCode, 0, 5, 2, 1)
        self.grid.attach(self.btnApply, 0, 6, 2, 1)
        
        self.show_all()

    def applySettings(self, widget):
        if (cfg.sections() == []):
            cfg['Location'] = {}
        cfg['Location']['latitude'] = self.entLat.get_text()
        cfg['Location']['longitude'] = self.entLong.get_text()
        cfg['Location']['timezone'] = self.entTz.get_text()
        cfg['Location']['calcCode'] = self.boxCalcCode.get_active_text()
        with open('athanpy.cfg', 'w') as cfgfile:
            cfg.write(cfgfile)

class AthanWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Athanpy")

        grid = Gtk.Grid()
        grid.set_hexpand(True)
        grid.set_vexpand(True)
        self.add(grid)

        textTitle = Gtk.Label("Title")
        textTitle.set_hexpand(True)
        textPrayerTimes = Gtk.Label(self.get_prayertime_text())
        textPrayerTimes.set_vexpand(True)

        grid.add(textTitle)
        grid.attach_next_to(textPrayerTimes, textTitle, Gtk.PositionType.BOTTOM, 1, 1)
        
        btn_showSettings = Gtk.Button(label="Settings")
        btn_showSettings.connect("clicked", self.showSettings)
        grid.attach_next_to(btn_showSettings, textPrayerTimes, Gtk.PositionType.BOTTOM, 1, 2)

    def get_prayertime_text(self):
        settingsmgr.refreshVariables(self.showSettings)
        self.lat = settingsmgr.lat
        self.lon = settingsmgr.lon
        self.tz  = settingsmgr.tz
        self.calcCode  = settingsmgr.calcCode
        prayTimes.setMethod(str(settingsmgr.calcCode))

        print("Settings chosen: ", self.lat, self.lon, self.tz)
        # getTimes(self, date, coords, timezone)
        times = prayTimes.getTimes(date.today(), (self.lat, self.lon), self.tz);
        output = ''
        for i in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha', 'Midnight']:
            output += (i + ': ' + times[i.lower()] + "\n")
        return output

    def showSettings(self, widget='clicked'):
        dialog = SettingsDialog(self)
        response = dialog.run()

        if (response == Gtk.ResponseType.OK):
            print("The OK button was clicked")
        elif (response == Gtk.ResponseType.CANCEL):
            print("The Cancel button was clicked")

        dialog.destroy()

win = AthanWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
