import tkinter as tk


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de tareas
        self.tasks = []

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de entrada
        self.label = tk.Label(self.root, text="Introduce una nueva tarea:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # Campo de entrada para nueva tarea
        self.task_entry = tk.Entry(self.root, width=35)
        self.task_entry.grid(row=1, column=0, padx=10, pady=5)
        self.task_entry.bind("<Return>", self.add_task_event)  # Añadir con tecla Enter

        # Botones
        self.add_button = tk.Button(self.root, text="Añadir", width=15, command=self.add_task)
        self.add_button.grid(row=1, column=1, padx=5, pady=5)

        self.complete_button = tk.Button(self.root, text="Completar", width=15, command=self.complete_task)
        self.complete_button.grid(row=2, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar", width=15, command=self.delete_task)
        self.delete_button.grid(row=3, column=1, padx=5, pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, height=10, width=50)
        self.task_listbox.grid(row=2, column=0, rowspan=2, padx=10, pady=10)

    def add_task_event(self, event):
        self.add_task()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index] += " (completada)"
            self.update_task_listbox()
        except IndexError:
            pass

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
