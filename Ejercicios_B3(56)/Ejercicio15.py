"""Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos
variables."""

A = int(input("Introduce el primer valor:"))
B = int(input("Introduce el segundo valor:"))
aux = B
B = A
A = aux

print("El valor de A ahora es", A, "y el valor de B es", B)
