""" Manejo de archivos """

""" w: abre el archivo para poder escribir sobre el """
file = open("myfiles/file.txt", "w")

file.write("Lenguaje multiplataforma: python\n")
file.write("Esta basado en POD\n")
file.write("Basado en diferentes paradigmas de programación")

file = open("myfiles/file.txt", "r")

print("nuestro file tiene el sgt contenido: ", file.read())

""" cierre del archivo """
file.close()