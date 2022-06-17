"""Programacion orientada a objetos"""

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

carro1 = Carro("Azul", 15)

print("la velocidad inicial del carro 1 es: ", carro1.velocidad)
carro1.acelera()
carro1.acelera()
carro1.acelera()

print("la velocidad final de mi carro luego de acelerarlo 3 veces es: ", carro1.velocidad)
carro1.frena()
carro1.frena()

print("la velocidad final de mi carro luego de frenarlo 2 veces es: ", carro1.velocidad)