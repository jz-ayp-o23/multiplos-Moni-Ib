"""
Diseña un programa para que, dados dos números enteros, determine si uno es múltiplo del otro.
"""

# Declaraciones
CONSTANTE = 0

# Entradas
numero_1 = int(input("Ingrese un número: "))
numero_2 = int(input("Ingrese otro número: "))

# Proceso
if numero_1 % numero_2 == CONSTANTE:
    print(f"El número {numero_1} es múltiplo del {numero_2}")
elif numero_2 % numero_1 == CONSTANTE:
    print(f"El número {numero_2} es múltiplo del {numero_1}")
else:
    print("Ninguno de los números es múltiplo del otro")

