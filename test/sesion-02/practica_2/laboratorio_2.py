
class Persona:
    """atributos"""
    nombre = "Juan"
    saldo = "saldo"

    """Constructor"""
    def __init__(self, edad, nacionalidad):
        self.edad = int(edad)
        self.nacionalidad = "Peruana"

    """Metodos"""

    def cumpleaños(self):
        self.edad = 1 + self.edad

    def saldo(self):
