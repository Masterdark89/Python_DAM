"""Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo"""

horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

segundos = segundos + 1
if segundos == 60:
    segundos = 0
    minutos = minutos + 1
    if minutos == 60:
        minutos = 0
        horas = horas + 1
        if horas == 24:
            horas = 0

print("Pasado un segundo seran las: ", horas, "horas",
      minutos, "minutos y", segundos, "segundos")
