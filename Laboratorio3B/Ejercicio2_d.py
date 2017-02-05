# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
pi=3.1416
x=np.linspace(0,2*pi,100)
y1=1+(2*np.sin(x))*(np.cos(x))
y2=1+(2*np.sin(x))*(np.sin(x))
texto = str('$s(x)=1+2sin(x)*cos(x) , v(x)=1+2sin(x)*sin(x)$')
print texto
plt.plot(x,y1,linewidth=3,color='r')
plt.plot(x,y2,linewidth=3,color='b')
plt.title("Graficas:  1+2sinx*cosx   ,   1+2sinx*sinx")
plt.xlabel("x")
plt.ylabel("s(x)  ,  v(x)")
plt.legend()
plt.show()
