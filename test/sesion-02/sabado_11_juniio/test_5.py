"""" Manejo de archivos """

tecnologiasBackend = ["\nPython", "\nJava"]

file = open("myfiles/file3.txt", "a+")

file.writelines(tecnologiasBackend)

file = open("myfiles/file3.txt", "r")

for newLine in file:
    if newLine.find("M"):
        print(newLine)
        print("Ha encontrado un varón")

""" cerrando el archivo abierto """
file.close()