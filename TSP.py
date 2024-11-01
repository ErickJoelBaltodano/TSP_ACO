from Ciudad import *
from Solucion import *


class TSP:
    #Método constructor de nuestra clase TSP.
    def __init__(self, lista_de_ciudades: list[Ciudad]):
        self.lista_de_ciudades = lista_de_ciudades

    #Método que nos regresa el núemro de ciudades que tenemos.
    def longitud(self):
        return len(self.lista_de_ciudades)

    #Método en el que agregaremos ciudades a nuestro problema de TSP.
    def append(self, ciudad: Ciudad):  
        self.lista_de_ciudades.append(ciudad)

    #Método en el que dejamos una representación en cadena de nuestro problema de TSP.
    def __str__(self):
        cadena = ""
        for x in self.lista_de_ciudades:
            cadena += (str(x) + "\n")
        return cadena  

    #Método en el cual accedemos a una ciudad en particular de nuestro problema del TSP.
    def get(self,posicion:int):
        return self.lista_de_ciudades[posicion]
    
    def distancia_euclidiana(self, ciudad1:int , ciudad2: int):
        return Ciudad.distancia_euclidiana (self.lista_de_ciudades[ciudad1-1],self.lista_de_ciudades[ciudad2-1])

    @staticmethod
    def read_lines(lista_de_strings: list[str]):
        tsp = TSP([])

        for line in lista_de_strings:
            ciudad = Ciudad.read_line(line)
            tsp.append (ciudad)

        return tsp
            

     #Metodo en el que dado el id de una ciudad inicial, recibimos un recorrido de ciudades y regresamos el valor total del recorrido.
    def evaluar_recorrido_tsp(self, solucion):
        #Inicializamos las variables 
        apuntador1 = 0
        apuntador2 = 1
        #Sacamos la distancia de la ciudad inicial a la primera ciudad

        resultado = 0
     
        #Iteramos sobre los indices de la solución y calculamos la distancia del recorrido
        while (apuntador2< len(solucion)):
            resultado +=self.distancia_euclidiana(solucion[apuntador1],solucion[apuntador2])      
            apuntador1+= 1
            apuntador2+=1
        
        
        
        return resultado

    #Método que nos regresa el aristade mayor peso.
    def arista_de_mayor_peso(self, solucion):
        maximo_inferior = 0
        maximo_superior = 1

        arista_mayor = self.distancia_euclidiana(solucion[0],solucion[1])

        apuntador1= 1
        apuntador2= 2
        
        #Iteramos sobre los indices de la solución y calculamos la distancia del recorrido
        while (apuntador2< len(solucion)):
            if (self.distancia_euclidiana(solucion[apuntador1],solucion[apuntador2])>arista_mayor):
                #Intercambiamos los máximos 
                maximo_inferior = apuntador1
                maximo_superior = apuntador2
                arista_mayor = self.distancia_euclidiana(solucion[apuntador1],solucion[apuntador2])
            #Incrementamos los valores de los apuntadones (iterando la lista)
            apuntador1 += 1
            apuntador2 += 1


        return [solucion[maximo_inferior],solucion[maximo_superior],arista_mayor]
