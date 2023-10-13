"""
Diseña un programa para que, dados dos números enteros, determine si uno es múltiplo del otro.
"""

# Declaraciones
CONSTANTE = 0

# Entradas
numero_1 = float(input("Ingrese un número: "))
numero_2 = float(input("Ingrese otro número: "))

# Proceso
if numero_1 % numero_2 == CONSTANTE:
    multiplo = "El número {numero_1} es múltiplo del {numero_2}"
elif numero_2 % numero_1 == CONSTANTE:
    multiplo = "El número {numero_2} es múltiplo del {numero_1}"
else:
    multiplo = "Ninguno de los números es múltiplo del otro"

# Salidas
print(multiplo)
