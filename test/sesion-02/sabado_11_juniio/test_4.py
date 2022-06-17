""" Manejo de archivos """

tecnologiasBackend = ["\nPython ", "Java ", "Ruby ", "NodeJS "]
tecnologiasFrontend = ["\nAngular ", "Javascript ", "ReactJS ", "Boostrap "]

""" Apertura de nuestro archivo """

""" a+: Permite escribir varias lineas de codigo al abrir nuestro archivo """
""" Escribe nuevas lineas sin borrar las lineas escritas previamente en el archivo """
file = open("myfiles/file2.txt", "a+")

""" writeLines: Permite escribir los datos de una lista """
file.writelines(tecnologiasBackend)

file.writelines(tecnologiasFrontend)

file = open("myfiles/file2.txt", "r")

print("El contenido de nuestro file es:", file.read())

"""cerrando"""
file.close()
