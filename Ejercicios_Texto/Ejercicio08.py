"""Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres 
sin usar los métodos upper() o lower())."""

cadena = input("Introduce una cadena: ")

print("Conversión a MAYÚSCULAS:")
resultado_mayusculas = ""

for caracter in cadena:
    if 'a' <= caracter <= 'z':
        codigo = ord(caracter)
        caracter_mayuscula = chr(codigo - 32)
        resultado_mayusculas += caracter_mayuscula
    else:
        resultado_mayusculas += caracter

print(f"Texto original: {cadena}")
print(f"Texto en mayúsculas: {resultado_mayusculas}")

print("\n" + "-"*40 + "\n")

print("Conversión a minúsculas:")
resultado_minusculas = ""

for caracter in cadena:
    if 'A' <= caracter <= 'Z':
        codigo = ord(caracter)
        caracter_minuscula = chr(codigo + 32)
        resultado_minusculas += caracter_minuscula
    else:
        resultado_minusculas += caracter

print(f"Texto original: {cadena}")
print(f"Texto en minúsculas: {resultado_minusculas}")

print("\n" + "-"*40 + "\n")
