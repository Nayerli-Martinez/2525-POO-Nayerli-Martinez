# Clase base que representa un día de clima
class DiaClima:
    def __init__(self, dia, temperatura):
        self.__dia = dia  # Encapsulamiento
        self.__temperatura = temperatura

    def obtener_temperatura(self):
        return self.__temperatura

    def obtener_dia(self):
        return self.__dia

# Clase derivada que representa una semana de clima
class SemanaClima:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, dia, temperatura):
        dia_clima = DiaClima(dia, temperatura)
        self.dias.append(dia_clima)

    def calcular_promedio(self):
        if not self.dias:
            return 0
        total = sum(dia.obtener_temperatura() for dia in self.dias)
        return total / len(self.dias)

    def mostrar_temperaturas(self):
        for dia in self.dias:
            print(f"{dia.obtener_dia()}: {dia.obtener_temperatura()} °C")

# Función principal
def main():
    semana = SemanaClima()
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Ingrese la temperatura para cada día de la semana:")
    for dia in dias_semana:
        temp = float(input(f"{dia}: "))
        semana.agregar_dia(dia, temp)

    print("\nTemperaturas registradas:")
    semana.mostrar_temperaturas()

    promedio = semana.calcular_promedio()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f} °C")

# Ejecutar el programa
main()
