from Tabla_de_Feromonas import *
from Tabla_de_Distancias import *
from Ciudad import *
import time
from Random_Solution_Generator import *
from Superciudad import * 
from Superciudad_Generator import *


class TSP:
    #Método constructor de nuestra clase TSP.
    def __init__(self, lista_de_ciudades: list[Ciudad]):
        self.lista_de_ciudades = lista_de_ciudades
        #Calculamos nuestras distancias para nuestro problema TSP. O(n²)
        self.tabla_de_distancias = Tabla_de_Distancias(self.lista_de_ciudades)
        
        #Inicializamos nuestros valores de la tabla de feromonas. O(n²)
        self.tabla_de_Feromonas = Tabla_de_Feromonas(self.longitud())
    
    # Getters
    def get_Feromonas(self):
        return self.tabla_de_Feromonas
    
    def get_Distancias(self):
        return self.tabla_de_distancias
    
    def get_Ciudades(self):
        return self.lista_de_ciudades

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
        tsp = []

        for line in lista_de_strings:
            ciudad = Ciudad.read_line(line)
            tsp.append (ciudad)
        result = TSP(tsp)
        return result
            

     #Metodo en el que dado el id de una ciudad inicial, recibimos un recorrido de ciudades y regresamos el valor total del recorrido.
    def evaluar_recorrido_tsp(self, solucion):
        resultado = 0
        for i in range(len(solucion) - 1):
            distancia = self.distancia_euclidiana(solucion[i], solucion[i + 1])
            resultado += distancia
            resultado += self.distancia_euclidiana(solucion[0],solucion[-1])
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
        self.tabla_de_Feromonas.clean(self.longitud())
    
    
    # Método que dado una colonia de hormigas(lista de hormigas) realiza búsquedas y un tiempo en segundos realiza una búsqueda de soluciones a partir del método generate
    def ACO(self,colonia_de_hormigas,tiempo_segundos,timeout,incremento):
        best_paths = []
        best_path = None
        shortest_score = None
        shortest_scores = []
        
        tiempo_inicial = time.time()
        tiempo_ultimo_timeout = tiempo_inicial
        
        while (time.time() - tiempo_inicial < tiempo_segundos):
            x = 0
            for hormiga in colonia_de_hormigas:
                # Generamos un camino
                x +=1
                path = hormiga.generate_path()
                hormiga.reset()
                # Marcamos el camino dado que fue visitado
                self.tabla_de_Feromonas.marcar_feromona(2,path)
                
                # Caso en el que encontramos un nuevo mejor camino
                if best_path is None or self.evaluar_recorrido_tsp(path)< shortest_score:
                    shortest_score = self.evaluar_recorrido_tsp(path)
                    best_path = path
            # Después de cada iteración evaporamos las feromonas y marcamos el mejor camino
            self.tabla_de_Feromonas.evaporacion()
            self.tabla_de_Feromonas.marcar_feromona(incremento,best_path)

            # Comprobamos si ha pasado el tiempo especificado para un timeout
            if (time.time() - tiempo_ultimo_timeout) >= timeout:
                # Almacenamos el mejor camino y su puntuación
                best_paths.append(best_path)
                shortest_scores.append(shortest_score)
                
                # Actualizamos el tiempo del último timeout
                tiempo_ultimo_timeout = time.time()
                print ("Mejor Camino: {} \nValor: {}".format(best_path,shortest_score))
        
        
        return best_paths , shortest_scores
    
    
    # Método donde dado una colonia de hormigas de superciudad realizamos el ACO.
    def ACO_Superciudad (self, colonia_de_hormigas, tiempo_segundos, timeout, incremento ):
        best_paths = []
        best_path = None
        shortest_score = None
        shortest_scores = []
        
        tiempo_inicial = time.time()
        tiempo_ultimo_timeout = tiempo_inicial
        
        while (time.time() - tiempo_inicial < tiempo_segundos):
            
            # Seccionamos el problema en 3 partes
            ciudades = Superciudad_Generator.generate(6,self.longitud(),self.tabla_de_distancias)
            y = 0
            # A cada hormiga le asignamos una sección
            while y < len(colonia_de_hormigas):
                colonia_de_hormigas[y].set_seccion(ciudades[y%6].lista_de_ciudades)
                
                y +=1
            
            
            x = 0
            path = []
            for hormiga in colonia_de_hormigas:
                # Generamos un camino
                x +=1
                p = hormiga.generate_path()
                path += p
                hormiga.reset()
                # Marcamos el camino dado que fue visitado
                self.tabla_de_Feromonas.marcar_feromona(2,path)
                
            # Caso en el que encontramos un nuevo mejor camino
            if (best_path is None or self.evaluar_recorrido_tsp(path)< shortest_score)and (len(path)== self.longitud()):
                shortest_score = self.evaluar_recorrido_tsp(path)
                best_path = path
                
                    
            # Después de cada iteración evaporamos las feromonas y marcamos el mejor camino
            self.tabla_de_Feromonas.evaporacion()
            self.tabla_de_Feromonas.marcar_feromona(incremento,best_path)

            # Comprobamos si ha pasado el tiempo especificado para un timeout
            if (time.time() - tiempo_ultimo_timeout) >= timeout:
                # Almacenamos el mejor camino y su puntuación
                if (best_paths != []and best_path == best_paths[-1]):
                    self.tabla_de_Feromonas.clean(self.longitud())
                best_paths.append(best_path)
                shortest_scores.append(shortest_score)
                
                
                # Actualizamos el tiempo del último timeout
                tiempo_ultimo_timeout = time.time()
                print ("Mejor Camino: {} \nValor: {}".format(best_path,shortest_score))
        
        
        return best_paths , shortest_scores
        
        
        
        
        
