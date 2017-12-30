#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(360, 240)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.lbl_lat = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_lat.setObjectName("lbl_lat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_lat)
        self.txt_lat = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_lat.setObjectName("txt_lat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_lat)

        self.lbl_lon = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_lon.setObjectName("lbl_lon")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_lon)
        self.txt_lon = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_lon.setObjectName("txt_lon")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_lon)

        self.lbl_tz = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_tz.setObjectName("lbl_tz")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_tz)
        self.txt_tz = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_tz.setObjectName("txt_tz")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_tz)

        self.lbl_calc = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_calc.setObjectName("lbl_calc")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_calc)
        self.box_calc = QtWidgets.QComboBox(self.formLayoutWidget)
        self.box_calc.setObjectName("box_calc")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.box_calc)

        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.pushButton)

        SettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 20))
        self.menubar.setObjectName("menubar")
        SettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.lbl_lat.setText(_translate("SettingsWindow", "Latitude"))
        self.lbl_lon.setText(_translate("SettingsWindow", "Longitude"))
        self.lbl_tz.setText(_translate("SettingsWindow", "Timezone"))
        self.lbl_calc.setText(_translate("SettingsWindow", "Calculation Method"))
        self.pushButton.setText(_translate("SettingsWindow", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())

