from Ciudad import *

class Tabla_de_Distancias:
    
    #Método Constructor donde generamos la tabla de feromonas.
    def __init__(self,lista_de_ciudades:list[Ciudad]):
        self.tabla =  [[0 for _ in range(len(lista_de_ciudades))] for _ in range(len(lista_de_ciudades))]
        
        for x in range (len(lista_de_ciudades)):
            for y in range(len(lista_de_ciudades)):
                
                self.tabla[x][y]= Ciudad.distancia_euclidiana(lista_de_ciudades[x],lista_de_ciudades[y])
    
    #Método donde regresamos el valor actual de la feromona dados dos vértices del tsp.
    def get_value(self,vertice1: int,vertice2:int):
        #Nota: NO IMPORTA EL ORDEN PUES LA TABLA ES SIMÉTRICA
        return self.tabla [vertice1][vertice2]
    
    
    
    