"""Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una
distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para
ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto
determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro"""

v1 = int(input("Introduce la velocidad del primer vehiculo:"))
v2 = int(input("Introduce la velocidad del segundo vehiculo:"))
distancia = int(input("¿Cual es la distacia?"))
minutos = 0

if v1 < v2:
    velocidad = v2 - v1
    horas = distancia / velocidad
    minutos = horas * 60
else:
    velocidad = v1 - v2
    horas = distancia / velocidad
    minutos = horas * 60

print("El vehiculo tardara", minutos, " minutos en alcanzarlo")
