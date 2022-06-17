"""Decoradores en python"""

""" Creación de función decoradora """
def funcionA(funcionB):
    """ funcion interna de la funcion decoradora """
    def funcionC():
        print("Antes de ejecutar la función a decorar")
        funcionB()
        print("Despues de ejecutar la funcion a decorar")

    return funcionC()


""" funcion a decorar """
@funcionA
def saludar():
    print("Hola Susana")