#Witek Aleksandra lista 6 zad 6

import numpy as np
from scipy.special import roots_legendre


def f(x):
    return np.log(x)/(x**2-2*x+2)

#pomocnicze zmienne
w = 0
w1 = 0      

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.roots_legendre.html

#współczynniki
a = 1
b = np.pi

#dla dwóch wezłów
x1,a1 = roots_legendre(2)
for i in range(len(a1)):
    w += (b-a)/2*a1[i] * f((b+a)/2 + (b-a)/2*x1[i])

#dla czterech wezłów
x2, a2 = roots_legendre(4)
for i in range(len(a2)):
    w1 += (b-a)/2*a2[i] * f((b+a)/2 + (b-a)/2*x2[i])

print("Dla dwóch węzłów: ", w)
print("Dla czterech węzłów:", w1)

#wartosc z wolfram alpha 0.584943