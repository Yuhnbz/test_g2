""" uso de la libreria de fechas y tiempos """

from datetime import datetime

strFecha = "2/6/2020"

conversion = datetime.strptime(strFecha, "%m/%d/%Y")

print("la fecha formateada es: ", conversion)

""" Traer el mes de la fecha con letras """

conversionMes = datetime.strftime(conversion, "%b %d, %Y")
print("Nuestra fecha con cambio en el mes es el siguiente: ", conversionMes)