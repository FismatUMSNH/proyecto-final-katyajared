# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import matplotlib . pyplot as plt
import numpy as np
pi=3.1416
z = np. arange (0 , 2*pi, 0.01)
r=2-2*np.sin(z)+np.sin(z)*(np.sqrt(np.cos(z))/np.sin(z)+1.4)
x = r*np.cos(z)
y = r*np.sin(z)
plt . subplot (3 ,1 ,1)
plt . fill_between ( z , 0, x, color='red' )
plt . ylabel ( ' between x and 0 ' )
plt.axis('equal')
plt.axis('off')
plt . subplot (3 ,1 ,2)
plt . fill_between ( z , x , 1, color='yellow')
plt . ylabel ( ' between x and 1 ' )
plt.axis('equal')
plt.axis('off')
plt . subplot (3 ,1 ,3)
plt . fill_between ( z , x , y )
plt . ylabel ( ' between x and y ' )
plt.axis('equal')
plt.axis('off')
plt . xlabel ( ' z ' )
plt . show()
