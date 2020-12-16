#Witek Aleksandra lista 5 zad 1

from scipy.interpolate import lagrange

h = [0,3,6]
ro = [1.225, 0.905,0.652]

funkcja = lagrange(h,ro)

print(funkcja)
