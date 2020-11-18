#Witek Aleksandra lista3 zad4

import numpy as np

def Gauss(A,B):
    n=len(A) #kolumny
    for k in range(n):
        i_max = abs(A[k:,k]).argmax() + k
        if i_max != k: #wiersze
            A[[k,i_max]] = A[[i_max, k]]
            B[[k,i_max]] = B[[i_max, k]]
        for row in range(k+1,n):
            f = A[row,k]/A[k,k]
            A[row, k:] = A[row, k:] - f*A[k, k:]
            B[row] = B[row] - f*B[k]

    x = np.zeros(n) #pomocniczo
    for k in range(n-1, -1,-1):
        x[k] = (B[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    return x
#macierze z zadania numer 3
A = np.array([[0,0,2,1,2],[0,1,0,2,-1], [1,2,0,-2,0], [0,0,0,-1,1], [0,1,-1,1,-1]])
B = np.array([[1],[1],[-4],[-2],[-1]])
print(Gauss(A,B))
