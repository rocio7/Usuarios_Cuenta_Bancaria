from CuentaBancaria2 import CuentaBancaria

class User:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = {
            "cuenta1": CuentaBancaria (.02,1000),
            "cuenta2": CuentaBancaria (.05,3000)
        }

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance Cuenta1: {self.cuenta['cuenta1'].mostrar_info_cuenta()}")
        print(f"Usuario: {self.nombre}, Balance Cuenta2: {self.cuenta['cuenta2'].mostrar_info_cuenta()}")

    def transfer_dinero(self, otro_usuario, cantidad):
        self.cuenta -= cantidad
        otro_usuario.cuenta += cantidad

    def transfer_money(self,cantidad,user):
        self.cuenta -= cantidad
        user.cuenta += cantidad
        self.mostrar_balance_usuario()
        user.mostrar_balance_usuario()
        return self

