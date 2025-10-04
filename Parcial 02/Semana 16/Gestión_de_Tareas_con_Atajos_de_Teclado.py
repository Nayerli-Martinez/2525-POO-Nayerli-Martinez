# Importamos los módulos necesarios
import tkinter as tk  # Para crear la interfaz gráfica
from tkinter import messagebox  # Para mostrar mensajes emergentes
import json  # Para guardar y cargar tareas en formato JSON
import os  # Para verificar si el archivo existe

# Nombre del archivo donde se guardarán las tareas
ARCHIVO_TAREAS = "archivos.json"

# Clase principal que gestiona la aplicación
class TaskManager:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Gestión de Tareas")  # Título de la ventana
        self.root.geometry("400x400")  # Tamaño de la ventana

        self.tareas = []  # Lista donde se almacenan las tareas

        # Campo de entrada para escribir nuevas tareas
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())  # Atajo: Enter para añadir tarea

        # Marco que contiene los botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        # Botón para añadir tarea
        tk.Button(btn_frame, text="Añadir", command=self.add_task).pack(side="left", padx=5)
        # Botón para marcar tarea como completada
        tk.Button(btn_frame, text="Completar", command=self.complete_task).pack(side="left", padx=5)
        # Botón para eliminar tarea
        tk.Button(btn_frame, text="Eliminar", command=self.delete_task).pack(side="left", padx=5)

        # Lista donde se muestran las tareas
        self.listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.listbox.pack(expand=True, fill="both", padx=10, pady=10)

        # Atajos de teclado
        self.root.bind("<c>", lambda event: self.complete_task())  # C para completar tarea
        self.root.bind("<d>", lambda event: self.delete_task())    # D para eliminar tarea
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Tecla Delete también elimina
        self.root.bind("<Escape>", lambda event: self.root.quit())  # Escape para cerrar la app

        # Cargar tareas guardadas al iniciar
        self.load_tasks()

    # Función para añadir una nueva tarea
    def add_task(self):
        task = self.entry.get().strip()  # Obtener texto del campo de entrada
        if task:
            self.tareas.append({"texto": task, "completada": False})  # Añadir tarea como pendiente
            self.entry.delete(0, tk.END)  # Limpiar campo de entrada
            self.update_listbox()  # Actualizar la lista visual
            self.save_tasks()  # Guardar cambios en el archivo
        else:
            messagebox.showwarning("Entrada vacía", "Por favor ingresa una tarea.")  # Advertencia

    # Función para marcar una tarea como completada
    def complete_task(self):
        selected = self.listbox.curselection()  # Obtener índice de tarea seleccionada
        if selected:
            index = selected[0]
            self.tareas[index]["completada"] = True  # Marcar como completada
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para completar.")  # Info

    # Función para eliminar una tarea
    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            del self.tareas[selected[0]]  # Eliminar tarea de la lista
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")

    # Función para actualizar la lista visual de tareas
    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Limpiar lista
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto = "✔️ " + texto  # Añadir ícono si está completada
            self.listbox.insert(tk.END, texto)  # Mostrar tarea en la lista

    # Función para guardar las tareas en el archivo JSON
    def save_tasks(self):
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
            json.dump(self.tareas, f, ensure_ascii=False, indent=2)  # Guardar con formato legible

    # Función para cargar tareas desde el archivo JSON
    def load_tasks(self):
        if os.path.exists(ARCHIVO_TAREAS):  # Verificar si el archivo existe
            with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
                self.tareas = json.load(f)  # Cargar tareas en memoria
            self.update_listbox()  # Mostrar tareas en la interfaz

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear ventana principal
    app = TaskManager(root)  # Instanciar la clase
    root.mainloop()  # Iniciar el bucle principal de la app
