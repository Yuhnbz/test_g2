"""programacion funcional"""

def multiplicar(a, b, c=10):
    resultado = a*b*c
    return resultado

print("el resultado es: ",multiplicar(40, 2, 2))
"""aunq exista un valor por defecto en la funcion, los valores ingresados manualmente tienen prioridad"""