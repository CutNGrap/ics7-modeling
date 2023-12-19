# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.label_9.setObjectName("label_9")
        self.t = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.t.setGeometry(QtCore.QRect(160, 0, 51, 22))
        self.t.setMinimum(0.1)
        self.t.setMaximum(10.0)
        self.t.setSingleStep(0.1)
        self.t.setProperty("value", 0.5)
        self.t.setObjectName("t")
        self.N = QtWidgets.QSpinBox(self.centralwidget)
        self.N.setGeometry(QtCore.QRect(160, 30, 51, 22))
        self.N.setMaximum(100000)
        self.N.setProperty("value", 500)
        self.N.setObjectName("N")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 101, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(150, 60, 16, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(230, 60, 16, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 100, 141, 20))
        self.label_14.setObjectName("label_14")
        self.m = QtWidgets.QSpinBox(self.centralwidget)
        self.m.setGeometry(QtCore.QRect(160, 100, 51, 22))
        self.m.setMaximum(100)
        self.m.setProperty("value", 5)
        self.m.setObjectName("m")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(226, 100, 20, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(150, 100, 16, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(310, 100, 16, 20))
        self.label_17.setObjectName("label_17")
        self.P = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.P.setGeometry(QtCore.QRect(320, 100, 51, 22))
        self.P.setMaximum(1.0)
        self.P.setSingleStep(0.1)
        self.P.setObjectName("P")
        self.a = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(160, 60, 51, 22))
        self.a.setMaximum(10.0)
        self.a.setObjectName("a")
        self.b = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(240, 60, 51, 22))
        self.b.setMaximum(100.0)
        self.b.setProperty("value", 10.0)
        self.b.setObjectName("b")
        self.sigma = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sigma.setGeometry(QtCore.QRect(240, 100, 51, 22))
        self.sigma.setMaximum(10.0)
        self.sigma.setSingleStep(0.1)
        self.sigma.setProperty("value", 2.0)
        self.sigma.setObjectName("sigma")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 111, 21))
        self.pushButton.setObjectName("pushButton")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(20, 190, 161, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(110, 220, 61, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(60, 250, 121, 20))
        self.label_20.setObjectName("label_20")
        self.d_t = QtWidgets.QSpinBox(self.centralwidget)
        self.d_t.setGeometry(QtCore.QRect(180, 220, 51, 22))
        self.d_t.setReadOnly(True)
        self.d_t.setMaximum(100000)
        self.d_t.setProperty("value", 0)
        self.d_t.setObjectName("d_t")
        self.ev = QtWidgets.QSpinBox(self.centralwidget)
        self.ev.setGeometry(QtCore.QRect(180, 250, 51, 22))
        self.ev.setReadOnly(True)
        self.ev.setMaximum(100000)
        self.ev.setProperty("value", 0)
        self.ev.setObjectName("ev")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа #4"))
        self.label_9.setText(_translate("MainWindow", "Общее число сообщений:"))
        self.label_10.setText(_translate("MainWindow", "Шаг по времени:"))
        self.label_11.setText(_translate("MainWindow", "Генератор"))
        self.label_12.setText(_translate("MainWindow", "a"))
        self.label_13.setText(_translate("MainWindow", "b"))
        self.label_14.setText(_translate("MainWindow", "Обслуживающий автомат"))
        self.label_15.setText(_translate("MainWindow", "σ2"))
        self.label_16.setText(_translate("MainWindow", "m"))
        self.label_17.setText(_translate("MainWindow", "P"))
        self.pushButton.setText(_translate("MainWindow", "Промоделировать"))
        self.label_18.setText(_translate("MainWindow", "Максимальная длина очереди:"))
        self.label_19.setText(_translate("MainWindow", "Принцип Δt:"))
        self.label_20.setText(_translate("MainWindow", "Событийный принцип:"))
