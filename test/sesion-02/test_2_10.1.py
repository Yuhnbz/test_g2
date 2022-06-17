"""manejo de caracteres"""
"""encontrar el indice de una cadena a partir de una cadena mayor"""

nombre = input("ingrese su nombre: ")
mensaje = "bienvenido {}".format(nombre)
print(mensaje)

indice = mensaje.find(nombre)

print("el indice que muestra nuestra subcadena mayor es: ", indice)

mensaje[0:indice].format(": ")
print("mi cadena modificada es la siguiente: {}".format(mensaje))