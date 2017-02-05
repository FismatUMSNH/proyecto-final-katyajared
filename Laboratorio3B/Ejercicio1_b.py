# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.linspace(-1,5,100)
y=2*(x**2)-(8*x)-11
texto = str('$g(x)=2^{2}-8x-11$')
print texto
plt.plot(x,y,linewidth=3,color='r')
plt.title("Grafica 2^{2}-8x-11")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.show()
