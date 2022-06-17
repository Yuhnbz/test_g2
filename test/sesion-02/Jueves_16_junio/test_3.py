"""Decoradores en python"""

""" Creación de función decoradora """

def funcionA(funcionB):
    def funcionC(*args, **kwargs):

        print("antes de ejecutar la funcion a decorar")

        resultado = funcionB(*args, **kwargs)

        return resultado

    return funcionC

@funcionA
def suma (a, b, c):
    s = a + b + c
    return print(s)


suma(30, 40, 70)