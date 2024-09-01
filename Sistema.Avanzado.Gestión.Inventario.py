import json

# Clase Producto: Define los atributos de un producto.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Representación en cadena de un producto.
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario: Gestiona la colección de productos usando un diccionario.
class Inventario:
    def __init__(self):
        self.productos = {}

    # Cargar el inventario desde un archivo JSON.
    def cargar_inventario(self, archivo='inventario.json'):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                # Reconstruir los objetos Producto desde los datos cargados.
                for id_producto, info in data.items():
                    self.productos[id_producto] = Producto(
                        id_producto, info['nombre'], info['cantidad'], info['precio']
                    )
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. Asegúrese de que el formato sea correcto.")

    # Guardar el inventario en un archivo JSON.
    def guardar_inventario(self, archivo='inventario.json'):
        try:
            # Convertir los objetos Producto a un diccionario para guardar en JSON.
            data = {id_producto: vars(producto) for id_producto, producto in self.productos.items()}
            with open(archivo, 'w') as f:
                json.dump(data, f, indent=4)
            print("Inventario guardado.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    # Agregar un producto al inventario.
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto '{producto.nombre}' agregado.")

    # Eliminar un producto del inventario por ID.
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto {id_producto} eliminado.")
        else:
            print("Producto no encontrado.")

    # Actualizar la cantidad o el precio de un producto por ID.
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto {id_producto} actualizado.")
        else:
            print("Producto no encontrado.")

    # Mostrar todos los productos en el inventario.
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


# Menú interactivo para gestionar el inventario.
def menu():
    inventario = Inventario()
    inventario.cargar_inventario()

    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Mostrar Inventario\n5. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            inventario.guardar_inventario()  # Guardar automáticamente después de agregar.
        elif opcion == '2':
            id_producto = input("ID del Producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            inventario.guardar_inventario()  # Guardar automáticamente después de eliminar.
        elif opcion == '3':
            id_producto = input("ID del Producto a actualizar: ")
            cantidad = input("Nueva Cantidad (dejar en blanco si no cambia): ")
            precio = input("Nuevo Precio (dejar en blanco si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
            inventario.guardar_inventario()  # Guardar automáticamente después de actualizar.
        elif opcion == '4':
            inventario.mostrar_inventario()
        elif opcion == '5':
            inventario.guardar_inventario()  # Guardar antes de salir.
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Punto de entrada del programa.
if __name__ == "__main__":
    menu()
