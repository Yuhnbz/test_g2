""" Manejo de excepciones"""

""" Manejo del type para saber que tipo de error ha ocurrido """

try:
    val1 = 2 + "hola"
except Exception as ex:
    print("Ha ocurrido una excepcion de tipo: ", type(ex))