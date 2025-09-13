import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al hacer clic en el botón "Agregar"
def agregar_dato():
    dato = entrada.get()
    if dato.strip():
        lista_datos.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese algún dato.")

# Función que elimina el elemento seleccionado de la lista
def eliminar_seleccionado():
    seleccion = lista_datos.curselection()
    if seleccion:
        lista_datos.delete(seleccion)
    else:
        messagebox.showinfo("Información", "Seleccione un elemento para eliminar.")

# Función que limpia toda la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos Básico")
ventana.geometry("400x350")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista de datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón para eliminar uno por uno
boton_eliminar = tk.Button(ventana, text="Eliminar seleccionado", command=eliminar_seleccionado)
boton_eliminar.pack(pady=5)

# Botón para limpiar toda la lista
boton_limpiar = tk.Button(ventana, text="Limpiar todo", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Inicia el bucle principal
ventana.mainloop()