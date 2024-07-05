class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """Agrega la cantidad especificada al saldo de la cuenta."""
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} unidades. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        """Retira la cantidad especificada del saldo de la cuenta si hay suficientes fondos."""
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades. Nuevo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente. No se pudo realizar el retiro.")

# Ejemplo de creación y uso de un objeto CuentaBancaria
mi_cuenta = CuentaBancaria("Luis Bautista", 2600)
print(f"Titular de la cuenta: {mi_cuenta.titular}")
mi_cuenta.depositar(800)
mi_cuenta.retirar(400)
mi_cuenta.retirar(1600)  # Intento de retirar más dinero del disponible

