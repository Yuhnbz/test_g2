"""estructura de datos: listas"""
"""eliminando un dato de una lista indicando el indice, usando el comando 'del' """

lista = []
lista.append(2022)
lista.append("Mayo")
lista.append("Python modulo I")
lista.append(30)

print(lista)

del lista[1]
print("la lista quedó asi: ",lista)

"""no es posible eliminar un elemento fuera de rango de elementos de la lista"""
