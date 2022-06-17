""" uso del for """

ingenierias = ("software", "sistemas", "industrial", "mecanica")
i=0

nombre = input("ingrese su primer nombre: ")

print("el tamaño de nuestra lista es: {}, programa creado por: {}".format(len(ingenierias), nombre))

for ingenieria in ingenierias:
    print("ingenieria", ingenieria)
    i += 1
    print("esta es la vuelta #", i)

print("llego al final del for")