#Witek Aleksandra lista4 zad2

import numpy as np
from scipy import optimize

print("Z jakiej liczby chcesz obliczyć pierwiastek")
x = input()
x = float(x)
n = 5
y = lambda x,a: x**n-a
dy = lambda  x,a: n*x**(n-1)
root = optimize.newton(y, 3, fprime=dy, args=(x,))

print("Pierwiastek %.0f-stopnia z %d jest równy %s" % (n,x,root))