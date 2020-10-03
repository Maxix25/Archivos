#Ejercicio 1
#for i in range(1,100,2):
	#print(i)
#Ejercicio 2
contra=input("Introduzca la password: ")
contador=0
for i in range(len(contra)):
	if contra[i]==" ":
		contador=1
if len(contra)<8 or contador>0:
	print("Password erronea")
else:
	print("Password OK")