#Witek Aleksandra lista4 zad7

import numpy as np

#kolejne wspolczynniki wielomianu
w = [1, complex(5,1), complex(-8,5), complex(30,-14), -84]
r = np.roots(w)
print("Pierwiastki tego równania to:")
print(r)
