import json

""" uso de la libreria JSON """
""" conversion inversa de tipo de dato python a JSON """

pythonDict = {"name": "mary", "edad": 27, "dni": "95847625"}

""" conversion de tipo de dato JSON """

dictToJson = json.dumps(pythonDict)
print("el dato convertido a json es el sgt: ", dictToJson)
print("el tipo de dato convertido es de tipo: ", type(dictToJson))