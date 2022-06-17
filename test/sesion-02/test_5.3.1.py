"""Programacion orientada a objetos"""

"""Herencia multiple"""

class Carro:
    """atributos"""
    ruedas = 4

    """constructor: valores que va a tener por defecto mi clase cuando se instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Metodos: son las funciones de la clase"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad<0:
            velocidad = 0
        self.velocidad = velocidad


class CarroSedan():

    def __init__(self):
        self.tamanio = 150

"""Aplicando herencia nultiple"""
"""Creando nuestras clases hijo"""
class CarroVolador(Carro, CarroSedan):

    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False



carroVolador = CarroVolador("Negro", 40)

"""Herencia del primer padre"""
print("la velocidad inicial de mi carro volador es: ", carroVolador.velocidad)

"""Herencia del segundo padre"""
print("El tamaño de mi carro volador es: ", carroVolador.tamanio)


