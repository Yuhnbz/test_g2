""" manejo de cadenas """

cadena = "Conexion a base de datos con Python"

cadena2 = cadena.replace(cadena[0:6],"CC")

print("cadena con reemplazo: {}".format(cadena2))

"""eliminando espacios en blanco de mi cadena"""

"""eliminando espacios de la izquierda"""
cadena3 = "     Conexion a base de datos con Python"
cadena4 = cadena3.lstrip()
print("mi cadena sin espacios en blanco es: {}".format(cadena4))

"""eliminando espacios de la derecja"""
cadena5 = "Conexion a base de datos con Python       "
cadena6 = cadena5.rstrip()
print("mi cadena sin espacios en blanco es: {}".format(cadena6))

texto = '   Hola Python   '
print(texto)
texto2 = texto.strip()
print(texto2)