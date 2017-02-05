#Katya Jared Amador Rodriguez
#22/11/2016
num=input("Favor de ingresar los segundos que duro su viaje: ")
dia=(num/86400)
hor=(num-(dia*86400))/3600
minu=(num-(hor*3600))/60
seg=num-((hor*3600)+(minu*60))
print "El tiempo que duro su viaje fue de: ", dia, "d ", hor , "h ", minu , "m ", seg , "s"
