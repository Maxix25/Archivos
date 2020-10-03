#Bucles IV
#While
#edad=int(input("Introduce tu edad: "))
#while edad<5 or edad>100:
	#print("Edad incorrecta")
	#print("Error: No se puede avanzar")
	#edad=int(input("Introduce tu edad: "))
#print("Gracias por colabrorar")
#print("Edad del aspirante "+str(edad))
#Programa 2
import math
print("Programa de caluclo de raiz cuadrado")
#Variables
numero=int(input("Introduce un numero: "))
intentos=0
#Declaracion del bucle
while numero<0:
	print("No se puede hallar la raiz de un numero negativo")
	if intentos==2:
		print("Has consumidos demasiados intentos, el programa ha finalizado")
		break;
	numero=int(input("Introduce un numero: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de "+ str(numero)+" es "+ str(solucion))
