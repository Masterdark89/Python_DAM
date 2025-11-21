"""Escriba un programa que lea un valor correspondiente a una distancia en millas marinas y
escriba la distancia en metros. Sabiendo que una milla marina equivale a 1.852 metros."""

print("Introduce la distancia en millas: ")
millas = input()
millas = int(millas)

metros = 1.852 * millas
print("La conversion en metros es de: ", metros, "metros")
