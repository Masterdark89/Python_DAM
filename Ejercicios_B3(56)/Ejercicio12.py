"""Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos"""

x1 = int(input("Introduce la X:"))
y1 = int(input("Introduce la Y:"))

x2 = int(input("Introduce la X:"))
y2 = int(input("Introduce la Y:"))

distanciaX = 0
distanciaY = 0

distanciaX = x1 - x2
distanciaY = y1 - y2

if distanciaX < 0:
    distanciaX = distanciaX * (-1)

if distanciaY < 0:
    distanciaY = distanciaY * (-1)

print("La distancia de ambos puntos es (", distanciaX, ",", distanciaY, ")")
