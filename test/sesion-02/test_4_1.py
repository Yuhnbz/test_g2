"""
1. pedir a un usuario su direccion email. imprimir un mensaje indicando si la dirección es valida o no
   valiendose de una funcion para decidirlo. se considerara valida si tiene el simbolo @
 """

def validar(email):
    caracterPedido = "@"
    emailValid = False
    for caracter in email:
        if caracter == caracterPedido:
            return True
    return False

emailUsuario = input("ingrese su email: ")
if validar(emailUsuario):
    print("email valido")
else:
    print("email invalido")