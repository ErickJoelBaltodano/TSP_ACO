from Ciudad import *
from Hormiga import *
from Tabla_de_Feromonas import *
from Tabla_de_Distancias import *

class Hormiga_Superciudad(Hormiga):
    # Método constructor que hereda de la clase base Hormiga
    def __init__(self, tabla_de_feromonas: Tabla_de_Feromonas, dimension, tabla_de_distancias: Tabla_de_Distancias,lista_de_ciudades):
        super().__init__(tabla_de_feromonas, dimension)
        self.distancias = tabla_de_distancias
        self.alpha = 1.0
        self.beta = 2.0
        # Ciudades representa las ciudades que son de nuestra superciudad
        self.ciudades = lista_de_ciudades
        
        
    # Sobreescribimos el método generate_colony de la clase Hormiga; generamos una colonia de hormigas de superciudad.
    @staticmethod
    def generate_colony(numero_de_hormigas:int,feromonas:Tabla_de_Feromonas,dimension:int,distancias:Tabla_de_Distancias):
        return [Hormiga_Superciudad(tabla_de_feromonas,dimension,distancias) for _ in range(numero_de_hormigas)]
    
    
    # Sobreescribimos el método generate_path de la clase Hormiga; generamos caminos con las hormigas de superciudad
    def generate_path(self):
        pass