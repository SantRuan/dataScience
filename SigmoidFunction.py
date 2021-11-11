import numpy as np
import matplotlib.pyplot as plt
import math

def sigmoid(x):
    y = 1 / (1 + math.exp(-x))
    return y

vSigX = np.linspace(-10,10,40)
vSigY = []
for i in range(len(vSigX)):
    vSigY.append(sigmoid(vSigX[i]))

vSigY = np.array(vSigY)

plt.plot(vSigX,vSigY)
plt.show()