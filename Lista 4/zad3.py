#Witek Aleksandra lista3 zad3

from math import log
import numpy as np

u = 2510
M0 = 2.8 * 10**6
m = 13.3 * 10**3
g = 9.81
v = 335

for t in np.arange(0.0, 1000, 0.001):
    v1 = u * log(M0 / (M0 - m * t)) - (g * t)
    if (round(v1) == v):
        break
print("Rakieta osiagnie predkosc dzwieku w t rownym")
print(t)
