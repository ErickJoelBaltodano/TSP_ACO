from Ciudad import *
from Hormiga import *
from Tabla_de_Feromonas import *
from Tabla_de_Distancias import *

class Hormiga_Superciudad(Hormiga):
    # Método constructor que hereda de la clase base Hormiga
    def __init__(self, tabla_de_feromonas: Tabla_de_Feromonas, dimension, tabla_de_distancias: Tabla_de_Distancias):
        super().__init__(tabla_de_feromonas, dimension)
        self.distancias = tabla_de_distancias
        self.alpha = 1.0
        self.beta = 2.0
    
    # Sobreescribimos el método generate de la clase Hormiga
    def generate(self):
        # Inicializamos la lista para almacenar el camino generado
        resultado = []

        # Elegimos una ciudad inicial de manera aleatoria
        ciudad_actual = random.randint(0, self.dimension - 1)
        resultado.append(ciudad_actual)
        
        # Mantenemos un conjunto de ciudades visitadas para evitar ciclos
        visitadas = set(resultado)
        
        # Construimos el camino hasta que hayamos visitado todas las ciudades
        while len(visitadas) < self.dimension:
            # Obtenemos las probabilidades de transición a las ciudades no visitadas
            probabilidades = self.calcular_probabilidades(ciudad_actual, visitadas)
            
            # Elegimos la siguiente ciudad basada en las probabilidades
            ciudad_siguiente = self.seleccionar_ciudad(probabilidades)
            resultado.append(ciudad_siguiente)
            visitadas.add(ciudad_siguiente)
            
            # Actualizamos la ciudad actual
            ciudad_actual = ciudad_siguiente
        
        # Retornamos al punto de inicio para cerrar el circuito (opcional, si es TSP clásico)
        resultado.append(resultado[0])
        
        return resultado

    # Método para calcular las probabilidades de transición
    def calcular_probabilidades(self, ciudad_actual, visitadas):
        probabilidades = []
        suma_total = 0.0

        for ciudad in range(self.dimension):
            if ciudad not in visitadas:
                # Recuperamos la feromona y la distancia
                feromona = self.feromonas.get_value(ciudad_actual, ciudad)
                distancia = self.distancias.get_value(ciudad_actual, ciudad)
                
                # Calculamos el peso (inversamente proporcional a la distancia)
                peso = (feromona ** self.alpha) * ((1 / distancia) ** self.beta)
                probabilidades.append((ciudad, peso))
                suma_total += peso
        
        # Normalizamos las probabilidades
        probabilidades = [(ciudad, peso / suma_total) for ciudad, peso in probabilidades]
        return probabilidades

    # Método para seleccionar la siguiente ciudad con base en las probabilidades
    def seleccionar_ciudad(self, probabilidades):
        # Generamos un número aleatorio para seleccionar la ciudad
        r = random.random()
        acumulado = 0.0

        for ciudad, probabilidad in probabilidades:
            acumulado += probabilidad
            if r <= acumulado:
                return ciudad
        
        # En caso de error numérico, devolvemos la última ciudad
        return probabilidades[-1][0]
