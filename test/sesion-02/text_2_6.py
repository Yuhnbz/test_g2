"""entradas y salidas con python"""

edad = input("por favor ingrese su edad: ")
print("el tipo de mi variable edad es: ", type(edad))

talla = input("ingrese su talla en cm: ")

"""convirtiendo nuestra edad"""
print("el nuevo tipo de dato de nuestra variable edad es: ", type(int(edad)))

"""convirtiendo el valor de nuestra variable"""
print("el nuevo tipo de dato de nuestra variable talla es: ", type(float(talla)))
print("el nuevo tipo de dato de nuestra variable talla a entero es: ", type(int(float(talla))))

print("al convertir mi nuevo valor a tipo entero tiene como dato lo siguiente: ", int(float(talla)))