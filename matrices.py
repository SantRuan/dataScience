import pandas as pd
import numpy as np



# Esta é uma função básico que cria uma matriz e insere em cada elemento um determinado valor inteiro 

def criaMATRIX():
    n = int(input('Numero de linhas: '))
    m = int(input('Numero de colunas: '))
    a = np.empty((n,m),int)

    for i in range(n):
        for j in range(m):
            a[i][j] = int(input('Digite o Valor do elemento da matriz na linha ' + ' '+ str(i) + ' e coluna ' + str(j) +' '))
    print(a)


criaMATRIX()


