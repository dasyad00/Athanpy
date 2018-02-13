#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import configparser

from core.settings import SettingsManager as settings
from core.praytimes import PrayTimes

cfg = configparser.ConfigParser()
prayTimes = PrayTimes()
#settingsmgr = SettingsManager()

class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        _translate = QtCore.QCoreApplication.translate
        
        self.setMinimumSize(QtCore.QSize(360,240))
        self.setObjectName("SettingsWindow")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_apply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_apply.setObjectName("btn_apply")
        self.btn_apply.clicked.connect(self.apply_settings)
        self.gridLayout.addWidget(self.btn_apply, 3, 0, 1, 1)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        ###--- Location ---###
        self.tab_location = QtWidgets.QWidget()
        self.tab_location.setObjectName("tab_location")
        self.layout_location = QtWidgets.QGridLayout(self.tab_location)
        self.layout_location.setObjectName("layout_location")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        # Latitude
        self.lbl_lat = QtWidgets.QLabel(self.tab_location)
        self.lbl_lat.setObjectName("lbl_lat")
        self.txt_lat = QtWidgets.QLineEdit(self.tab_location)
        self.txt_lat.setObjectName("txt_lat")
        self.txt_lat.setText(str(settings.location['lat']))
        self.txt_lat.setValidator(
                QtGui.QDoubleValidator(-90.0, 90.0, 5))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_lat)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_lat)

        # Longitude
        self.lbl_lon = QtWidgets.QLabel(self.tab_location)
        self.lbl_lon.setObjectName("lbl_lon")
        self.txt_lon = QtWidgets.QLineEdit(self.tab_location)
        self.txt_lon.setObjectName("txt_lon")
        self.txt_lon.setValidator(
                QtGui.QDoubleValidator(-180.0, 180.0, 5))
        self.txt_lon.setText(str(settings.location['lon']))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_lon)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_lon)

        # Timezone
        self.lbl_tz = QtWidgets.QLabel(self.tab_location)
        self.lbl_tz.setObjectName("lbl_tz")
        self.txt_tz = QtWidgets.QLineEdit(self.tab_location)
        self.txt_tz.setObjectName("txt_tz")
        self.txt_tz.setValidator(
                QtGui.QDoubleValidator(-12, 14, 2))
        self.txt_tz.setText(str(settings.location['tz']))
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_tz)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_tz)

        # Calculation method
        self.lbl_calc = QtWidgets.QLabel(self.tab_location)
        self.lbl_calc.setObjectName("lbl_calc")
        self.combo_calc = QtWidgets.QComboBox(self.tab_location)
        self.combo_calc.setObjectName("combo_calc")

        calcCodes = prayTimes.methods
        for code in calcCodes:
            self.combo_calc.addItem(code)
        if (settings.location['calcCode'] != ''):
            self.combo_calc.setCurrentText(settings.calcCode)

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_calc)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.combo_calc)
        self.layout_location.addLayout(self.formLayout, 0, 0, 1, 1)
        
        self.tabWidget.addTab(self.tab_location, "")

        self.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.lbl_lat.setText(_translate("SettingsWindow", "Latitude"))
        self.lbl_lon.setText(_translate("SettingsWindow", "Longitude"))
        self.lbl_tz.setText(_translate("SettingsWindow", "Timezone"))
        self.lbl_calc.setText(_translate("SettingsWindow", "Calculation Method"))
        self.btn_apply.setText(_translate("SettingsWindow", "Apply"))

        ###--- Reminders ---###
        self.tab_reminders = QtWidgets.QWidget()
        self.tab_reminders.setObjectName("tab_reminders")
        self.layout_reminders = QtWidgets.QGridLayout(self.tab_reminders)
        self.layout_reminders.setObjectName("layout_reminders")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_reminders)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 304, 598))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        ##-- Athan group--##
        self.group_athan = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_athan.setObjectName("group_athan")
        self.group_athan_layout = QtWidgets.QGridLayout(self.group_athan)
        self.group_athan_layout.setObjectName("group_athan_layout")

        self.check_athan = {}
        y = 1
        x = 0
        for name in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
            self.check_athan[name.lower()] = QtWidgets.QCheckBox(self.group_athan)
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
        self.desc_athan_method = QtWidgets.QLabel(self.group_athan)
        self.desc_athan_method.setObjectName("desc_athan_method")
        self.desc_athan = QtWidgets.QLabel(self.group_athan)
        self.desc_athan.setObjectName("desc_athan")
        self.check_athan_dialog = QtWidgets.QCheckBox(self.group_athan)
        self.check_athan_dialog.setObjectName("check_athan_dialog")
        self.check_athan_dialog.setChecked(
                settings.reminder_athan['dialog_enabled'] == '1')
        self.check_athan_notification = QtWidgets.QCheckBox(self.group_athan)
        self.check_athan_notification.setObjectName("check_athan_notification")
        self.check_athan_notification.setChecked(
                settings.reminder_athan['notification_enabled'] == '1')

        self.group_athan_layout.addWidget(self.desc_athan_method, 4, 0, 1, 2)
        self.group_athan_layout.addWidget(self.desc_athan, 0, 0, 1, 2)
        self.group_athan_layout.addWidget(self.check_athan_dialog, 5, 0, 1, 2)
        self.group_athan_layout.addWidget(self.check_athan_notification, 6, 0, 1, 2)

        self.verticalLayout.addWidget(self.group_athan)

        ##-- Iqomah --##
        self.group_iqomah = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_iqomah.setFlat(False)
        self.group_iqomah.setCheckable(False)
        self.group_iqomah.setObjectName("group_iqomah")
        self.group_iqomah_layout = QtWidgets.QGridLayout(self.group_iqomah)
        self.group_iqomah_layout.setObjectName("group_iqomah_layout")

        valid_iqomah = QtGui.QIntValidator(1, 60)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.check_iqomah = {}
        self.text_iqomah = {}
        y = 2
        for name in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
            self.check_iqomah[name.lower()] = QtWidgets.QCheckBox(self.group_iqomah)
            self.check_iqomah[name.lower()].setObjectName("check_iqomah_" + name.lower())
            self.check_iqomah[name.lower()].setText(_translate("SettingsWindow", name))
            self.check_iqomah[name.lower()].setChecked(
                settings.reminder_iqomah[name.lower() + '_enabled'] == '1')

            self.text_iqomah[name.lower()] = QtWidgets.QLineEdit(self.group_iqomah)
            self.text_iqomah[name.lower()].setSizePolicy(sizePolicy)
            self.text_iqomah[name.lower()].setBaseSize(QtCore.QSize(0, 0))
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

        self.check_iqomah_notification = QtWidgets.QCheckBox(self.group_iqomah)
        self.check_iqomah_notification.setObjectName("check_iqomah_notification")
        self.check_iqomah_notification.setChecked(
                settings.reminder_iqomah['notification_enabled'] == '1')
        self.desc_iqomah = QtWidgets.QLabel(self.group_iqomah)
        self.desc_iqomah.setObjectName("desc_iqomah")
        self.group_iqomah_layout.addWidget(self.desc_iqomah, 0, 0, 1, 2)
        self.check_iqomah_dialog = QtWidgets.QCheckBox(self.group_iqomah)
        self.check_iqomah_dialog.setObjectName("check_iqomah_dialog")
        self.check_iqomah_dialog.setChecked(
                settings.reminder_iqomah['dialog_enabled'] == '1')
        self.lbl_timeafterathan = QtWidgets.QLabel(self.group_iqomah)
        self.lbl_timeafterathan.setObjectName("lbl_timeafterathan")
        self.desc_iqomah_method = QtWidgets.QLabel(self.group_iqomah)
        self.desc_iqomah_method.setObjectName("desc_iqomah_method")
        self.verticalLayout.addWidget(self.group_iqomah)

        self.group_iqomah_layout.addWidget(self.lbl_timeafterathan, 1, 1, 1, 1)
        self.group_iqomah_layout.addWidget(self.desc_iqomah_method, 8, 0, 1, 1)
        self.group_iqomah_layout.addWidget(self.check_iqomah_dialog, 9, 0, 1, 1)
        self.group_iqomah_layout.addWidget(self.check_iqomah_notification, 10, 0, 1, 2)

        self.group_custom = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_custom.setObjectName("group_custom")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.group_custom)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.desc_custom = QtWidgets.QLabel(self.group_custom)
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

        self.desc_athan_method.setText(_translate("SettingsWindow", "Method of reminder"))
        self.desc_athan.setText(_translate("SettingsWindow", "Enable/disable athan reminder"))
        self.check_athan_dialog.setText(_translate("SettingsWindow", "Pop up dialog"))
        self.check_athan_notification.setText(_translate("SettingsWindow", "Pop up notification"))

        self.group_iqomah.setTitle(_translate("SettingsWindow", "Iqomah"))
        self.check_iqomah_notification.setText(_translate("SettingsWindow", "Pop up notification"))
        self.desc_iqomah.setText(_translate("SettingsWindow", "Enable/disable iqomah reminder"))
        self.check_iqomah_dialog.setText(_translate("SettingsWindow", "Pop up dialog"))
        self.lbl_timeafterathan.setText(_translate("SettingsWindow", "Time after Athan"))
        self.desc_iqomah_method.setText(_translate("SettingsWindow", "Method of reminder"))

        self.group_custom.setTitle(_translate("SettingsWindow", "Custom"))
        self.desc_custom.setText(_translate("SettingsWindow", "Coming Soon!"))

        self.tabWidget.setTabText(
                self.tabWidget.indexOf(self.tab_reminders),
                _translate("SettingsWindow", "Reminders"))
        QtCore.QMetaObject.connectSlotsByName(self)

    def apply_settings(self):
        location_settings = {
                'title'    : 'Location', 
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

        athan_settings['dialog_enabled']        = str( int(self.check_athan_dialog.isChecked()) )
        athan_settings['notification_enabled']  = str( int(self.check_athan_notification.isChecked()) )
        iqomah_settings['dialog_enabled']       = str( int(self.check_iqomah_dialog.isChecked()) )
        iqomah_settings['notification_enabled'] = str( int(self.check_iqomah_notification.isChecked()) )

        sections = [location_settings, athan_settings, iqomah_settings]
        settings.apply_settings(sections)
