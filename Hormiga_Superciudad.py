
from Ciudad import *
from Hormiga import *
from Tabla_de_Feromonas import *
from Tabla_de_Distancias import *

class Hormiga_Superciudad(Hormiga):
    # Método constructor que hereda de la clase base Hormiga
    def __init__(self, tabla_de_feromonas: Tabla_de_Feromonas, dimension, tabla_de_distancias: Tabla_de_Distancias):
        super().__init__(tabla_de_feromonas, dimension)
        self.distancias = tabla_de_distancias
        self.alpha = 2.0  # Parámetro que controla la importancia de las feromonas
        self.beta = 3.0   # Parámetro que controla la importancia de las distancias
        self.ciudades = None  # Lista de ciudades en la sección de la superciudad

    # Método donde asignamos a esta hormiga una sección de la super ciudad para generar caminos en esta
    def set_seccion(self, lista):
        self.ciudades = lista
        
        
    @staticmethod
    def generate_colony(numero,feromonas,dimension,distancias):
        return [Hormiga_Superciudad(feromonas,dimension,distancias) for _ in range(numero)]
    
    
    # Sobreescribimos el método generate_path de la clase Hormiga; generamos caminos con las hormigas de superciudad
    def generate_path(self):
        resultado = [self.ciudad_base]
        self.ciudades_visitadas[self.ciudad_base] = False

        while len(resultado) < len(self.ciudades):  # Recorremos solo las ciudades de la sección de la superciudad
            ciudad_actual = resultado[-1]
            probabilidades = []

            # Calculamos las probabilidades basadas en feromonas y distancias
            for i in self.ciudades:
                if self.ciudades_visitadas[i]:  # Solo consideramos las ciudades no visitadas
                    feromona = self.feromonas.get_value(ciudad_actual, i)  # Feromonas en el camino
                    distancia = self.distancias.get_value(ciudad_actual, i)  # Distancia entre las dos ciudades
                    visibilidad = 1 / distancia if distancia != 0 else float('inf')  # Visibilidad
                    probabilidad = (feromona ** self.alpha) * (visibilidad ** self.beta)
                    probabilidades.append(probabilidad)
                else:
                    probabilidades.append(0)

            # Normalizamos las probabilidades para que sumen 1
            suma_probabilidades = sum(probabilidades)
            if suma_probabilidades > 0:
                probabilidades = [p / suma_probabilidades for p in probabilidades]

            # Elegimos la siguiente ciudad utilizando la ruleta
            ruleta = random.random()
            acumulado = 0.0
            for i, probabilidad in enumerate(probabilidades):
                acumulado += probabilidad
                if ruleta <= acumulado:
                    siguiente_ciudad = self.ciudades[i]
                    resultado.append(siguiente_ciudad)
                    self.ciudades_visitadas[siguiente_ciudad] = False
                    break

        return resultado
