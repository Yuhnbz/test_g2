""" Manejo de excepciones"""

""" Manejo del error de division entre cero """

try:
    val1 = 5/0
    val2 = 2 + "hola pythonistas"
except ZeroDivisionError:
    print("no es posible dividir entre 0")
except TypeError:
    print("Problema de tipo de datos")