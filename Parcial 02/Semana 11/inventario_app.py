import json  # Librería para trabajar con archivos JSON

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto       # Identificador único del producto
        self.nombre = nombre        # Nombre del producto
        self.cantidad = cantidad    # Cantidad disponible
        self.precio = precio        # Precio por unidad

    def actualizar_cantidad(self, nueva_cantidad):
        # Actualiza la cantidad del producto
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        # Actualiza el precio del producto
        self.precio = nuevo_precio

    def to_dict(self):
        # Convierte el producto en un diccionario para guardarlo en JSON
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        # Crea un producto a partir de un diccionario (al cargar desde JSON)
        return Producto(
            id_producto=data["id"],
            nombre=data["nombre"],
            cantidad=data["cantidad"],
            precio=data["precio"]
        )

# Clase que gestiona el inventario completo
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario que almacena productos por ID

    def agregar_producto(self, producto):
        # Añade un producto si no existe ya en el inventario
        if producto.id in self.productos:
            print(" El producto ya existe. Usa actualizar para modificarlo.")
        else:
            self.productos[producto.id] = producto
            print(" Producto añadido.")

    def eliminar_producto(self, id_producto):
        # Elimina un producto por su ID
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(" Producto eliminado.")
        else:
            print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza cantidad y/o precio de un producto existente
        producto = self.productos.get(id_producto)
        if producto:
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            print(" Producto actualizado.")
        else:
            print(" Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # Busca productos cuyo nombre contenga el texto ingresado
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_todos(self):
        # Devuelve todos los productos como lista
        return list(self.productos.values())

    def guardar_en_archivo(self, archivo):
        # Guarda el inventario en un archivo JSON
        with open(archivo, 'w') as f:
            json.dump({id: p.to_dict() for id, p in self.productos.items()}, f, indent=4)
        print(" Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo):
        # Carga el inventario desde un archivo JSON
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                self.productos = {id: Producto.from_dict(p) for id, p in data.items()}
            print(" Inventario cargado desde archivo.")
        except FileNotFoundError:
            print(" Archivo no encontrado. Se iniciará un inventario vacío.")
            self.productos = {}

# Muestra el menú de opciones al usuario
def mostrar_menu():
    print("\n MENÚ DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")

# Función principal que ejecuta el programa
def main():
    inventario = Inventario()         # Creamos el inventario
    archivo = "inventario.json"       # Nombre del archivo para guardar/cargar

    while True:
        mostrar_menu()                # Mostramos el menú
        opcion = input(" Selecciona una opción: ")

        if opcion == "1":
            # Añadir producto
            id = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print(" Entrada inválida. Usa números para cantidad y precio.")

        elif opcion == "2":
            # Eliminar producto
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            # Actualizar producto
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no aplica): ")
            precio = input("Nuevo precio (dejar vacío si no aplica): ")
            inventario.actualizar_producto(
                id,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            # Buscar producto por nombre
            nombre = input(" Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p.to_dict())
            else:
                print(" No se encontraron productos con ese nombre.")

        elif opcion == "5":
            # Mostrar todos los productos
            todos = inventario.mostrar_todos()
            if todos:
                for p in todos:
                    print(p.to_dict())
            else:
                print(" Inventario vacío.")

        elif opcion == "6":
            # Guardar inventario en archivo
            inventario.guardar_en_archivo(archivo)

        elif opcion == "7":
            # Cargar inventario desde archivo
            inventario.cargar_desde_archivo(archivo)

        elif opcion == "8":
            # Salir del programa
            print(" Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            # Opción inválida
            print(" Opción inválida. Intenta de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()