#Witek Aleksandra lista 6 zad 8

import numpy as np
from scipy.integrate import dblquad

def f(x, y):
    return np.sin(np.pi*x)*np.sin(np.pi*(y-x))

def lim(x):
    return x

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.dblquad.html
wynik = dblquad(f, 0, 1, 0, lim)
print('Całka wynosi ', wynik[0])