archivo = ["D:\ipython\Laboratorio4\Tortugas_marinas.txt"]

with open("D:\ipython\Laboratorio4\ejercicio3", "w") as outfile:
    for fname in archivo:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
    print "Se ha creado el nuevo archivo"
