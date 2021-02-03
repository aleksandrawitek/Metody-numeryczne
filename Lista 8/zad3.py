#Witek Aleksandra lista 8 zad 3

import numpy as np
from scipy.sparse.linalg import eigsh

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.eigsh.html
#https://numpy.org/doc/stable/reference/generated/numpy.diag.html 
#tablica diagonalna

def macierz(n):

    #pomoniczo
    x=-1*np.ones(int(n)-1)                                  
    y=2*np.ones(int(n)) 

    #z dokumentacji kint, optional
    #Diagonal in question. The default is 0. Use k>0 for diagonals above the main diagonal, and k<0 for diagonals below the main diagonal.   
                                     
    A = np.diag(y) + np.diag(x, k=1) + np.diag(x, k=-1)

    #z dokumentacji ‘SM’ : Smallest (in magnitude) eigenvalues.
        
    wartosci,wektory=eigsh(A,k=5,which='SM') 

    #wydruk macierzy, aby sprawdzic czy jest poprawna#

    print("Dla n równego",n)
    print(A)          

    #Wartości i wektory własne
    print("Wartości własne:")
    print(wartosci)
    print("Wektory własne:")
    print(wektory)

#n rowne 10 i n rowne 100

macierz(10)
macierz(100)

