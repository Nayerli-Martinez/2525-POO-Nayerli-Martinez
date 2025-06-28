# Programa que convierte una temperatura de Celsius a Fahrenheit.
# El usuario ingresa una temperatura en Celsius y el programa calcula y muestra su equivalente en Fahrenheit.

def convertir_celsius_a_fahrenheit(temp_celsius):
    # Fórmula: (°C × 9/5) + 32 = °F
    temp_fahrenheit = (temp_celsius * 9 / 5) + 32
    return temp_fahrenheit

# Solicita al usuario que introduzca una temperatura
entrada_usuario = input("Introduce la temperatura en grados Celsius: ")

# Convierte la entrada a float y verifica si es válida
if entrada_usuario.replace('.', '', 1).isdigit():
    temperatura_celsius = float(entrada_usuario)
    resultado = convertir_celsius_a_fahrenheit(temperatura_celsius)

    print("Temperatura en Fahrenheit:", resultado)
    es_calor = resultado > 86  # Usamos un valor booleano para mostrar lógica adicional
    print("¿Hace calor?:", es_calor)
else:
    print("Entrada no válida. Por favor, introduce un número.")
