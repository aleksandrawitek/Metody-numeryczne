#Witek Aleksandra lista 6 zad 1

import numpy as np
from scipy.misc import derivative 

x = 0.2

def f(x):
    return np.log(np.tanh(x/(x**2+1)))

#pochodne odpowiednio 1,2,3 rzedu
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.derivative.html

fx = derivative(f, x, dx=0.0001,n=1, order = 5)
fx1 = derivative(f, x, dx=0.0001,n=2, order = 5)
fx2 = derivative(f, x, dx=0.0001,n=3, order = 5)

print('Pochodna pierwszego rzędu: ', fx)
print('Pochodna drugiego rzędu: ', fx1)
print('Pochodna trzeciego rzędu: ', fx2)

#wyniki sprawdzone zostały w wolfram alpha
