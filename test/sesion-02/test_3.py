"""programacion funcional en python"""

var1 = 50
var2 = 100

"""input 2 variables por parametro"""
def sumar(a, b):
    suma = a + b
    return suma
"""output lo q retorna la funcion"""


sumar(var1, var2)
print("la suma es: {}".format(sumar(var1, var2)))
