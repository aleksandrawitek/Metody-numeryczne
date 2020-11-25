#Witek Aleksandra lista4 zad2

import math
print("Podaj liczbę: ")
liczba = input()
liczba = float(liczba)
tmp=[1]
for x in range(0,6):
    tmp.append(tmp[x]-(math.pow(tmp[x],5)-liczba)/(5*math.pow(tmp[x],4)))
print("Pierwiastek 5 stopnia z tej liczby to:")
print(tmp[6])