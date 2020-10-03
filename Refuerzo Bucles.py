#Ejercicio 1
#for i in range(1,101,2):
	#print(i, end=" ")
#Ejercicio 2
#password=input("Introduce tu password: ")
#if len(password)<8:
	#print("Contraseña erronea")
#elif password==" ":
	#print("Contraseña erronea")
#else:
	#print("Contraseña OK")
#Ejercicio 3
email=False
email_input=input("Introduce tu email: ")
for i in email_input:
	if email_input[i]=="@" and email_input[i]==".":
		email=True
if email:
	print("El email es correcto")
else:
	print("El email es incorrecto")
