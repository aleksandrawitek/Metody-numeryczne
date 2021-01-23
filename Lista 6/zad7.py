#Witek Aleksandra lista 6 zad 7 

from scipy.integrate import simps
import numpy as np
from math import exp

#oznaczenie całki
#https://eduinf.waw.pl/inf/alg/004_int/0004.php

a = -1
b = 1

def calka(a,b,s):
    x = np.linspace(a,b, num = s)
    y = (np.cos(x)-np.exp(x))/(np.sin(x))
    wynik = simps(y,x)
    return print('Obliczona całka: ', wynik)

calka(a,b,10)

#wolfram alpha pokazuje wynik -2.24659