"""
Diseña un programa para que, dados dos números enteros, determine si uno es múltiplo del otro.
"""

# Declaraciones
CONSTANTE = 0

# Entradas
numero_1 = float(input("Ingrese un número: "))
numero_2 = float(input("Ingrese otro número: "))

# Proceso
if numero_1 % numero_2 == CONSTANTE or numero_2 % numero_1 == CONSTANTE:
    mayor = max(numero_1, numero_2)
    menor = min(numero_1, numero_2)
    multiplo = "El número {mayor} es múltiplo del {menor}"
else:
    multiplo = "Ninguno de los números es múltiplo del otro"

# Salidas
print(multiplo)
