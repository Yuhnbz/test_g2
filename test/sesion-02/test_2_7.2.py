""" uso del bucle while """

year = 2011

while year < 2022:
    print("informes del año: ", year)
    year += 1

    if year == 2019:
        break #fuerza el final del bucle while o de cualquier condicional

print("llego al final de nuestra sentencia while")