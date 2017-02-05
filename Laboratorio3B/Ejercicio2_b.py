# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.linspace(0,2,100)
y1=x*np.exp(abs(-3*x))
y2=np.exp(-3*x)*(1-3*x)
texto = str('$f(x)=xexp(-3x) , g(x)=exp(−3x)(1 − 3x)$')
print texto
plt.plot(x,y1,linewidth=3,color='r')
plt.plot(x,y2,linewidth=3,color='b')
#plt.title("Graficas:  xexp(-3x)   ,   exp(−3x)(1 − 3x)")
plt.xlabel("x")
plt.ylabel("f(x)  ,  g(x)")
plt.legend()
plt.show()
