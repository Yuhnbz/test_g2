""" uso de la libreria de fechas y tiempos """
""" comparacion de fechas """

import datetime

fecha1 = datetime.datetime(2014, 4, 13) #tipos de datos datetime
fecha2 = datetime.datetime(2014, 4, 15)

if fecha1 == fecha2:
    print("nacieron el mismo dia")
elif fecha1 < fecha2:
    print("El niño 1 es mayor que el niño 2")
else:
    print("El niño 2 es mayor que el niño 1")