"""Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' en caso
contrario, el programa termina cuando se introduce un espacio."""

caracter = "algo"

while caracter != " ":
    caracter = input("Introduce un caracter: ")

    if caracter.lower() == "a":
        print("VOCAL")

    elif caracter.lower() == "e":
        print("VOCAL")

    elif caracter.lower() == "i":
        print("VOCAL")

    elif caracter.lower() == "o":
        print("VOCAL")

    elif caracter.lower() == "u":
        print("VOCAL")

    else:
        print("NO VOCAL")
