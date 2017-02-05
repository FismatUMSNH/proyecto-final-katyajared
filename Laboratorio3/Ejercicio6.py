def calcular(n):
  if(n<0):
    print "El numero que ingreso es negativo"
  else:
      if (n<=2):
          edad=n*10.5
          print "Su equivalente en anos perro es igual a ",edad
      else:
          edad=((n-2)*4)+21
          return edad

  #x=float(input())
  #if x<0:
    #  print "El numero que ingreso es negativo"
  #else:
    #  if x<=2:
    #      edad=x*10.5
    #      print edad

    #      edad=((x-2)*4)+21
