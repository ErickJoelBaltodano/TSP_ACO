from Ciudad import *
from TSP import *
from TSP_Extendido import *
import sklearn


# Uso del código:
lista_ciudades = [Ciudad(0, 1, 2), Ciudad(1, 5, 8), Ciudad(2, 2, 3), Ciudad(3, 7, 9)]
tsp = TSP_Extendido(lista_ciudades)

# Agrupamos en 2 superciudades
superciudades = tsp.agrupar_superciudades(2)

# Generamos caminos entre superciudades usando centroides
caminos = tsp.generar_caminos_superciudades(superciudades, metodo='centroide')

for x in superciudades:
    print (x)
print("Caminos entre Superciudades:", caminos)
