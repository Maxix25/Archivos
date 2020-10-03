#Ejercicio 1
#num1=int(input("Introduce un numero: "))
#num2=0
#while num1>num2:
	#num1=int(input("Introduce un numero: "))
	#num2=num2+1
	#if num1<=num2:
		#print("Has introducido un numero menor al anterior")
		#print("Finalizo el programa")
#Ejercicio 2
numeros_positivos=int(input("Introduce un numero positivo: "))
suma=int(0)
while numeros_positivos>0:
	suma=suma + numeros_positivos
	numeros_positivos=int(input("Introduce un numero positivo: "))
	if numeros_positivos<0:
		print("Introduciste un numero negativo, el resultado de la suma es: "+ str(suma))
