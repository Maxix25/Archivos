run = True
while True:
	try:
		x1 = int(input("Introduce el valor de x1: "))
		y1 = int(input("Introduce el valor de y1: "))
		x2 = int(input("Introduce el valor de x2: "))
		y2 = int(input("Introduce el valor de y2: "))
		break
	except ValueError:
		print("Has introducido un valor no numerico")
		continue

m = (y2-y1) // (x2-x1)
print(f"El valor de la pendiente es: {m}")
#y=f(x)=mx+n
mx = m * x1
n = y1 - mx
print(f"El valor de n es: {n}")
while run == True:
	try:
                f_de_x = int(input("Introduce el valor de f(x): "))
                funcion = m * f_de_x + n
                print(f"El valor de la funcion que introduciste es: {funcion}")
                while True:
                    opcion = input("Quieres ir de nuevo? [Y/n]").lower()
                    if opcion == "y" or opcion == "":
                        continue
                    elif opcion == "n":
                        print("Saliendo del programa...")
                        run = False
                        break
                    else:
                        print("Has introducido una opcion no valida")
                        continue
	except ValueError:
		print("Has introducido un valor no numerico")
		continue
