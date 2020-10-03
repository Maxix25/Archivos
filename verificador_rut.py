def verificador_rut():
	bucle=0
#Se le pide al usuario introducir un rut y verificiar si este tiene 10 caracteres
#Si esta condicion se cumple el programa seguira
#Si esta condicion NO se cumple el programa volvera a pedir el rut
	rut = input("Introduce tu rut: ")
	for num in rut:
		try:
			int(num)
		except:
			rut.replace(".", "")
#Bucle para que por cada vuelta de bucle se le asigne a una variable el valor de number
	for number in rut:
		bucle = bucle+1
		if bucle == 1:
			num1_multiplicado=int(number)* 3
		elif bucle == 2:
			num2_multiplicado=int(number)* 2
		elif bucle == 3:
			num3_multiplicado=int(number)* 3
		elif bucle == 4:
			num4_multiplicado=int(number)* 6
		elif bucle == 5:
			num5_multiplicado=int(number)* 5
		elif bucle == 6:
			num6_multiplicado=int(number)* 4
		elif bucle == 7:
			num7_multiplicado=int(number)* 3
		elif bucle == 8:
			num8_multiplicado=int(number) *2

#Ahora con las multiplicaciones llega sumar los resultados
	suma = num8_multiplicado + num7_multiplicado + num6_multiplicado + num5_multiplicado + num4_multiplicado + num3_multiplicado + num2_multiplicado + num1_multiplicado


#Ahora llega dividirlo por 11 ya que el algoritmo es llamado modulo 11
	division = suma // 11
	resto_division = suma - (11*division)
	ultima_operacion = 11 - resto_division
#Ahora llega los condicionales para verificar si el rut es correcto
	if rut.endswith("0") and ultima_operacion == 11:
		print("El rut introducido es correcto")

	elif ultima_operacion == 10 and rut.endswith("k"):
		print("El rut introducio es correcto")

	elif ultima_operacion == 9 and rut.endswith("9"):
		print("El rut introducido es correcto")

	elif ultima_operacion == 8 and rut.endswith("8"):
		print("El rut introducido es correcto")

	elif ultima_operacion == 7 and rut.endswith("7"):
		print("El rut introducido es correcto")

	elif ultima_operacion == 6 and rut.endswith("6"):
		print("El rut introducido es correcto")

	elif ultima_operacion == 5 and rut.endswith("5"):
		print("El rut introducido es correcto")

	elif ultima_operacion == 4 and rut.endswith("4"):
		print("El rut introducido es correcto")

	elif ultima_operacion == 3 and rut.endswith("3"):
		print("El rut introducido es correcto")

	elif ultima_operacion == 2 and rut.endswith("2"):
		print("El rut introducido es correcto")

	elif ultima_operacion == 1 and rut.endswith("1"):
		print("El rut introducido es correcto")

	else:
		print("El rut introducido es incorrecto, intentelo de nuevo")
		verificador_rut()
verificador_rut()
