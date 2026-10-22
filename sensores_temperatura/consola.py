from sensor import Sensor


class Consola:
    def __init__(self, titulo_modulo):
        self.titulo = titulo_modulo

    def iniciar_modulo(self):
        print("--- " + self.titulo + " ---")

    def registrar_sensores(self):
        cant = int(input("digite la cantidad de sensores instalados: "))

        frias = 0
        optimas = 0
        calientes = 0

        for i in range(cant):
            temp = float(input("digite la temperatura del sensor " + str(i + 1) + ": "))
            obj_sensor = Sensor(i + 1, temp)
            self.ver_info(obj_sensor)

            categoria = obj_sensor.clasificar()
            if categoria == "fria":
                frias = frias + 1
            elif categoria == "optima":
                optimas = optimas + 1
            else:
                calientes = calientes + 1

        self.ver_resumen(frias, optimas, calientes)

    def ver_info(self, obj_sensor):
        print(obj_sensor.imprimir_dato())

    def ver_resumen(self, frias, optimas, calientes):
        print("--- RESUMEN FINAL ---")
        print("habitaciones frias: " + str(frias))
        print("habitaciones optimas: " + str(optimas))
        print("habitaciones calientes: " + str(calientes))
