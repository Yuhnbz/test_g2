""" Gestion de errores """
""" Estructura y uso """

while True:
    try:
        numero = input("ingrese numero entero: ")

    except: #aqui se activara una accion si ocurre cierto tipo de error dentro del try
        print("no es un valor entero")