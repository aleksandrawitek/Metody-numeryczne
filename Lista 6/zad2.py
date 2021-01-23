#Witek Aleksandra lista 6 zad 2

import numpy as np
from scipy.interpolate import lagrange
from scipy.misc import derivative 

x = [0, 0.1, 0.2, 0.3, 0.4]
fx = [0,0.078348, 0.13891, 0.192916, 0.244981]
x1 = 0.2

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.lagrange.html

f = lagrange(x,fx)

fx1 = derivative(f, x1, dx=0.0001,n=1)

print("f'(0.2) = ", fx1)



