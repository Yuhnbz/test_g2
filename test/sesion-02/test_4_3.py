"""
3. pedir numero al usuario hasta que ingrese el cero, por cada uno mostrar la suma de digitos.
   Al finalizar mostrar la suma de todos los numeros y de sus digitos, utilizar la funcion de ejercicio 2
"""

def sumarDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = int(numero/10)
    return suma

sumatoria = 0

num = int(input("ingrese numero a procesar: "))
while num!= 0:
    print("suma: ", sumarDigitos(num))
    sumatoria = sumatoria + num
    num = int(input("ingrese numero a procesar: "))

print("la sumatoria final es: ", sumatoria)
print("la suma de digitos es: ", sumarDigitos(sumatoria))