"""Crea un programa que pida al usuario dos números y muestre su división si el segundo no
es cero, o un mensaje de aviso en caso contrario"""

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if num2 == 0:
    print("No se puede dividir por 0")
else:
    total = num1 / num2
    print("La división es", total)
