#Ejemplo Continue
#Asi se pueden ignorar caracteres en python usando continue
#for letra in "Python":
	#if letra=="h":
		#continue
	#print("Viendo la letra: "+letra)
#Ejemplo continue 2
#Otro ejemplo parecido
#nombre="Pildoras Informaticas"
#contador=0
#for i in nombre:
	#if i==" ":
		#continue
	#contador+=1

#print(contador)
#Ejemplo 3
email=input("Introduce tu email: ")
for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False
print(arroba)