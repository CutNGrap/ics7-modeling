from math import *
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(rang, sp_an,  label = "Аналит", c = 'b')
    plot.plot(rang, sp_ei, label="Эйлер", c = 'g')
    plot.plot(rang, sp[0],  label="Пикар 1", c = 'r')
    plot.plot(rang, sp[1],  label="Пикар 2", c = 'magenta')
    plot.plot(rang, sp[2],  label="Пикар 3", c = 'black')
    plot.plot(rang, sp[3],  label="Пикар 4", c = 'cyan')
    plot.legend()
    plot.grid()
    plt.ylabel("x")
    plt.xlabel("u")
    plt.show()