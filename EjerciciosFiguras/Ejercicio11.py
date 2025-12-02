
n = int(input("¿Cuantas veces se repite?  "))
veces = 4

for i in range(n):
    for j in range(3):
        print(("   " + "***") * veces)
    for j in range(3):
        print(("***" + "   ") * veces)
