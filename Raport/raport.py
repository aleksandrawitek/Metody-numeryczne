#Witek Aleksandra Raport MN

import numpy as np
from scipy.special import roots_laguerre, laguerre
import matplotlib.pyplot as plt

#zdefiniowanie funkcji podcałkowej podanej w zadaniu, zaleznej od z i t
def function(z,t):
    return t**(z-1)*np.exp(-t)

#funkcja podcałkowa bez funkcji wagowej
def function1(z,t):
    return t**(z-1)

#parametr z 
#wartosc 2.51 bo wtedy otrzymamy otrzymamy zakres od 0.5 do 2.5
#gdyby w miejscu wartości 2.51 była wartość 2.5
#to zakres kończyłby się na 2.49
z = np.arange(0.5,2.51,10**(-2))

#krok z jest stosunkowo niewielki, aby w przejrzysty sposob pokazac przebieg całki

#zakres calki
#a = 0
#b = np.Infinity
#nie bedzie konieczne definiowanie zakresu calki wynika to bezposrednio 
#ze specyfikacji scipy.special.roots_laguerre 
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.roots_laguerre.html

#ilość wezłów
#ilosc wybrana przy pomocy wolframalpha oraz obliczenia I_n dla przykładowych wartości z z zakresu [0.5,2.5],
# gdzie I_n += ai[i]*function1(z, ti[i]) dla wybranych kilku próbnych z
n = 20

#wezły oraz współczynniki kwadratury Gaussa- Laguerre'a
ti,ai = roots_laguerre(n)

#pomocnicza pusta tablica
calki = []

print("  z  ", "Obliczona całka")
for j in range (len(z)):
    I_n = 0
    for i in range (len(ai)): 
        I_n += ai[i]*function1(z[j], ti[i])
    calki.append(I_n)

for i in range (len(calki)):
    print("%1.2f %18.15f" % (z[i], calki[i]))

#wartość minimalna całki

minimum = min(calki)

#którym elementem z kolei jest wartosc minimum
k = calki.index(minimum)

print("Całka przyjmuje wartość minimalną równą ", "%18.15f" %  minimum, " dla z równego ", "%1.2f" %z[k])



#wykres
plt.plot(z,calki)
plt.xlabel('z')
plt.ylabel('g(z)')
plt.title('Wykres funkcji g(z)')
plt.plot(z[k], minimum, 'o')
plt.text(z[k], minimum + 0.05, 'minimum')
plt.show()
