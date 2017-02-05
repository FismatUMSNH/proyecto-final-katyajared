# -*- coding: utf-8 -*-
#Katya Jared Amador Rodriguez
#06/12/16
import matplotlib . pyplot as plt
import numpy as np
pi=3.1416
z = np. arange (0 , 4*pi, 0.04)
r= 105+100*np.sin(4.5*z)
s= z-(np.cos(10*z)/10)
x = 320+r*np.cos(s)
y = -240-r*np.sin(s)
plt . subplot (3 ,1 ,1)
plt . fill_between ( z , 0, x, color='red' )
plt . ylabel ( ' between x and 0 ' )
#plt.axis('equal')
#plt.axis('off')
plt . subplot (3 ,1 ,2)
plt . fill_between ( z , x , 1, color='yellow')
plt . ylabel ( ' between x and 1 ' )
#plt.axis('equal')
#plt.axis('off')
plt . subplot (3 ,1 ,3)
plt . fill_between ( z , x , y )
plt . ylabel ( ' between x and y ' )
#plt.axis('equal')
#plt.axis('off')
plt . xlabel ( ' z ' )
plt . show()
