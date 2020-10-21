#Witek Aleksandra lista 1 zad4

import numpy as np

n1 = 4
n2 = 8

m1 = []
m2 = []
m3 = []
x = []
y = []
z = []

for n in range(0,n1):
    for k in range (0,n1):
        x.append(round(1/(n+k+1),2))
    m1.append(x)
    x = []

for n in range(0,n2):
    for k in range (0,n2):
        x.append(round(1/(n+k+1),2))
    m2.append(x)
    x = []

for i in range (5,22):
    for n in range(0,i):
        for k in range (0,i):
            x.append(round(1/(n+k+1),2))
        m3.append(x)
        x = []
    m3 = np.array(m3)
    wyznacznik = np.linalg.det(m3)
    m3 = []
    z.append(wyznacznik)




print("Macierz Hilberta dla n = 4:")
print(m1)

print("Macierz Hilberta dla n = 8:")
print(m2)

print("Macierz odwrotna do macierzy Hilbelrta dla n=4")
print(np.linalg.inv(m1))

print("Macierz odwrotna do macierzy Hilbelrta dla n=8")
print(np.linalg.inv(m2))

print("Kolejne wyznaczniki macierzy Hilberta dla 5=<n<=21:")
print(z)
