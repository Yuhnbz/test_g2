""" Manejo de archivos """
""" Apertura y lectura de archivos """

""" r: Leer archivo """
file = open("../myfiles/file.txt", "r")

print("Contenido de nuestro archivo: ", file.read())
#siempre debemos cerrar el archivo que hemos abierto al inicio
file.close()