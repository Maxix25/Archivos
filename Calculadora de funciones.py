print("Calculadora de funciones")
x1=int(input("Introduce el valor de x1: "))
y1=int(input("Introduce el valor de y1: "))
x2=int(input("Introduce el valor de x2: "))
y2=int(input("Introduce el valor de y2: "))
suma_y2_y1=y2-y1
suma_x2_x1=x2-x1
m=suma_y2_y1/suma_x2_x1
print(f"El valor de la pendiente es: {m}")
#y=f(x)=mx+n
x=x1
y=y1
multiplicacion=m*x
n=y-multiplicacion
print(f"El valor de n es: {n}")
f_de_x=int(input("Introduce el valor de el numero que te toco: "))
funcion=m*f_de_x+n
print(f"El valor de la funcion que te toco es: {funcion}")
