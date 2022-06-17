""""ejercicio de lista"""
"""crear un programa q contenga 20 numero aleatorios"""
"""Mostrar en pantalla su cuadrado y su cubo"""

import random
listaNumeros = []

for indice in range(1,21):
    """print(indice)"""
    listaNumeros.append(random.randint(1,21))

print(listaNumeros)

"""contar los elementos de una lista"""
print(len(listaNumeros))

"""segundo recorrido"""
for numero in listaNumeros:
    print(numero, "cuadrado:", numero**2, "cubo:", numero**3)