""" Manejo de excepciones"""

""" Manejo del error de division entre cero y tipo de datos """
""" multiples except en una sola linea """

try:
    #val1 = 5/0
    val2 = 2 + "hola pythonistas"
except (ZeroDivisionError, TypeError):
    print("error division entre cero, TypeError")