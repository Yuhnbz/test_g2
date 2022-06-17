""" Uso de la libreria de fechas y tiempos"""

""" importando las librerias y renombrandolas"""
from datetime import date, datetime, time

""" uso del date """
fecha = date.today()
print("la fecha a manejar es la siguente: ", fecha)

tiempo = datetime.now()
anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("el tiempo actual es: ", tiempo)
print("el año actual es: ", anio)
print("el mes actual es: ", mes)
print("el dia actual es: ", dia)

"""uso del datetime para extraer el año, mes y dia """
hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("la hora actual es: {} con {} minutos y {} segundos".format(hora, minuto, segundo))



