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
        MainWindow.resize(879, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but1 = QtWidgets.QPushButton(self.centralwidget)
        self.but1.setGeometry(QtCore.QRect(20, 460, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but1.setFont(font)
        self.but1.setObjectName("but1")
        self.table1 = QtWidgets.QTableWidget(self.centralwidget)
        self.table1.setGeometry(QtCore.QRect(20, 30, 131, 331))
        self.table1.setRowCount(10)
        self.table1.setColumnCount(1)
        self.table1.setObjectName("table1")
        self.table2 = QtWidgets.QTableWidget(self.centralwidget)
        self.table2.setGeometry(QtCore.QRect(180, 30, 331, 331))
        self.table2.setRowCount(10)
        self.table2.setColumnCount(3)
        self.table2.setObjectName("table2")
        self.table3 = QtWidgets.QTableWidget(self.centralwidget)
        self.table3.setGeometry(QtCore.QRect(540, 30, 331, 331))
        self.table3.setRowCount(10)
        self.table3.setColumnCount(3)
        self.table3.setObjectName("table3")
        self.coef1 = QtWidgets.QTableWidget(self.centralwidget)
        self.coef1.setGeometry(QtCore.QRect(20, 400, 121, 51))
        self.coef1.setRowCount(1)
        self.coef1.setColumnCount(1)
        self.coef1.setObjectName("coef1")
        self.but2 = QtWidgets.QPushButton(self.centralwidget)
        self.but2.setGeometry(QtCore.QRect(180, 460, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but2.setFont(font)
        self.but2.setObjectName("but2")
        self.coef2 = QtWidgets.QTableWidget(self.centralwidget)
        self.coef2.setGeometry(QtCore.QRect(180, 400, 321, 51))
        self.coef2.setRowCount(1)
        self.coef2.setColumnCount(3)
        self.coef2.setObjectName("coef2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 10, 171, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 10, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 370, 81, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 370, 81, 21))
        self.label_6.setObjectName("label_6")
        self.coef3 = QtWidgets.QTableWidget(self.centralwidget)
        self.coef3.setGeometry(QtCore.QRect(540, 400, 321, 51))
        self.coef3.setRowCount(1)
        self.coef3.setColumnCount(3)
        self.coef3.setObjectName("coef3")
        self.but3 = QtWidgets.QPushButton(self.centralwidget)
        self.but3.setGeometry(QtCore.QRect(540, 460, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but3.setFont(font)
        self.but3.setObjectName("but3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 370, 81, 21))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа #3"))
        self.but1.setText(_translate("MainWindow", "Вычислить"))
        self.but2.setText(_translate("MainWindow", "Вычислить"))
        self.label_2.setText(_translate("MainWindow", "Ручной ввод"))
        self.label_3.setText(_translate("MainWindow", "Алгоритмический способ"))
        self.label_4.setText(_translate("MainWindow", "Табличный способ"))
        self.label_5.setText(_translate("MainWindow", "Коэффициенты"))
        self.label_6.setText(_translate("MainWindow", "Коэффициенты"))
        self.but3.setText(_translate("MainWindow", "Вычислить"))
        self.label_7.setText(_translate("MainWindow", "Коэффициенты"))