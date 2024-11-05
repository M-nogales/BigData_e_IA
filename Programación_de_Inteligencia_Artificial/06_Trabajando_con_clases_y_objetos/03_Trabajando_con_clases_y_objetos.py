# 03. **Clase CuentaBancaria**
# Crea una clase CuentaBancaria con atributos como titular, saldo y tipo de cuenta.
# Métodos para depositar, retirar dinero (sin permitir retiros si el saldo es insuficiente)
# y mostrar el saldo actual.

class CuentaBancaria:
    def __init__(self, titular, saldo, tipo_cuenta):
        self.titular = ""
        self.saldo = 0
        self.tipo_cuenta = ""

    def depositar(self,cantidad):
        self.saldo += cantidad

    def retirar(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")
    
    def mostrar_saldo(self):
        return self.saldo

cuenta1 = CuentaBancaria("Juan", 1000, "Ahorros")
print('cuenta1.mostrar_saldo(): ', cuenta1.mostrar_saldo())
cuenta1.depositar(500)
print('cuenta1.depositar(500): 500')
print('cuenta1.mostrar_saldo(): ', cuenta1.mostrar_saldo())
cuenta1.retirar(100)
print('cuenta1.retirar(100): -100')
print('cuenta1.mostrar_saldo(): ', cuenta1.mostrar_saldo())
