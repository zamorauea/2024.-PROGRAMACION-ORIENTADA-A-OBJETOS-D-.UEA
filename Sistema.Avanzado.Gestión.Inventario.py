class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (titulo, autor)  # Usamos una tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.detalles[0]}', autor='{self.detalles[1]}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)
        print(f"Libro '{libro.detalles[0]}' prestado a {self.nombre}.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print(f"Libro '{libro.detalles[0]}' devuelto por {self.nombre}.")
        else:
            print(f"El libro '{libro.detalles[0]}' no está prestado a {self.nombre}.")

    def listar_libros_prestados(self):
        return [libro.detalles[0] for libro in self.libros_prestados]  # Devuelve solo los títulos

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}')"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = {}  # Diccionario de usuarios con ID de usuario como clave

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.detalles[0]}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.detalles[0]}' quitado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)
        if libro and usuario:
            usuario.prestar_libro(libro)
        else:
            print(f"Error: libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)
        if libro and usuario:
            usuario.devolver_libro(libro)
        else:
            print(f"Error: libro o usuario no encontrado.")

    def buscar_libro(self, **kwargs):
        # Permite buscar por título, autor o categoría
        resultados = []
        for libro in self.libros.values():
            if any(getattr(libro, key, None) == value for key, value in kwargs.items()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            return usuario.listar_libros_prestados()
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")
            return []

    def __repr__(self):
        return f"Biblioteca: {len(self.libros)} libros, {len(self.usuarios)} usuarios."


# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", "2345")
libro2 = Libro("1984", "George Orwell", "Distopía", "6789")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Carlos Díaz", "u1001")
usuario2 = Usuario("María López", "u1002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("2345", "u1001")

# Listar libros prestados por un usuario
print("Libros prestados por Carlos Díaz:", biblioteca.listar_libros_prestados("u1001"))

# Buscar libros
print("Buscar libro por autor 'George Orwell':", biblioteca.buscar_libro(autor="George Orwell"))

# Devolver libros
biblioteca.devolver_libro("2345", "u1001")
print("Libros prestados por Carlos Díaz después de devolver:", biblioteca.listar_libros_prestados("u1001"))

# Quitar libro
biblioteca.quitar_libro("6789")

