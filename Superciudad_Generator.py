from TSP import *
from Superciudad import *
import random

class Superciudad_Generator:
    
    
    # Método donde generamos superciudades  y generamos caminos entre las ciudades de la conforman.
    @staticmethod
    def generate(n,tsp :TSP):
        #Escogemos n ciudades base
        ciudades_base = [random.randint(0, tsp.longitud()-1) for _ in range(n)]

        # Agrupamos las superciudades según su cercanía
        ciudad = 0
        grupitos = [[] for _ in range(n)]
        
        while ciudad < tsp.longitud():
            # Checamos comparamos las distancias con cada una de las ciudades base.
            ciudad_base = 0
            mejor_distancia = None
            ciudades_base_mas_cercana= None
            
            while ciudad_base < len(ciudades_base):
                #Caso en el que hay una distancia mejor
                if mejor_distancia is None or tsp.distancia_euclidiana(ciudad,ciudad_base):
                    #Actualizamos los valores    
                    mejor_distancia = tsp.distancia_euclidiana(ciudad,ciudad_base)
                    ciudades_base_mas_cercana = ciudad_base

                ciudad_base += 1
            
            #Agregamos la ciudad al grupo.
            grupitos[ciudades_base_mas_cercana].append(ciudad)
            
            
            ciudad += 1
        
        
        #Generamos las superciudades.
        superciudades= [Superciudad (ciudades_base[i],tsp.tabla_de_distancias,grupitos[i])  for i in range[n]]
       
        return superciudades
    
    
   
        
            
            
            
    