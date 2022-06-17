"""Programacion orientada a objetos"""

class Carro:
    """atributos"""
    ruedas = 4

    """constructor: valores que va a tener por defecto mi clase cuando se instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion

    """Metodos: son las funciones de la clase"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad<0:
            velocidad = 0
        self.velocidad = velocidad

""" instanciamos nuestra clase """
carro1 = Carro("Negro", 50)
print("El color de mi primer carro es: ", carro1.color)
print("La aceleracion de mi primer carro es: ", carro1.aceleracion)
print("la cantidad total de ruedas de mi primer carro es: ", carro1.ruedas)

carro2 = Carro("Blanco", 30)
print("El color de mi segundo carro es: ", carro2.color)
print("la aceleracion de mi primer carro es: ", carro2.aceleracion)
print("la cantidad total de ruedas de mi primer carro es: ", carro2.ruedas)