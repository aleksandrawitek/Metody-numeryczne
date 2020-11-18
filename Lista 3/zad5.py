#Witek Aleksandra lista3 zad5

import numpy as np
from numpy.linalg import cond

n1 = 5
n2 = 10
n3 = 20

m1 = []
m2 = []
m3 = []
x = []




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

for n in range(0,n3):
    for k in range (0,n3):
        x.append(round(1/(n+k+1),2))
    m3.append(x)
    x = []
m1 = np.array(m1)
m2 = np.array(m2)
m3 = np.array(m3)

def norma(A):
    y = []
    z = 0
    norma = 0
    k = len(A)
    for i in range (0, k):
        kolumna = A[:, [i]]
        for j in range (0, len(kolumna)):
            z += kolumna[j]
        z = float(z)    
        y.append(z)
        z = 0
    return max(y)

print("Norma macierzy Hilberta n = ", n1)
print(norma(m1))
print("Norma macierzy Hilberta n = ", n2)
print(norma(m2))
print("Norma macierzy Hilberta n = ", n3)
print(norma(m3))
print("Współczynnik uwarunkowania macierzy Hilberta n = ", n1)
print(cond(m1))
print("Współczynnik uwarunkowania macierzy Hilberta n = ", n2)
print(cond(m2))
print("Współczynnik uwarunkowania macierzy Hilberta n = ", n3)
print(cond(m3))





