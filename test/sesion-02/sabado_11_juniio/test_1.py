""" Uso de la libreria JSON para tratar tipos de datos JSON """

import json

""" creando nuestra variable con un tipo de dato JSON """
jsonData = '{ "nombre":"python", "tipo":"backend", "paradigma":"POD" }'

""" convertirlo en un tipo de dato manejable para python """

jsonToPython = json.loads(jsonData)

print("nuestro tipo de dato json a dato para python: ", jsonToPython)
print("El tipo de dato de nuestra variable es: ", type(jsonToPython))
