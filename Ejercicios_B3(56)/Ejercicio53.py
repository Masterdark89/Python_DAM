"""Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para
esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para
determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por
los N empleados"""

N = int(input("Introduce el número de trabajadores: "))
horas = 0
total_sueldo = 0

for i in range(1, N+1):
    print("Trabajador", i, ":")
    dias = int(input("¿Cuantos dias trabajo?"))
    tarifa = float(input("¿Cual es su tarifa?"))

    for j in range(1, dias+1):
        print("Horas dia", j, ":")
        hora = int(input())
        horas += hora

    sueldo = tarifa * horas
    total_sueldo += sueldo
    print("El sueldo del trabajador es de", sueldo, " euros")
    print(" ")

print("El total por todos los empleados es de", total_sueldo, " euros")
