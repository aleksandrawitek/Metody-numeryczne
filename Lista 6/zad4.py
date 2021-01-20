#Witek Aleksandra lista 6 zad 4

from scipy.integrate import simps
import numpy as np

#oznaczenie całki
#https://eduinf.waw.pl/inf/alg/004_int/0004.php

a = -1
b = 1

#węzły
s1 = 3
s2 = 5
s3 = 7

#dla węzła s1 

def calka(a,b,s):
    x = np.linspace(a,b, num = s)
    y = np.cos(2/(np.cos(x)))
    wynik = simps(y,x)
    return print('Dla ', s, ' węzłów otrzymujemy wynik ', wynik)

calka(a,b,s1)
calka(a,b,s2)
calka(a,b,s3)

#im większa liczba wezlow tym wieksza dokladnosc wyniku
#wolfram alpha pokazuje wynik -1.36554