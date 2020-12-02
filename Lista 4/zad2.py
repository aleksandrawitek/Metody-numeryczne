#Witek Aleksandra lista4 zad2

import math
print("Podaj liczbę: ")
liczba = input()
liczba = float(liczba)
y =[1]
for x in range(0,6):
    z = y[x]-(math.pow(y[x],5)-liczba)/(5*math.pow(y[x],4))
    y.append(z)
print("Pierwiastek 5 stopnia z tej liczby to:")
print(y[6])