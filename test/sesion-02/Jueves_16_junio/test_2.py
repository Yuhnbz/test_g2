"""Decoradores en python"""

""" Creación de función decoradora """
def funcionA(funcionB):
    """ funcion interna de la funcion decoradora """
    def funcionC(*args, **kwargs):  #*args, **kwargs: recibir "n" parametros que tenga la funcion
        print("Antes de ejecutar la función a decorar") # 1er bloque de codigo
        resultado = funcionB(*args, **kwargs)
        print("Despues de ejecutar la funcion a decorar") # 2do bloque de codigo

        return resultado
    return funcionC()


""" funcion a decorar """
@funcionA
def saludar(nombre):
    return print("Hola {}".format(nombre))

saludo = input("ingrese su nombre: ")
print(saludar(saludo))
