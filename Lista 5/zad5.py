#Witek Aleksandra lista 5 zad 5

import numpy as np
import matplotlib.pyplot as plt 

#dane z treści zadania
x = [1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7]
y = [6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828]

w=np.polyfit(x,y,1)
w1=np.poly1d(w)
w2=np.polyfit(x,y,2)
w3=np.poly1d(w2)
x1 = np.arange(0,4.5,0.1)
y1 = w1(x1)
y2 = w3(x1)

plt.plot(x,y, 'o')
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.show()

#lepiej dopasowany jest wielomian 2 stopnia (f.kwadratowa)


