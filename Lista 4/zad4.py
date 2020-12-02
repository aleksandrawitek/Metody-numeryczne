#Witek Aleksandra lista4 zad4

from scipy import optimize
import numpy as np
from math import tan,e 

def y(x):
    return [x[0]**2+e**(-1*x[0])+x[1]**3, x[0]**2+2*x[0]*x[1]-x[1]**2 + tan(x[0])]

#przyblizone wartosci odczytane z wykresu
x0 = np.array([1.2,-1.2])
x01 = np.array([-1.4,-1.3])
x02 = np.array([-0.8, -0.7])
x1 = optimize.root(y,x0)
x2 = optimize.root(y,x01)
x3 = optimize.root(y,x02)

if x1.success:
    #zapewnienie warunku ze na pewno lezy w kole s = (0,0) i r = 2
    if(-2 <= x1.x[0] <=2 and -2 <= x1.x[1] <=2):
        print(x1.x)
if x2.success:
    if(-2 <= x2.x[0] <=2 and -2 <= x2.x[1] <=2):
        print(x2.x)
if x3.success:
    if(-2 <= x3.x[0] <=2 and -2 <= x3.x[1] <=2):
        print(x3.x)