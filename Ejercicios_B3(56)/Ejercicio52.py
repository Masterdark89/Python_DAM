"""Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule
cuánto pagó la empresa por los N empleados"""

trabajadores = int(input("¿Cuantos trabajadores hay?"))
horas = int(input("¿Cuantas horas han trabajado esta semana (cada uno)?"))
tarifa = float(input("¿Cual es la tarifa por hora?"))

sueldo = horas * tarifa
total_sueldo = trabajadores * sueldo

print("El sueldo de cada trabajador es de ", sueldo, " euros")
print("El pago por todos los sueldos es", total_sueldo, " euros")
