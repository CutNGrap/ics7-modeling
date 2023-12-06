from numpy import *
import matplotlib.pyplot as plt
import time

max_time = 10
dt = 1e-2
eps = 1e-9

class AlgorithmGenerator:
    def __init__(self, n_min: int, n_max: int):
        self.n_min: int = n_min
        self.n_max: int = n_max

    def get_random_numbers(self, n, seed = -1):
        if seed == -1:
            seed = round(time.time())
        a = 16807
        m = 0x7fffffff

        numbers = []
        for i in range(n):
            seed = seed * a % m
            numbers.append(seed % (self.n_max - self.n_min) + self.n_min)

        return numbers
    
class TableGenerator:
    def __init__(self, file_path):
        self.table = open(file_path, 'r')

    def get_random_numbers(self, digits, total):
        s = []
        divider = pow(10, digits)
        while total:
            item = self.table.read(6)
            if item == '':
                self.table.seek(0)
                item = self.table.read(6)
            item = int(item[:5])
            while item:
                if total:
                    random = item % divider

                    if len(str(random)) == digits:
                        s.append(random)
                        total -= 1

                    item //= 10
                else:
                    return s

        return s

    def __del__(self):
        self.table.close()
        
def calc_chi(arr, n, start, end): 
    tab = [0 for i in range(end - start + 1)]
    for i in arr:
        tab[i - start] += 1
    s = 0
    for i in tab:
        s += i*i
    return s * (end-start + 1) / n - n, tab
