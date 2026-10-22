class Cuenta:
    def __init__(self, dato_saldo):
        self.saldo = dato_saldo

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, nuevo_saldo):
        self.saldo = nuevo_saldo

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo = self.saldo - monto
            return True
        return False

    def depositar(self, monto):
        if monto > 0:
            self.saldo = self.saldo + monto
            return True
        return False

    def imprimir_dato(self):
        info = "saldo actual: $" + str(self.saldo)
        return info
