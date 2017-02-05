#import  csv
#    open ( 'D:\ipython\Laboratorio4a\periodica.csv','rb' ) as csvfile :
#    lector  =  csv.DictReader ( csvfile )
#    for  fila  in lector :
#        print ( fila [ 'NO_ATOMICO' ],  fila [ 'SIMBOLO' ],  fila [ 'NOMBRE' ],  fila [ 'MASA_ATOMICA' ])

# -*- coding: utf-8 -*-
#!/usr/bin/env python
a=input("Bienvenido a la Tabla Periodica, aqui podra encontrar informacion sobre los elementos de la tabla periodica, para eso puede ingresar el nombre o numero atomico del elemento que guste. Si usted ingresara el numero atomico, favor de oprimir un 0; Si usted ingresara el nombre, favor de oprimir un 1: ")
if (a==0):
    num=input("Ingrese el numero atomico: ")
    if (num==1):
        print "\nNombre: Hidrogeno \nSimbolo: H \nMasa Atomica: 1.0079"
    if (num==2):
        print "\nNombre: Helio \nSimbolo: He \nMasa Atomica: 4.0026"
    if (num==3):
        print "\nNombre: Litio \nSimbolo: Li \nMasa Atomica: 6.941"
    if (num==4):
        print "\nNombre: Berilio \nSimbolo: Be \nMasa Atomica: 9.0121"
    if (num==5):
        print "\nNombre: Boro  \nSimbolo: B \nMasa Atomica: 10.811"
    if (num==6):
        print "\nNombre: Carbono \nSimbolo: C \nMasa Atomica: 12.0107"
    if (num==7):
        print "\nNombre: Nitrogeno \nSimbolo: N \nMasa Atomica: 14.0067"
    if (num==8):
        print "\nNombre: Oxigeno \nSimbolo: O \nMasa Atomica: 15.9994"
    if (num==9):
        print "\nNombre: Fluor \nSimbolo: F \nMasa Atomica: 18.9984"
    if (num==10):
        print "\nNombre: Neon \nSimbolo: Ne \nMasa Atomica: 20.1797"
    if (num==11):
        print "\nNombre: Sodio \nSimbolo: Na \nMasa Atomica: 22.9897"
    if (num==12):
        print "\nNombre: Magnesio \nSimbolo: Mg \nMasa Atomica: 24.3050"
    if (num==13):
        print "\nNombre: Aluminio \nSimbolo: Al \nMasa Atomica: 26.9815"
    if (num==14):
        print "\nNombre: Silicio \nSimbolo: Si \nMasa Atomica: 28.0855"
    if (num==15):
        print "\nNombre: Fosforo \nSimbolo: P \nMasa Atomica: 30.9769"
    if (num==16):
        print "\nNombre: Azufre \nSimbolo: S \nMasa Atomica: 32.065"
    if (num==17):
        print "\nNombre: Cloro \nSimbolo: Cl \nMasa Atomica: 35.453"
    if (num==18):
        print "\nNombre: Argon \nSimbolo: Ar \nMasa Atomica: 39.948"
    if (num==19):
        print "\nNombre: Potasio \nSimbolo: K \nMasa Atomica: 39.0983"
    if (num==20):
        print "\nNombre: Calcio \nSimbolo: Ca \nMasa Atomica: 40.078"
    if (num==21):
        print "\nNombre: Escandio \nSimbolo: Sc \nMasa Atomica: 44.9559"
    if (num==22):
        print "\nNombre: Titanio \nSimbolo: Ti \nMasa Atomica: 47.867"
    if (num==23):
        print "\nNombre: Vanadio \nSimbolo: V \nMasa Atomica: 50.9415"
    if (num==24):
        print "\nNombre: Cromo \nSimbolo: Cr \nMasa Atomica: 51.9962"
    if (num==25):
        print "\nNombre: Manganeso \nSimbolo: Mn \nMasa Atomica: 54.9380"
    if (num==26):
        print "\nNombre: Hierro \nSimbolo: Fe \nMasa Atomica: 55.845"
    if (num==27):
        print "\nNombre: Cobalto \nSimbolo: Co \nMasa Atomica: 58.9331"
    if (num==28):
        print "\nNombre: Niquel \nSimbolo: Ni \nMasa Atomica: 58.6934"
    if (num==29):
        print "\nNombre: Cobre \nSimbolo: Cu \nMasa Atomica: 63.546"
    if (num==30):
        print "\nNombre: Zinc \nSimbolo: Zn \nMasa Atomica: 65.38"
    if (num==31):
        print "\nNombre: Galio \nSimbolo: Ga \nMasa Atomica: 69.723"
    if (num==32):
        print "\nNombre: Germanio \nSimbolo: Ge \nMasa Atomica: 72.64"
    if (num==33):
        print "\nNombre: Arsenico \nSimbolo: As \nMasa Atomica: 74.9216"
    if (num==34):
        print "\nNombre: Selenio \nSimbolo: Se \nMasa Atomica: 78.96"
    if (num==35):
        print "\nNombre: Bromo \nSimbolo: Br \nMasa Atomica: 79.904"
    if (num==36):
        print "\nNombre: Kripton \nSimbolo: Kr \nMasa Atomica: 83.798"
    if (num==37):
        print "\nNombre: Rubidio \nSimbolo: Rb \nMasa Atomica: 85.4678"
    if (num==38):
        print "\nNombre: Estroncio \nSimbolo: Sr \nMasa Atomica: 87.62"
    if (num==39):
        print "\nNombre: Itrio \nSimbolo: Y \nMasa Atomica: 88.9058"
    if (num==40):
        print "\nNombre: Zirconio \nSimbolo: Zr \nMasa Atomica: 91.224"
    if (num==41):
        print "\nNombre: Niobio \nSimbolo: Nb \nMasa Atomica: 92.9063"
    if (num==42):
        print "\nNombre: Molibdeno \nSimbolo: Mo \nMasa Atomica: 95.96"
    if (num==43):
        print "\nNombre: Tecnecio \nSimbolo: Tc \nMasa Atomica: 98"
    if (num==44):
        print "\nNombre: Rutenio \nSimbolo: Ru \nMasa Atomica: 101.07"
    if (num==45):
        print "\nNombre: Rodio \nSimbolo: Rh \nMasa Atomica: 102.9055"
    if (num==46):
        print "\nNombre: Paladio \nSimbolo: Pd \nMasa Atomica: 106.42"
    if (num==47):
        print "\nNombre: Plata \nSimbolo: Ag \nMasa Atomica: 107.8682"
    if (num==48):
        print "\nNombre: Cadmio \nSimbolo: Cd \nMasa Atomica: 112.441"
    if (num==49):
        print "\nNombre: Indio \nSimbolo: In \nMasa Atomica: 114.818"
    if (num==50):
        print "\nNombre: Estano \nSimbolo: Sn \nMasa Atomica: 118.710"
    if (num==51):
        print "\nNombre: Antimonio \nSimbolo: Sb \nMasa Atomica: 121.760"
    if (num==52):
        print "\nNombre: Telurio \nSimbolo: Te \nMasa Atomica: 127.60"
    if (num==53):
        print "\nNombre: Yodo \nSimbolo: I \nMasa Atomica: 126.9044"
    if (num==54):
        print "\nNombre: Xenon \nSimbolo: Xe \nMasa Atomica: 131.293"
    if (num==55):
        print "\nNombre: Cesio \nSimbolo: Cs \nMasa Atomica: 132.9054"
    if (num==56):
        print "\nNombre: Bario \nSimbolo: Ba \nMasa Atomica: 137.327"
    if (num==57):
        print "\nNombre: Lantano \nSimbolo: La \nMasa Atomica: 138.9054"
    if (num==58):
        print "\nNombre: Cerio \nSimbolo: Ce \nMasa Atomica: 140.116"
    if (num==59):
        print "\nNombre: Praseodimio \nSimbolo: Pr \nMasa Atomica: 140.9076"
    if (num==60):
        print "\nNombre: Neodimio \nSimbolo: Nd \nMasa Atomica: 144.242"
    if (num==61):
        print "\nNombre: Prometio \nSimbolo: Pm \nMasa Atomica: 145"
    if (num==62):
        print "\nNombre: Samario \nSimbolo: Sm \nMasa Atomica: 150.36"
    if (num==63):
        print "\nNombre: Europio \nSimbolo: Eu \nMasa Atomica: 151.964"
    if (num==64):
        print "\nNombre: Gadolinio \nSimbolo: Gd \nMasa Atomica: 157.25"
    if (num==65):
        print "\nNombre: Terbio \nSimbolo: Tb \nMasa Atomica: 158.9253"
    if (num==66):
        print "\nNombre: Disprosio \nSimbolo: Dy \nMasa Atomica: 162.500"
    if (num==67):
        print "\nNombre: Holmio \nSimbolo: Ho \nMasa Atomica: 164.9303"
    if (num==68):
        print "\nNombre: Erbio \nSimbolo: Er \nMasa Atomica: 167.259"
    if (num==69):
        print "\nNombre: Tulio \nSimbolo: Tm \nMasa Atomica: 168.9342"
    if (num==70):
        print "\nNombre: Iterbio \nSimbolo: Yb \nMasa Atomica: 173.054"
    if (num==71):
        print "\nNombre: Lutecio \nSimbolo: Lu \nMasa Atomica: 174.9668"
    if (num==72):
        print "\nNombre: Hafnio \nSimbolo: Hf \nMasa Atomica: 178.49"
    if (num==73):
        print "\nNombre: Tantalio \nSimbolo: Ta \nMasa Atomica: 180.9478"
    if (num==74):
        print "\nNombre: Wolframio \nSimbolo: W \nMasa Atomica: 183.84"
    if (num==75):
        print "\nNombre: Renio \nSimbolo: Re \nMasa Atomica: 186.207"
    if (num==76):
        print "\nNombre: Osmio \nSimbolo: Os \nMasa Atomica: 190.23"
    if (num==77):
        print "\nNombre: Iridio \nSimbolo: Ir \nMasa Atomica: 192.217"
    if (num==78):
        print "\nNombre: Platino \nSimbolo: Pt \nMasa Atomica: 195.084"
    if (num==79):
        print "\nNombre: Oro \nSimbolo: Au \nMasa Atomica: 196.9665"
    if (num==80):
        print "\nNombre: Mercurio \nSimbolo: Hg \nMasa Atomica: 200.59"
    if (num==81):
        print "\nNombre: Talio \nSimbolo: Tl \nMasa Atomica: 204.3833"
    if (num==82):
        print "\nNombre: Plomo \nSimbolo: Pb \nMasa Atomica: 207.2"
    if (num==83):
        print "\nNombre: Bismuto \nSimbolo: Bi \nMasa Atomica: 208.9804"
    if (num==84):
        print "\nNombre: Polonio \nSimbolo: Po \nMasa Atomica: 210"
    if (num==85):
        print "\nNombre: Astato \nSimbolo: At \nMasa Atomica: 210"
    if (num==86):
        print "\nNombre: Radon \nSimbolo: Rn \nMasa Atomica: 220"
    if (num==87):
        print "\nNombre: Francio \nSimbolo: Fr \nMasa Atomica: 223"
    if (num==88):
        print "\nNombre: Radio \nSimbolo: Ra \nMasa Atomica: 226"
    if (num==89):
        print "\nNombre: Actinio \nSimbolo: Ac \nMasa Atomica: 227"
    if (num==90):
        print "\nNombre: Torio \nSimbolo: Th \nMasa Atomica: 232.0380"
    if (num==91):
        print "\nNombre: Protactinio \nSimbolo: Pa \nMasa Atomica: 231.0380"
    if (num==92):
        print "\nNombre: Uranio \nSimbolo: U \nMasa Atomica: 238.0289"
    if (num==93):
        print "\nNombre: Neptunio \nSimbolo: Np \nMasa Atomica: 237"
    if (num==94):
        print "\nNombre: Plutonio \nSimbolo: Pu \nMasa Atomica: 244"
    if (num==95):
        print "\nNombre: Americio \nSimbolo: Am \nMasa Atomica: 243"
    if (num==96):
        print "\nNombre: Curio \nSimbolo: Cm \nMasa Atomica: 247"
    if (num==97):
        print "\nNombre: Berkelio \nSimbolo: Bk \nMasa Atomica: 247"
    if (num==98):
        print "\nNombre: Californio \nSimbolo: Cf \nMasa Atomica: 251"
    if (num==99):
        print "\nNombre: Einstenio \nSimbolo: Es \nMasa Atomica: 252"
    if (num==100):
        print "\nNombre: Fermio \nSimbolo: Fm \nMasa Atomica: 257"
    if (num==101):
        print "\nNombre: Mendelevio \nSimbolo: Md \nMasa Atomica: 258"
    if (num==102):
        print "\nNombre: Nobelio \nSimbolo: No \nMasa Atomica: 259"
    if (num==103):
        print "\nNombre: Laurencio \nSimbolo: Lr \nMasa Atomica: 262"
    if (num==104):
        print "\nNombre: Rutherfordio \nSimbolo: Rf \nMasa Atomica: 261"
    if (num==105):
        print "\nNombre: Dubnio \nSimbolo: Db \nMasa Atomica: 262"
    if (num==106):
        print "\nNombre: Seaborgio \nSimbolo: Sg \nMasa Atomica: 266"
    if (num==107):
        print "\nNombre: Bohrio \nSimbolo: Bh \nMasa Atomica: 264"
    if (num==108):
        print "\nNombre: Hassio \nSimbolo: Hs \nMasa Atomica: 277"
    if (num==109):
        print "\nNombre: Meitnerio \nSimbolo: Mt \nMasa Atomica: 268"
    if (num==110):
        print "\nNombre: Darmstadio \nSimbolo: Ds \nMasa Atomica: 271"
    if (num==111):
        print "\nNombre: Roentgenio \nSimbolo: Rg \nMasa Atomica: 272"
    if (num==112):
        print "\nNombre: Copernicio \nSimbolo: Cn \nMasa Atomica: 285"


if (a==1):
    nombre=input("Ingrese el nombre del elemento (Recuerde escribir siempre la primera letra en mayusculas y toda la palabra entre comillas): ")
    if nombre=="Hidrogeno":
        print "\nNumero Atomico: 1 \nSimbolo: H \nMasa Atomica: 1.0079"
    if (nombre=="Helio"):
        print "\nNumero Atomico: 2 \nSimbolo: He \nMasa Atomica: 4.0026"
    if (nombre=="Litio"):
        print "\nNumero Atomico: 3 \nSimbolo: Li \nMasa Atomica: 6.941"
    if (nombre=="Berilio"):
        print "\nNumero Atomico: 4 \nSimbolo: Be \nMasa Atomica: 9.0121"
    if (nombre=="Boro"):
        print "\nNumero Atomico: 5  \nSimbolo: B \nMasa Atomica: 10.811"
    if (nombre=="Carbono"):
        print "\nNumero Atomico: 6 \nSimbolo: C \nMasa Atomica: 12.0107"
    if (nombre=="Nitrogeno"):
        print "\nNumero Atomico: 7 \nSimbolo: N \nMasa Atomica: 14.0067"
    if (nombre=="Oxigeno"):
        print "\nNumero Atomico: 8 \nSimbolo: O \nMasa Atomica: 15.9994"
    if (nombre=="Fluor"):
        print "\nNumero Atomico: 9 \nSimbolo: F \nMasa Atomica: 18.9984"
    if (nombre=="Neon"):
        print "\nNumero Atomico: 10 \nSimbolo: Ne \nMasa Atomica: 20.1797"
    if (nombre=="Sodio"):
        print "\nNumero Atomico: 11 \nSimbolo: Na \nMasa Atomica: 22.9897"
    if (nombre=="Magnesio"):
        print "\nNumero Atomico: 12 \nSimbolo: Mg \nMasa Atomica: 24.3050"
    if (nombre=="Aluminio"):
        print "\nNumero Atomico: 13 \nSimbolo: Al \nMasa Atomica: 26.9815"
    if (nombre=="Silicio"):
        print "\nNumero Atomico: 14 \nSimbolo: Si \nMasa Atomica: 28.0855"
    if (nombre=="Fosforo"):
        print "\nNumero Atomico: 15 \nSimbolo: P \nMasa Atomica: 30.9769"
    if (nombre=="Azufre"):
        print "\nNumero Atomico: 16 \nSimbolo: S \nMasa Atomica: 32.065"
    if (nombre=="Cloro"):
        print "\nNumero Atomico: 17 \nSimbolo: Cl \nMasa Atomica: 35.453"
    if (nombre=="Argon"):
        print "\nNumero Atomico: 18 \nSimbolo: Ar \nMasa Atomica: 39.948"
    if (nombre=="Potasio"):
        print "\nNumero Atomico: 19 \nSimbolo: K \nMasa Atomica: 39.0983"
    if (nombre=="Calcio"):
        print "\nNumero Atomico: 20 \nSimbolo: Ca \nMasa Atomica: 40.078"
    if (nombre=="Escandio"):
        print "\nNumero Atomico: 21 \nSimbolo: Sc \nMasa Atomica: 44.9559"
    if (nombre=="Titanio"):
        print "\nNumero Atomico: 22 \nSimbolo: Ti \nMasa Atomica: 47.867"
    if (nombre=="Vanadio"):
        print "\nNumero Atomico: 23 \nSimbolo: V \nMasa Atomica: 50.9415"
    if (nombre=="Cromo"):
        print "\nNumero Atomico: 24 \nSimbolo: Cr \nMasa Atomica: 51.9962"
    if (nombre=="Manganeso"):
        print "\nNumero Atomico: 25 \nSimbolo: Mn \nMasa Atomica: 54.9380"
    if (nombre=="Hierro"):
        print "\nNumero Atomico: 26 \nSimbolo: Fe \nMasa Atomica: 55.845"
    if (nombre=="Cobalto"):
        print "\nNumero Atomico: 27 \nSimbolo: Co \nMasa Atomica: 58.9331"
    if (nombre=="Niquel"):
        print "\nNumero Atomico: 28 \nSimbolo: Ni \nMasa Atomica: 58.6934"
    if (nombre=="Cobre"):
        print "\nNumero Atomico: 29 \nSimbolo: Cu \nMasa Atomica: 63.546"
    if (nombre=="Zinc"):
        print "\nNumero Atomico: 30 \nSimbolo: Zn \nMasa Atomica: 65.38"
    if (nombre=="Galio"):
        print "\nNumero Atomico: 31 \nSimbolo: Ga \nMasa Atomica: 69.723"
    if (nombre=="Germanio"):
        print "\nNumero Atomico: 32 \nSimbolo: Ge \nMasa Atomica: 72.64"
    if (nombre=="Arsenico"):
        print "\nNumero Atomico: 33 \nSimbolo: As \nMasa Atomica: 74.9216"
    if (nombre=="Selenio"):
        print "\nNumero Atomico: 34 \nSimbolo: Se \nMasa Atomica: 78.96"
    if (nombre=="Bromo"):
        print "\nNumero Atomico: 35 \nSimbolo: Br \nMasa Atomica: 79.904"
    if (nombre=="Kripton"):
        print "\nNumero Atomico: 36 \nSimbolo: Kr \nMasa Atomica: 83.798"
    if (nombre=="Rubidio"):
        print "\nNumero Atomico: 37 \nSimbolo: Rb \nMasa Atomica: 85.4678"
    if (nombre=="Estroncio"):
        print "\nNumero Atomico: 38 \nSimbolo: Sr \nMasa Atomica: 87.62"
    if (nombre=="Itrio"):
        print "\nNumero Atomico: 39 \nSimbolo: Y \nMasa Atomica: 88.9058"
    if (nombre=="Zirconio"):
        print "\nNumero Atomico: 40 \nSimbolo: Zr \nMasa Atomica: 91.224"
    if (nombre=="Niobio"):
        print "\nNumero Atomico: 41 \nSimbolo: Nb \nMasa Atomica: 92.9063"
    if (nombre=="Molibdeno"):
        print "\nNumero Atomico: 42 \nSimbolo: Mo \nMasa Atomica: 95.96"
    if (nombre=="Tecnecio"):
        print "\nNumero Atomico: 43 \nSimbolo: Tc \nMasa Atomica: 98"
    if (nombre=="Rutenio"):
        print "\nNumero Atomico: 44 \nSimbolo: Ru \nMasa Atomica: 101.07"
    if (nombre=="Rodio"):
        print "\nNumero Atomico: 45 \nSimbolo: Rh \nMasa Atomica: 102.9055"
    if (nombre=="Paladio"):
        print "\nNumero Atomico: 46 \nSimbolo: Pd \nMasa Atomica: 106.42"
    if (nombre=="Plata"):
        print "\nNumero Atomico: 47 \nSimbolo: Ag \nMasa Atomica: 107.8682"
    if (nombre=="Cadmio"):
        print "\nNumero Atomico: 48 \nSimbolo: Cd \nMasa Atomica: 112.441"
    if (nombre=="Indio"):
        print "\nNumero Atomico: 49 \nSimbolo: In \nMasa Atomica: 114.818"
    if (nombre=="Estano"):
        print "\nNumero Atomico: 50 \nSimbolo: Sn \nMasa Atomica: 118.710"
    if (nombre=="Antimonio"):
        print "\nNumero Atomico: 51 \nSimbolo: Sb \nMasa Atomica: 121.760"
    if (nombre=="Telurio"):
        print "\nNumero Atomico: 52 \nSimbolo: Te \nMasa Atomica: 127.60"
    if (nombre=="Yodo"):
        print "\nNumero Atomico: 53 \nSimbolo: I \nMasa Atomica: 126.9044"
    if (nombre=="Xenon"):
        print "\nNumero Atomico: 54 \nSimbolo: Xe \nMasa Atomica: 131.293"
    if (nombre=="Cesio"):
        print "\nNumero Atomico: 55 \nSimbolo: Cs \nMasa Atomica: 132.9054"
    if (nombre=="Bario"):
        print "\nNumero Atomico: 56 \nSimbolo: Ba \nMasa Atomica: 137.327"
    if (nombre=="Lantano"):
        print "\nNumero Atomico: 57 \nSimbolo: La \nMasa Atomica: 138.9054"
    if (nombre=="Cerio"):
        print "\nNumero Atomico: 58 \nSimbolo: Ce \nMasa Atomica: 140.116"
    if (nombre=="Praseodimio"):
        print "\nNumero Atomico: 59 \nSimbolo: Pr \nMasa Atomica: 140.9076"
    if (nombre=="Neodimio"):
        print "\nNumero Atomico: 60 \nSimbolo: Nd \nMasa Atomica: 144.242"
    if (nombre=="Prometio"):
        print "\nNumero Atomico: 61 \nSimbolo: Pm \nMasa Atomica: 145"
    if (nombre=="Samario"):
        print "\nNumero Atomico: 62 \nSimbolo: Sm \nMasa Atomica: 150.36"
    if (nombre=="Europio"):
        print "\nNumero Atomico: 63 \nSimbolo: Eu \nMasa Atomica: 151.964"
    if (nombre=="Gadolinio"):
        print "\nNumero Atomico: 64 \nSimbolo: Gd \nMasa Atomica: 157.25"
    if (nombre=="Terbio"):
        print "\nNumero Atomico: 65 \nSimbolo: Tb \nMasa Atomica: 158.9253"
    if (nombre=="Disprosio"):
        print "\nNumero Atomico: 66 \nSimbolo: Dy \nMasa Atomica: 162.500"
    if (nombre=="Holmio"):
        print "\nNumero Atomico: 67 \nSimbolo: Ho \nMasa Atomica: 164.9303"
    if (nombre=="Erbio"):
        print "\nNumero Atomico: 68 \nSimbolo: Er \nMasa Atomica: 167.259"
    if (nombre=="Tulio"):
        print "\nNumero Atomico: 69 \nSimbolo: Tm \nMasa Atomica: 168.9342"
    if (nombre=="Iterbio"):
        print "\nNumero Atomico: 70 \nSimbolo: Yb \nMasa Atomica: 173.054"
    if (nombre=="Lutecio"):
        print "\nNumero Atomico: 71 \nSimbolo: Lu \nMasa Atomica: 174.9668"
    if (nombre=="Hafnio"):
        print "\nNumero Atomico: 72 \nSimbolo: Hf \nMasa Atomica: 178.49"
    if (nombre=="Tantalio"):
        print "\nNumero Atomico: 73 \nSimbolo: Ta \nMasa Atomica: 180.9478"
    if (nombre=="Wolframio"):
        print "\nNumero Atomico: 74 \nSimbolo: W \nMasa Atomica: 183.84"
    if (nombre=="Renio"):
        print "\nNumero Atomico: 75 \nSimbolo: Re \nMasa Atomica: 186.207"
    if (nombre=="Osmio"):
        print "\nNumero Atomico: 76 \nSimbolo: Os \nMasa Atomica: 190.23"
    if (nombre=="Iridio"):
        print "\nNumero Atomico: 77 \nSimbolo: Ir \nMasa Atomica: 192.217"
    if (nombre=="Platino"):
        print "\nNumero Atomico: 78 \nSimbolo: Pt \nMasa Atomica: 195.084"
    if (nombre=="Oro"):
        print "\nNumero Atomico: 79 \nSimbolo: Au \nMasa Atomica: 196.9665"
    if (nombre=="Mercurio"):
        print "\nNumero Atomico: 80 \nSimbolo: Hg \nMasa Atomica: 200.59"
    if (nombre=="Talio"):
        print "\nNumero Atomico: 81 \nSimbolo: Tl \nMasa Atomica: 204.3833"
    if (nombre=="Plomo"):
        print "\nNumero Atomico: 82 \nSimbolo: Pb \nMasa Atomica: 207.2"
    if (nombre=="Bismuto"):
        print "\nNumero Atomico: 83 \nSimbolo: Bi \nMasa Atomica: 208.9804"
    if (nombre=="Polonio"):
        print "\nNumero Atomico: 84 \nSimbolo: Po \nMasa Atomica: 210"
    if (nombre=="Astato"):
        print "\nNumero Atomico: 85 \nSimbolo: At \nMasa Atomica: 210"
    if (nombre=="Radon"):
        print "\nNumero Atomico: 86 \nSimbolo: Rn \nMasa Atomica: 220"
    if (nombre=="Francio"):
        print "\nNumero Atomico: 87 \nSimbolo: Fr \nMasa Atomica: 223"
    if (nombre=="Radio"):
        print "\nNumero Atomico: 88 \nSimbolo: Ra \nMasa Atomica: 226"
    if (nombre=="Actinio"):
        print "\nNumero Atomico: 89 \nSimbolo: Ac \nMasa Atomica: 227"
    if (nombre=="Torio"):
        print "\nNumero Atomico: 90 \nSimbolo: Th \nMasa Atomica: 232.0380"
    if (nombre=="Protactinio"):
        print "\nNumero Atomico: 91 \nSimbolo: Pa \nMasa Atomica: 231.0380"
    if (nombre=="Uranio"):
        print "\nNumero Atomico: 92 \nSimbolo: U \nMasa Atomica: 238.0289"
    if (nombre=="Neptunio"):
        print "\nNumero Atomico: 93 \nSimbolo: Np \nMasa Atomica: 237"
    if (nombre=="Plutonio"):
        print "\nNumero Atomico: 94 \nSimbolo: Pu \nMasa Atomica: 244"
    if (nombre=="Americio"):
        print "\nNumero Atomico: 95 \nSimbolo: Am \nMasa Atomica: 243"
    if (nombre=="Curio"):
        print "\nNumero Atomico: 96 \nSimbolo: Cm \nMasa Atomica: 247"
    if (nombre=="Berkelio"):
        print "\nNumero Atomico: 97 \nSimbolo: Bk \nMasa Atomica: 247"
    if (nombre=="Californio"):
        print "\nNumero Atomico: 98 \nSimbolo: Cf \nMasa Atomica: 251"
    if (nombre=="Einstenio"):
        print "\nNumero Atomico: 99 \nSimbolo: Es \nMasa Atomica: 252"
    if (nombre=="Fermio"):
        print "\nNumero Atomico: 100 \nSimbolo: Fm \nMasa Atomica: 257"
    if (nombre=="Mendelevio"):
        print "\nNumero Atomico: 101 \nSimbolo: Md \nMasa Atomica: 258"
    if (nombre=="Nobelio"):
        print "\nNumero Atomico: 102 \nSimbolo: No \nMasa Atomica: 259"
    if (nombre=="Laurencio"):
        print "\nNumero Atomico: 103 \nSimbolo: Lr \nMasa Atomica: 262"
    if (nombre=="Rutherfordio"):
        print "\nNumero Atomico: 104 \nSimbolo: Rf \nMasa Atomica: 261"
    if (nombre=="Dubnio"):
        print "\nNumero Atomico: 105 \nSimbolo: Db \nMasa Atomica: 262"
    if (nombre=="Seaborgio"):
        print "\nNumero Atomico: 106 \nSimbolo: Sg \nMasa Atomica: 266"
    if (nombre=="Bohrio"):
        print "\nNumero Atomico: 107 \nSimbolo: Bh \nMasa Atomica: 264"
    if (nombre=="Hassio"):
        print "\nNumero Atomico: 108 \nSimbolo: Hs \nMasa Atomica: 277"
    if (nombre=="Meitnerio"):
        print "\nNumero Atomico: 109 \nSimbolo: Mt \nMasa Atomica: 268"
    if (nombre=="Darmstadio"):
        print "\nNumero Atomico: 110 \nSimbolo: Ds \nMasa Atomica: 271"
    if (nombre=="Roentgenio"):
        print "\nNumero Atomico: 111 \nSimbolo: Rg \nMasa Atomica: 272"
    if (nombre=="Copernicio"):
        print "\nNumero Atomico: 112 \nSimbolo: Cn \nMasa Atomica: 285"
