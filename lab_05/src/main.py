import sys
from numpy import *

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from func import *
import matplotlib.pyplot as plt
from scipy.stats import chisquare

from mainwindow_ui import *

clients_number = 300
t = 1/100

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.reset()

        self.bind()

        labels = ["Обработано", "Отказано", "P отказа"]
        self.table.setHorizontalHeaderLabels(labels)

    def bind(self):
        self.pushButton.clicked.connect(self.model)

    def reset(self):
        self._generator = Generator(UniformDistribution(8, 12), clients_number)
        self._operators = [
            Processor(
                UniformDistribution(15, 25),
                max_queue=1,
            ),
            Processor(
                UniformDistribution(30, 50),
                max_queue=1,
            ),
            Processor(
                UniformDistribution(20, 60),
                max_queue=1,
            ),
        ]

        self._computers = [
            Processor(UniformDistribution(15, 15),),
            Processor(UniformDistribution(30, 30),),
        ]

    def model(self):
        for i in range(15):
            self.reset()
            ans = self.event_mode()
            for j in range(3):
                item =  QDoubleSpinBox()
                item.lineEdit().setReadOnly(True)
                item.setMaximum(400)
                item.setValue(ans[j])
                item.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons) 
                item.setReadOnly(True)
                self.table.setCellWidget(i, j, item)

    def event_mode(self):
        refusals = 0
        processed = 0
        generated_requests = clients_number
        generator = self._generator

        generator.receivers = self._operators.copy()
        self._operators[0].receivers = [self._computers[0]]
        self._operators[1].receivers = [self._computers[0]]
        self._operators[2].receivers = [self._computers[1]]

        generator.next = generator.next_time()
        self._operators[0].next = self._operators[0].next_time()

        blocks = [
            generator,
            self._operators[0],
            self._operators[1],
            self._operators[2],
            self._computers[0],
            self._computers[1],
        ]

        while generator.num_requests >= 0:
            current_time = generator.next
            for block in blocks:
                if 0 < block.next < current_time:
                    current_time = block.next

            for block in blocks:
                # если событие наступило для этого блока
                if current_time == block.next:
                    if not isinstance(block, Processor):
                        # генератор
                        next_generator = generator.generate_request()
                        if next_generator is not None:
                            next_generator.next = \
                                current_time + next_generator.next_time()
                            processed += 1
                        else:
                            refusals += 1
                        generator.next = current_time + generator.next_time()
                    else:
                        block.process_request()
                        if block.current_queue_size == 0:
                            block.next = 0
                        else:
                            block.next = current_time + block.next_time()

        return [processed,refusals,refusals / generated_requests * 100]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())