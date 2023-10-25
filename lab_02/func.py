from numpy import *
import matplotlib.pyplot as plt
from scipy.integrate import *

max_time = 10
dt = 1e-2
eps = 1e-6

def kolm_coef(matrix):
    n = len(matrix)

    koef = [[0 for _ in range(n)] for i in range(n)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                koef[i][j] = matrix[j][i]
                koef[i][i] -= matrix[i][j]
    koef[0] = [1] * n
    return koef

def limit_prob(matrix):
    n = len(matrix)
    koef = kolm_coef(matrix)

    return linalg.solve(koef, [0 if i != 0 else 1 for i in range(n)])

def f(y, t, koef):
    sp = [0 for i in range(len(y))]
    for i in range(len(y)):
        for j in range(len(y)):
            sp[i] += koef[i][j] * y[j]
    return sp

def integ(matrix, t):
    n = len(matrix)

    start_p = [0] * n
    start_p[0] = 1
    koef = kolm_coef(matrix)
    return odeint(f, start_p, t, args = (koef,))

def stable_time(matrix, probs):
    n = len(probs)
    time = arange(0, max_time, dt)
    start = [1] + [0] * (n - 1)

    koef = kolm_coef(matrix)

    probabilities = odeint(f,start,time, args=(koef,))

    # plt.plot(time,probabilities[0])
    # plt.show()
    time_to_stable = [0 for _ in range(n)] 

    for i in range(n):
        for j in range(n):
            if abs(probs[i] - probabilities[j][i]) < eps:
                time_to_stable[i] = time[i]
                break

            if i == len(probabilities) - 1:
                time_to_stable[i] = -1

    return time_to_stable
