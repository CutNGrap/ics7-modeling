import sys
from numpy import *

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from func import *
import matplotlib.pyplot as plt

from mainwindow_ui import *


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
    

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

        self.bind()
        self.resize_m()
   
    def bind(self):
        for i in range(10):
            self.table.setColumnWidth(i, 50)
            self.table.setRowHeight(i, 70)
        self.but_matr.clicked.connect(self.resize_m)
        self.but_close_4.clicked.connect(self.calc)

    def resize_m(self):
        self.cur_size = self.spinBox.value()
        a = self.cur_size
        self.table.setColumnCount(a)
        self.table.setRowCount(a + 2)
        
        for i in range(a):
            for j in range(a):
                item =  QDoubleSpinBox()
                item.setMaximum(1e5)
                item.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons) 
                if i==j:
                    item.setDisabled(True)
                self.table.setCellWidget(i, j, item)

        for i in (a, a+1):
            for j in range(a):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() ^ ~QtCore.Qt.ItemIsEditable)
                self.table.setItem(i, j, item)

        labels = [str(i+1) for i in range(a)] + ["P_i","t_пр"]
        self.table.setVerticalHeaderLabels(labels)


    def calc(self):
        matrix = self.extract()
        n = len(matrix)
        
        sp = limit_prob(matrix)

        for i in range(n):
            self.table.item(n, i).setText(str(round(sp[i], 4)))

        sp1 = stable_time(matrix, sp)

        for i in range(n):
            self.table.item(n+1, i).setText(str(round(sp1[i], 4)))

        self.table.viewport().update()


    def extract(self):
        n = self.table.columnCount()
        sp = [[0 for _ in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                a = self.table.cellWidget(i, j)
                sp[i][j] = float(a.value())

        return sp






if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())