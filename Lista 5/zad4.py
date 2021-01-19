#Witek Aleksandra lista 5 zad 4
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

#dane z zadania
Re = [0.2, 2, 20, 200, 2000, 20000]
cd = [103, 13.9, 2.72, 0.8, 0.401, 0.433]

plt.plot(Re,cd, 'o')

logRe=np.log(Re)
logcd=np.log(cd)

w = lagrange (logRe, logcd)

Re1=np.arange(0.2,20000,0.1)

x1 = 5
x2 = 50
x3 = 500

y1 = np.exp(w(np.log(x1)))
y2 = np.exp(w(np.log(x2)))
y3 = np.exp(w(np.log(x3)))
print('Dla x1 = ', x1, ' wynosi ', y1)
print('Dla x2 = ', x2, ' wynosi ', y2)
print('Dla x3 = ', x3, ' wynosi ', y3)

plt.plot([x1,x2,x3], [y1,y2,y3])
plt.plot(Re1, np.exp(w(np.log(Re1))))
plt.xscale('log')
plt.yscale('log')
plt.show()