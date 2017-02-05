# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
pi=3.1416
t=np.linspace(0,2*pi,100)
x=(np.cos(t))**3
y=(np.sin(t))**3
texto = str('$x=cos^3(t) , y=sin^3(t)$')
print texto
plt.plot(t,x,linewidth=3,color='r')
plt.plot(t,y,linewidth=3,color='b')
plt.title("Graficas:  cos^3(t)   ,   sin^3(t)")
plt.xlabel("t")
plt.ylabel("x(t)  ,  y(t)")
plt.legend()
plt.show()
