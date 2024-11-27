from Tabla_de_Feromonas import *
from Tabla_de_Distancias import *
from Ciudad import *
import time
from Random_Solution_Generator import *


class TSP:
    #Método constructor de nuestra clase TSP.
    def __init__(self, lista_de_ciudades: list[Ciudad]):
        self.lista_de_ciudades = lista_de_ciudades
        #Calculamos nuestras distancias para nuestro problema TSP. O(n²)
        self.tabla_de_distancias = None
        
        #Inicializamos nuestros valores de la tabla de feromonas. O(n²)
        self.tabla_de_Feromonas = None
    
    def get_tablas(self,feromonas:Tabla_de_Feromonas,distancias:Tabla_de_Distancias):
        self.tabla_de_distancias = distancias
        self.tabla_de_Feromonas = feromonas


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
            cadena += (str(x) + ", ")
        return cadena  

    #Método en el cual accedemos a una ciudad en particular de nuestro problema del TSP.
    def get(self,posicion:int):
        return self.lista_de_ciudades[posicion]
    
    def distancia_euclidiana(self, ciudad1:int , ciudad2: int):
        return self.tabla_de_distancias.get_value(ciudad1,ciudad2)

    @staticmethod
    def read_lines(lista_de_strings: list[str]):
        tsp = TSP([])

        for line in lista_de_strings:
            ciudad = Ciudad.read_line(line)
            tsp.append (ciudad)

        return tsp
            

     #Metodo en el que dado el id de una ciudad inicial, recibimos un recorrido de ciudades y regresamos el valor total del recorrido.
    def evaluar_recorrido_tsp(self, solucion):
        resultado = 0
        print(f"Evaluando recorrido: {solucion}")
        for i in range(len(solucion) - 1):
            distancia = self.distancia_euclidiana(solucion[i], solucion[i + 1])
            print(f"Distancia de {solucion[i]} a {solucion[i + 1]}: {distancia}")
            resultado += distancia
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
    
    # Método donde reiniciamos una tabla de feromonas.
    def clean_table (self):
        self.tabla_de_Feromonas.clean(self.longitud)
    
    
    # Método que dado una colonia de hormigas(lista de hormigas) realiza búsquedas y un tiempo en segundos realiza una búsqueda de soluciones a partir del método generate
    def ACO(self,colonia_de_hormigas,tiempo_segundos,incremento):
        best_paths = []
        best_path = None
        shortest_score = None
        shortest_scores = []
        
        tiempo_inicial = time.time()
        
        while (time.time() - tiempo_inicial < tiempo_segundos):
            
            for hormiga in colonia_de_hormigas:
                # Generamos caminos en cada una de las hormigas
                path = hormiga.generate()
                
                # Método donde evaluamos el camino de la hormiga
                if (shortest_score is None or shortest_score > self.evaluar_recorrido_tsp(path)):
                    shortest_score = self.evaluar_recorrido_tsp(path)
                    shortest_scores.append(shortest_score)
                    best_path = path
                    best_paths.append(best_path)
                    
                # Aumentamos las feromonas del mejor camino.
                self.tabla_de_Feromonas.marcar_feromona(incremento,best_path)
                
                #Evaporación
                self.tabla_de_Feromonas.evaporacion()
                
            
        
        
        return best_paths , shortest_scores
        
        
        
