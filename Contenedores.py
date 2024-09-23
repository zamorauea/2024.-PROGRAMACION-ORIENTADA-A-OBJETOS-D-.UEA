import tkinter as tk
from tkinter import ttk, messagebox


# Función para agregar un evento al Treeview
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if fecha and hora and descripcion:
        tree.insert("", tk.END, values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Advertencia", "Completa todos los campos.")


# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmar", "Eliminar este evento?"):
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un evento.")


# Limpiar los campos de entrada
def limpiar_campos():
    fecha_entry.delete(0, tk.END)
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)


# Salir de la aplicación
def salir():
    root.quit()


# Ventana principal
root = tk.Tk()
root.title('Agenda Personal')
root.geometry('500x400')

# Contenedor principal
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=tk.NSEW)

# Título
titulo = ttk.Label(frame, text="Agenda Personal")
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada
ttk.Label(frame, text="Fecha (dd-mm-yyyy):").grid(row=1, column=0)
fecha_entry = ttk.Entry(frame, width=18)
fecha_entry.grid(row=1, column=1)

ttk.Label(frame, text="Hora:").grid(row=2, column=0)
hora_entry = ttk.Entry(frame, width=20)
hora_entry.grid(row=2, column=1)

ttk.Label(frame, text="Descripción:").grid(row=3, column=0)
descripcion_entry = ttk.Entry(frame, width=20)
descripcion_entry.grid(row=3, column=1)

# Botones
ttk.Button(frame, text="Agregar Evento", command=agregar_evento).grid(row=4, column=0, pady=10)
ttk.Button(frame, text="Eliminar Evento", command=eliminar_evento).grid(row=5, column=0, pady=10)
ttk.Button(frame, text="Salir", command=salir).grid(row=5, column=1, pady=10)

# Treeview para eventos
tree = ttk.Treeview(frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=10)
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

# Iniciar la aplicación
root.mainloop()
