
#from funciones import suma, resta, multiplicacion, division
from funciones import *

x = int(input("ingrese un valor: "))
y = int(input("ingrese un segundo valor: "))

sum = suma(x, y)
print("el resultado de la suma es: ", sum)

div = division(x, y)
print("el resulado de la division es: ", div)

res = resta(x, y)
print("el resultado de la resta es: ", res)