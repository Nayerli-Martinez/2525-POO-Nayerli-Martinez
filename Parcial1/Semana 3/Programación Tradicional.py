# Función para ingresar las temperaturas de cada día de la semana
def ingresar_temperaturas():
    temperaturas = []  # Lista donde se almacenarán las temperaturas
    print("Ingrese la temperatura de cada día de la semana:")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        # Solicita al usuario la temperatura para el día actual
        temp = float(input(f"{dia}: "))
        temperaturas.append(temp)  # Guarda la temperatura en la lista

    return temperaturas  # Devuelve la lista completa de temperaturas


# Función que calcula el promedio semanal de temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)  # Promedio = suma total / número de días


# Función principal que organiza el flujo del programa
def main():
    temperaturas = ingresar_temperaturas()  # Se recopilan los datos ingresados
    promedio = calcular_promedio(temperaturas)  # Se calcula el promedio
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f} °C")  # Se muestra el resultado


# Punto de entrada del programa
main()