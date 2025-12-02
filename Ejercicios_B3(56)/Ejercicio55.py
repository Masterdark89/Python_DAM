"""Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que
seleccionamos la opción de "Salir"""

seguir = True

while seguir:
    print("Bienvenido al menú")
    print("------------------------------")
    print("1. Opcion1")
    print("2. Opcion2")
    print("3. Opcion3")
    print("4. Salir")
    print("-------------------------------")
    opcion = int(input("Introduce la opcion elegida...  "))

    match opcion:
        case 1:
            print("Has elegido la opcion 1")
        case 2:
            print("Has elegido la opcion 2")
        case 3:
            print("Has elegido la opcion 3")
        case 4:
            print("Saliendo del programa...")
            seguir = False
        case _:
            print("Error, opcion invalida")
            print("")
            print("")
