""" tipos de datos basicos """

valor1 = 15
valor2 = 8
suma = valor1 + valor2
resta = valor1 - valor2

print("mi suma es : ", suma)
print("mi resta es : ", resta)

""" flotantes: numero decimales """

real = 1.1 + 2.2

print("el valor de mi variable tipo flotante es: ", real)
print(f"{real:.5f}")

""" conocer el tipo de dato de mi variable """
print("el tipo de dato de mi variable suma es: ",type(suma))

""" conocer el tipo de dato de mi variable """
print("el tipo de dato de mi variable real es: ",type(real))

"""conversion de tipo de datos"""
print("conversion de tipo flotante a entero:", int(real))