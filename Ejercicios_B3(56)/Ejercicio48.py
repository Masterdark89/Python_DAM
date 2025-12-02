"""Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de
cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva
ahorrado cada mes"""
seguir = True

while seguir:
    ingreso = float(input("¿Cuanto vas a ingresar?"))
    gastos = float(input("¿Cuanto vas a sacar?"))
    ahorro = ingreso - gastos

    respuesta = input("¿Quieres terminar el programa? (si/no)")
    if respuesta.lower() == "si":
        seguir = False

print("Has ahorrado", ahorro, "euros")
