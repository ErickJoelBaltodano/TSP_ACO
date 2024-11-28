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

   

"""Generamos la colonia de hormigas normales y generamos caminos"""
colonia1 =Hormiga.generate_colony(6,tsp.longitud(),tsp.get_Feromonas())

print ("Calculando ...")
paths1,scores1=tsp.ACO(colonia1,30,1,4)
x = 0 
while x < len(paths1):
    print ("Camino: {} Valor: {}".format(paths1[x],scores1[x]))
    x +=1



"""Limpiamos las Feromonas de nuestro modelo del TSP"""
#tsp.clean_table()


"""Generamos la colonia de hormigas con heurística"""



