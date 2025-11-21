"""La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch)."""

nombre = input("Introduce el nombre del postulante: ")
facultad = input("¿A que facultad va ir?")

match facultad:
    case "Ing. Sistemas":
        importe = 350
        mensualidad = 650
        igv = (importe + mensualidad) * 18 / 100
        totalpagar = igv + importe + mensualidad
        print("Ha de pagar de importe: ", importe, "euros")
        print("Ha de pagar de mensualidad: ", mensualidad, "euros")
        print("El IGV es de ", igv, "euros")
        print("Un total a pagar de: ", totalpagar, "euros")

    case "Derecho":
        importe = 300
        mensualidad = 550
        igv = (importe + mensualidad) * 18 / 100
        totalpagar = igv + importe + mensualidad
        print("Ha de pagar de importe: ", importe, "euros")
        print("Ha de pagar de mensualidad: ", mensualidad, "euros")
        print("El IGV es de ", igv, "euros")
        print("Un total a pagar de: ", totalpagar, "euros")

    case "Ing. Naviera":
        importe = 300
        mensualidad = 500
        igv = (importe + mensualidad) * 18 / 100
        totalpagar = igv + importe + mensualidad
        print("Ha de pagar de importe: ", importe, "euros")
        print("Ha de pagar de mensualidad: ", mensualidad, "euros")
        print("El IGV es de ", igv, "euros")
        print("Un total a pagar de: ", totalpagar, "euros")

    case "Ing. Pesquera":
        importe = 310
        mensualidad = 460
        igv = (importe + mensualidad) * 18 / 100
        totalpagar = igv + importe + mensualidad
        print("Ha de pagar de importe: ", importe, "euros")
        print("Ha de pagar de mensualidad: ", mensualidad, "euros")
        print("El IGV es de ", igv, "euros")
        print("Un total a pagar de: ", totalpagar, "euros")

    case "Contabilidad":
        importe = 280
        mensualidad = 490
        igv = (importe + mensualidad) * 18 / 100
        totalpagar = igv + importe + mensualidad
        print("Ha de pagar de importe: ", importe, "euros")
        print("Ha de pagar de mensualidad: ", mensualidad, "euros")
        print("El IGV es de ", igv, "euros")
        print("Un total a pagar de: ", totalpagar, "euros")

    case "Administracion":
        importe = 360
        mensualidad = 520
        igv = (importe + mensualidad) * 18 / 100
        totalpagar = igv + importe + mensualidad
        print("Ha de pagar de importe: ", importe, "euros")
        print("Ha de pagar de mensualidad: ", mensualidad, "euros")
        print("El IGV es de ", igv, "euros")
        print("Un total a pagar de: ", totalpagar, "euros")

    case _:
        print("Facultad invalida")
