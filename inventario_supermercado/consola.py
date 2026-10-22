from producto import Producto


class Consola:
    def __init__(self, titulo_modulo):
        self.titulo = titulo_modulo

    def iniciar_modulo(self):
        print("--- " + self.titulo + " ---")

    def registrar_productos(self):
        cant = int(input("digite la cantidad de productos en inventario: "))

        criticos = 0
        bajos = 0
        suficientes = 0

        for i in range(cant):
            print("producto " + str(i + 1))
            codigo = input("escriba el codigo: ")
            nombre = input("escriba el nombre: ")
            cantidad = int(input("escriba la cantidad disponible: "))

            obj_producto = Producto(codigo, nombre, cantidad)
            self.ver_info(obj_producto)

            estado = obj_producto.evaluar_stock()
            if estado == "critico":
                criticos = criticos + 1
            elif estado == "bajo stock":
                bajos = bajos + 1
            else:
                suficientes = suficientes + 1

        self.ver_reporte(criticos, bajos, suficientes)

    def ver_info(self, obj_producto):
        print(obj_producto.imprimir_dato())

    def ver_reporte(self, criticos, bajos, suficientes):
        print("--- REPORTE DE INVENTARIO ---")
        print("productos criticos (reabastecer urgente): " + str(criticos))
        print("productos con bajo stock: " + str(bajos))
        print("productos con stock suficiente: " + str(suficientes))
