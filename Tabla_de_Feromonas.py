from Ciudad import *


class Tabla_de_Feromonas:
    
    # Método Constructor donde generamos la tabla de feromonas.
    def __init__(self, dimension:int):
        # Nota: Inicializamos todos los valores en 0.
        self.tabla = [[1 for _ in range(dimension)] for _ in range(dimension)]
    
    # Método donde regresamos el valor actual de la feromona dados dos vértices del TSP.
    def get_value(self, vertice1: int, vertice2: int):
        # Nota: NO IMPORTA EL ORDEN PUES LA TABLA ES SIMÉTRICA.
        return self.tabla[vertice1][vertice2]
    
    # Método donde incrementamos una determinada feromona dados dos puntos.
    def marcar_feromona(self, incremento: int, camino):
        # MARCAMOS AMBOS LADOS DE LA TABLA PARA QUE LA TABLA PERMANEZCA SIMÉTRICA.
        for i in range(len(camino) - 1):
            v1 = camino[i]
            v2 = camino[i + 1]
            self.tabla[v1][v2] = min(self.tabla[v1][v2] + incremento, 5)
            self.tabla[v2][v1] = min(self.tabla[v2][v1] + incremento, 5)  
            
            
    # Método donde decrementamos la feromona en los caminos que no fueron recorridos.
    def evaporacion(self):
        # Itera sobre toda la tabla para restar 1 a cada valor
        for i in range(len(self.tabla)):
            for j in range(len(self.tabla[i])):
                # Evita valores negativos; asegúrate de que no bajen de 1
                self.tabla[i][j] = max(1, self.tabla[i][j] - 1)
    
    
    # Método donde checamos las probabilidades de escoger la próxima ciudad dada una ciudad desde la cual partimos.
    def check_column(self,ciudad_base:int):
         # Sumamos de todas las feromonas de la fila correspondiente a la ciudad base.
        suma_total = sum(self.tabla[ciudad_base])
        
        # Si la suma es 0, todas las probabilidades son iguales (sin preferencia).
        if suma_total == 0:
            num_ciudades = len(self.tabla[ciudad_base])
            return [1/num_ciudades for _ in range(num_ciudades)]
        
        # Calcula la probabilidad para cada ciudad como el valor de la feromona dividido por la suma total.
        probabilidades =[]
        numero =0
        
        for h in range(len(self.tabla)):
            numero += self.tabla[ciudad_base][h]/suma_total
            probabilidades.append(numero)
        
        return probabilidades
        
        
    def clean(self,dimension):
        self.tabla = [[1 for _ in range(dimension)] for _ in range(dimension)]
