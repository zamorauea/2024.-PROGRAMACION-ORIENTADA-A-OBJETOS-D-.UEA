class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        if cantidad < 0 or precio < 0:
            raise ValueError("La cantidad y el precio no pueden ser negativos.")
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        try:
            if producto.id_producto in self.productos:
                raise KeyError(f"El producto con ID {producto.id_producto} ya existe.")
            self.productos[producto.id_producto] = producto
            print(f"Producto '{producto.nombre}' agregado exitosamente.")
        except KeyError as e:
            print(e)

    def eliminar_producto(self, id_producto):
        try:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        except KeyError:
            print(f"Error: No se encontró un producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        try:
            if id_producto not in self.productos:
                raise KeyError(f"Error: No se encontró un producto con ID {id_producto}.")
            producto = self.productos[id_producto]
            if nombre:
                producto.nombre = nombre
            if cantidad is not None:
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
                producto.cantidad = cantidad
            if precio is not None:
                if precio < 0:
                    raise ValueError("El precio no puede ser negativo.")
                producto.precio = precio
            print(f"Producto con ID {id_producto} actualizado exitosamente.")
        except (KeyError, ValueError) as e:
            print(e)

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if resultados:
            for producto in resultados:
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
        else:
            print(f"No se encontró ningún producto con el nombre '{nombre}'.")

    def mostrar_inventario(self):
        if self.productos:
            print("Inventario actual:")
            for producto in self.productos.values():
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
        else:
            print("El inventario está vacío.")

# Ejemplo de uso del sistema de inventario mejorado
inventario = Inventario()

# Agregar productos al inventario
try:
    inventario.agregar_producto(Producto(1, "Naranjas", 70, 0.50))
    inventario.agregar_producto(Producto(2, "Fresas", 10, 0.30))
    # Intentar agregar un producto con cantidad negativa
    inventario.agregar_producto(Producto(3, "Manzanas", -10, 0.20))
except ValueError as e:
    print(f"Error al agregar producto: {e}")

# Mostrar el inventario actual
inventario.mostrar_inventario()

# Actualizar un producto
inventario.actualizar_producto(2, cantidad=25)

# Intentar actualizar un producto con precio negativo
inventario.actualizar_producto(2, precio=-0.50)

# Buscar un producto
inventario.buscar_producto("Fresas")

# Eliminar un producto
inventario.eliminar_producto(1)

# Intentar eliminar un producto que no existe
inventario.eliminar_producto(3)

# Mostrar el inventario después de las operaciones
inventario.mostrar_inventario()
