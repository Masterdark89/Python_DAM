"""Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena"""

cadena = input("Introduce una cadena:")

buscar = input("¿Que carácter quieres reemplazar?")
reemplazar = input("¿Por cual?")
nuevacadena = ""
print("")

for i in range(len(cadena)):

    if buscar == cadena[i]:
        nuevacadena += reemplazar
    else:
        nuevacadena += cadena[i]

print(nuevacadena)
