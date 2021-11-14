# Função Bissesão

import numpy as np
import math
import matplotlib.pyplot as plt



def f(x):
    y = x**2 + 1
    return y

def bissecao(x1, xu, es, imax, xr, ea):
    iter=0
    while ea> es:
        print(xold = xr) 
        xr = (x1 + xu) / 2
        iter = iter + 1
        if  f(x1) * f(xr):
            x_bisect = xr
        if f(x1) * f(xr) < 0:
            xu = xr
        elif f(x1) * f(xr) > 0:
            x1 = xr
        else:
            ea = 0
        if ea < es or iter >= imax:
            break


print(bissecao(0.5,2, 0.05, 30, 1.75,1))



