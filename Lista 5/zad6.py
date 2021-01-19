#Witek Aleksandra lista 5 zad 6

from scipy.optimize import curve_fit

#dane z zadania 

h = [0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150]
g = [1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741]
h1 = 10.5

def f(x,a,b,c):
    #ax^2 + bx + c
    return a*x**2+b*x+c 

parametr,m=curve_fit(f,h,g)     
# m to macierz kowariancji

print("Wartość ciśnienia na wysokości h=10.5 wynosi", h1**2 * parametr[0] + h1 * parametr[1] + parametr[2])