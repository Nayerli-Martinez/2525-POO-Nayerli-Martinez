class VisitanteBiblioteca:
    def __init__(self, nombre):
        """
        Constructor (__init__): se llama al crear una instancia del visitante.
        Aquí simulamos que el visitante entra a la biblioteca.
        """
        self.nombre = nombre
        print(f" {self.nombre} ha ingresado a la biblioteca.")

    def leer_libro(self, titulo):
        """
        Simula la lectura de un libro por parte del visitante.
        """
        print(f" {self.nombre} está leyendo '{titulo}'.")

    def __del__(self):
        """
        Destructor (__del__): se llama automáticamente cuando el objeto se elimina.
        Aquí simulamos que el visitante sale de la biblioteca.
        """
        print(f" {self.nombre} ha salido de la biblioteca.")


#  Código principal (ejecución)
if __name__ == "__main__":
    visitante1 = VisitanteBiblioteca("Nayerli Martinez")
    visitante1.leer_libro("Cien años de soledad")

    # Forzamos la salida del visitante (eliminamos el objeto)
    del visitante1

    # Opcional: Pausa para mantener la consola abierta si lo ejecutas fuera de PyCharm
    input("\nPresiona Enter para cerrar...")