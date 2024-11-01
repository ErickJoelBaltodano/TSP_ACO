from Ciudad import *
from TSP import *
from Reader import *
from Solucion import *



documento = str(input("Ingrese el nombre del archivo:  "))
tsp =TSP.read_lines(Reader.read (documento))

camino_aleatorio =Solucion.permutación_aleatoria_tsp(tsp.longitud(),5)

print (camino_aleatorio)
numero1 = tsp.evaluar_recorrido_tsp(camino_aleatorio)
print ("==============================================================================================================================================")
print (numero1)
maximo = tsp.arista_de_mayor_peso(camino_aleatorio)
print ("==============================================================================================================================================")

print ( "La arista mayor del camino es:  {} - {} con una longitud de {}.".format(maximo[0],maximo[1],maximo[2]))


