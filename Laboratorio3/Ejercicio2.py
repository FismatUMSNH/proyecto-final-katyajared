#Katya Jared Amador Rodriguez
#29/11/16
def sumar_digitos (n):
    resultado = 0
    if n>999:
      while n > 9:
          resultado = resultado + n % 10
          n = n / 10
      return resultado + n
