""" uso de la libreria de fechas y tiempos """
""" conversion total del tiempo """

from datetime import datetime

""" uso del timestamp """
timeNow = datetime.strptime("2022/02/01 18:40:10", "%Y/%m/%d %H:%M:%S").timestamp()

print("la conversion de nuestro valor en timeNow es:", timeNow)


