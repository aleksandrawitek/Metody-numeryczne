#Witek Aleksandra lista 1 zad3

import numpy as np

A = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
B = np.array([[4, 2, 0], [2, 5, 2], [0, 2, 4]])
w = np.array([1, -2, 3])

AB = A.dot(B) #mnozenie macierzy
print('AB = ', AB)

Aw = A.dot(w)
print('Aw = ', Aw)

BAw = B.dot(Aw)
print('B(Aw) = ', BAw)

wa = np.linalg.det(A) #wyznacznik macierzy
print("Wyznacznik macierzy A: ", wa)

wb = np.linalg.det(B)
print("Wyznacznik macierzy B: ", wb)

A1 = np.linalg.inv(A) #macierz odwrotna
print("Macierz odwrotna A: ", A1)

B1 = np.linalg.inv(B)
print("Macierz odwrotna B: ", B1)





