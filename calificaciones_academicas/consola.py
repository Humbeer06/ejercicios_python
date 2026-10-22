from estudiante import Estudiante


class Consola:
    def __init__(self, titulo_modulo):
        self.titulo = titulo_modulo

    def iniciar_modulo(self):
        print("--- " + self.titulo + " ---")

    def registrar_estudiantes(self):
        cant = int(input("digite el numero de estudiantes del curso: "))

        suma_promedios = 0
        mejor = 0
        peor = 5
        reprobados = 0
        regulares = 0
        buenos = 0
        excelentes = 0

        for i in range(cant):
            print("estudiante " + str(i + 1))
            nombre = input("escriba el nombre: ")

            notas = []
            for j in range(4):
                nota = float(input("digite la calificacion " + str(j + 1) + ": "))
                notas.append(nota)

            obj_estudiante = Estudiante(nombre, notas)
            self.ver_info(obj_estudiante)

            prom = obj_estudiante.calcular_promedio()
            suma_promedios = suma_promedios + prom
            if prom > mejor:
                mejor = prom
            if prom < peor:
                peor = prom

            categoria = obj_estudiante.categorizar()
            if categoria == "reprobado":
                reprobados = reprobados + 1
            elif categoria == "regular":
                regulares = regulares + 1
            elif categoria == "bueno":
                buenos = buenos + 1
            else:
                excelentes = excelentes + 1

        if cant > 0:
            prom_curso = suma_promedios / cant
            self.ver_resumen(prom_curso, mejor, peor, reprobados, regulares, buenos, excelentes)

    def ver_info(self, obj_estudiante):
        print(obj_estudiante.imprimir_dato())

    def ver_resumen(self, prom_curso, mejor, peor, reprobados, regulares, buenos, excelentes):
        print("--- RESUMEN DEL CURSO ---")
        print("promedio del curso: " + str(round(prom_curso, 2)))
        print("mejor promedio: " + str(round(mejor, 2)))
        print("peor promedio: " + str(round(peor, 2)))
        print("reprobados: " + str(reprobados))
        print("regulares: " + str(regulares))
        print("buenos: " + str(buenos))
        print("excelentes: " + str(excelentes))
