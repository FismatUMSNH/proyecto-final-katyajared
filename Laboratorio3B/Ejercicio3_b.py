# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
pi=3.1416
t=np.linspace(-2*pi,2*pi,100)
x=t+2*np.sin(2*t)
y=t+2*np.cos(5*t)
texto = str('$x=t+2*sin(2t) , y=t+2*cos(5t)$')
print texto
plt.plot(t,x,linewidth=3,color='r')
plt.plot(t,y,linewidth=3,color='b')
plt.title("Graficas:  t+2sin(2t)   ,   t+2cos(5t)")
plt.xlabel("t")
plt.ylabel("x(t)  ,  y(t)")
plt.legend()
plt.show()
