#Witek Aleksandra lista 1 zad1

import matplotlib.pyplot as plt
from math import cos, sin, tan
import numpy as np

x = np.arange(0,1.5,0.000001) #przykladowe wartosci x
y = [] #pusta tablica, do ktorej bedziemy doklejac kolejne wartosci f(x)
x1 = []

for n in x:
    y.append(cos(n) - 3*sin(tan(n)-1))
    x1.append(n)

plt.plot(x1,y)
plt.title("Wykres f(x)")
plt.xlabel("x")
plt.ylabel('y')
plt.show()

