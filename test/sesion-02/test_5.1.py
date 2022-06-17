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


carro1 = Carro("Rojo", 20)
print("El color de mi primer carro es: ", carro1.color)

carro2 = Carro("Blanco", 30)
"Se le asignará un atributo de dato a la instancia de nuestro segundo carro"

carro2.marchas = 1000
print("El número de marchas de mi carro es: ", carro2.marchas)

"""no es posible llamar a un atributo de dato que se le ha dado a otra instancia de clase"""
print("El número de marchas de mi primer carro es: ",carro1.marchas)