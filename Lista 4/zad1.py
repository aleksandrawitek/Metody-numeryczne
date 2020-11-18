#Witek Aleksandra lista4 zad1

from scipy import optimize

def f(x):
    return (2*(x**4)+24*(x**3)+61*(x**2)-16*x+1)
pierwiastek = optimize.ridder(f,-9,-8)
#pierwszy pierwiastek
print(pierwiastek)

