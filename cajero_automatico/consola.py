from cuenta import Cuenta


class Consola:
    def __init__(self, titulo_modulo):
        self.titulo = titulo_modulo

    def iniciar_modulo(self):
        print("--- " + self.titulo + " ---")

    def pedir_opcion(self):
        print("--- MENU ---")
        print("1. Consultar saldo")
        print("2. Retirar")
        print("3. Depositar")
        print("4. Salir")
        op = int(input())
        return op

    def iniciar_cajero(self):
        saldo_inicial = float(input("digite el saldo inicial: "))
        obj_cuenta = Cuenta(saldo_inicial)

        op = -1
        while op != 4:
            op = self.pedir_opcion()

            match op:
                case 1:
                    self.ver_info(obj_cuenta)
                case 2:
                    self.retirar_dinero(obj_cuenta)
                case 3:
                    self.depositar_dinero(obj_cuenta)
                case 4:
                    print("saliendo del cajero")
                    print("su saldo final es: $" + str(obj_cuenta.get_saldo()))
                case _:
                    print("opcion no valida")

    def retirar_dinero(self, obj_cuenta):
        monto = float(input("digite el monto a retirar: "))
        if monto <= 0:
            print("el monto debe ser positivo")
        elif monto > obj_cuenta.get_saldo():
            print("saldo insuficiente")
        else:
            obj_cuenta.retirar(monto)
            print("retiro exitoso")
            self.ver_info(obj_cuenta)

    def depositar_dinero(self, obj_cuenta):
        monto = float(input("digite el monto a depositar: "))
        if obj_cuenta.depositar(monto):
            print("deposito exitoso")
            self.ver_info(obj_cuenta)
        else:
            print("monto no valido, debe ser positivo")

    def ver_info(self, obj_cuenta):
        print(obj_cuenta.imprimir_dato())
