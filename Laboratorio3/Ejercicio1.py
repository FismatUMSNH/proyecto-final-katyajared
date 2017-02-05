#Katya Jared Amador Rodriguez
#29/11/16
import math as r
def cos(ang):
    return r.cos(r.radians(ang))
def sin(ang):
    return r.sin(r.radians(ang))
def acos(ang):
    return r.acos(r.radians(acos))
x1=float(input ("Introduzca latitud: "))
y1=float(input ("Introduzca longitud: "))
x2=float(input ("Introduzca latitud: "))
y2=float(input ("Introduzca longitud: "))
def distancia(x1,y1,x2,y2):
    a=6371.01*r.acos(r.sin(x1)*r.sin(x2)+r.cos(x1)*r.cos(x2)*r.cos(y1-y2))
    print a
distancia(x1,x2,y1,y2)
