#!/usr/bin/python
from core.praytimes import PrayTimes
from core.settings import SettingsManager
from core.alarmdaemon import AlarmDaemon

from datetime import date
import configparser
import sys
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
        QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp
from PyQt5.QtCore import QSize

prayTimes = PrayTimes()
settings = SettingsManager()
cfg = configparser.ConfigParser()

#class AthanWindow(QMainWindow):
#    check_box = None
#    tray_icon = None
#
#    def __init__(self):
#        QMainWindow.__init__(self)
#        self.setMinimumSize(QSize(480, 240))
#        self.setWindowTitle("AthanPy")
#        central_widget = QWidget(self)
#        self.setCentralWidget(central_widget)
#
#        grid_layout = QGridLayout(self)
#        central_widget.setLayout(grid_layout)

from windows.MainWindow import MainWindow, main as start

start()
