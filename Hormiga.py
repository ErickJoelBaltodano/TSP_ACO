from Ciudad import *
from Tabla_de_Feromonas import *
import random

class Hormiga:
    
    # Método Constructor de la clase hormiga
    def __init__(self, lista_de_feromonas: Tabla_de_Feromonas, dimension: int):
        self.ciudades_visitadas = [True for _ in range(dimension)]
        self.feromonas = lista_de_feromonas
        self.dimension = dimension
        self.ciudad_base = random.randint(0, dimension - 1)
    
    # Método donde generamos un recorrido de la hormiga basado en la tabla de feromonas
    def generate(self):
        resultado = [self.ciudad_base]
        self.ciudades_visitadas[self.ciudad_base] = False

        while len(resultado) < len(self.ciudades_visitadas):
            ciudad_actual = resultado[-1]
            probabilidades = self.feromonas.check_column(ciudad_actual)
            
            # Normalizamos probabilidades solo para ciudades no visitadas
            probabilidades = [
                (p if self.ciudades_visitadas[i] else 0) 
                for i, p in enumerate(probabilidades)
            ]
            suma_probabilidades = sum(probabilidades)
            if suma_probabilidades > 0:
                probabilidades = [p / suma_probabilidades for p in probabilidades]
            
            # Elegimos la siguiente ciudad
            ruleta = random.random()
            acumulado = 0.0
            for i, probabilidad in enumerate(probabilidades):
                acumulado += probabilidad
                if ruleta <= acumulado:
                    resultado.append(i)
                    self.ciudades_visitadas[i] = False
                    break

        return resultado
