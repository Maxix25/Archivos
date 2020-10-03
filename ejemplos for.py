#Bucles I
#contador=0
#miemail=input("Introduzca su direccion de email: ")

#for i in miemail:
	#if(i=="@" or i=="."):
		#contador=contador+1
#if contador==2:
	#print("El email es correcto")
#else:
	#print("El email es incorrecto")
#Siguiente capitulo
#Bucles II
#for i in range(1,100,2):
	#print(i)
#El primer valor puede ser las veces que se repite o el primer rango
#El segundo valor se le da el maximo de valor(Este numero esta excluido del listado)
#El ultimo numero le da de cuanto en cuanto debe avanzar
valido=False
email=input("Introduce tu mail: ")
for i in range(len(email)):
	if email[i]=="@":
		valido=True
if valido:
	print("El email es correcto")
else:
	print("El email es incorrecto")