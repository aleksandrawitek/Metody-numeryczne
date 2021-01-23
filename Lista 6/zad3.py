#Witek Aleksandra lista 6 zad 3

import numpy as np
from scipy.interpolate import lagrange
from scipy.misc import derivative 

x = [-2.2, -0.3, 0.8, 1.9]
fx = [15.18, 10.962, 1.92, -2.04]
x1 = 0

f = lagrange(x,fx)

fx1 = derivative(f, x1, dx=0.0001,n=1)
fx2 = derivative(f, x1, dx=0.0001,n=2)

print("f'(0) = ", fx1)
print("f''(0) = ", fx2)

#pomocniczo do sprawdzenia w wolfram alpha
#print(f)
