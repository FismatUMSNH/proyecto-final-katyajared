# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
pi=3.1416
t=np.linspace(0,2*pi,100)
x=np.sin(3*t)
y=np.sin(4*t)
texto = str('$x=sin(3t) , y=sin(4t)$')
print texto
plt.plot(t,x,linewidth=3,color='r')
plt.plot(t,y,linewidth=3,color='b')
plt.title("Graficas:  sin(3t)   ,   sin(4t)")
plt.xlabel("t")
plt.ylabel("x(t)  ,  y(t)")
plt.legend()
plt.show()
