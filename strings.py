#nombreusuario=input("Introduce tu nombre de usuario: ")

#Este es el metodo upper que transforma los caracteres a 

#print("El nombre es: ", nombreusuario.upper())

#Lower en el otro caso es lo contrario y transforma los carracteres a minuscula

#print("El nombre es: ", nombreusuario.lower())

#capitalize transforma la primera letra en mayuscula

#print("El nombre es: ", nombreusuario.capitalize())

#isdigit se usa para saber si un valor es numerico o no
#Esto devuelve un valor booleano (True o False)

edad=input("Introduce la edad: ")

while(edad.isdigit()==False):
	print("Por favor, introduce un valor numerico")


	edad=input("Introduce la edad: ")


if (int(edad)<18):
	print("No puede pasar")
else:
	print("Puede pasar")