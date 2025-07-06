# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre         # Encapsulamiento: atributo protegido
        self._edad = edad

    #Método común para todos los animales
    def hacer_sonido(self):
        return f"{self._nombre} hace un sonido."

    def descripcion(self):
        return f"{self._nombre} tiene {self._edad} años."


# Clase derivada: Perro (hereda de Animal)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self._raza = raza

    # Polimorfismo: sobrescribir método hacer_sonido
    def hacer_sonido(self):
        return f"{self._nombre} dice: ¡Guau!"

    # Método adicional solo de Perro
    def obtener_raza(self):
        return f"{self._nombre} es un {self._raza}."


# Clase derivada: Gato (hereda de Animal)
class Gato(Animal):
    def hacer_sonido(self):
        return f"{self._nombre} dice: Miau."


# Clase con encapsulamiento fuerte
class Jaula:
    def __init__(self, identificador):
        self.__identificador = identificador   # Atributo completamente privado
        self.__animales = []

    def agregar_animal(self, animal):
        self.__animales.append(animal)

    def mostrar_habitantes(self):
        for a in self.__animales:
            print(a.descripcion())
            print(a.hacer_sonido())


# Ejecución del Programa

# Crear instancias
perro1 = Perro("Rex", 5, "Pastor Alemán")
gato1 = Gato("Michi", 3)

# Demostración de polimorfismo y herencia
print(perro1.hacer_sonido())  # Usa su versión propia del método
print(gato1.hacer_sonido())   # También tiene su propia versión

# Uso de encapsulamiento con la clase Jaula
jaula1 = Jaula("Jaula-A")
jaula1.agregar_animal(perro1)
jaula1.agregar_animal(gato1)

print("\n Animales en la jaula:")
jaula1.mostrar_habitantes()

