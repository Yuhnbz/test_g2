"""ejercicios de listas"""
"""Crear una lista con 10 valores aleatorios"""
"""ordenar los elementos de mayor a menor"""

import random

miLista = []

for indice in range(1,11):
    miLista.append(random.randint(1,30))

"""ordenando la lista"""
miLista.sort()

"""segundo recorrido"""
"""quitando la lista"""
for numero in miLista:
    print(numero, " ", end="")