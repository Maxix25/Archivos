#def Prueba ():

	#print("Hola como estas")
	#print("Estoy bien")
	#print ("Vale master")

#Prueba()

#Prueba()

#Prueba()
#Siguiente capitulo
#def suma():
	#num1=5
	#num2=7
	#print(num1+num2)

#Tambien se les puede cambiar los valores
def suma(num1, num2):

	resultado=num1+num2
	return resultado
almacena_resultado=suma(5,3)
print (almacena_resultado)

#Siguiente capitulo
#Listas
MiLista=["Maximiliano", "Damian", "Jose Tomas"]
MiLista.extend(["Lucas", "Manuel"])
#print (MiLista)
MiLista.remove("Damian")
#print (MiLista)
#print (MiLista.index("Jose Tomas")
#----------------------------------
Lista1=["Pera", "Manzana", "Arbol"]
Lista2=["Tomate", "Lechuga", "Frutilla"]
Lista3=Lista1+Lista2
#print(Lista3)
#Siguiente capitulo
#Tuplas
#Esto es para cambiar de una tupla a una lista
mitupla=("Maxi", 13, 1, 1995,)
milista=list (mitupla)
#print(milista)
#Eso es para cambiar de una lista a una tupla
milista2=["Maxi", 13, 1, 1995]
mitupla2=tuple(milista2)
#print (mitupla2)
#print ("Maxi" in mitupla2)
#print (mitupla2.count (13))
#print (len(mitupla2))
#Otra forma de escribir la tupla es asi
mitupla3="Maxi", 13, 1, 1995
#print (mitupla3)
#Este metodo se llama empaquetado de tupla
#Otro metodo es el desempaquetado de tupla
mitupla4=("Maxi", 13, 1, 1995)
name, day, month, year=mitupla4
#print(name)
#Este asigna a variables diferentes, diferentes valores de la tupla
#Siguiente capitulo
#Diccionarios
midiccionario={"Chile":"Santiago", "Argentina":"Buenos Aires"}
midiccionario["Peru"]="Wenas"
#print(midiccionario)
midiccionario["Peru"]="Lima"
#print(midiccionario)
#del midiccionario["Chile"]
#print(midiccionario)
#Tambien le puedes dar un valor a una tupla con el diccionario
midiccionario={"Name":"Maximiliano", "Surname":"Besoain", "Nickname":"Maxigamer25"}
#print(midiccionario.keys())
#print(midiccionario.values())
#print(len(midiccionario))
#Estos son metodos para ver las llaves y valores de cada elemento en un diccionario ademas puedes ver cuantos pares hay
#Siguiente capitulo
#Condicionales
#print("Programa de evaluacion de notas de alumnos")
#nota_alumno=input()
#def evaluacion(nota):
	#valoracion="aprobado"
	#if nota<5:
		#valoracion="suspenso"
	#return valoracion
#print(evaluacion(int(nota_alumno)))
#Siguiente capitulo
#Condicionales II
#print("Verificacion de acceso")
#edad_usuario=int(input("Introduce tu edad: "))
#if edad_usuario<18:
	#print("Acceso denegado")
#elif edad_usuario>100:
	#print("Edad Incorrecta")
#else:
	#print("Acceso Garantizado")
#El condicional "else" depende de un "if"
#Siguiente escenario
#print("Notas alumnos")
#nota_alumno2=int(input("Introduce la nota: "))
#if nota_alumno2<5:
	#print("Insuficiente")
#elif nota_alumno2<6:
	#print("Suficiente")
#elif nota_alumno2<7:
	#print("Bien")
#elif nota_alumno2<9:
	#print("Notable")
#else:
	#print("Sobresalienrte")
#Siguiente capitulo
#Condicionales III
#salario_presidente=int(input("Introduce el salario del presidente: "))
#print("El Salario del presidente es: " + str(salario_presidente))

#salario_director=int(input("Introduce el salario del director: "))
#print("El salario del director es: " + str(salario_director))

#salario_jefe_area=int(input("Introduce el salario del jefe de area: "))
#print("El salario del jefe de area es: " + str(salario_jefe_area))

#salario_administrativo=int(input("Introduce el salario del administrativo: "))
#print("El salario del administrativo es: " + str(salario_administrativo))

#if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	#print("Todo funciona correctamente")
#else:
	#print("Algo falla en esta empresa")
#Estos son elementos concatenados

#Siguiente capitulo
#Condicionales IV
#print("Programa de becas year 2020")

#distancia_escuela=int(input("Introduce la distancia a la escuela en kilometros: "))
#print(distancia_escuela)

#numero_de_hermanos=int(input("Introduce el numero de hermanos en el centro: "))
#print(numero_de_hermanos)

#salario_familiar=int(input("Introduce el salario anual bruto: "))
#print(salario_familiar)

#if distancia_escuela>40 and numero_de_hermanos>2 or salario_familiar<=20000:
	#print("Tienes derecho a beca")
#else:
	#print("No tienes derecho a beca :(")

print("Asignaturas optativas 2020")
print("Asiganturas optativas: Informatica grafica - Pruebas de Software - Usabilidad y Accesibilidad")
asignatura=input("Escribe la asignatura escogida: ")

if asignatura in("Informatica grafica", "Pruebas de software", "Usabilidad y Accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura escogida no esta disponible")
