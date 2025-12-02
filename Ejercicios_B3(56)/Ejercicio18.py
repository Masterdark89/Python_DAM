"""Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales. Mostramos las
Iniciales en Mayúsculas sí o sí"""

nombre = input("Introduce el nombre: ")
apellidos = input("Introduce el apellido: ")

inicial_nombre = nombre[0].upper()
inicial_apellido = apellidos[0].upper()

print("Las iniciales son ", inicial_nombre, " ", inicial_apellido)
