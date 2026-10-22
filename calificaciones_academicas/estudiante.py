class Estudiante:
    def __init__(self, dato_nombre, dato_notas):
        self.nombre = dato_nombre
        self.notas = dato_notas

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_notas(self):
        return self.notas

    def set_notas(self, nuevas_notas):
        self.notas = nuevas_notas

    def calcular_promedio(self):
        suma = 0
        for nota in self.notas:
            suma = suma + nota
        prom = suma / len(self.notas)
        return prom

    def categorizar(self):
        prom = self.calcular_promedio()
        if prom < 3.0:
            categoria = "reprobado"
        else:
            if prom < 4.0:
                categoria = "regular"
            else:
                if prom <= 4.5:
                    categoria = "bueno"
                else:
                    categoria = "excelente"
        return categoria

    def imprimir_dato(self):
        info = "estudiante: " + self.nombre + " - promedio: " + str(round(self.calcular_promedio(), 2))
        info = info + " - categoria: " + self.categorizar()
        return info
