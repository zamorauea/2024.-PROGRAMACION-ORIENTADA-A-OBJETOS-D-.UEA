import os

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido del archivo especificado.

    Parámetros:
    ruta_script (str): La ruta al archivo cuyo contenido se quiere mostrar.
    """
    try:
        with open(ruta_script, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """
    Muestra el menú principal y gestiona las selecciones del usuario.

    El menú permite al usuario seleccionar un archivo para ver su contenido
    o salir del programa.
    """
    ruta_base = os.path.dirname(__file__)

    # Diccionario que mapea opciones del menú a rutas de archivos
    opciones = {
        '1': 'Tarea.2.Tecnicas.programación.POO.(Figura.geometrica).py',
        '2': 'Tarea.3.Comparación de Programación Tradicional y POO en Python.py',
        '3': 'Tarea.4.Ejemplo_mundo_real.(Cuenta _bancaria).py',
        '4': 'Tarea.5.Tipos.Datos.(Libros).py',
        '5': 'Tarea.6.Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '6': 'Tarea.7.Implementación.Constructores.y.Destructores.py',
        '7': 'Tarea.8.Dashboard.py'
    }

    while True:
        print("\nMenú Principal - Dashboard")
        print("Selecciona una opción para ver el contenido del archivo o '0' para salir:")

        # Imprime las opciones del menú
        for key, value in opciones.items():
            print(f"{key} - {value}")

        print("0 - Salir")
        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            # Sale del bucle y termina el programa
            break
        elif eleccion in opciones:
            # Construye la ruta completa al archivo seleccionado
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            # Mensaje de error para opciones inválidas
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecuta la función principal si el archivo se ejecuta como script
if __name__ == "__main__":
    mostrar_menu()

