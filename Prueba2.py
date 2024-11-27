from Ciudad import *
from TSP import *
from TSP_Extendido import *
from Hormiga import *
from Hormiga_Superciudad import *
import sklearn


# Definir un conjunto de ciudades
ciudades = [
    Ciudad(0, 0, 0),
    Ciudad(1, 2, 3),
    Ciudad(2, 5, 1),
    Ciudad(3, 6, 4),
    Ciudad(4, 8, 0)
]

# Crear una instancia TSP_Extended
tsp = TSP_Extendido(ciudades)

# Crear tabla de feromonas y tabla de distancias
tabla_feromonas = Tabla_de_Feromonas(len(ciudades))
tabla_distancias = tsp.tabla_de_distancias

# Crear una hormiga básica
hormiga = Hormiga(tabla_feromonas, len(ciudades))

# Generar un recorrido
recorrido = hormiga.generate()

# Imprimir el recorrido
print("Recorrido generado por hormiga básica:", recorrido)

# Agrupar ciudades en superciudades (por ejemplo, 2 grupos)
superciudades = tsp.agrupar_superciudades(num_superciudades=2)

# Crear una instancia de Hormiga_Superciudad
hormiga_superciudad = Hormiga_Superciudad(tabla_feromonas, len(superciudades), tabla_distancias)

# Generar un recorrido entre superciudades
recorrido_superciudad = hormiga_superciudad.generate()

# Imprimir el recorrido
print("Recorrido generado por hormiga de superciudades:", recorrido_superciudad)

# Crear una colonia de hormigas para el TSP base
colonia = [Hormiga(tabla_feromonas, len(ciudades)) for _ in range(10)]

# Ejecutar ACO en la instancia TSP base
caminos, puntajes = tsp.ACO(colonia_de_hormigas=colonia, tiempo_segundos=10, incremento=1.0)

# Imprimir los mejores caminos encontrados
print("Caminos óptimos TSP base:", caminos)
print("Puntajes TSP base:", puntajes)

# Crear una colonia de hormigas para superciudades
colonia_superciudad = [Hormiga_Superciudad(tabla_feromonas, len(superciudades), tabla_distancias) for _ in range(5)]

# Ejecutar ACO en las superciudades
caminos_superciudad, puntajes_superciudad = tsp.ACO(colonia_de_hormigas=colonia_superciudad, tiempo_segundos=10, incremento=1.0)

# Imprimir los mejores caminos encontrados entre superciudades
print("Caminos óptimos Superciudades:", caminos_superciudad)
print("Puntajes Superciudades:", puntajes_superciudad)



print("Distancia total mejor camino base:", tsp.evaluar_recorrido_tsp(caminos[-1]))
print("Distancia total mejor camino superciudad:", tsp.evaluar_recorrido_tsp(caminos_superciudad[-1]))
