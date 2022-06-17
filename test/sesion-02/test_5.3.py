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

"""Aplicando herencia"""
"""Creando nuestra clase hijo"""
class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False

carro1 = Carro("Rojo", 30)
carroVolador = CarroVolador("Blanco", 40)

print("El color de mi carro volador es: ", carroVolador.color)
print("El estado volando de mi carro volador es: ", carroVolador.estadoVolando)

"""aqui aplicamos el efecto de herencia al usar el metodo de la clase padre"""
carroVolador.acelera()
carroVolador.acelera()

print("La velocidad actual de mi carro volador es: ", carroVolador.velocidad)

"""Esto no puede ocurrir"""
#print("El estado de vuelo de mi carro volador es: ", carro1.estadoVolando)