"""problema 1"""

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))

print("el tipo de dato del nombre es: ", type(nombre))
print("el tipo de dato de la edad es: ", type(edad))

nombre1 = input("ingrese el nombre de la persona 1: ")
edad1 = int(input("ingrese la edad de la persona 1: "))
nombre2 = input("ingrese el nombre de la persona 2: ")
edad2 = int(input("ingrese la edad de la persona 2: "))
suma = edad1 + edad2

print("la suma de las edades de", nombre1, "y", nombre2, "es:", suma)