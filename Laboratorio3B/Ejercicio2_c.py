# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
pi=3.1416
x=np.linspace(0,4*pi,100)
y1=np.sin(3*x)*np.cos(2*x)
y2=(1/2)*np.cos(x)+(5/2)*np.cos(5*x)
texto = str('$f(x)=sin(3x)cos(2x) , g(x)=1/2cos(x)+5/2cos(5x)$')
print texto
plt.plot(x,y1,linewidth=3,color='r')
plt.plot(x,y2,linewidth=3,color='b')
plt.title("Graficas:  sin3x*cos2x   ,   1/2cosx+5/2cos5x")
plt.xlabel("x")
plt.ylabel("f(x)  ,  g(x)")
plt.legend()
plt.show()
