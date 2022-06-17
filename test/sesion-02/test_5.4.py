"""POO en python"""
"""Encapsulamiento"""

class A():

    def __init__(self):
        """Encapsulamiento"""
        self._contador = 0 #definiendo mis atributos como privados usando el " _ "

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador

class B():

    def __init__(self):
        """Encapsulamiento"""
        self.__contador = 0 #definiendo mis atributos como privados usando el " __ "

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador


varA = A()
varA._contador
varA.inicial = False
varA.incrementa()
varA.incrementa()
print(varA.cuenta())
print(varA.inicial)
"""Si es posible indicarlo pero solo se hace ..."""


varB = B()
varB.inicial = False
varB.incrementa()
varB.incrementa()
varB.incrementa()
print(varB.cuenta())
print(varB.inicial)
"""No es posible indicarlo porq el encapsulamiento es fuerte por los 2 guiones bajos"""
