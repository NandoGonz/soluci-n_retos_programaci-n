"""
Este script realiza varias operaciones de ejemplo en Python:
1. Imprime números pares entre 10 y 55 que no sean múltiplos de 3 y excluye el número 16.
2. Incluye ejemplos comentados sobre comparación de variables y operaciones a nivel de bit.
"""

# Imprime números pares entre 10 y 55, excluyendo múltiplos de 3 y el número 16
for i in range(10, 56, 1):
    if i % 3 != 0 and i % 2 == 0 and i != 16:
        print(i, end = "--")  # Imprime el número seguido de '--' si cumple las condiciones

'''
# Ejemplo de comparación de variables
number_1 = 12
number_2 = 12
print(f"my number_1 is = my number_2 it's: {number_1 is number_2}")     # Verifica si ambas variables son el mismo objeto
print(f"my number_1 is different  my number_2 it's:{number_1 is not number_2}")     # Verifica si son objetos diferentes

# Ejemplo de operaciones a nivel de bit usando el operador &
a = 7
b = 9
print(f"a & b = {a & b}")  # Realiza la operación AND bit a bit entre a y b
'''


