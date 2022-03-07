
class CuentaBancaria:
    cuentas = []
    def __init__(self,tasa_interés,balance):
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, cantidad):
        self.balance += cantidad
        return self

    def retiro(self,cantidad):
        if(self.balance - cantidad) >= 0:
            self.balance -= cantidad
        else:
            print("Fondos Insuficientes: Cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        return f"{self.balance}"

    def generar_interés(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interés)
        return self

    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.cuentas:
            print(f"Balance: {cuenta.balance}, Tasa de interés: {cuenta.tasa_interés}")

