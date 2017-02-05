#Katya Jared Amador Rodriguez
#22/11/2016
p=input("Hola, calcularemos tu indice de msas corporal, por favor ingresa tu peso en kg: ")
h=input("ingresa tu altura en m: ")
imc=p/h**h
print "Tu indice de masa corporal es: ", imc
if imc<16.0:
    print "De acuerdo a tu IMC, tienes delgadez"
elif imc>=16 and imc<=16.99:
    print "De acuerdo a tu IMC, tienes delgadez moderada"
elif imc>=17 and imc<=18.49:
    print "De acuerdo a tu IMC, tienes delgadez leve"
elif imc>=18.5 and imc<=24.99:
    print "De acuerdo a tu IMC, su peso es normal"
elif imc<=25:
    print "De acuerdo a tu IMC, tienes sobrepeso"
elif imc<=30:
    print "De acuerdo a tu IMC, tienes obesidad"
elif imc<=40:
    print "De acuerdo a tu IMC, tienes obesidad morbida"
