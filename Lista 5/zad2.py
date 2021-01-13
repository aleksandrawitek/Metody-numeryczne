#Witek Aleksandra lista 5 zad 2

import numpy as np
from scipy import optimize
from sympy import *

x=[1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
y=[-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334]


#przyblizenie wielomianem 
#6 stopien jest dokladny, odczytane z zalaczonego wykresu
w=np.polyfit(x,y,6)

#konstrukcja wielomianu https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html
w1=np.poly1d(w)

#zakres wartosci o xmin do xmax
x1=np.arange(1,3,0.1)
y1=w1(x1)

# Znajdowanie pierwiastkow https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.ridder.html
xmin=1
n=1
for xmax in np.arange(1,3,0.001):
    if np.sign(w1(xmin))!=np.sign(w1(xmax)):
        root=optimize.ridder(w1,xmin,xmax)
        tekst = 'Pierwiastek nr ' + str(n)
        print(tekst)
        print(root)
        n+=1
    xmin=xmax

#Pochodna w punkcie
tekst2 = 'Pochodna w punkcie 2.1 wynosi'
fprim = np.poly1d(w1)
fprim2 = fprim.deriv()
print(tekst2)
print(fprim2(2.1))