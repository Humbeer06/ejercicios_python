class Sensor:
    def __init__(self, dato_numero, dato_temp):
        self.numero = dato_numero
        self.temp = dato_temp

    def get_numero(self):
        return self.numero

    def set_numero(self, nuevo_numero):
        self.numero = nuevo_numero

    def get_temp(self):
        return self.temp

    def set_temp(self, nueva_temp):
        self.temp = nueva_temp

    def clasificar(self):
        if self.temp < 18:
            categoria = "fria"
        elif self.temp <= 25:
            categoria = "optima"
        else:
            categoria = "caliente"
        return categoria

    def decidir_accion(self):
        categoria = self.clasificar()
        if categoria == "fria":
            accion = "se enciende la calefaccion"
        elif categoria == "optima":
            accion = "sin accion"
        else:
            accion = "se activa el aire acondicionado"
        return accion

    def imprimir_dato(self):
        info = "sensor " + str(self.numero) + " - temperatura: " + str(self.temp) + "C"
        info = info + " - " + self.clasificar() + " - " + self.decidir_accion()
        return info
