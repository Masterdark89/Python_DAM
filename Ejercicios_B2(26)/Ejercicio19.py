"""Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir"""

saldo = 1000

while True:
    print("Bienvenido a su Cajero Virtual:")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            ingreso = int(input("¿Cuánto dinero vas a ingresar? "))
            saldo = saldo + ingreso
            print("Saldo actual: ", saldo)
            print("")
            print("")
            print("")
            print("")

        case 2:
            retirar = int(input("¿Cuánto dinero vas a retirar? "))
            if retirar <= saldo:
                saldo = saldo - retirar
                print("Saldo actual: ", saldo)
                print("")
                print("")
                print("")
                print("")
            else:
                print("Dinero insuficiente")

        case 3:
            print("Saliendo del programa")
            print("Saldo final: ", saldo)
            break

        case _:
            print("Error: Opción no válida")
            print("")
            print("")
            print("")
            print("")
