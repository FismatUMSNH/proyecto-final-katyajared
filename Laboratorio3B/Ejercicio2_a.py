# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
pi=3.1416
x=np.linspace(0,4*pi,100)
y1=np.cos(2*x)+np.sin(3*x)
y2=abs(-2)*np.sin(2*x)+3*np.cos(3*x)
texto = str('$s(x)=cos(2x)+sin(3x) , v(x)=2sin(2x)+3cos(3x)$')
print texto
plt.plot(x,y1,linewidth=3,color='r')
plt.plot(x,y2,linewidth=3,color='b')
plt.title("Graficas:  cos2x+sin3x   ,   -2sin2x+3cos3x")
plt.xlabel("x")
plt.ylabel("s(x)  ,  v(x)")
plt.legend()
plt.show()
