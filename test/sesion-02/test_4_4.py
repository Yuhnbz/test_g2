""""
4. pedir al usuario que ingrese un numero entero e informar si es primo o no, utilizando una funcion booleana que lo decida
"""

def primo(numero):
    for i in range(2, numero):
        if numero%i==0:
            return False
    return True

num = int(input("ingrese numero a evaluar: "))
if primo(num):
    print("El numero es primo")
else:
    print("el numero no es primo")