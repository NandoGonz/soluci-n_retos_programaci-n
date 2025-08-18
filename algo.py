"""
Este script realiza varias operaciones de ejemplo en Python:
1. Imprime números pares entre 10 y 55 que no sean múltiplos de 3 y excluye el número 16.
2. Incluye ejemplos comentados sobre comparación de variables y operaciones a nivel de bit.
"""

# Imprime números pares entre 10 y 55, excluyendo múltiplos de 3 y el número 16
"""for i in range(10, 56, 1):
    if i % 3 != 0 and i % 2 == 0 and i != 16:
        print(
            i, end="--"
        )  # Imprime el número seguido de '--' si cumple las condiciones"""

"""
# Ejemplo de comparación de variables
number_1 = 12
number_2 = 12
print(f"my number_1 is = my number_2 it's: {number_1 is number_2}")     # Verifica si ambas variables son el mismo objeto
print(f"my number_1 is different  my number_2 it's:{number_1 is not number_2}")     # Verifica si son objetos diferentes

# Ejemplo de operaciones a nivel de bit usando el operador &
a = 7
b = 9
print(f"a & b = {a & b}")  # Realiza la operación AND bit a bit entre a y b
"""

"""Cuenta del 10 al 1 usando while y luego muestra "¡Despegue!"."""

"""contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
print("¡Despegue!")"""

"""Pide números al usuario y suma todos hasta que ingrese un número negativo."""

"""suma = 0

while True:
    num_sumar = int(input("Ingrese un número positivo: "))
    if num_sumar < 0:
        break
    suma += num_sumar
print(f"El total de los numeros es: {suma}")"""

"""Pide al usuario que escriba una palabra hasta que escriba "salir"."""

"""palabra_correcta = "salir"

while True:
    palabra_usuario = input("Ingrese una palabra para ser libre: ").lower()
    if palabra_usuario == palabra_correcta:
        break
print("Felicidades eres libre")"""

"""while True:
    print("ingrese un número verificación de valor o digite 0 para salir")
    num_usuario = int(input("Ingrese un número: "))
    if num_usuario > 0:
        print(f" ➕ El numero: {num_usuario} es positivo")
    elif num_usuario < 0:
        print(f" ➖ El numero: {num_usuario} es negativo")
    else:
        print("📤 Saliendo del verificador")
        break"""

"""Pide dos números y muestra cuál es mayor o si son iguales."""

"""while True:
    salir = input("para salir escriba si, para continuar cualquiera caracter: ")

    if salir == "si":
        print("📤 Saliendo del comparador")
        break

    num_1 = int(input("Ingrese un valor: "))
    num_2 = int(input("Ingrese un valor: "))
    if num_1 > num_2:
        print(f"El número 1: {num_1} es mayor a el número 2: {num_2}")
    elif num_2 > num_1:
        print(f"El número 2: {num_2} es mayor a el número 1: {num_1}")
    else:
        print(f"El número 1 {num_1} y el número 2 {num_2} son iguales")"""


# Ejercicio  3 Pide la edad de una persona y muestra: "Menor de edad" si es menor de 18 "Mayor de edad" si tiene entre 18 y 64 "Adulto mayor" si tiene 65 o más

while True:
    try:
        edad = int(input("Ingrese su edad o ingrese 0 para salir: "))

        if edad > 0 and edad < 18:
            print(f"Su edad es: {edad} es menor de edad 🧒")
        elif edad >= 18 and edad <= 64:
            print(f"Su edad es: {edad} es mayor de edad 🧑")
        elif edad >= 65:
            print(f"Su edad es: {edad} es un adulto mayor 👨‍🦳")
        elif edad == 0:
            print("📤 Saliendo del programa")
            break

    except ValueError:
        print(" ❌Ingrese un valor numerico ❌")

# ejercicio 4 Muestra los números del 1 al 10 usando un for.
for i in range(1, 11):
    print(i)

# Ejercicio 5 Pide un número y muestra su tabla de multiplicar del 1 al 10.

numero = int(input("ingrese un número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"La multiplicación de {numero} * {i} = {resultado}")

"""
Ejercicio 6

Pide 5 números al usuario y muestra la suma total.
"""

total_suma = 0
cantidad_de_veces = int(
    input("Ingrese la cantidad de numeros que desea sumar: ")
)  # tambien podemos crear una  variable con el valor de 5

for valor in range(cantidad_de_veces):
    valor_a_sumar = float(input("Ingrese el valor a sumar: "))
    total_suma += valor_a_sumar
print(f"El valor de la suma es: {total_suma}")
