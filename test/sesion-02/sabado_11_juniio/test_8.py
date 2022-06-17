import requests

""" Lectura de un API el cual nos va a traer un JSON """
res = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(res.status_code)
print(res.text)
json = res.json()
print(json)