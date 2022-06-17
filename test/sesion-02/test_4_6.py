"""
6. Escribir un programa que pida numero al usuario, mostrar el factorial de cada uno y, al finalizar,
   la cantidad total de numeros leidos en total. Utilizar una o mas funciones de ser necesario
"""

def factorial(numero):
    fact = 1
    if numero != 0:
        for num in range(1, numero+1):
            fact = fact * num
    return fact

cantidad = 0
num = int(input("ingrese un numero"))

while num != -1:
    print("factorial: ", factorial())
    cantidad = cantidad + 1
    num = int(input("ingrese un numero (-1 para terminar): "))

print("se leyeron {} numeros".format(cantidad))