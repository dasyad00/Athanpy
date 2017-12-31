#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import configparser

from core.settings import SettingsManager
from core.alarmdaemon import AlarmDaemon
from windows.SettingsWindow import SettingsWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.minimize_to_tray = True
        # Window definitions
        self.setMinimumSize(QtCore.QSize(480,320))
        self.setWindowTitle("AthanPy")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Layout definitions
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # Widget definitions
        self.txt_times = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_times.sizePolicy().hasHeightForWidth())
        self.txt_times.setSizePolicy(sizePolicy)
        self.txt_times.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_times.setObjectName("txt_times")
        self.txt_times.setText(self.get_prayertime_text())
        self.gridLayout.addWidget(self.txt_times, 1, 0, 1, 1)

        self.txt_date = QtWidgets.QLabel(self.centralwidget)
        self.txt_date.setObjectName("txt_date")
        self.gridLayout.addWidget(self.txt_date, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        # Menu bar
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.actionSettings = QtWidgets.QAction(self)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings.setText("Settings")
        self.actionSettings.triggered.connect(self.show_settings)

        self.actionQuit = QtWidgets.QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setText("Quit")
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)

        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.setTitle("File")

        self.menubar.addAction(self.menuFile.menuAction())

        # QSystemTrayIcon
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ComputerIcon))

        show_action = QtWidgets.QAction("Show", self)
        quit_action = QtWidgets.QAction("Quit", self)
        hide_action = QtWidgets.QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(QtWidgets.qApp.quit)
        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        tray_menu.addAction(hide_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Settings window
        self.settingswindow = SettingsWindow()

    def closeEvent(self, event):
        if self.minimize_to_tray:
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Tray Program",
                "Application was minimized to tray",
                QtWidgets.QSystemTrayIcon.Information,
                2000
            )

    def get_prayertime_text(self):
        SettingsManager.refreshVariables(self.show_settings)
        SettingsManager.calcTimes()

        times = SettingsManager.times
        output = ''
        for i in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha', 'Midnight']:
            output += (i + ': ' + times[i.lower()] + "\n")
        self.alarm = AlarmDaemon()
        self.alarm.schedule_alarm(times)
        return output

    def show_settings(self):
        self.settingswindow.show()

def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
