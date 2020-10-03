#Excepciones II
def divide():
	while True:
		try:
			op1=(float(input("Introduce el primero numero: ")))
			op2=(float(input("Introduce el segundo numero: ")))
			print("La division es igual a "+ str(op1/op2))
			break
		except ValueError:
			print("El valor introducido no es correcto")
			continue
		except ZeroDivisionError:
			print("No se puede dividir entre 0")
			continue
		print("Calculo finalizado")
divide()
#import math
# def calcula_raiz(num1):
# 	if num1<0:
# 		raise ValueError("El numero no puede ser negativo")
# 	else:
# 		return math.sqrt(num1)
# op1=int(input("Introduce un numero: "))
# try:
# 	print(calcula_raiz(op1))
# except ValueError as ErrorNumeroNegativo:
# 	print(ErrorNumeroNegativo)
# print("El programa ha finalizado")