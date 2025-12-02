"""Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior
es mayor que el superior lo tiene que volver a pedir. A continuación, se van introduciendo
números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes
informaciones:
• La suma de los números que están dentro del intervalo (intervalo abierto).
• Cuantos números están fuera del intervalo.
• He informa si hemos introducido algún número igual a los límites del intervalo"""

inf = float(input("Introduce el límite inferior: "))
sup = float(input("Introduce el límite superior: "))

while sup < inf:
    print("Error, intentalo otra vez")
    inf = float(input("Introduce el límite inferior: "))
    sup = float(input("Introduce el límite superior: "))

num = 1
suma = 0
fuera = 0
igual = 0

while num != 0:
    num = int(input("Introduce un número: "))

    if num > inf and num < sup:
        suma += num
    else:
        if num == inf or num == sup:
            igual += 1
        fuera += 1

print("La suma total es de", suma)

if fuera != 0:
    print(fuera, "números fuera del intervalo")
else:
    print("Ningún números fuera del intervalo")

if igual != 0:
    print(igual, "números iguales al intervalo")
else:
    print("No hay números iguales al intervalo")
