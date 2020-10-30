#Witek Aleksandra lista2 zad5

from math import exp

n = 2
I = 1
tab = [1] #pomocnicza tablica

while n <= 20:
    y = exp(1) - ((n+1)*I)
    tab.append(y)
    I = y
    n +=1

print("Kolejne wartości całek: ")
print(tab)
    
