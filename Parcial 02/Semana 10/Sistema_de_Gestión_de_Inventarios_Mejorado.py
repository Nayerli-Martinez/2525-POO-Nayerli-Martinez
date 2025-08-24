import json
import os

class Inventario:
    def __init__(self, archivo='uinventario.json'):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo JSON al iniciar el programa."""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    self.productos = json.load(f)
            else:
                print(f"[INFO] El archivo '{self.archivo}' no existe. Se creará automáticamente.")
                self.guardar_en_archivo()
        except json.JSONDecodeError:
            print("[ERROR] El archivo está corrupto o mal formado. Se iniciará un inventario vacío.")
            self.productos = {}
        except PermissionError:
            print("[ERROR] No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda el inventario actual en el archivo JSON."""
        try:
            with open(self.archivo, 'w') as f:
                json.dump(self.productos, f, indent=4)
        except PermissionError:
            print("[ERROR] No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al guardar el archivo: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        self.productos[nombre] = {'cantidad': cantidad, 'precio': precio}
        self.guardar_en_archivo()
        print(f"[✔] Producto '{nombre}' agregado exitosamente.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre]['cantidad'] = cantidad
            if precio is not None:
                self.productos[nombre]['precio'] = precio
            self.guardar_en_archivo()
            print(f"[✔] Producto '{nombre}' actualizado.")
        else:
            print(f"[✘] El producto '{nombre}' no existe.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_en_archivo()
            print(f"[✔] Producto '{nombre}' eliminado.")
        else:
            print(f"[✘] El producto '{nombre}' no existe.")

    def mostrar_inventario(self):
        if not self.productos:
            print("[INFO] El inventario está vacío.")
        else:
            print("\n Inventario Actual:")
            for nombre, datos in self.productos.items():
                print(f" - {nombre}: {datos['cantidad']} unidades, ${datos['precio']:.2f}")

def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            inventario.mostrar_inventario()
        elif opcion == '2':
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(nombre, cantidad, precio)
            except ValueError:
                print("[✘] Entrada inválida. Asegúrate de ingresar números válidos.")
        elif opcion == '3':
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            try:
                inventario.actualizar_producto(
                    nombre,
                    int(cantidad) if cantidad else None,
                    float(precio) if precio else None
                )
            except ValueError:
                print("[✘] Entrada inválida. Asegúrate de ingresar números válidos.")
        elif opcion == '4':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("[✘] Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()