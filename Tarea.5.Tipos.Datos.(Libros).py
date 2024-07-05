class Libro:
    def __init__(self, titulo, autor, paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.estado = "disponible"

    def prestar(self):
        """Cambia el estado del libro a prestado si está disponible."""
        if self.estado == "disponible":
            self.estado = "prestado"
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para prestar.")

    def devolver(self):
        """Cambia el estado del libro a disponible si estaba prestado."""
        if self.estado == "prestado":
            self.estado = "disponible"
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

# Ejemplo de creación y uso de un objeto Libro
mi_libro = Libro("Odisea", "Homero", 448, "Poema épico")
print(f"Información del libro:")
print(f"Título: {mi_libro.titulo}")
print(f"Autor: {mi_libro.autor}")
print(f"Páginas: {mi_libro.paginas}")
print(f"Género: {mi_libro.genero}")

mi_libro.prestar()
mi_libro.prestar()  # Intenta prestar el libro nuevamente
mi_libro.devolver()
mi_libro.devolver()  # Intenta devolver el libro nuevamente
