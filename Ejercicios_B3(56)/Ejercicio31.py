"""El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
La forma de cobrar es la siguiente: 
si son 100 alumnos o más, el costo por cada alumno es de 65
euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de
30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que
debe pagar cada alumno por el viaje"""

cant_alumnos = int(input("¿Cuantos alumnos son?"))

match cant_alumnos:
    case cant_alumnos if cant_alumnos >= 100:
        precio = 65 * cant_alumnos
    case cant_alumnos if cant_alumnos >= 50:
        precio = 70 * cant_alumnos
    case cant_alumnos if cant_alumnos >= 30:
        precio = 95 * cant_alumnos
    case _:
        precio = 4000

total = precio / cant_alumnos
print("El precio a pagar es", precio, " euros y el precio por alumno es", total)
