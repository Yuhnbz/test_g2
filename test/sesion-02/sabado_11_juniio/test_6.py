""" Manejo de archivos """

def fileManipulation(dir, node):

    try:
        file = open(dir, node)
        print(file.read())
        file.close()
        return file
    except OSError as err: #tipo de error de apertura de archivo
        print("Error de lectura {}".format(err))

fileWrite = "myfiles/file2.txt"

print("Lectura de un archivo")
fileManipulation(fileWrite, "r")

""" Lectura de un archivo que no existe """
fileWrite2 = "myfiles/file10.txt"

fileManipulation(fileWrite2, "r")