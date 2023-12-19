from numpy import random as nr
from numpy.random import gamma, normal
import random
import numpy as np
import math

class Generator:
    def __init__(self, generator, count):
        self._generator = generator
        self.receivers = []
        self.num_requests = count
        self.next = 0 

    def next_time(self):
        return self._generator.generate()
    
    def generate_request(self):
        self.num_requests -= 1
        for receiver in self.receivers:
            if receiver.receive_request():
                return receiver
        return None

class Processor(Generator):
    def __init__(self, generator, max_queue=-1):
        self._generator = generator
        self.current_queue_size = 0
        self.max_queue_size = max_queue
        self.processed_requests = 0
        self.received_requests  = 0
        self.next = 0

# обрабатываем запрос, если они есть
    def process_request(self):
        if self.current_queue_size > 0:
            self.processed_requests += 1
            self.current_queue_size -= 1
            #self.emit_request()
    
# добавляем реквест в очередь
    def receive_request(self):
        # print(self.max_queue_size, self.current_queue_size ) 
        if self.max_queue_size == -1 or self.max_queue_size > self.current_queue_size:
            self.current_queue_size += 1
            self.received_requests += 1
            return True
        return False

    def next_time(self):
        return self._generator.generate()

class UniformDistribution:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random.random()
    
class NormalDistribution:
    def __init__(self, m: float, d: float):
        self.d = d
        self.m = m

    def generate(self):
        return random.normalvariate(self.m, math.sqrt(self.d))



class ErlangDistribution:
    def __init__(self, k, l):
        self.l = l
        self.k = k

    def _erlang_pdf(self, x):
        if x < 0: 
            return 0
        return (pow(self.l, self.k+1) * 
                pow(x, self.k) * 
                np.exp(- self.l * x) / 
                math.factorial(self.k))
    def _erlang_cdf(self, x):
        if x < 0:
            return 0
        return 1 - (1 + self.l * x) * np.exp( - self.l * x)


    def generate(self):
        return gamma(self.k, self.l)
