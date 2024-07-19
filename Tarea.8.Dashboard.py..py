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
        '1': 'Tecnicas POO.py',
        '2': 'Tarea_2/2.2_Tecnicas_Programacion.(Figura geometrica).py',
        '3': 'Tarea_3/3.3_Comparación de Programción Tradicional y POO EN Paython.py',
        '4': 'Tarea_4/4.4_Ejemplo_mundo_real.(Cuenta_Bancaria).py',
        '5': 'Tarea_5/5.5_Tipos.Datos.(Libros).py',
        '6': 'Tarea_6/6.6_Clase.objetos/Herencia/Encapsulado/Polimorfismo.py',
        '7': 'Tarea_7/7.7_Implementación.Contructores.y.Destructores.py',
        '8': 'Tarea_8/8.8_Deshboard.py'
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
