# Importamos los módulos necesarios
import tkinter as tk  # Para crear la interfaz gráfica
from tkinter import messagebox  # Para mostrar mensajes emergentes
import json  # Para guardar y cargar tareas en formato JSON
import os  # Para verificar si el archivo de tareas existe

# Nombre del archivo donde se guardarán las tareas
TASKS_FILE = "tasks.json"

# Definimos la clase principal de la aplicación
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")  # Título de la ventana
        self.root.geometry("400x400")  # Tamaño de la ventana

        self.tasks = []  # Lista donde se almacenan las tareas
        self.load_tasks()  # Cargamos las tareas desde el archivo

        # Campo de entrada para escribir nuevas tareas
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())  # Añadir tarea al presionar Enter

        # Marco para los botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        # Botones para añadir, marcar como completada , eliminar tareas y salir
        tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Marcar como Completada", command=self.mark_completed).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task).grid(row=0, column=2, padx=5)



        # Lista visual donde se muestran las tareas
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", lambda event: self.mark_completed())  # Marcar tarea al hacer doble clic

        self.update_listbox()  # Actualizamos la lista visual
        tk.Button(root, text="Salir", command=self.root.quit).pack(pady=10)

    # Carga las tareas desde el archivo JSON
    def load_tasks(self):
        if os.path.exists(TASKS_FILE):  # Verifica si el archivo existe
            try:
                with open(TASKS_FILE, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)  # Carga las tareas
            except json.JSONDecodeError:
                self.tasks = []  # Si hay error, se inicia con lista vacía

    # Guarda las tareas en el archivo JSON
    def save_tasks(self):
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    # Añade una nueva tarea
    def add_task(self):
        task = self.entry.get().strip()  # Obtiene el texto y elimina espacios
        if task:
            self.tasks.append({"text": task, "completed": False})  # Añade tarea como no completada
            self.entry.delete(0, tk.END)  # Limpia el campo de entrada
            self.update_listbox()  # Actualiza la lista visual
            self.save_tasks()  # Guarda los cambios
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")  # Muestra advertencia

    # Marca o desmarca una tarea como completada
    def mark_completed(self):
        selected = self.listbox.curselection()  # Obtiene la tarea seleccionada
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]  # Alterna el estado
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla.")  # Muestra mensaje

    # Elimina una tarea seleccionada
    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]  # Elimina la tarea
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminarla.")

    # Actualiza la lista visual con las tareas
    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Limpia la lista
        for task in self.tasks:
            # Muestra la tarea con un símbolo según si está completada o no
            display_text = f"[✔] {task['text']}" if task["completed"] else f"[ ] {task['text']}"
            self.listbox.insert(tk.END, display_text)

# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = TodoApp(root)  # Instancia la aplicación
    root.mainloop()  # Inicia el bucle principal de la interfaz