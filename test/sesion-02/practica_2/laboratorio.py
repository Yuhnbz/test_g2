
class Persona:

    """Atributos"""
    nombre = "Juan"

    """Constructor"""
    def __init__(self, edad, nacionalidad):
        self.edad = int(edad)
        self.nacionalidad = "Peruana"

    """Metodos"""
    def cumpleaños(self):
        self.edad = 1 + self.edad


nuevaPersona = Persona(25, "nacionalidad")
print("la edad de mi persona es", nuevaPersona.edad)
print("la nacionalidad de mi persona es", nuevaPersona.nacionalidad)

nuevaPersona.cumpleaños()
nuevaPersona.cumpleaños()

print("la edad de mi persona es: ", nuevaPersona.cumpleaños())