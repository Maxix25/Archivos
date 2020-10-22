print("Calculadora de funciones")
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

resta_y2_y1 = y2 - y1
resta_x2_x1 = x2 - x1
m = resta_y2_y1 // resta_x2_x1
print(f"El valor de la pendiente es: {m}")
#y=f(x)=mx+n
x = x1
y = y1
mx = m * x
n = y - mx
print(f"El valor de n es: {n}")
while True:
	try:
		f_de_x = int(input("Introduce el valor de f(x): "))
		break
	except ValueError:
		print("Has introducido un valor no numerico")
		continue
funcion = m * f_de_x + n
print(f"El valor de la funcion que introduciste es: {funcion}")