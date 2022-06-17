""" uso del flujo condicional if """

edad = int(input("cual es su edad?: "))

if 0 < edad < 18:
    print("usted es menor de edad")
elif 18 < edad and edad < 65:
    print("ud es una persona adulta")
elif edad > 65:
    print("ud es una persona de tercera edad")
else:
    print("ud ha ingresado una edad erronea")

