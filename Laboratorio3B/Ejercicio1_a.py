# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.linspace(-6,2,100)
y=5-(4*x)-(x**2)
texto = str('$f(x)=5−4x−x^{2}$')
print texto
plt.plot(x,y,linewidth=3,color='r')
#Esta parte me marca error al querer mostrarlo
#plt.title(r"Grafico de $f(x)=5−4x−x^{2}$")
plt.title("Grafica")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
