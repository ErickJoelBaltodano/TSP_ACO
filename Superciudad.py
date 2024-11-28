from TSP import *
from Tabla_de_Distancias import *
import random

class Superciudad:
    
    # Método Constructor de la clase SuperCiudad.
    def __init__ (self,ciudad_base:int,tabla:Tabla_de_Distancias, lista_de_ciudades):
        self.path = [ciudad_base]
        self.tabla_de_distancias = tabla
        self.lista_de_ciudades = lista_de_ciudades
        self.ciudades = []
        
    
    