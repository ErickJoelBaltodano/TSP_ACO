from TSP import *
from Ciudad import *

class Reader:

    @staticmethod
    def read(documento: str):
        lista = []
        try:
            with open(documento, 'r') as file:
                lines = file.readlines()
                iteraciones  = int(lines[6])
                x = 7
                while (x < (iteraciones + 7)):
                    lista.append(lines[x])
                    x = x +1

        except FileNotFoundError:
            print(f"El archivo {documento} no se encontró.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

        return lista


    @staticmethod
    def abrir_solucion(nombre_archivo):
        arreglo = []
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                arreglo.append(int(linea.strip()))
        return arreglo

    @staticmethod
    def guardar_solucion(arreglo,nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            for elemento in arreglo:
                archivo.write(f"{elemento}\n")