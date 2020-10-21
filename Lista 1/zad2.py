#Witek Aleksandra lista 1 zad2

import matplotlib.pyplot as plt

x0 = 0.1
y = [x0]
x = [0]

for n in range (1,101):
    xn = 3.5 * x0 * (1 - x0)
    x.append(n)
    y.append(xn)
    x0 = xn

plt.scatter(x,y)
plt.title("Wynik obliczen")
plt.xlabel("x")
plt.ylabel('y')
plt.show()
    
    

