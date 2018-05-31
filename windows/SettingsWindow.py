#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtCore import QCoreApplication, QSize, QRect, QMetaObject
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QFormLayout, QTabWidget, QLineEdit, QComboBox, QScrollArea, QVBoxLayout, QGroupBox, QCheckBox, QSizePolicy
import configparser

from core.settings import SettingsManager as settings
from core.praytimes import PrayTimes

cfg = configparser.ConfigParser()
prayTimes = PrayTimes()
#settingsmgr = SettingsManager()

class SettingsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        _translate = QCoreApplication.translate
        
        self.setMinimumSize(QSize(360,240))
        self.setObjectName("SettingsWindow")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_apply = QPushButton(self.centralwidget)
        self.btn_apply.setObjectName("btn_apply")
        self.btn_apply.clicked.connect(self.apply_settings)
        self.gridLayout.addWidget(self.btn_apply, 3, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        ###--- Location ---###
        self.tab_location = QWidget()
        self.tab_location.setObjectName("tab_location")
        self.layout_location = QGridLayout(self.tab_location)
        self.layout_location.setObjectName("layout_location")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")

        ## Saved coordinates
        self.coordinates = settings.load_coordinates()
        lbl_country = QLabel(self.tab_location)
        lbl_country.setObjectName("lbl_country")
        self.combo_country = QComboBox(self.tab_location)
        self.combo_country.setObjectName("combo_country")
        self.combo_country.addItems(self.coordinates.keys())

        lbl_prov = QLabel(self.tab_location)
        lbl_prov.setObjectName("lbl_prov")
        self.combo_prov = QComboBox(self.tab_location)
        self.combo_prov.setObjectName("combo_prov")

        lbl_city = QLabel(self.tab_location)
        lbl_city.setObjectName("lbl_city")
        self.combo_city = QComboBox(self.tab_location)
        self.combo_city.setObjectName("combo_city")

        #self.combo_country.setCurrentText('')
            #lambda x: self.combo_prov.addItems(coordinates[x])
            #lambda x: combo_city.addItems(coordinates[x])

        


        self.formLayout.setWidget(1, QFormLayout.LabelRole, lbl_country)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.combo_country)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, lbl_prov)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.combo_prov)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, lbl_city)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.combo_city)
        ## Custom
        # Latitude
        self.lbl_lat = QLabel(self.tab_location)
        self.lbl_lat.setObjectName("lbl_lat")
        self.txt_lat = QLineEdit(self.tab_location)
        self.txt_lat.setObjectName("txt_lat")
        self.txt_lat.setText(str(settings.location['lat']))
        self.txt_lat.setValidator(
                QDoubleValidator(-90.0, 90.0, 5))
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.txt_lat)
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_lat)

        # Longitude
        self.lbl_lon = QLabel(self.tab_location)
        self.lbl_lon.setObjectName("lbl_lon")
        self.txt_lon = QLineEdit(self.tab_location)
        self.txt_lon.setObjectName("txt_lon")
        self.txt_lon.setValidator(
                QDoubleValidator(-180.0, 180.0, 5))
        self.txt_lon.setText(str(settings.location['lon']))
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_lon)
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.txt_lon)

        # Timezone
        self.lbl_tz = QLabel(self.tab_location)
        self.lbl_tz.setObjectName("lbl_tz")
        self.txt_tz = QLineEdit(self.tab_location)
        self.txt_tz.setObjectName("txt_tz")
        self.txt_tz.setValidator(
                QDoubleValidator(-12, 14, 2))
        self.txt_tz.setText(str(settings.location['tz']))
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_tz)
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.txt_tz)

        # Calculation method
        self.lbl_calc = QLabel(self.tab_location)
        self.lbl_calc.setObjectName("lbl_calc")
        self.combo_calc = QComboBox(self.tab_location)
        self.combo_calc.setObjectName("combo_calc")

        calcCodes = prayTimes.methods
        for code in calcCodes:
            self.combo_calc.addItem(code)
        if (settings.location['calcCode'] != ''):
            #self.combo_calc.setCurrentText(settings.calcCode)
            self.combo_calc.setCurrentIndex(
                    self.combo_calc.findText(settings.location['calcCode']))

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_calc)
        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.combo_calc)
        self.layout_location.addLayout(self.formLayout, 0, 0, 1, 1)
        
        self.tabWidget.addTab(self.tab_location, "")

        # Extra functions
        self.combo_country.currentTextChanged.connect(self.setProvText)
        self.combo_prov.currentTextChanged.connect(self.setCityText)
        self.combo_city.currentTextChanged.connect(self.setCoordinates)

        self.combo_country.setCurrentIndex(
                self.combo_country.findText(settings.location['country']))
        self.combo_prov.setCurrentIndex(
                self.combo_prov.findText(settings.location['province']))
        self.combo_city.setCurrentIndex(
                self.combo_city.findText(settings.location['city']))

        self.setWindowTitle(_translate("SettingsWindow", "Settings"))
        lbl_country.setText(_translate("SettingsWindow", "Country"))
        lbl_prov.setText(_translate("SettingsWindow", "Province"))
        lbl_city.setText(_translate("SettingsWindow", "City"))
        self.lbl_lat.setText(_translate("SettingsWindow", "Latitude"))
        self.lbl_lon.setText(_translate("SettingsWindow", "Longitude"))
        self.lbl_tz.setText(_translate("SettingsWindow", "Timezone"))
        self.lbl_calc.setText(_translate("SettingsWindow", "Calculation Method"))
        self.btn_apply.setText(_translate("SettingsWindow", "Apply"))

        ###--- Reminders ---###
        self.tab_reminders = QWidget()
        self.tab_reminders.setObjectName("tab_reminders")
        self.layout_reminders = QGridLayout(self.tab_reminders)
        self.layout_reminders.setObjectName("layout_reminders")
        self.scrollArea = QScrollArea(self.tab_reminders)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 598))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        ##-- Athan group--##
        self.group_athan = QGroupBox(self.scrollAreaWidgetContents)
        self.group_athan.setObjectName("group_athan")
        self.group_athan_layout = QGridLayout(self.group_athan)
        self.group_athan_layout.setObjectName("group_athan_layout")

        self.check_athan = {}
        y = 1
        x = 0
        for name in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
            self.check_athan[name.lower()] = QCheckBox(self.group_athan)
            self.check_athan[name.lower()].setObjectName("check_athan_" + name.lower())
            self.check_athan[name.lower()].setText(_translate("SettingsWindow", name))
            self.check_athan[name.lower()].setChecked(
                    settings.reminder_athan[name.lower() + '_enabled'] == '1')
            self.group_athan_layout.addWidget(self.check_athan[name.lower()], y, x, 1, 1)
            if name == 'Asr':
                y = 1
                x = 1
            else:
                y += 1
#        self.desc_athan_method = QLabel(self.group_athan)
#        self.desc_athan_method.setObjectName("desc_athan_method")
        self.desc_athan = QLabel(self.group_athan)
        self.desc_athan.setObjectName("desc_athan")
#        self.check_athan_dialog = QCheckBox(self.group_athan)
#        self.check_athan_dialog.setObjectName("check_athan_dialog")
#        self.check_athan_dialog.setChecked(
#                settings.reminder_athan['dialog_enabled'] == '1')
#        self.check_athan_notification = QCheckBox(self.group_athan)
#        self.check_athan_notification.setObjectName("check_athan_notification")
#        self.check_athan_notification.setChecked(
#                settings.reminder_athan['notification_enabled'] == '1')

#        self.group_athan_layout.addWidget(self.desc_athan_method, 4, 0, 1, 2)
        self.group_athan_layout.addWidget(self.desc_athan, 0, 0, 1, 2)
#        self.group_athan_layout.addWidget(self.check_athan_dialog, 5, 0, 1, 2)
#        self.group_athan_layout.addWidget(self.check_athan_notification, 6, 0, 1, 2)

        self.verticalLayout.addWidget(self.group_athan)

        ##-- Iqomah --##
        self.group_iqomah = QGroupBox(self.scrollAreaWidgetContents)
        self.group_iqomah.setFlat(False)
        self.group_iqomah.setCheckable(False)
        self.group_iqomah.setObjectName("group_iqomah")
        self.group_iqomah_layout = QGridLayout(self.group_iqomah)
        self.group_iqomah_layout.setObjectName("group_iqomah_layout")

        valid_iqomah = QIntValidator(1, 60)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.check_iqomah = {}
        self.text_iqomah = {}
        y = 2
        for name in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
            self.check_iqomah[name.lower()] = QCheckBox(self.group_iqomah)
            self.check_iqomah[name.lower()].setObjectName("check_iqomah_" + name.lower())
            self.check_iqomah[name.lower()].setText(_translate("SettingsWindow", name))
            self.check_iqomah[name.lower()].setChecked(
                settings.reminder_iqomah[name.lower() + '_enabled'] == '1')

            self.text_iqomah[name.lower()] = QLineEdit(self.group_iqomah)
            self.text_iqomah[name.lower()].setSizePolicy(sizePolicy)
            self.text_iqomah[name.lower()].setBaseSize(QSize(0, 0))
            self.text_iqomah[name.lower()].setReadOnly(False)
            self.text_iqomah[name.lower()].setObjectName("txt_iqomah_" + name.lower())
            self.text_iqomah[name.lower()].setValidator(valid_iqomah)
            self.text_iqomah[name.lower()].setText(
                settings.reminder_iqomah[name.lower() + '_time'])
            self.text_iqomah[name.lower()].setDisabled(not self.check_iqomah[name.lower()].isChecked())

            self.check_iqomah[name.lower()].toggled.connect(
                    lambda state, n=name.lower(): self.text_iqomah[n].setDisabled(not state))
            self.group_iqomah_layout.addWidget(self.check_iqomah[name.lower()], y, 0, 1, 1)
            self.group_iqomah_layout.addWidget(self.text_iqomah[name.lower()], y, 1, 1, 1)
            y += 1

#        self.check_iqomah_notification = QCheckBox(self.group_iqomah)
#        self.check_iqomah_notification.setObjectName("check_iqomah_notification")
#        self.check_iqomah_notification.setChecked(
#                settings.reminder_iqomah['notification_enabled'] == '1')
        self.desc_iqomah = QLabel(self.group_iqomah)
        self.desc_iqomah.setObjectName("desc_iqomah")
        self.group_iqomah_layout.addWidget(self.desc_iqomah, 0, 0, 1, 2)
#        self.check_iqomah_dialog = QCheckBox(self.group_iqomah)
#        self.check_iqomah_dialog.setObjectName("check_iqomah_dialog")
#        self.check_iqomah_dialog.setChecked(
#                settings.reminder_iqomah['dialog_enabled'] == '1')
        self.lbl_timeafterathan = QLabel(self.group_iqomah)
        self.lbl_timeafterathan.setObjectName("lbl_timeafterathan")
#        self.desc_iqomah_method = QLabel(self.group_iqomah)
#        self.desc_iqomah_method.setObjectName("desc_iqomah_method")
        self.verticalLayout.addWidget(self.group_iqomah)

        self.group_iqomah_layout.addWidget(self.lbl_timeafterathan, 1, 1, 1, 1)
#        self.group_iqomah_layout.addWidget(self.desc_iqomah_method, 8, 0, 1, 1)
#        self.group_iqomah_layout.addWidget(self.check_iqomah_dialog, 9, 0, 1, 1)
#        self.group_iqomah_layout.addWidget(self.check_iqomah_notification, 10, 0, 1, 2)

        self.group_custom = QGroupBox(self.scrollAreaWidgetContents)
        self.group_custom.setObjectName("group_custom")
        self.gridLayout_6 = QGridLayout(self.group_custom)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.desc_custom = QLabel(self.group_custom)
        self.desc_custom.setObjectName("desc_custom")
        self.gridLayout_6.addWidget(self.desc_custom, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.group_custom)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout_reminders.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_reminders, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(0)

        self.tabWidget.setTabText(
                self.tabWidget.indexOf(self.tab_location),
                _translate("SettingsWindow", "Location"))
        self.group_athan.setTitle(_translate("SettingsWindow", "Athan"))

#        self.desc_athan_method.setText(_translate("SettingsWindow", "Method of reminder"))
        self.desc_athan.setText(_translate("SettingsWindow", "Enable/disable athan reminder"))
#        self.check_athan_dialog.setText(_translate("SettingsWindow", "Pop up dialog"))
#        self.check_athan_notification.setText(_translate("SettingsWindow", "Pop up notification"))

        self.group_iqomah.setTitle(_translate("SettingsWindow", "Iqomah"))
#        self.check_iqomah_notification.setText(_translate("SettingsWindow", "Pop up notification"))
        self.desc_iqomah.setText(_translate("SettingsWindow", "Enable/disable iqomah reminder"))
#        self.check_iqomah_dialog.setText(_translate("SettingsWindow", "Pop up dialog"))
        self.lbl_timeafterathan.setText(_translate("SettingsWindow", "Time after Athan"))
#        self.desc_iqomah_method.setText(_translate("SettingsWindow", "Method of reminder"))

        self.group_custom.setTitle(_translate("SettingsWindow", "Custom"))
        self.desc_custom.setText(_translate("SettingsWindow", "Coming Soon!"))

        self.tabWidget.setTabText(
                self.tabWidget.indexOf(self.tab_reminders),
                _translate("SettingsWindow", "Reminders"))
        QMetaObject.connectSlotsByName(self)

    def apply_settings(self):
        location_settings = {
                'title'    : 'Location', 
                'country'  : self.combo_country.currentText(),
                'province' : self.combo_prov.currentText(),
                'city'     : self.combo_city.currentText(),
                'latitude' : self.txt_lat.text(),
                'longitude': self.txt_lon.text(),
                'timezone' : self.txt_tz.text(),
                'calcCode' : self.combo_calc.currentText()
                }

        athan_settings = {'title': 'Reminder: Athan'}
        iqomah_settings = {'title': 'Reminder: Iqomah'}
        
        for name in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
            athan_settings[name + '_enabled']  = str( int(self.check_athan[name.lower()].isChecked()) )
            iqomah_settings[name + '_enabled'] = str( int(self.check_iqomah[name.lower()].isChecked()) )
            iqomah_settings[name + '_time']    = str(self.text_iqomah[name.lower()].text())

#        athan_settings['dialog_enabled']        = str( int(self.check_athan_dialog.isChecked()) )
#        athan_settings['notification_enabled']  = str( int(self.check_athan_notification.isChecked()) )
#        iqomah_settings['dialog_enabled']       = str( int(self.check_iqomah_dialog.isChecked()) )
#        iqomah_settings['notification_enabled'] = str( int(self.check_iqomah_notification.isChecked()) )

        sections = [location_settings, athan_settings, iqomah_settings]
        settings.apply_settings(sections)

    def setProvText(self, country):
        try: self.combo_prov.currentTextChanged.disconnect()
        except TypeError: pass
        if self.coordinates[country] != '':
            self.enableProv = self.coordinates[self.combo_country.currentText()]['province'] 
            self.combo_prov.setDisabled(not self.enableProv)
            self.combo_prov.clear()
            if self.enableProv:
                for item in self.coordinates[country].keys():
                    if item != 'province':
                        self.combo_prov.addItem(item)
                self.combo_prov.currentTextChanged.connect(self.setCityText)
            else:
                self.setCityText(country)
        self.combo_prov.setCurrentText('')
        self.combo_city.setCurrentText('')
    
    def setCityText(self, countryprov):
        self.combo_city.clear()
        if self.enableProv:
            if self.coordinates[self.combo_country.currentText()][self.combo_prov.currentText()] != '':
                for item in self.coordinates[self.combo_country.currentText()][self.combo_prov.currentText()].keys():
                    if item != 'province':
                        self.combo_city.addItem(item)
        else:
            if self.coordinates[self.combo_country.currentText()] != '':
                for item in self.coordinates[self.combo_country.currentText()].keys():
                    if item != 'province':
                        self.combo_city.addItem(item)
        self.combo_city.setCurrentText('')

    def setCoordinates(self, city):
        # TODO make this work
        if self.combo_country.currentText() != '' and \
                self.combo_prov.currentText() != '' and \
                self.combo_city.currentText() != '':
            if self.enableProv:
                latlon = self.coordinates[self.combo_country.currentText()][self.combo_prov.currentText()][self.combo_city.currentText()]
            else:
                latlon = self.coordinates[self.combo_country.currentText()][self.combo_city.currentText()]
            lat = latlon[0]
            lon = latlon[1]
            self.txt_lat.setText(lat)
            self.txt_lon.setText(lon)
