"""Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad de
números primos que queremos mostrar"""

try:
    n = int(input("¿Cuántos números primos quieres mostrar? "))

    if n <= 0:
        print("Por favor, ingresa un número positivo.")
    else:
        print(f"\nLos primeros {n} números primos son:")

        contador = 0
        numero = 2

        while contador < n:
            es_primo = True

            if numero < 2:
                es_primo = False
            else:
                for i in range(2, int(numero**0.5) + 1):
                    if numero % i == 0:
                        es_primo = False
                        break

            if es_primo:
                print(numero, end=" ")
                contador += 1

            numero += 1

except ValueError:
    print("Error: Por favor, ingresa un número válido.")
