import random
class Random_Solution_Generator:

    #Método que nos genera una permutación aleatoria desde el 1 hasta el número longitud
    @staticmethod
    def permutación_aleatoria(longitud:int):
        arr = list(range(1, longitud + 1))
        random.shuffle(arr)
        return (arr)
        

    #Método que nos genera una permutación aleatoria pero elimina pero nos deja siempre a la ciudad inicial al principio.
    @staticmethod
    def permutación_aleatoria_tsp(longitud:int,ciudad: int ):
        arr = list(range(1, longitud + 1))
        arr.remove(ciudad)
        random.shuffle(arr)
        arr.insert(0,ciudad)
        return (arr)
        
