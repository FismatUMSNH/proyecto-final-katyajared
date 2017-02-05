archivos = ['D:\ipython\Laboratorio4\orchivo1.txt', 'D:\ipython\Laboratorio4\orchivo2.txt']
with open("D:\ipython\Laboratorio4\orchivo3", "w") as outfile:
    for fname in archivos:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
    print "Se ha creado el nuevo archivo"            
