#Witek Aleksandra lista 8 zad 2

import numpy as np
from scipy.linalg import hilbert

#macierz Hilberta

macierz = hilbert(6)


#https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html

wartosci, wektory = np.linalg.eig(macierz)

print("Wartości własne: ", wartosci)
print("Wektory własne: ", wektory)