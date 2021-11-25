import numpy as np

M = np.array([[1,2,4], [-3,-5,6], [-1,3,-3]])
Msize = M.shape
b = np.array([[1],[2],[3]])
x = np.array([0,0,0])
print(M)
def gaussianElimination(Msize,M):
    for k in range(Msize[0] - 1):
        for i in range(k+1,Msize[0]):
             fator = M[i][k] / M[k][k]
             for j in range(k+1,Msize[0]):
                 M[i][j]= M[i][j] - fator * M[k][j]
             b[i] = b[i] - fator * b[k]
    x[Msize[0]-1]= b[Msize[0]-1] / M[Msize[0]-1][Msize[0]-1]          
    print(x)


gaussianElimination(Msize,M)