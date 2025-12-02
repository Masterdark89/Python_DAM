"""Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas)."""

cadena = input("Introduce una cadena: ")

primeros_tres = slice(0, 3)
ultimos_tres = slice(-3, None)
cada_segundo = slice(None, None, 2)

print("Primeros 3 caracteres:", cadena[primeros_tres])
print("Últimos 3 caracteres:", cadena[ultimos_tres])
print("Cada segundo carácter:", cadena[cada_segundo])
