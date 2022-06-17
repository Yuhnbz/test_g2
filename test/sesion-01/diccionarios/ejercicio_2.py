"""
Crear un diccionario con 6 nombre de cursos que llevas o llevaste en el pregrado
-Borrar cualquier curso usando del
-comprobar que un curso este en el diccionario
-Ingresar el nombre de tu carrera dentro de los valores q tiene el diccionario
-Mostrar en consola los valores de su variable final (lista)

"""

miDiccionario = {"programacion", "curso2", "curso3", "curso4", "curso5", "curso6"}

print("mi diccionario es", miDiccionario)
"""borrando"""
del miDiccionario["programacion"]
print("mi diccionario es", miDiccionario)
