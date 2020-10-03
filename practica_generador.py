#Generadores I
#def genera_pares(limite):
	#num=1
	#while num<limite:
		#yield num*2
		#num=num + 1
#devuelvepares=genera_pares(10)
#print(next(devuelvepares))
#print("Aqui podria haber mas codigo...")
#print(next(devuelvepares))
#print("Aqui podria haber mas codigo...")
#print(next(devuelvepares))
#print("Aqui podria haber mas codigo...")
#Generadores II
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		yield from elemento
ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))