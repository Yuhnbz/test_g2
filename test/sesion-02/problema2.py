"""problema 2"""
import random

lista1 = []

for indice in range(1,11):
    lista1.append(random.randint(1,20))

print(lista1)

for cubo in lista1:
    lista2=[print(cubo**3, " ", end="")]

for cuadrado in lista1:
    lista3=[print(cuadrado**2, " ", end="")]

lista4 = lista2 + lista3
print(lista4)


