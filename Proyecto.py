import os
import numpy as np  # Necesitamos numpy para calcular la desviación estándar
from Ciudad import *
from TSP import *
from Reader import *
from Random_Solution_Generator import *
from Hormiga import *
from Hormiga_Superciudad import *
from Tabla_de_Distancias import *
from Superciudad_Generator import *
import matplotlib.pyplot as plt

# Leemos un archivo y generamos un problema de TSP
tsp = TSP.read_lines(Reader.read("Berlin52.txt"))

# Definir las carpetas donde se guardarán los resultados
carpeta1 = 'ACO/Berlin'
carpeta2 = 'ACO_H/Berlin'

# Crear las carpetas si no existen
os.makedirs(carpeta1, exist_ok=True)
os.makedirs(carpeta2, exist_ok=True)

# Generamos la colonia de hormigas normales y generamos caminos
colonia1 = Hormiga.generate_colony(6, tsp.longitud(), tsp.get_Feromonas())

# Iteración de ACO normal
for i in range(20):
    paths1, scores1 = tsp.ACO(colonia1, 20, 1, 3)
    
    # Calcular la aptitud promedio y la desviación estándar
    aptitud_promedio = sum(scores1) / len(scores1)
    desviacion_estandar = np.std(scores1)
    
    # Formatear el resultado en una cadena para guardarlo en un archivo
    string1 = "Caminos: {}\nAptitudes:{}\nAptitud Promedio: {}\nDesviación Estándar: {}\nMejor Valor: {}\nPeor Valor: {}".format(paths1,scores1, aptitud_promedio, desviacion_estandar, min(scores1),max(scores1))
    
    # Aseguramos que el nombre del archivo sea correcto, incluyendo el índice
    archivo = os.path.join(carpeta1, 'berlin{}.txt'.format(i + 1))  # Usamos i+1 para el número de archivo
    with open(archivo, 'w') as f:
        f.write(string1)
    
    print(f"Resultado de la iteración {i+1} guardado en {archivo}")
    
    #Generamos la gráfica dentro de la carpeta
    plt.plot( scores1)
    
    plt.title('Gráfica de Aptitud Berlin {}'.format(i+1))
    plt.xlabel('Segundos')
    plt.ylabel('Aptitud')
    
    plt.legend()
    
    ruta_archivo = os.path.join(carpeta1, 'Berlin52_{}.png'.format(i+1))
    plt.savefig(ruta_archivo)

    # Limpiamos las feromonas después de cada iteración
    plt.clf()
    tsp.clean_table()


    # Generamos la colonia de hormigas con heurística
    colonia2 = Hormiga_Superciudad.generate_colony(6, tsp.get_Feromonas(), tsp.longitud(), tsp.get_Distancias())

    # Ejecutamos el ACO con la colonia de superciudad
    paths2, scores2 = tsp.ACO_Superciudad(colonia2, 20, 1, 3)

    # Calcular la aptitud promedio y la desviación estándar para la colonia de superciudad
    aptitud_promedio_superciudad = sum(scores2) / len(scores2)
    desviacion_estandar_superciudad = np.std(scores2)

    # Guardar los resultados de ACO Superciudad
    string2 = "Caminos: {}\nAptitudes{}:\nAptitud Promedio: {}\nDesviación Estándar: {}\nMejor Valor: {}\nPeor Valor: {}".format(paths2, scores2,aptitud_promedio_superciudad, desviacion_estandar_superciudad, min(scores1),max(scores1))

    # Guardar el resultado de la colonia heurística en otro archivo
    archivo2 = os.path.join(carpeta2, 'berlin_superciudad.txt')
    with open(archivo2, 'w') as f:
        f.write(string2)

    print(f"Resultado de ACO Superciudad guardado en {archivo2}")
    
    #Generamos la gráfica dentro de la carpeta
    plt.plot( scores2)
    
    plt.title('Gráfica de Aptitud Berlin {}'.format(i+1))
    plt.xlabel('Segundos')
    plt.ylabel('Aptitud')
    
    plt.legend()
    
    ruta_archivo = os.path.join(carpeta2, 'Berlin52_{}.png'.format(i+1))
    plt.savefig(ruta_archivo)

    # Limpiamos las feromonas después de cada iteración
    plt.clf()
    tsp.clean_table()
