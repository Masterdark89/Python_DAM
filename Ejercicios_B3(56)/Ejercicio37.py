"""Una compañía de transporte internacional tiene servicio en algunos países de América del
Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se
basa en el peso del paquete y la zona a la que va dirigido..."""

peso = float(input("¿Cual es el peso del paquete?"))
zona = (input("¿Cual es la zona?"))
zona.lower()

match zona:
    # faltan datos de las tarifas
    case "américa del norte":
        total = peso + 50
    case "américa central":
        total = peso + 40
    case "américa del sur":
        total = peso + 245
    case "europa":
        total = peso + 70
    case "asia":
        total = peso + 200

print("El coste total es", total, " euros")
