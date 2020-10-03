import os

def init():
	print(""""""" ADMINISTRAR ARCHIVOS Y CARPETAS """"""""")
	opcion=input("Seleccione una opcion crear=Crear un directorio y rm=eliminar: ")
	if(opcion == "crear"):
		ruta = input("Indique la ruta, si no indica la ruta, la ruta sera la actual: ")
		if (ruta == ""): ruta = os.getcwd() + "\\"
		#Comprobar si la ruta existe
		if(os.path.isdir(ruta)):
			tipo= input("Indique el tipo de archivo a=archivo, c=carpeta")
			if(tipo == "a"):
				archivo=input("Indique el nombre del archivo")
				#Crear el archivo
				maejador= open(ruta+archivo, "w")
				manejador.close()
				print("Archivo", archivo, "creado con exito")
			elif(tipo=="c"):
				carpeta= input("Indique el nombre de la carpeta")
				#Crear la carpeta
				os.mkdir(ruta+carpeta)
				print("Carpeta", carpeta, "creada con exito")
			else: init() #Se reinicia el programa
	elif(opcion == "rm"):
		ruta = input("Indique la ruta, si no indica la ruta, la ruta sera la actual")
		if (ruta==""): ruta = os.getcwd() + "\\"
		eliminar= input("Indique el nombre de la carpeta o archivo a eliminar: ")
		#Comprobar si es un archivo
		if(os.path.isfile(ruta+eliminar)):
			os.remove(ruta+eliminar)
			print("Archivo ",eliminar, " eliminado con exito")
		#Comprobar si es una carpeta
		elif(os.path.isdir(ruta+eliminar)):
			os.rmdir(ruta+eliminar)
			print("Carpeta", eliminar, " eliminada con exito")
		else: init() #Se reinicia el programa
	else: init() #Se reinicia el programa
#Llamar a la funcion
init()