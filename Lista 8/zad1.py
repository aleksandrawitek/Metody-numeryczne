#Witek Aleksandra lista 8 zad 1

import numpy as np

macierz = np.array([[-1, -4, 1], [-1, -2, -5], [5, 4, 3]])

#https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html

wartosci, wektory = np.linalg.eig(macierz)

print("Wartości własne: ", wartosci)
print("Wektory własne: ", wektory)