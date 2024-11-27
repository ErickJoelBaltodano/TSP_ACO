from sklearn.cluster import KMeans
import numpy as np
from TSP import *

class TSP_Extendido(TSP):
    def __init__(self, lista_de_ciudades):
        super().__init__(lista_de_ciudades)

    # Método para agrupar ciudades en superciudades
    def agrupar_superciudades(self, num_superciudades):
        # Extraemos las coordenadas de las ciudades
        coordenadas = np.array([[ciudad.coordenadax, ciudad.coordenaday] for ciudad in self.lista_de_ciudades])
        
        # Usamos K-Means para agrupar ciudades
        kmeans = KMeans(n_clusters=num_superciudades, random_state=42)
        kmeans.fit(coordenadas)
        
        # Asignamos etiquetas a cada ciudad
        etiquetas = kmeans.labels_
        
        # Creamos los grupos de superciudades
        superciudades = {i: [] for i in range(num_superciudades)}
        for i, etiqueta in enumerate(etiquetas):
            superciudades[etiqueta].append(self.lista_de_ciudades[i])
        
        return superciudades

    # Método para generar caminos entre superciudades
    def generar_caminos_superciudades(self, superciudades, metodo='centroide'):
        caminos = {}
        
        # Calculamos el centroide o punto representativo para cada superciudad
        representativos = {}
        for clave, ciudades in superciudades.items():
            if metodo == 'centroide':
                # Calculamos el promedio de las coordenadas
                x_prom = np.mean([ciudad.coordenadax for ciudad in ciudades])
                y_prom = np.mean([ciudad.coordenaday for ciudad in ciudades])
                representativos[clave] = (x_prom, y_prom)
            elif metodo == 'ciudad_cercana':
                # Tomamos una ciudad arbitraria como representante
                representativos[clave] = (ciudades[0].x, ciudades[0].y)
        
        # Generamos caminos entre superciudades
        superciudades_ids = list(superciudades.keys())
        for i in range(len(superciudades_ids)):
            for j in range(i + 1, len(superciudades_ids)):
                id1, id2 = superciudades_ids[i], superciudades_ids[j]
                punto1, punto2 = representativos[id1], representativos[id2]
                
                # Calculamos la distancia entre los puntos representativos
                distancia = np.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)
                
                # Almacenamos el camino
                caminos[(id1, id2)] = distancia
        
        return caminos