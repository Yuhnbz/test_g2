""" Manejo de excepciones"""

""" Manejo del type para saber que tipo de error ha ocurrido """

try:
    val1 = 2 / 0
except:
    print("entro al except, ocurrio una excepcion")
else:
    print("entro al else, no ha ocurrido ni una excepcion")