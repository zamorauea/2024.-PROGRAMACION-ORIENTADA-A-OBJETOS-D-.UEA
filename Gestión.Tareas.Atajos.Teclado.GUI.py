import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

# Función para marcar tarea como completada
def mark_completed(event=None):
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(tk.END, f"{task} (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

# Función para eliminar tarea
def delete_task(event=None):
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Campo de entrada para nueva tarea
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Botón para añadir tarea
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.grid(row=0, column=1, padx=10)

# Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar tarea como completada
complete_button = tk.Button(root, text="Marcar Completada", command=mark_completed)
complete_button.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar tarea
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Asignación de atajos de teclado
root.bind("<Return>", add_task)          # Atajo para añadir tarea (Enter)
root.bind("<c>", mark_completed)         # Atajo para marcar como completada (C)
root.bind("<Delete>", delete_task)       # Atajo para eliminar tarea (Delete)
root.bind("<d>", delete_task)            # Atajo para eliminar tarea (D)
root.bind("<Escape>", close_app)         # Atajo para cerrar la aplicación (Escape)

root.mainloop()
