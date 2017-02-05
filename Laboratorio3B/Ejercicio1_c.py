# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.linspace(-1,5,100)
y=x*np.exp(-2*x)
texto = str('$f(x)=x*exp{-2x}$')
print texto
plt.plot(x,y,linewidth=3,color='r')
plt.title("Grafica x*exp{-2x}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
