# Função Bissesão

import numpy as np
import math
import matplotlib.pyplot as plt



def f(x):
    y = x**2 + 1
    return y

def bissecao(x1, xu, es, imax, xr, ea):
    iter=0
    f1 = f(x1)
    while ea> es:
        xold = xr
        xr = (x1 + xu) / 2
        print(xr)
        fr = f(xr)
        iter = iter + 1
        test = f1*fr
        if  xr != 0:
            ea = (abs(xr - xold)/xr) * 100
        if test < 0:
            xu = xr
        elif test > 0:
            x1 = xr
            f1 = fr
        else:
            ea = 0
        return xr


print(bissecao(0.5,2, 0.05, 30, 1.75,1))




