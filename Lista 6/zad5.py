#Witek Aleksandra lista 6 zad 5

from scipy.integrate import quad
import numpy as np

def f(x,t):
    return 1/np.sqrt(1-np.sin(t/2)**2*np.sin(x)**2)

#zamiana stopni na radiany    

alfa1 = np.radians(15)
alfa2 = np.radians(30)
alfa3 = np.radians(45)
#kąt testowy
alfa4 = np.radians(0)

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html

h1 = quad(f, 0, np.pi/2, args =(alfa1,))
h2 = quad(f, 0, np.pi/2, args =(alfa2,))
h3 = quad(f, 0, np.pi/2, args =(alfa3,))
h4 = quad(f, 0, np.pi/2, args =(alfa4,))
print('h(15) = ', h1[0])
print('h(30) = ', h2[0])
print('h(45) = ', h3[0])
print("Wartości testowe")
print('h(0) = ', h4[0])
print('Wartość pi/2', np.pi/2)
