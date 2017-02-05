def leer(archivo,n):
	archivo = open("D:\ipython\Laboratorio4\Tortugas_marinas.txt", "r")
	lista = archivo.readlines()
	numlin = 0

	for linea in lista:
		numlin += 1
		if numlin<=n:
			print(numlin, linea)
