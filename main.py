from Usuario import User
from CuentaBancaria2 import CuentaBancaria


adrien = User("Adrien")

adrien.cuenta['cuenta1'].deposito(100)
adrien.mostrar_balance_usuario()


