#def IVA():
	#print("Bienvenido a la calculadora del IVA")
	#precio_producto=int(input("Introduzca el valor de su producto: "))
	#suma_precio_final=(precio_producto*21)//100
	#precio_final=suma_precio_final+precio_producto
	#print(precio_final)
	#return
#IVA()

#Ejercicio video 33
def email_verificator():

	email=input("Introduce your email: ")
	if email.startswith("@") or email.endswith("@") or email.count("@")>1 or email.count("@")<1:
		print("The email introduced isn't correct :(, try again")
		email_verificator()
	else:
		print("The email introduced is correct you :)")
email_verificator()