class Vehiculo:
    def __init__(self, marca, modelo):
        """
        Método constructor para inicializar un objeto Vehiculo.

        Args:
        - marca (str): La marca del vehículo.
        - modelo (str): El modelo del vehículo.
        """
        self.marca = marca
        self.modelo = modelo
        print(f"Se ha creado un nuevo vehículo {self.marca} {self.modelo}.")

    def __del__(self):
        """
        Método destructor para liberar recursos utilizados por el objeto Vehiculo.
        """
        print(f"El vehículo {self.marca} {self.modelo} está siendo destruido.")

    def conducir(self):
        """
        Método para simular la acción de conducir el vehículo.
        """
        print(f"El vehículo {self.marca} {self.modelo} está siendo conducido.")


if __name__ == "__main__":
    # Crear una instancia de Vehiculo
    coche = Vehiculo("Chevrolet", "Spark")

    # Probar el método conducir
    coche.conducir()

    # Eliminar explícitamente el objeto para activar el destructor
    del coche
