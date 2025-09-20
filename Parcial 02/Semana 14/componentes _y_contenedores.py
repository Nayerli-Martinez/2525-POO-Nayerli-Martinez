## Importamos los módulos necesarios
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Widget para seleccionar fechas con calendario
from datetime import date         # Para trabajar con fechas válidas
import json                       # Para guardar y cargar datos en formato JSON

# Función para guardar los eventos actuales en un archivo JSON
def guardar_eventos_en_json():
    eventos = []
    # Recorremos todos los elementos del Treeview
    for item in tree.get_children():
        valores = tree.item(item)['values']
        eventos.append({
            "fecha": valores[0],
            "hora": valores[1],
            "descripcion": valores[2]
        })
    # Guardamos la lista de eventos en un archivo JSON
    with open("eventos.json", "w", encoding="utf-8") as f:
        json.dump(eventos, f, ensure_ascii=False, indent=4)

# Función para cargar eventos desde el archivo JSON al iniciar la app
def cargar_eventos_desde_json():
    try:
        with open("eventos.json", "r", encoding="utf-8") as f:
            eventos = json.load(f)
            # Insertamos cada evento en el Treeview
            for evento in eventos:
                tree.insert('', 'end', values=(evento["fecha"], evento["hora"], evento["descripcion"]))
    except FileNotFoundError:
        # Si el archivo no existe, simplemente no cargamos nada
        pass

# Función que se ejecuta al hacer clic en "Agregar Evento"
def agregar_evento():
    fecha = date_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    # Verificamos que todos los campos estén llenos
    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))  # Agregamos al Treeview
        guardar_eventos_en_json()  # Guardamos en el archivo JSON

        # Limpiamos los campos de entrada
        date_entry.set_date(date.today())
        hora_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")

# Función que se ejecuta al hacer clic en "Eliminar Evento Seleccionado"
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Deseas eliminar el evento seleccionado?")
        if confirmar:
            tree.delete(seleccionado)  # Eliminamos del Treeview
            guardar_eventos_en_json()  # Actualizamos el archivo JSON
    else:
        messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")

# Función que se ejecuta al hacer clic en "Salir"
def salir():
    root.destroy()  # Cierra la aplicación

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")     # Título de la ventana
root.geometry("600x400")          # Tamaño de la ventana

# Frame para mostrar la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Creamos el Treeview para mostrar los eventos como una tabla
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Cargamos los eventos guardados previamente (si existen)
cargar_eventos_desde_json()

# Frame para los campos de entrada
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Etiqueta y campo para la fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo para la hora
tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta y campo para la descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
descripcion_entry = tk.Entry(frame_entrada, width=40)
descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

# Frame para los botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para agregar evento
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

# Botón para eliminar evento
btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

# Botón para salir de la aplicación
btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)

# Ejecutamos el bucle principal de la aplicación
root.mainloop()