#Witek Aleksandra lista 7 zad 1

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

y=[2,2.5,3,3.5]


def f(t,y):
    return np.sin(t*y)

for i in y:
    equation = solve_ivp(f, [0,6], [i])
    plt.plot(equation.t, equation.y[0],'o-')

plt.legend(['y = 2', 'y = 2.5', 'y = 3', 'y = 3.5'])
plt.show()