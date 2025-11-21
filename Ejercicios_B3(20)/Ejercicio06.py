"""Programa que lea un número positivo N y calcule y visualice su factorial N! Siendo el
factorial:
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2* 1
N! = N * (N-1) * (N-2) * … * ."""
factorial = 1

N = int(input("Introduce un número:"))

while N < 0:
    N = int(input("Tiene que ser un numero positivo:"))

if N == 1 or N == 0:
    print("El factorial es 1")
else:
    for i in range(1, N + 1):
        factorial *= i 
    print("El factorial de", N, "es", factorial)
