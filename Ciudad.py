import math 
class Ciudad:

    def __init__(self,id:int ,coordenadax: float, coordenaday: float):
        self.id = id
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday


    #Getters
    def get_coordenadax (self):
        return self.coordenadax

    def get_coordenaday (self):
        return self.coordenaday


    @staticmethod
    def read_line(linea: str):
        try:
            # Divide la línea en partes usando el espacio como separador
            partes = linea.split()
            
            # Verifica que la línea tenga exactamente 3 partes
            if len(partes) != 3:
                raise ValueError("La línea debe contener exactamente 3 partes.")
            
            # Asigna las partes a las variables correspondientes
            id_temp = int(partes[0])          # Convertir el primer elemento a entero
            x_temp = float(partes[1])         # Convertir el segundo elemento a float
            y_temp = float(partes[2])         # Convertir el tercer elemento a float
            
            # Crea una instancia de la clase Ciudad
            ciudad = Ciudad(id_temp, x_temp, y_temp)
            
        except ValueError as ve:
            print(f"Error en los datos de entrada: {ve}")
            ciudad = None
        except Exception as ex:
            print(f"Argumentos no válidos: {ex}")
            ciudad = None
        
        return ciudad

    #Método en el cual calculamos la distancia euclidiana una ciudad y otra ciudad.
    @staticmethod 
    def distancia_euclidiana(ciudad1:'Ciudad' , ciudad2: 'Ciudad'):  
        x = ciudad1.get_coordenadax()- ciudad2.get_coordenadax()
        y = ciudad1.get_coordenaday()- ciudad2.get_coordenaday()
        x = x * x
        y = y * y
        numero = x +y
        return math.sqrt(numero)


    #Método que nos da la representación en cadena de una ciudad.
    def __str__(self):
        cadena = ""
        cadena += (str(self.id)+ " ")
        cadena += (str(self.coordenadax)+ " ")
        cadena += str(self.coordenaday)
        return cadena
        

   