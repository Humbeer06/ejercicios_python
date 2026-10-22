class Producto:
    def __init__(self, dato_codigo, dato_nombre, dato_cantidad):
        self.codigo = dato_codigo
        self.nombre = dato_nombre
        self.cantidad = dato_cantidad

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def evaluar_stock(self):
        if self.cantidad < 10:
            estado = "critico"
        elif self.cantidad <= 50:
            estado = "bajo stock"
        else:
            estado = "suficiente"
        return estado

    def imprimir_dato(self):
        info = "codigo: " + self.codigo + " - nombre: " + self.nombre
        info = info + " - cantidad: " + str(self.cantidad) + " - estado: " + self.evaluar_stock()
        return info
