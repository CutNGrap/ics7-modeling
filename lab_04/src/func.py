from numpy import random as nr
from numpy.random import gamma, normal
import random
import numpy as np
import math

class Generator:
    def __init__(self, generator):
        self._generator = generator
        self._receivers = set()

    def add_receiver(self, receiver):
        self._receivers.add(receiver)

    def remove_receiver(self, receiver):
        try:
            self._receivers.remove(receiver)
        except KeyError:
            pass

    def next_time(self):
        return self._generator.generate()

    def emit_request(self):
        for receiver in self._receivers:
            receiver.receive_request()

class Processor(Generator):
    def __init__(self, generator, reenter_probability=0):
        super().__init__(generator)
        self.current_queue_size = 0
        self.max_queue_size = 0
        self.processed_requests = 0
        self.reenter_probability = reenter_probability
        self.reentered_requests = 0

    def process(self):
        if self.current_queue_size > 0:
            self.processed_requests += 1
            self.current_queue_size -= 1
            self.emit_request()
            if nr.random_sample() <= self.reenter_probability:
                self.reentered_requests += 1
                self.receive_request()

    def receive_request(self):
        self.current_queue_size += 1
        if self.current_queue_size > self.max_queue_size:
            self.max_queue_size = self.current_queue_size

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
