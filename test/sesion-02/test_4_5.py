""""
5. solicitar al usuario un numero entero y luego un digito, informar la cantidad de ocurrencias del digito
   utilizando para ello una funcion que calcule la frecuencia
"""

def frecuencia(numero, digito):
    cantidad = 0
    while numero!=0:
        ultDigito = numero%10
        if ultDigito==digito:
            cantidad = cantidad + 1
        numero = int(numero/10)
    return cantidad

num = int(input("ingrese un numero: "))
uDigito = int(input("ingrese digito a encontrar: "))
print("frecuencia del digito {uDigito} en el numero {num} es de : {frecuencia}".format(num=num, uDigito=uDigito,
                                                                      frecuencia=frecuencia(num, uDigito)))

