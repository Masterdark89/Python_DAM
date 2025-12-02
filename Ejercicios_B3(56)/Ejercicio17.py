"""Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de
viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora
de llegada a la ciudad B."""
horas = 0
minutos = 0
segundos = 0

HH = int(input("Introduce la hora:"))

while HH < 0 or HH > 23:
    HH = int(input("Error, vuelve a intentarlo: "))

MM = int(input("Introduce los minutos:"))
while MM < 0 or MM > 59:
    MM = int(input("Error, vuelve a intentarlo: "))

SS = int(input("Introduce los segundos:"))
while SS < 0 or SS > 59:
    SS = int(input("Error, vuelve a intentarlo: "))

T = int(input("Introduce el tiempo de viaje(en segundos):"))

while T >= 60:
    T -= 60
    minutos += 1

while minutos >= 60:
    minutos -= 60
    horas += 1

horas = HH + horas
if horas >= 24:
    horas -= 24

minutos = minutos + MM
if minutos >= 60:
    minutos -= 60

segundo = SS + T
if segundos >= 60:
    segundos -= 60

print("La hora de llega es", horas, "horas, ",
      minutos, "minutos y ", segundos, "segundos.")
