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

    def bind(self):
        self.pushButton.clicked.connect(self.model)

    def model(self):
        self.ev.setProperty("value", self.event_based_modelling(self.N.value()))
        self.d_t.setProperty("value", self.time_based_modelling(self.N.value(), self.t.value()))

    def event_based_modelling(self, request_count):
        self._generator = Generator(UniformDistribution(self.a.value(), self.b.value()))
        self._processor = Processor(NormalDistribution(self.m.value(), self.sigma.value()), self.P.value())
        self._generator.add_receiver(self._processor)
        generator = self._generator
        processor = self._processor

        gen_period = generator.next_time()
        proc_period = gen_period +processor.next_time()

        while processor.processed_requests < request_count:
            if gen_period <= proc_period:
                # появился новый запрос
                # добавляем оправляем его в процессор
                generator.emit_request()
                gen_period += generator.next_time()
            if gen_period >= proc_period:
                # закончилась обработка
                # обрабатываем запрос
                processor.process()

                # проверка для самого первого запроса
                if processor.current_queue_size > 0:
                    proc_period += processor.next_time()
                else:
                    proc_period = gen_period + processor.next_time()

        return processor.max_queue_size

    def time_based_modelling(self, request_count, dt):
        self._generator = Generator(UniformDistribution(self.a.value(), self.b.value()))
        self._processor = Processor(NormalDistribution(self.m.value(), self.sigma.value()), self.P.value())
        self._generator.add_receiver(self._processor)
        generator = self._generator
        processor = self._processor

        gen_period = generator.next_time()
        proc_period = gen_period
        current_time = 0
        while processor.processed_requests < request_count:
            if gen_period <= current_time:
                # появился новый запрос
                # добавляем оправляем его в процессор
                generator.emit_request()
                gen_period += generator.next_time()
            if current_time >= proc_period:
                # закончилась обработка
                # обрабатываем запрос
                processor.process()
                if processor.current_queue_size > 0:
                    proc_period += processor.next_time()
                else:
                    proc_period = gen_period + processor.next_time()

            # прибавляем дельту
            current_time += dt

        return processor.max_queue_size



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())