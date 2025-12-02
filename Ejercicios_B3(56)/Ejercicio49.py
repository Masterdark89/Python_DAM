"""Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la
semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por
las horas trabajadas"""

total = 0

tarifa = float(input("¿Cual es la tarifa por hora? "))

for i in range(1, 7):
    print("¿Cuantas horas a trabajado el ", i, "º día?")
    horas = int(input())
    total += horas

cobro = tarifa * total
print("Total de horas trabajadas: ", total)
print("Total a cobrar:", cobro, " euros")
