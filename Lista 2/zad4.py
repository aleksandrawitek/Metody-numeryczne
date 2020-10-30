#Witek Aleksandra lista2 zad4

from math import sqrt

print("Podaj x:")
x = input()
x = float(x)
a = sqrt((x**4)+4) - 2
b = x**4/(sqrt((x**4)+4)+2)
print(a)
print(b)
print("Róznica między metodami")
print(b-a)