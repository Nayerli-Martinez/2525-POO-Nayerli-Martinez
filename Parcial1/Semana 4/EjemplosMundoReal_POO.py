# Clase que representa una Habitación en el hotel
class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def __str__(self):
        return f"Habitación {self.numero} - Tipo: {self.tipo} - Precio: ${self.precio} - Disponible: {self.disponible}"

# Clase que representa un Cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Cliente: {self.nombre} - Cédula: {self.cedula}"

# Clase que representa una Reserva
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.disponible = True
            return f"Reserva confirmada para {self.cliente.nombre} en la habitación {self.habitacion.numero}."
        else:
            return f"La habitación {self.habitacion.numero} no está disponible."

# Ejemplo de uso
habitacion1 = Habitacion(101, "Suite", 120)
cliente1 = Cliente("Juan Pérez", "1234567890")
reserva1 = Reserva(cliente1, habitacion1)

print(reserva1.confirmar_reserva())
print(habitacion1)


#