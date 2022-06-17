"""
2. pedir numero al usuario hasta que ingrese el cero. Por cada uno, muestre la suma de sus digitos
   (utilizando una funcion que realize dicha suma)
"""

def sumarDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = int(numero/10)
    return suma

num = int(input("ingrese numero a procesar: "))
while num!= 0:
    print("suma: ", sumarDigitos(num))
    num = int(input("ingrese numero a procesar: "))