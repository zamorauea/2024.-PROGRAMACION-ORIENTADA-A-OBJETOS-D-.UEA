from abc import ABC, abstractmethod
import math


# Clase abstracta FiguraGeometrica
class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


# Clase Rectangulo que hereda de FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# Clase Circulo que hereda de FiguraGeometrica
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# Función para mostrar información de cualquier figura geométrica
def mostrar_informacion(figura):
    if isinstance(figura, FiguraGeometrica):
        print(f"Área: {figura.calcular_area()}")
        print(f"Perímetro: {figura.calcular_perimetro()}")
    else:
        print("No es una figura geométrica válida.")


# Creamos instancias de Rectangulo y Circulo
rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)

# Aplicamos polimorfismo
print("Rectángulo:")
mostrar_informacion(rectangulo)
print("---")
print("Círculo:")
mostrar_informacion(circulo)

