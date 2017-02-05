# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.linspace(0,24,100)
y=np.exp(-0.1*x)*(np.sin(2*x))
texto = str('$h(x)=exp{-0.1*x}*(sen(2*x))$')
print texto
plt.plot(x,y,linewidth=3,color='r')
plt.title("Grafica exp{-0.1*x}*sen(2*x)")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.legend()
plt.show()
