#Witek Aleksandra lista4 zad6

import numpy as np 
from math import tan,cos,asin\

xi = []

for x in np.arange(0,1.5,0.001):
    y1 = tan(x) - 1
    y2 = asin(cos(x)/3)
    if ("{:.2f}".format(y1))== ("{:.2f}".format(y2)):
        xi.append(round(x,2))
print("Z ukladu rownan x wychodzi:")
print(xi[0])

    
    