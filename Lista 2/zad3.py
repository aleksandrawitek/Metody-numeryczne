#Witek Aleksandra lista2 za3

from math import sqrt
n1 = 2
n2 = 2

tab1 = [] #pomocnicza tablica
tab2 = []



while n1<= 24:
    x = 2**(-1*n1)
    y = sqrt((x**2)+1) - 1
    tab1.append(y)
    n1 += 2

while n2<= 24:
    x = 2**(-1*n2)
    y = x**2/(sqrt((x**2)+1)+1)
    tab2.append(y)
    n2 += 2

print("Kolejne wyniki metody 1:")
print(tab1)
print("Kolejne wyniki metody 2:")
print(tab2) #dokładniejsze są wyniki metody 2