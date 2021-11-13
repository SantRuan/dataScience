
# Aqui irei interpolar uma equação utilizando os os vetores x e y como pontos 

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')


x = [0,1,2]
y = [1,3,2]

f = interp1d(x,y)
y_hat = f(1.5)

plt.figure(figsize= (10,8))
plt.plot(x,y, "-ob")
plt.plot(1.5,y_hat,'ro')
plt.title("Interpolação linear em x = 1.5")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

