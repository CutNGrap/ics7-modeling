import sys

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QColorDialog, QMessageBox, QGraphicsScene, QWidget, QListWidget, QListWidgetItem, QTableWidgetItem
from PyQt5.QtGui import QColor, QPen, QPixmap, QBrush, QImage, QPainter, QTransform
from PyQt5.QtCore import QRect, QCoreApplication, QEventLoop, QPointF, QTimerEvent, Qt, QPoint
from math import sqrt
from func import *


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

    def resize_m(self):
        a = int(self.lineEdit_1.text())
        self.table.setColumnCount(a)
        self.table.setRowCount(a + 2)

        labels = [str(i+1) for i in range(a)] + ["t_пр", "P_i"]
        self.table.setVerticalHeaderLabels(labels)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())