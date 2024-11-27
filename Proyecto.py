from Ciudad import *
from TSP import *
from Reader import *
from Random_Solution_Generator import *
from Hormiga import *
from Ciudad import *
from Hormiga_Superciudad import *
from Tabla_de_Distancias import *
"""Leemos un archivo y generamos un problema de TSP"""
tsp =TSP.read_lines(Reader.read ("Berlin52.txt"))
for x in tsp.lista_de_ciudades:
    print (x)


    
tabla_D= Tabla_de_Distancias(tsp.lista_de_ciudades)
tabla_F= Tabla_de_Feromonas (tsp.longitud())


tsp.get_tablas(tabla_F,tabla_D)

print (tabla_D == tsp.tabla_de_distancias)
for x in tabla_F.tabla:
    print (len(x))
"""Generamos la colonia de hormigas normales"""





"""Limpiamos las Feromonas de nuestro modelo del TSP"""


"""Generamos la colonia de hormigas con heurística"""



