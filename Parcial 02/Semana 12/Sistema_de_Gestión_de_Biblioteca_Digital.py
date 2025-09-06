import json

# -------------------- Clases --------------------

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[1]} por {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = {}
        self.ids_usuarios = set()

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"📚 Libro añadido: {libro}")
        else:
            print("⚠ El libro ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"🗑 Libro con ISBN {isbn} eliminado.")
        else:
            print("⚠ Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"👤 Usuario registrado: {usuario}")
        else:
            print("⚠ ID de usuario ya existe.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"🚫 Usuario con ID {id_usuario} dado de baja.")
        else:
            print("⚠ Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"✅ Libro prestado: {libro}")
        else:
            print("⚠ Usuario o libro no disponible.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"🔄 Libro devuelto: {libro}")
                    return
            print("⚠ El usuario no tiene ese libro.")
        else:
            print("⚠ Usuario no encontrado.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            return self.usuarios_registrados[id_usuario].libros_prestados
        else:
            print("⚠ Usuario no encontrado.")
            return []

    def guardar_datos(self, archivo="datos_biblioteca.json"):
        datos = {
            "usuarios": {},
            "libros_disponibles": {}
        }

        for id_usuario, usuario in self.usuarios_registrados.items():
            datos["usuarios"][id_usuario] = {
                "nombre": usuario.nombre,
                "libros_prestados": [
                    {
                        "titulo": libro.info[1],
                        "autor": libro.info[0],
                        "categoria": libro.categoria,
                        "isbn": libro.isbn
                    } for libro in usuario.libros_prestados
                ]
            }

        for isbn, libro in self.libros_disponibles.items():
            datos["libros_disponibles"][isbn] = {
                "titulo": libro.info[1],
                "autor": libro.info[0],
                "categoria": libro.categoria,
                "isbn": libro.isbn
            }

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("💾 Datos guardados correctamente.")

    def cargar_datos(self, archivo="datos_biblioteca.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)

            for id_usuario, info in datos["usuarios"].items():
                usuario = Usuario(info["nombre"], id_usuario)
                for libro_data in info["libros_prestados"]:
                    libro = Libro(libro_data["titulo"], libro_data["autor"], libro_data["categoria"], libro_data["isbn"])
                    usuario.libros_prestados.append(libro)
                self.usuarios_registrados[id_usuario] = usuario
                self.ids_usuarios.add(id_usuario)

            for isbn, libro_data in datos["libros_disponibles"].items():
                libro = Libro(libro_data["titulo"], libro_data["autor"], libro_data["categoria"], libro_data["isbn"])
                self.libros_disponibles[isbn] = libro

            print("📂 Datos cargados correctamente.")
        except FileNotFoundError:
            print("📁 No se encontró archivo de datos. Se iniciará con una biblioteca vacía.")

# -------------------- Menú Interactivo --------------------

def mostrar_menu():
    print("\n📘 MENÚ DE BIBLIOTECA DIGITAL")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados")
    print("9. Salir")

def ejecutar_sistema():
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID único del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            print("\n📚 Libros disponibles actualmente:")
            for libro in biblioteca.libros_disponibles.values():
                print(libro)

            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            valor = input("Valor de búsqueda: ")
            resultados = biblioteca.buscar_libros(criterio, valor)
            print("\n🔍 Resultados de búsqueda:")
            for libro in resultados:
                print(libro)

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            libros = biblioteca.listar_libros_prestados(id_usuario)
            print("\n📋 Libros prestados:")
            for libro in libros:
                print(libro)

        elif opcion == "9":
            biblioteca.guardar_datos()
            print("👋 ¡Gracias por usar la biblioteca digital!")
            break

        else:
            print("⚠ Opción inválida. Intenta de nuevo.")

# -------------------- Ejecutar --------------------

if __name__ == "__main__":
    ejecutar_sistema()