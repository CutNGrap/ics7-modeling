from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import *

max_time = 10
dt = 1e-2
eps = 1e-9

def kolm_coef(matrix):
    n = len(matrix)

    koef = [[0 for _ in range(n)] for i in range(n)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            koef[i][j] += matrix[j][i]
            koef[i][i] -= matrix[i][j]
    return koef

def limit_prob(matrix):
    n = len(matrix)
    koef = kolm_coef(matrix)
    koef[0] = [1] * n

    free = [1] + [0] * (n - 1)

    return linalg.solve(koef, free)

def f(y, t, koef):
    sp = [0 for i in range(len(y))]
    for i in range(len(y)):
        for j in range(len(y)):
            sp[i] += koef[i][j] * y[j]
    return sp


def stable_time(matrix, probs):
    n = len(probs)
    time = arange(0, max_time, dt)

    start = [1] + [0] * (n - 1)
    koef = kolm_coef(matrix)
    probabilities = transpose(odeint(f, start, time, args = (koef,)))

    time_to_stable = [-1] * n

    for i in range(n):
        for j, cur_prob in enumerate(probabilities[i]):
            if abs(probs[i] - cur_prob) < eps:
                time_to_stable[i] = time[j]
                break

    return time_to_stable