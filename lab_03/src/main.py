import sys
from numpy import *

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from func import *
import matplotlib.pyplot as plt
from scipy.stats import chisquare

from mainwindow_ui import *


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.bind()

        for i in range(10):
            item =  QSpinBox()
            item.setMaximum(9)
            item.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons) 
            self.table1.setCellWidget(i, 0, item)
    
    def alg_gen(self):
        intervals = [(0, 9), (10, 99), (100, 999)]

        for i, interval in enumerate(intervals):
            a, b = interval
            alg_generator = AlgorithmGenerator(a, b)

            alg_numbers = alg_generator.get_random_numbers(10)

            for j in range(len(alg_numbers)):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() ^ ~QtCore.Qt.ItemIsEditable)
                item.setText(str(alg_numbers[j]))
                self.table2.setItem(j, i, item)

            ans, f_obs = calc_chi(alg_numbers, 10, a, b)
            ans2 = chisquare(f_obs=f_obs).pvalue

            item = QtWidgets.QTableWidgetItem()
            item.setFlags(item.flags() ^ ~QtCore.Qt.ItemIsEditable)
            item.setText(str(round(ans2, 6)))
            self.coef2.setItem(0, i, item)

    def table_gen(self):
        
        intervals = [(0, 9), (10, 99), (100, 999)]

        for i, interval in enumerate(intervals):
            a, b = interval
            tab_numbers = self.table_generator.get_random_numbers(i + 1, 10)

            for j in range(len(tab_numbers)):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() ^ ~QtCore.Qt.ItemIsEditable)
                item.setText(str(tab_numbers[j]))
                self.table3.setItem(j, i, item)
            
            ans, f_obs = calc_chi(tab_numbers, 10, a, b)
            ans2 = chisquare(f_obs=f_obs).pvalue

            item = QtWidgets.QTableWidgetItem()
            item.setFlags(item.flags() ^ ~QtCore.Qt.ItemIsEditable)
            item.setText(str(round(ans2, 6)))
            self.coef3.setItem(0, i, item)

    
    def count_manual(self):
        sp = self.extract_manual()

        ans, f_obs = calc_chi(sp, 10, 0, 9)
        ans2 = chisquare(f_obs=f_obs).pvalue

        item = QtWidgets.QTableWidgetItem()
        item.setFlags(item.flags() ^ ~QtCore.Qt.ItemIsEditable)
        item.setText(str(round(ans2, 6)))
        self.coef1.setItem(0, 0, item)


    def extract_manual(self):
        n = 10
        sp = [0 for i in range(n)]

        for i in range(n):
            a = self.table1.cellWidget(i, 0)
            sp[i] = int(a.value())
        return sp

    def bind(self):
        self.table_generator = TableGenerator('lab_03/number_table.txt')
        self.but2.clicked.connect(self.alg_gen)
        self.but3.clicked.connect(self.table_gen)
        self.but1.clicked.connect(self.count_manual)

        self.alg_gen()
        self.table_gen()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())