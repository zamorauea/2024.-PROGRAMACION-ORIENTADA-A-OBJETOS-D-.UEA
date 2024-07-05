# Definición de la clase Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return f"{self.nombre}: ${self.salario:.2f} por mes"


# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def __str__(self):
        return f"{self.nombre} es gerente del departamento {self.departamento}, con un salario de ${self.salario:.2f} por mes"


# Función para mostrar información de un empleado
def mostrar_informacion_empleado(empleado):
    print(empleado)


# Ejemplo de uso del programa
if __name__ == "__main__":
    empleado1 = Empleado("Juan Pérez", 3000)
    gerente1 = Gerente("María López", 5000, "Ventas")

    print("Información de los empleados:")
    mostrar_informacion_empleado(empleado1)
    mostrar_informacion_empleado(gerente1)
