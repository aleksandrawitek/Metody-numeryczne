#Witek Aleksandra lista 5 zad 3

from scipy.interpolate import CubicSpline
import numpy as np

#dane z zadania
Re = [0.2, 2, 20, 200, 2000, 20000]
cd = [103, 13.9, 2.72, 0.8, 0.401, 0.433]

logRe=np.log(Re)
logcd=np.log(cd)
log=CubicSpline(logRe, logcd)

x1 = 5
x2 = 50
x3 = 500

print('Dla x1 = ', x1, ' wynosi ', np.exp(log(np.log(x1))))
print('Dla x2 = ', x2, ' wynosi ', np.exp(log(np.log(x2))))
print('Dla x3 = ', x3, ' wynosi ', np.exp(log(np.log(x3))))