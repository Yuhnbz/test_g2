"""" manejo de cadenas """
""" concatenación"""

nombre = "luke"
apellido = "skywalker"

nombreCompleto = "el nombre completo del usuario es: "+ nombre + " " + apellido
print(nombreCompleto)

"""usando el format"""
nombreCompleto2 = "el nombre completo del usuario es: {} {}".format(nombre,apellido)
print(nombreCompleto2)