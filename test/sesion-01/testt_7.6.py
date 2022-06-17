"""estructura de datos"""
"""Listas: cantidad de veces que se repite un elemento en una lista"""

lista = ["python", "java", "php", "ruby"]

"""limpiando elementos"""
lista.append("python")
lista.append("php")
lista.append("python")

lista.count("python")
print("el nuevo valor de mi lista es: ", lista)
print("python se repite: ", lista.count("python"))