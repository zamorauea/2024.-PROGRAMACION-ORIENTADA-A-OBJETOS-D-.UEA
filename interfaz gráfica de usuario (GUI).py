import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Función para agregar datos a la tabla
def agregar_dato():
    nombre = entry_nombre.get()
    edad = entry_edad.get()

    if nombre and edad:
        treeview.insert("", tk.END, values=(nombre, edad))
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Complete todos los campos")


# Función para limpiar la tabla
def limpiar_tabla():
    for item in treeview.get_children():
        treeview.delete(item)


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos con Tabla")

# Etiqueta y campo de texto para nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo de texto para edad
label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

# Botón para agregar dato
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Tabla (Treeview) para mostrar los datos
columns = ("Nombre", "Edad")
treeview = ttk.Treeview(ventana, columns=columns, show="headings")
treeview.heading("Nombre", text="Nombre")
treeview.heading("Edad", text="Edad")
treeview.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Botón para limpiar la tabla
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_tabla)
boton_limpiar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Iniciar la aplicación
ventana.mainloop()
