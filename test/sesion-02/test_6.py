"""POO en python"""
"""Polimorfismo"""

class Perro():
    def sonido(self):
        print("guauu")

class Gato():
    def sonido(self):
        print("miauu")

class Vaca():
    def sonido(self):
        print("muu")

vaca = Vaca()
perro = Perro()
gato = Gato()

listaAnimales = [vaca, perro, gato]

def cantar(animales):
    for animal in animales:
        animal.sonido()

"""Aplicando polimorfismo: Es el uso de los metodos que tienen el mismo nombre en diferentes clases"""
cantar(listaAnimales)