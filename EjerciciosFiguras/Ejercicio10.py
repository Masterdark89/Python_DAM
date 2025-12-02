
n = int(input("¿Cuantas veces quieres que se repita el patrón?  "))
longitud = 17  # IMPORTANTE: tiene que ser impar
espacios = 8  # La mitad de longitud -1 // espacios = (longitud - 1) / 2

for i in range(n):
    print(("*" + " ") * longitud)
    print("*", end="")
    for j in range(espacios):
        print("   " + "*", end="")
    print("")

print(("*" + " ") * longitud)
