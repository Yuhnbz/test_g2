""" uso del flujo condicional if """

#var1 = 100
#var2 = 200
var1 = int(input("ingrese el primer valor "))
var2 = int(input("ingrese el segundo valor "))


if var1 >= var2: #si es verdadero ejecuta la logica interna del flujo condicional
    print("el primer valor es mayor que el segundo")
    print("Es verdadero")
else:
    print("el segundo valor no es mayor que el primero")
    print("la sentencia es falsa")