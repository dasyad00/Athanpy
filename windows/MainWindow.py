#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QSize, Qt, QRect, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QSizePolicy, QMenuBar, QMenu, QStatusBar, QAction, qApp, QSystemTrayIcon, QStyle, QApplication
import configparser

from core.settings import SettingsManager
from core.alarmdaemon import AlarmDaemon
from windows.SettingsWindow import SettingsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.minimize_to_tray = True
        self.alarm = AlarmDaemon(self)

        # Window definitions
        self.setMinimumSize(QSize(480,320))
        self.setWindowTitle("AthanPy")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Layout definitions
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # Widget definitions
        self.txt_times = QLabel(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_times.sizePolicy().hasHeightForWidth())
        self.txt_times.setSizePolicy(sizePolicy)
        self.txt_times.setAlignment(Qt.AlignCenter)
        self.txt_times.setObjectName("txt_times")
        self.txt_times.setText(self.get_prayertime_text())
        self.gridLayout.addWidget(self.txt_times, 1, 0, 1, 1)

        self.txt_date = QLabel(self.centralwidget)
        self.txt_date.setObjectName("txt_date")
        self.gridLayout.addWidget(self.txt_date, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        # Menu bar
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 480, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.actionSettings = QAction(self)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings.setText("Settings")
        self.actionSettings.triggered.connect(self.show_settings)

        self.actionQuit = QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setText("Quit")
        self.actionQuit.triggered.connect(qApp.quit)

        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.setTitle("File")

        self.menubar.addAction(self.menuFile.menuAction())

        # QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))

        show_action = QAction("Show", self)
        hide_action = QAction("Hide", self)
        mute_action = QAction("Mute sound", self)
        stopsound_action = QAction("Stop sound", self)
        quit_action = QAction("Quit", self)

        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        mute_action.setCheckable(True)
        mute_action.changed.connect(
            lambda: self.alarm.set_mute(mute_action.isChecked()))
        stopsound_action.triggered.connect(self.alarm.stop_sound)
        quit_action.triggered.connect(QCoreApplication.quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addSeparator()
        tray_menu.addAction(stopsound_action)
        tray_menu.addAction(mute_action)
        tray_menu.addSeparator()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Settings window
        self.settingswindow = SettingsWindow()

    def closeEvent(self, event):
        if self.minimize_to_tray:
            print('triggered 1')
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Tray Program",
                "Application was minimized to tray",
                QSystemTrayIcon.Information,
                2000
            )

    def get_prayertime_text(self):
        SettingsManager.refreshVariables(self.show_settings)
        SettingsManager.calcTimes()

        times = SettingsManager.times
        # For testing purposes, comment/delete when not in use
        #times['dhuhr'] = '08:02'
        #times['asr'] = '08:03'
#        times['isha'] = '16:20'
        output = ''
        for i in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha', 'Midnight']:
            output += (i + ': ' + times[i.lower()] + "\n")
        self.alarm.schedule_alarm(times)
        self.alarm.start()
        return output

    def show_settings(self):
        self.settingswindow.show()

def main():
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
