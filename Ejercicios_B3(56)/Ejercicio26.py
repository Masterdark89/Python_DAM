"""Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
• El exponente sea positivo, sólo tienes que imprimir la potencia.
• El exponente sea 0, el resultado es 1.
• El exponente sea negativo, el resultado es 1/potencia con el exponente positivo."""

base = int(input("Introduce la base: "))
exponente = int(input("Introduce la exponente: "))

if exponente == 0:
    print("El resultado es 1")

if exponente > 0:
    total = base ** exponente
    print("El resultado es: ", total)
else:
    exponente *= -1
    total = 1/(base ** exponente)
    print("El resultado es: ", total)
