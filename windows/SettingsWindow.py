#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        
        self.setMinimumSize(QtCore.QSize(360,240))
        self.setObjectName("SettingsWindow")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        # Latitude
        self.lbl_lat = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_lat.setObjectName("lbl_lat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_lat)
        self.txt_lat = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_lat.setObjectName("txt_lat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_lat)

        # Latitude
        self.lbl_lon = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_lon.setObjectName("lbl_lon")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_lon)
        self.txt_lon = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_lon.setObjectName("txt_lon")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_lon)

        # Longitude
        self.lbl_tz = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_tz.setObjectName("lbl_tz")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_tz)
        self.txt_tz = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_tz.setObjectName("txt_tz")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_tz)

        # Calclation methods
        self.lbl_calc = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_calc.setObjectName("lbl_calc")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_calc)
        self.box_calc = QtWidgets.QComboBox(self.formLayoutWidget)
        self.box_calc.setObjectName("box_calc")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.box_calc)

        # Apply button
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.pushButton)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 20))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.lbl_lat.setText(_translate("SettingsWindow", "Latitude"))
        self.lbl_lon.setText(_translate("SettingsWindow", "Longitude"))
        self.lbl_tz.setText(_translate("SettingsWindow", "Timezone"))
        self.lbl_calc.setText(_translate("SettingsWindow", "Calculation Method"))
        self.pushButton.setText(_translate("SettingsWindow", "Apply"))
        QtCore.QMetaObject.connectSlotsByName(self)
