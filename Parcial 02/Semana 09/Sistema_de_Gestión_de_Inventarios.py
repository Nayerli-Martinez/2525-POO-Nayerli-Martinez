
# sistema_inventario.py

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa los atributos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener los atributos
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos para modificar los atributos
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Representación en texto del producto
    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# Clase que gestiona el inventario de productos
class Inventario:
    def __init__(self):
        # Lista que almacena los productos
        self.productos = []

    # Añade un producto si el ID no está repetido
    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(" Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            print(" Producto añadido correctamente.")

    # Elimina un producto por su ID
    def eliminar_producto(self, id_producto):
        original_len = len(self.productos)
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        if len(self.productos) < original_len:
            print("Producto eliminado.")
        else:
            print("️ Producto no encontrado.")

    # Actualiza cantidad y/o precio de un producto
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print(" Producto no encontrado.")

    # Busca productos por nombre (parcial o completo)
    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Resultados de búsqueda:")
            for p in resultados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    # Muestra todos los productos en el inventario
    def mostrar_todos(self):
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print(" Productos en inventario:")
            for p in self.productos:
                print(p)


# Función principal que muestra el menú y gestiona la interacción con el usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Captura datos del nuevo producto
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print(" Error: cantidad y precio deben ser numéricos.")

        elif opcion == "2":
            # Elimina producto por ID
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualiza cantidad y/o precio
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            # Busca productos por nombre
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            # Muestra todos los productos
            inventario.mostrar_todos()

        elif opcion == "6":
            # Sale del programa
            print(" Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()
