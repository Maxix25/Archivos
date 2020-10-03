#Definiendo la clase
class Coche():
    #Si le damos esta funcion __init__ decimos que este va a ser el estado INICIAL de la clase
    def __init__(self):

        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4
        self.enmarcha=False
#En este caso esta clase tiene 4 PROPIEDADES (largoChasis, anchoChasis, ruedas y enmarcha)
#Si ponemos dos guiones bajos ("__") lo que hacemos es ENCAPSULAR ese parametro de la clase por lo cual no lo hace cambiar FUERA DE LA CLASE
#Es decir no se podra editar si no estamos escribiendo dentro de la sangria de la clase
    def arrancar(self,arrancamos):
            self.enmarcha=arrancamos
            if (self.enmarcha):
            	chequeo=self.__chequeo_interno()

            if(self.enmarcha and chequeo):
                return "El coche esta en marcha"
            elif (self.enmarcha and chequeo==False):
            	return "Algo ha ido mal en el chequeo no se ha podido arrancar"

            else:
                return "El coche esta parado"


    def estado(self):
        print("El coche tiene ", self.__ruedas," ruedas. Un ancho de ",self.anchoChasis, " y un largo de ",
        self.largoChasis)
    def __chequeo_interno(self):
    	print("Realizando chequeo interno")
    	self.__gasolina="ok"
    	self.__aceite="ok"
    	self.__puertas="cerradas"
    	if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
    		return True
    	else:
    		return False
#Y tiene 2 COMPORTAMIENTOS (estado y arrancar)

miCoche=Coche()


print(miCoche.arrancar(True))

miCoche.estado()


print("-----------------------------A continuacion creamos el segundo objeto---------------------------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))
#Como la variable "ruedas" esta ENCAPSULADA no se puede editar fuera de la clase por lo cual seguira con el mismo valor
#Pero si no pones dos guinoes bajos ("__") el programa hablara de una variable DISTINTA a la ENCAPSULADA

miCoche2.estado()

