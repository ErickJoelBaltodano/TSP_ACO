import random
from TSP import *
from Superciudad import *

class Superciudad_Generator:
    
    # Método donde generamos superciudades y generamos caminos entre las ciudades que las conforman.
    @staticmethod
    def generate(n, dimension,tabla_de_distancias):
        # Escogemos n ciudades base aleatorias
        ciudades_base = [random.randint(0, dimension - 1) for _ in range(n)]

        # Agrupamos las superciudades según su cercanía
        grupitos = [[] for _ in range(n)]  # Lista para almacenar grupos de ciudades

        for ciudad in range(dimension):
            # Comparamos las distancias de cada ciudad con las ciudades base
            mejor_distancia = None
            ciudad_base_mas_cercana = None

            for ciudad_base in range(len(ciudades_base)):
                distancia = tabla_de_distancias.get_value(ciudad, ciudades_base[ciudad_base])

                # Si encontramos una distancia mejor, actualizamos
                if mejor_distancia is None or distancia < mejor_distancia:
                    mejor_distancia = distancia
                    ciudad_base_mas_cercana = ciudad_base

            # Agregamos la ciudad al grupo más cercano
            grupitos[ciudad_base_mas_cercana].append(ciudad)

        # Generamos las superciudades a partir de los grupos de ciudades
        superciudades = [
            Superciudad(ciudades_base[i], tabla_de_distancias, grupitos[i]) for i in range(n)
        ]
       
        return superciudades
