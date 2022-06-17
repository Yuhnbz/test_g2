
file = open("../my_files/agenda.txt", "a+")

file.close()

def AñadirCliente(nombre, telefono):
    try:
        file = open(nombre, telefono)
        datos = ["\nJuan ", ",", "958665474"]
        file.close()
        return file
    except OSError as err: #tipo de error de apertura de archivo
        print("Error de lectura {}".format(err))


fileWrite = "../my_files/agenda.txt"
print(AñadirCliente(nombre="Juan", telefono="a"))
AñadirCliente(fileWrite, "r")

